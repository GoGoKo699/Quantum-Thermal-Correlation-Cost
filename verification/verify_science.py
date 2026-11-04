#!/usr/bin/env python3
"""Finite diagnostics for the thermal-correlation construction.

The wavefunction route integrates the oscillator recovery directly. It is
independent of the finite qubit comparator. Other checks compare numerical
quadratures with the analytic energy, Fourier coefficients and wrapped-normal
cell construction. The universal theorems are established in science/, not
by the finite examples generated here.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import scipy
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.special import ndtr


B = math.sqrt(math.pi)
ETA = 0.9
M = 64
E0 = 2 * math.pi / 3 - 1 / (4 * math.pi) - 0.5
S2 = (1 - ETA) / ETA
R_NOISE = math.sqrt(S2)
PERIOD = 2 * B / R_NOISE


def entropy(probabilities):
    p = np.asarray(probabilities, dtype=float)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def g(x):
    """Bosonic entropy, evaluated without cancellation at large occupation."""
    if x == 0:
        return 0.0
    return math.log1p(x) / math.log(2) + x * math.log1p(1 / x) / math.log(2)


def packet(u):
    return math.sqrt(2 / B) * math.sin(math.pi * u / B) if 0 < u < B else 0.0


def packet_derivative(u):
    return math.sqrt(2 / B) * (math.pi / B) * math.cos(math.pi * u / B) if 0 < u < B else 0.0


def psi(j, q):
    return packet(q + B) if j == 0 else packet(q)


def psi_derivative(j, q):
    return packet_derivative(q + B) if j == 0 else packet_derivative(q)


def integrate_code(function):
    return sum(quad(function, lo, hi, epsabs=2e-13, epsrel=2e-13)[0]
               for lo, hi in [(-B, 0.0), (0.0, B)])


def energy_check():
    gram = np.zeros((2, 2))
    q2 = np.zeros((2, 2))
    p2 = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            gram[i, j] = integrate_code(lambda q: psi(i, q) * psi(j, q))
            q2[i, j] = integrate_code(lambda q: q * q * psi(i, q) * psi(j, q))
            # Quadratic-form expectation of p^2, not a second-derivative
            # evaluation at the packet's derivative discontinuities.
            p2[i, j] = integrate_code(lambda q: psi_derivative(i, q) * psi_derivative(j, q))
    number_form = (q2 + p2 - gram) / 2
    expected_q2 = math.pi / 3 - 1 / (2 * math.pi)
    errors = {
        "normalization": float(np.max(np.abs(gram - np.eye(2)))),
        "q_squared": float(np.max(np.abs(q2 - expected_q2 * np.eye(2)))),
        "p_squared": float(np.max(np.abs(p2 - math.pi * np.eye(2)))),
        "number_form": float(np.max(np.abs(number_form - E0 * np.eye(2)))),
    }
    assert max(errors.values()) < 2e-12, errors
    return {"max_entry_errors": errors, "number_form": number_form.tolist()}


def direct_matrix_unit(source_i, source_j, v, w):
    """Trace the gauge coordinates of displaced physical wavefunctions."""
    out = np.zeros((2, 2), dtype=complex)
    center_m = math.floor(v / (2 * B))
    for i in range(2):
        for j in range(2):
            for m in range(center_m - 2, center_m + 3):
                qi0 = 2 * B * m + (i - 1) * B
                qj0 = 2 * B * m + (j - 1) * B
                cuts = [0.0, B]
                for source, q0 in [(source_i, qi0), (source_j, qj0)]:
                    left = -B if source == 0 else 0.0
                    cuts.extend(x for x in [left + v - q0, left + B + v - q0] if 0 < x < B)
                cuts = sorted(set(cuts))
                integral = sum(quad(
                    lambda u: psi(source_i, qi0 + u - v) * psi(source_j, qj0 + u - v),
                    lo, hi, epsabs=2e-12, epsrel=2e-12,
                )[0] for lo, hi in zip(cuts[:-1], cuts[1:]))
                out[i, j] += integral * np.exp(1j * w * (qi0 - qj0))
    return out


def retention(v):
    v = (v + B) % (2 * B) - B
    x = abs(v) / B
    return 1 - x + math.sin(2 * math.pi * x) / (2 * math.pi)


def predicted_matrix_unit(i, j, v, w):
    keep = retention(v)
    out = np.zeros((2, 2), dtype=complex)
    if i == j:
        out[i, i] = keep
        out[1 - i, 1 - i] = 1 - keep
    else:
        out[i, j] = keep * np.exp(1j * (i - j) * B * w)
    return out


def choi_from_map(function):
    return np.block([[function(i, j) for j in range(2)] for i in range(2)]) / 2


def wavefunction_check():
    cases = [(x * B, (0.17 + 0.11 * k) * (-1 if k % 2 else 1))
             for k, x in enumerate([0, .01, .1, .49, .9, .999999, 1,
                                    1.000001, 1.3, 1.99, 2.1,
                                    -.001, -.49, -.999999, -1, -1.3])]
    cases += [(0.0, 0.0), (2 * B * 31 + .1, -2 * B * 17 + .2),
              (-2 * B * 41 - .17, 2 * B * 29 - .13),
              (2 * B * 100 + .23, 2 * B * 83 - .31)]
    max_error = 0.0
    max_trace_error = 0.0
    min_choi_eigenvalue = 1.0
    for v, w in cases:
        direct = {(i, j): direct_matrix_unit(i, j, v, w)
                  for i in range(2) for j in range(2)}
        for (i, j), matrix in direct.items():
            error = np.max(np.abs(matrix - predicted_matrix_unit(i, j, v, w)))
            max_error = max(max_error, float(error))
            max_trace_error = max(max_trace_error, float(abs(np.trace(matrix) - (i == j))))
        choi = choi_from_map(lambda i, j: direct[i, j])
        min_choi_eigenvalue = min(min_choi_eigenvalue, float(np.min(np.linalg.eigvalsh(choi))))
    assert max_error < 2e-9, max_error
    assert max_trace_error < 2e-10, max_trace_error
    assert min_choi_eigenvalue > -2e-10, min_choi_eigenvalue

    # Average a physical four-point symmetric product displacement law. This
    # independently checks that the surviving coherence gives the stated
    # Pauli probabilities, including p_X=p_Y after crossing pieces are traced.
    v, w = .39 * B, .43
    symmetric = {(i, j): sum(direct_matrix_unit(i, j, sv * v, sw * w)
                             for sv in [-1, 1] for sw in [-1, 1]) / 4
                 for i in range(2) for j in range(2)}
    choi = choi_from_map(lambda i, j: symmetric[i, j])
    eigenvalues = np.linalg.eigvalsh(choi)
    expected = np.sort(pauli_probabilities(retention(v), math.cos(B * w)))
    pauli_error = float(np.max(np.abs(eigenvalues - expected)))
    assert pauli_error < 2e-12, pauli_error
    return {
        "displacement_cases": len(cases),
        "matrix_unit_comparisons": 4 * len(cases),
        "largest_lattice_index": 100,
        "max_entry_error": max_error,
        "max_trace_error": max_trace_error,
        "minimum_choi_eigenvalue": min_choi_eigenvalue,
        "symmetric_noise_pauli_eigenvalue_error": pauli_error,
    }


def fourier_coefficient(k):
    if k % 2 == 0:
        return 0.0
    return 16 / (math.pi**2 * k**2 * (4 - k**2))


def fourier_check():
    mean = quad(lambda v: retention(v), -B, B, points=[0], epsabs=2e-13)[0] / (2 * B)
    errors = []
    for k in range(1, 18):
        numerical = quad(lambda v: retention(v) * math.cos(k * math.pi * v / B),
                         -B, B, points=[0], epsabs=2e-13, epsrel=2e-13)[0] / B
        errors.append(abs(numerical - fourier_coefficient(k)))
    assert abs(mean - .5) < 2e-12
    assert max(errors) < 2e-12, max(errors)
    return {"mean_error": abs(mean - .5), "coefficients_compared": len(errors),
            "max_coefficient_error": max(errors)}


def pauli_probabilities(a, c):
    return np.array([a * (1 + c) / 2, a * (1 - c) / 2, (1 - a) / 2, (1 - a) / 2])


def analytic_bound():
    theta = math.pi * S2 / 2
    c1 = fourier_coefficient(1)
    c_low = math.exp(-theta) * math.cos(2 * math.pi / M)
    a_low = .5 + c1 * c_low - (c1 - .5) * math.exp(-9 * theta)
    probabilities = pauli_probabilities(a_low, c_low)
    rate = 1 - entropy(probabilities)
    alternate_rate = a_low - entropy([a_low, 1 - a_low]) - a_low * entropy([(1 - c_low) / 2, (1 + c_low) / 2])
    assert abs(rate - alternate_rate) < 1e-14
    assert rate > .24259
    assert abs(sum(probabilities) - 1) < 1e-14 and np.min(probabilities) >= 0
    return {"eta": ETA, "residue_cells_per_axis": M,
            "input_mean_photons": E0, "bath_mutual_information_upper_bits": 2 * math.log2(M),
            "gaussian_displacement_variance_per_quadrature": S2,
            "A_lower": a_low, "c_lower": c_low, "pauli_probabilities_at_lower_parameters": probabilities.tolist(),
            "coherent_information_lower": rate,
            "displayed_rate_lower_rounded_down": .24259,
            "product_bath_EB_threshold_N": ETA / (1 - ETA),
            "auxiliary_thermal_input_coherent_information": g(ETA * E0) - g((1 - ETA) * E0)}


def gaussian_inner_code_check(bound):
    """The same finite-energy code with no residue error."""
    theta = math.pi * S2 / 2
    c = math.exp(-theta)
    a = .5 + fourier_coefficient(1) * c - (fourier_coefficient(1) - .5) * math.exp(-9 * theta)
    rate = 1 - entropy(pauli_probabilities(a, c))
    assert c >= bound["c_lower"] and a >= bound["A_lower"]
    assert rate >= bound["coherent_information_lower"]
    return {"A_lower": a, "c_lower": c, "coherent_information_lower": rate,
            "input_energy_every_logical_state": E0,
            "role": "Matching Gaussian bath feasibility with the same finite-energy inner encoder, amplifier, and decoder."}


def robustness_check(bound):
    """Evaluate only the perturbation bounds stated in science/robustness.md."""
    a_star, b_star = bound["A_lower"], bound["A_lower"] * bound["c_lower"]

    def spectrum(a, abs_b):
        return np.array([(a + abs_b) / 2, (a - abs_b) / 2, (1 - a) / 2, (1 - a) / 2])

    def rms_bound(d):
        a = a_star - 2 * d / B
        abs_b = b_star - 2 * d / B - B * d
        assert 0 <= abs_b <= a <= 1
        assert a >= (1 + abs_b**2) / 2
        return 1 - entropy(spectrum(a, abs_b))

    # A biased, correlated displacement distribution. Its coherence is complex;
    # this checks the use of |B| in the general Choi spectrum.
    law = [(0.2, .13, .21), (0.35, -.37, .52), (0.45, .29, -.18)]
    direct = {(i, j): sum(weight * direct_matrix_unit(i, j, v, w) for weight, v, w in law)
              for i in range(2) for j in range(2)}
    a = sum(weight * retention(v) for weight, v, w in law)
    coherence = sum(weight * retention(v) * np.exp(-1j * B * w) for weight, v, w in law)
    eigenvalues = np.linalg.eigvalsh(choi_from_map(lambda i, j: direct[i, j]))
    general_spectrum_error = float(np.max(np.abs(eigenvalues - np.sort(spectrum(a, abs(coherence))))))
    assert general_spectrum_error < 2e-12

    rates = {str(d): rms_bound(d) for d in [.01, .02]}
    assert rates["0.01"] > .1586 and rates["0.02"] > .0794
    delta = .05
    theta = math.pi * (S2 + delta) / 2
    c = math.exp(-theta) * math.cos(2 * math.pi / M)
    a = .5 + fourier_coefficient(1) * c - (fourier_coefficient(1) - .5) * math.exp(-9 * theta)
    gaussian_rate = 1 - entropy(pauli_probabilities(a, c))
    assert gaussian_rate > .0217
    t = .005
    chi = 2 * t + (1 + t) * entropy([t / (1 + t), 1 / (1 + t)])
    combined = rates["0.01"] - chi
    assert combined > .10
    return {
        "general_correlated_noise_Choi_spectrum_error": general_spectrum_error,
        "additional_RMS_displacement_bounds": rates,
        "extra_Gaussian_variance": delta,
        "extra_Gaussian_rate_lower": gaussian_rate,
        "vacuum_channel_half_trace_distance_bound": t,
        "conditional_entropy_penalty": chi,
        "combined_rate_lower_at_RMS_0.01": combined,
    }


def wrapped_normal_density(x, sigma):
    """One-period density of a real N(0,sigma^2) variable.

    Use spatial images for a narrow distribution and Poisson summation for a
    broad one. Both truncate beyond a term/tail smaller than 1e-16.
    """
    x = np.asarray(x)
    ratio = sigma / PERIOD
    if ratio < .2:
        images = int(math.ceil(12 * ratio)) + 2
        ks = np.arange(-images, images + 1)
        z = (x[..., None] + PERIOD * ks) / sigma
        return np.sum(np.exp(-z * z / 2), axis=-1) / (math.sqrt(2 * math.pi) * sigma)
    count = max(1, int(math.ceil(math.sqrt(-math.log(1e-17) / (2 * math.pi**2 * ratio**2)))))
    ks = np.arange(1, count + 1)
    coefficients = np.exp(-2 * math.pi**2 * ratio**2 * ks**2)
    return (1 + 2 * np.sum(coefficients * np.cos(2 * math.pi * x[..., None] * ks / PERIOD), axis=-1)) / PERIOD


def cell_probabilities_cdf(sigma):
    """Cell masses computed from normal CDFs, independently of quadrature."""
    boundaries = np.linspace(0, PERIOD, M + 1)
    ratio = sigma / PERIOD
    if ratio <= 4:
        images = int(math.ceil(12 * ratio)) + 2
        ks = np.arange(-images, images + 1)
        lo = (boundaries[:-1, None] + PERIOD * ks) / sigma
        hi = (boundaries[1:, None] + PERIOD * ks) / sigma
        # Survival-function form avoids cancellation for positive far tails.
        pieces = np.where(lo > 0, ndtr(-lo) - ndtr(-hi), ndtr(hi) - ndtr(lo))
        return np.sum(pieces, axis=1)
    count = max(1, int(math.ceil(math.sqrt(-math.log(1e-17) / (2 * math.pi**2 * ratio**2)))))
    ks = np.arange(1, count + 1)
    coeff = np.exp(-2 * math.pi**2 * ratio**2 * ks**2)
    sines = np.sin(2 * math.pi * boundaries[:, None] * ks / PERIOD)
    return np.full(M, 1 / M) + np.sum(coeff * np.diff(sines, axis=0) / (math.pi * ks), axis=1)


def thermal_cell_diagnostic(n, order):
    sigma = math.sqrt(n / 2)
    nodes, weights = leggauss(order)
    width = PERIOD / M
    x = (np.arange(M)[:, None] + (nodes[None, :] + 1) / 2) * width
    measure = wrapped_normal_density(x, sigma) * weights[None, :] * width / 2
    masses = np.sum(measure, axis=1)
    cdf_masses = cell_probabilities_cdf(sigma)
    ks = np.arange(1, 16, 2)
    phase = np.exp(2j * math.pi * x[..., None] * ks / PERIOD)
    amplitudes = np.sum(measure[..., None] * phase, axis=1)
    populated = masses > 1e-250
    phi = np.sum(np.abs(amplitudes[populated])**2 / masses[populated, None], axis=0)
    theta = math.pi * S2 / 2
    c = math.exp(-theta) * phi[0]
    a = .5 + sum(fourier_coefficient(int(k)) * math.exp(-k * k * theta) * value
                 for k, value in zip(ks, phi))
    rate = 1 - entropy(pauli_probabilities(a, c))
    tail_bound = (fourier_coefficient(1) - .5) * math.exp(-17**2 * theta)
    return {
        "N": n,
        "label_entropy_bits_two_axes": 2 * entropy(masses),
        "cell_mass_sum_error": abs(float(np.sum(masses)) - 1),
        "cell_mass_CDF_vs_quadrature_max_error": float(np.max(np.abs(masses - cdf_masses))),
        "first_residual_characteristic": float(phi[0]),
        "A_numerical": float(a), "c_numerical": float(c),
        "decoded_coherent_information_numerical": float(rate),
        "omitted_Fourier_tail_bound_for_A": tail_bound,
    }, phi, masses


def thermal_cells_check(bound):
    results = []
    for n in [.001, .1, 1, 9, 100, 1e4, 1e8]:
        low, low_phi, low_p = thermal_cell_diagnostic(n, 48)
        high, high_phi, high_p = thermal_cell_diagnostic(n, 96)
        convergence = max(float(np.max(abs(low_phi - high_phi))), float(np.max(abs(low_p - high_p))))
        assert convergence < 2e-10, (n, convergence)
        assert high["cell_mass_sum_error"] < 2e-11, high
        assert high["cell_mass_CDF_vs_quadrature_max_error"] < 2e-11, high
        assert high["label_entropy_bits_two_axes"] <= 2 * math.log2(M) + 2e-10, high
        assert high["c_numerical"] >= bound["c_lower"] - 2e-11, high
        assert high["A_numerical"] >= bound["A_lower"] - 2e-11, high
        assert high["decoded_coherent_information_numerical"] >= bound["coherent_information_lower"] - 2e-10, high
        high["quadrature_order_48_vs_96_max_error"] = convergence
        results.append(high)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    bound = analytic_bound()
    result = {
        "scope": "Finite numerical diagnostics of independent representations and evaluation of analytic bounds; universal proofs are in science/.",
        "software": {"numpy": np.__version__, "scipy": scipy.__version__},
        "energy": energy_check(),
        "wavefunction_decoder": wavefunction_check(),
        "fourier": fourier_check(),
        "analytic_operating_point": bound,
        "matching_Gaussian_inner_code": gaussian_inner_code_check(bound),
        "robustness": robustness_check(bound),
        "finite_temperature_cell_diagnostics": thermal_cells_check(bound),
        "pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"pass": True, "output": str(args.output),
                      "direct_decoder_max_error": result["wavefunction_decoder"]["max_entry_error"],
                      "quantum_rate_lower": bound["coherent_information_lower"]}, indent=2))


if __name__ == "__main__":
    main()
