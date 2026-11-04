#!/usr/bin/env python3
"""Plot analytic correlation-cost bounds, not optimized costs."""

from pathlib import Path
import csv
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def g(x):
    x = np.asarray(x, dtype=float)
    return (np.log1p(x) + x * np.log1p(1 / x)) / math.log(2)


def main():
    out = Path(__file__).resolve().parent
    n = np.geomspace(9, 1e10, 301)
    gaussian_upper = 2 * g(n) - g(2 * n)
    target_rate = .2
    gaussian_lower = np.maximum(target_rate, gaussian_upper - g(9))
    non_gaussian_upper = np.full_like(n, 12.0)

    with (out / "correlation_cost_bounds.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["N", "gaussian_lower_bits", "gaussian_constructive_upper_bits", "separable_constructive_upper_bits"])
        writer.writerows(zip(n, gaussian_lower, gaussian_upper, non_gaussian_upper))

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.labelsize": 12, "svg.fonttype": "none"})
    fig, ax = plt.subplots(figsize=(8.8, 5.5), layout="constrained")
    navy, blue, purple = "#174a74", "#2f7eb5", "#8a3b8f"
    ax.fill_between(n, gaussian_lower, gaussian_upper, color=blue, alpha=.10)
    ax.plot(n, gaussian_upper, color=blue, lw=2.2,
            label="Gaussian construction: upper bound")
    ax.plot(n, gaussian_lower, color=navy, lw=2.0, ls="--",
            label="Gaussian converse: lower bound")
    ax.plot(n, non_gaussian_upper, color=purple, lw=2.3, ls=(0, (6, 3)),
            label="Separable non-Gaussian construction: upper bound")
    ax.set_xscale("log")
    ax.set_xlim(9, 1e10)
    ax.set_ylim(0, 36)
    ax.set_xticks([1e1, 1e3, 1e5, 1e7, 1e9])
    ax.set_xlabel("Local thermal occupation N (photons per reservoir mode)")
    ax.set_ylabel("Reservoir mutual information (bits per pair)")
    ax.set_title("Bounds on the correlation cost of quantum communication", loc="left", fontsize=15, pad=30)
    ax.text(0, 1.015, "Fixed target R = 0.2 qubits/use;  η = 0.9;  input energy E₀ ≈ 1.5148 photons/use",
            transform=ax.transAxes, fontsize=10.5, color="#424b56")
    ax.text(2e7, 13.1, "12-bit uniform upper bound", color=purple, fontsize=10.5)
    ax.grid(axis="y", color="#dbe2e8", lw=.7)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#84929f")
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    fig.savefig(out / "correlation_cost_bounds.svg", metadata={"Date": None})
    fig.savefig(out / "correlation_cost_bounds.preview.png", dpi=160)
    plt.close(fig)
    print(out / "correlation_cost_bounds.svg")


if __name__ == "__main__":
    main()
