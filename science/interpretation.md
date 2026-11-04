# Why structured hot noise can carry quantum information

At fixed attenuation, independent thermal reservoirs eventually make the signal channel entanglement breaking. Correlating the reservoirs changes the state of the collective mode that meets the signal. The central result compares how much mutual information is needed to make this change useful when both local thermal states become arbitrarily hot.

The Gaussian and non-Gaussian constructions use the same passive interface, signal-energy budget, and quantum communication task. Their difference is the structure of the joint reservoir state. The [cost theorem](model.md#main-result) makes this difference quantitative: a fixed positive quantum rate costs a constant amount of reservoir mutual information in the general class, while every Gaussian reservoir family requires a logarithmically growing amount.

## Two ways to use correlations

The matching Gaussian construction prepares the coupled collective mode in vacuum and puts all thermal energy in the unused collective mode. Reversing the balanced mixer makes each physical reservoir exactly thermal. The signal then sees a pure-loss channel. The mutual information of this bath is

```math
I_{\mathrm G}(N)=2g(N)-g(2N)
=\log_2N+\log_2e-1+o(1).
```

The general Gaussian lower bound has the same leading term. Allowing a squeezed collective mode or entanglement between the two reservoirs does not remove it, because the entanglement-breaking criterion constrains the collective mode's symplectic entropy. The endpoint decoder remains unrestricted throughout that comparison.

The non-Gaussian construction uses a different preparation. A finite label selects small residue cells in each quadrature, and the two coherent amplitudes are drawn independently conditional on that label. Their individual distributions remain exactly Gaussian, giving exact thermal quantum marginals. Their difference is a large lattice displacement plus a uniformly bounded remainder. Only the remainder affects the logical subsystem after decoding.

The label is part of reservoir preparation and is discarded. The receiver recovers the quantum information from the signal alone. The joint state is a separable mixture of coherent product states with a positive Glauber–Sudarshan representation. Such a preparation can still have quantum discord; separability and positive-P classicality do not assert a classical-classical density operator.

## Finite input energy and large displacements

An ordinary normalizable wave packet cannot remain unchanged under every arbitrarily large displacement. The construction does not require that property. It decomposes the oscillator Hilbert space into a logical qubit and an auxiliary subsystem. Lattice displacements act only on the auxiliary subsystem, and the decoder traces that subsystem out.

The two encoding packets have compact support and square-integrable weak first derivatives. Their oscillator energy is finite, and the two-dimensional compression of the number-operator quadratic form is exactly $`E_0 I`$. An arbitrary outer code, including entangled code states, therefore has the same energy per oscillator use. Large reservoir-induced displacements increase the energy carried by the discarded subsystem without increasing the source's input energy.

This is the role of the inherited modular-bosonic subsystem framework. The [modular-code proof](modular-code.md) gives the exact coordinate map, verifies global decoder invariance, and derives the actual decoded qubit channel. A surviving entangled state alone would not establish the claimed communication rate; the positive coherent information of that finite-dimensional channel supplies the coding statement.

## The useful collective reservoir stays highly mixed

The bounded-correlation construction cannot hide its success in a collective reservoir of bounded entropy. Let $`c,d`$ be the two outputs of the passive reservoir mixer. Their joint entropy is unchanged, and their total mean occupation is $`2N`$. Subadditivity and the thermal maximum-entropy bound give

```math
\begin{aligned}
S(c)
&\ge S(cd)-S(d)\\
&\ge2g(N)-I(E_1:E_2)-g(2N).
\end{aligned}
```

For $`I(E_1:E_2)\le I_0`$ with fixed $`I_0`$, this implies

```math
S(c)\ge\log_2N-O(1).
```

Its mean energy must also diverge, because $`S(c)\le g(\langle\hat n_c\rangle)`$. The noise remains hot in both entropy and energy. Its periodic displacement structure makes it compatible with the encoded logical degree of freedom.

For a Gaussian collective mode, high symplectic entropy eventually forces the attenuator to be entanglement breaking. The non-Gaussian bath avoids that inference while retaining the same local thermal marginals. This is the physical content of the resource separation.

## What the comparison measures

All rates are per signal use, with one fresh reservoir pair consumed on that use. The local occupations and the fixed signal-energy budget are matched between the Gaussian and general classes. The Gaussian converse allows arbitrary Gaussian bath correlations, including entanglement, and arbitrary non-Gaussian signal processing.

The statement concerns mutual information between the reservoirs. A finite preparation label supplies a useful upper bound on this resource, but it does not establish bounded thermodynamic work or an efficient sampler. At growing temperature, preparing the conditional amplitude distributions and handling the energetic output may become more costly even though the mutual-information budget stays bounded.

The bath state and channel parameters are known. Independent copies of the bath are supplied across uses. This excludes a temporal-memory resource from the comparison and permits an outer code tailored to each channel. The exact inner code and physical lattice scale are fixed as $`N`$ changes.

## Calibration and additional noise

The construction has a finite tolerance to additional displacement noise. Such perturbations change the small residual error seen by the logical qubit, and the [robustness bounds](robustness.md) quantify the resulting achievable rate.

A coupling or phase mismatch is different: its error can multiply an amplitude whose typical size grows as $`\sqrt N`$. A fixed laboratory mismatch is therefore not covered by the statement that the nominal attenuation is fixed. The specified perturbation model yields a sufficient accuracy scaling, while the central theorem concerns the exactly specified interface. No optimal calibration law or temperature-independent implementation cost is inferred.

The established contribution is the asymptotic correlation-resource law. Its practical use depends on how the reservoir preparation, modular decoding, and calibration can be realized in a chosen platform. Those implementation questions retain their own resource accounting.

## Relation to earlier environmental assistance

Environmental reactivation, non-Gaussian ancillary states, and lattice-compatible decoding are established mechanisms. Pirandola's separable reactivation results, the passive-environment constructions of Lami and collaborators, and the GKP/environment matching of Wang and Jiang are direct precedents. The exact thermal-marginal and fixed-loss correlation budget is the additional constraint studied here. The [source comparison](../references/related_work.md) separates the earlier results from this claim and identifies the role of the finite-energy proof.
