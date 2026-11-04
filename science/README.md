# Scientific overview

A fixed attenuator couples a signal to the difference of two locally thermal reservoir modes. With independent reservoirs, sufficiently high temperature makes the signal channel entanglement breaking. The project asks how much mutual information must be introduced between the reservoirs to preserve a fixed quantum communication rate at fixed input energy.

The [main theorem](model.md#main-result) compares two resource classes under the same interface. A finite-label, separable non-Gaussian preparation uses at most 12 bits of reservoir mutual information at every temperature. Every Gaussian preparation that supports a positive rate requires at least $`2g(N)-g(2N)-g(9)`$ bits at the explicit transmissivity $`\eta=0.9`$. A matching Gaussian construction has cost $`2g(N)-g(2N)`$. This gives constant versus logarithmically growing correlation cost.

## Follow the argument

1. [Model and cost theorem](model.md) defines the exact thermal marginals, fresh-pair channel, uniform input-energy condition, and optimized correlation costs. The benchmark fixes $`\eta=0.9`$, $`E_0\lt1.514818`$ photons, and a positive target rate independent of $`N`$.
2. [Reservoir construction](bath-construction.md) samples two coherent amplitudes independently conditional on a finite residue-cell label. Their marginals remain exactly thermal. Their difference is a lattice displacement plus a bounded error, while finite-register data processing bounds the mutual information.
3. [Modular code](modular-code.md) identifies a logical qubit and an auxiliary subsystem inside one oscillator. Every lattice displacement acts only on the auxiliary subsystem. Two sine packets encode the logical basis with the same finite energy for every input state.
4. [Achievable rate](achievable-rate.md) derives the exact decoded Pauli channel, bounds its parameters through an absolutely convergent Fourier series, and applies the finite-dimensional quantum coding theorem. The inner embedding makes the oscillator energy of every outer code explicit.
5. [Correlation converse](correlation-converses.md) compares an arbitrary communication protocol with the same protocol supplied product thermal reservoirs. The comparison output is separable. Relative-entropy data processing and a final maximally entangled-state test imply $`Q_2\le I(E_1:E_2)`$ above the product-bath entanglement-breaking threshold.
6. [Gaussian comparison](gaussian-comparison.md) uses the Gaussian entanglement-breaking criterion to bound the entropy of the coupled collective mode. Subadditivity and total reservoir energy then force logarithmic mutual information. Preparing that collective mode in vacuum gives the matching order.
7. [Robustness](robustness.md) separates additional displacement noise from errors in the passive coupling, attenuation, and receiver gain. It states the sufficient perturbation bounds with their temperature dependence.
8. [Interpretation](interpretation.md) explains why bounded correlations leave the useful collective reservoir at diverging entropy and energy, and identifies the physical resources beyond the stated cost.

## What carries the result

The state preparation and the decoder solve different parts of the problem. The preparation enforces the local thermal constraints with a finite correlation budget. The decoder removes an unbounded lattice component without requiring the finite-energy input packets to be translation invariant. Their combination yields a finite-dimensional channel whose positive coherent information is uniform in temperature.

The converses use an entanglement-breaking reference and its Gaussian criterion. They allow arbitrary endpoint operations and do not infer impossibility from a vanishing Gaussian-input lower bound. The Gaussian cost is therefore a reservoir-state restriction, not a restriction on the receiver's code.

For direct verification, start with the [numerical guide](../verification/README.md). For attribution, use the [primary-source comparison](../references/related_work.md), which distinguishes this resource law from established environmental reactivation and GKP-assisted transmission.
