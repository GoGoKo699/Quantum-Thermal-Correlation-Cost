# Related work and attribution

The contribution concerns a particular resource constraint. Each fresh reservoir pair has exactly thermal marginals of occupation $`N`$. The passive interface, its transmissivity, and the signal-energy budget are fixed as $`N`$ increases. The resource is the pair's quantum mutual information; the preparation label and all reservoir outputs are unavailable to the communication endpoints.

Under these constraints, a finite classical preparation label supplies a separable non-Gaussian reservoir with a temperature-uniform positive quantum rate. The cost for a fixed rate in the established range is $`\Theta(1)`$, whereas Gaussian reservoirs require $`\Theta(\log N)`$. The relevant predecessors establish environmental reactivation, environment engineering, and modular decoding. The comparison below identifies how those ingredients enter this result.

## Closest physical comparisons

| Source and inspected result | Established contribution | Relation to the present cost law |
|---|---|---|
| [Pirandola (2013)](#pirandola-2013), Secs. II–III, especially the symmetric and antisymmetric Gaussian analyses | Separable correlations reactivate entanglement despite locally entanglement-breaking noise. Some thresholds need fewer than two correlation bits. | The bounded-bit hot limit follows $`\tau\to1`$ with $`\omega=(1+\tau)/(1-\tau)`$. Here the nonzero loss remains fixed while $`N\to\infty`$. |
| [Pirandola et al. (2021)](#pirandola-et-al-2021), Results and Supplementary Secs. 2–3 | Correlated Gaussian thermal noise reactivates swapping, teleportation, distillation, and key distribution at a relay, with finite-energy examples and an experiment. | These are important operational precedents. The present theorem holds a correlation budget fixed in a different, single-input interface and an unbounded-temperature limit. |
| [Lami et al. (2020)](#lami-et-al-2020), Theorem 2 | For every transmissivity $`\lambda>0`$, a suitable pure environment gives a universal positive quantum-rate lower bound at input-energy budget $`1/2`$. | Finite signal energy and a positive rate under engineered bosonic noise are inherited capabilities. The new constraint is exact hot thermal marginals and the mutual-information cost of their correlations. |
| [Wang and Jiang (2025)](#wang-and-jiang-2025), Theorem 2, Secs. III.3 and IV | Matching ideal GKP lattices at the signal and environment ports gives perfect transfer at suitable rational transmissivities, including arbitrarily small values. The paper develops logical/gauge structure and finite-energy performance. | Matching environmental structure to a code and using a gauge subsystem are established. The present bath is a highly mixed, positive-P state with exact thermal marginals and a bounded pair-correlation budget. |
| [Voss et al. (2026)](#voss-et-al-2026), Secs. II–IV | Fock, cat, and squeezed-cat ancillas support optimized and analytical passive environment-assisted communication schemes. | The study chooses nonclassical ancilla states. The present resource theorem instead constrains local thermal states and charges only their joint mutual information. |
| [Hou et al. (2025, 2026)](#hou-et-al-2025-and-2026), the direct-transduction noise formula and its extension | Cross correlations and tunable coupling phases suppress effective Gaussian noise in a multiport transducer. | These are physical precedents for correlated-noise engineering. Their multiport apparatus and additional inputs differ from the fixed two-reservoir interface used in the cost theorem. |

The first two comparisons prevent attributing environmental reactivation itself to this work. The latter three prevent attributing the general advantage of engineered non-Gaussian environments or code-matched noise to this work. The surviving result is the asymptotic correlation-cost separation under the simultaneous marginal, loss, and signal-energy constraints.

### Pirandola (2013)

Stefano Pirandola, **Entanglement reactivation in separable environments**, *New Journal of Physics* **15**, 113046 (2013). [Publisher](https://doi.org/10.1088/1367-2630/15/11/113046) · [Full preprint, v4](https://arxiv.org/html/1210.2119v4).

Section II also treats non-Gaussian correlated phase rotations. These are distinct physical channels from the thermal-marginal beam-splitter interface here. Section III quantifies Gaussian environmental correlations by mutual information, classical correlations, and discord. Its few-bit hot limit changes loss together with temperature. The paper already demonstrates that equal scalar correlation measures need not imply equal usefulness.

### Pirandola et al. (2021)

Stefano Pirandola, Carlo Ottaviani, Christian S. Jacobsen, Gaetana Spedalieri, Samuel L. Braunstein, Tobias Gehring, and Ulrik L. Andersen, **Environment-assisted bosonic quantum communications**, *npj Quantum Information* **7**, 77 (2021). [Publisher](https://doi.org/10.1038/s41534-021-00413-2) · [Full preprint, v1](https://arxiv.org/html/2003.09246v1).

The Gaussian relay model has collective-noise parameters proportional to $`(\tau^{-1}-1)(\omega-g)`$ and $`(\tau^{-1}-1)(\omega+g')`$. Correlations can keep them small enough for useful protocols. Its additive-noise limit takes $`\tau\to1`$ and $`\omega\to\infty`$ jointly. The present Gaussian converse instead quantifies the correlation cost when loss is fixed.

### Lami et al. (2020)

Ludovico Lami, Martin B. Plenio, Vittorio Giovannetti, and Alexander S. Holevo, **Bosonic quantum communication across arbitrarily high loss channels**, *Physical Review Letters* **125**, 110504 (2020). [Publisher](https://doi.org/10.1103/PhysRevLett.125.110504) · [Full preprint, v2](https://arxiv.org/html/2003.08895v2).

The general attenuator is formed by a beam splitter and a supplied environment state. Theorem 2 selects that state as a function of transmissivity, using vacuum, low-Fock superpositions, or Fock states depending on the parameter. The theorem does not charge correlations between two prescribed thermal marginals. This work retains that general-attenuator viewpoint while imposing the thermal correlation resource.

### Wang and Jiang (2025)

Zhaoyou Wang and Liang Jiang, **Passive environment-assisted quantum communication with GKP states**, *Physical Review X* **15**, 021003 (2025). [Publisher](https://doi.org/10.1103/PhysRevX.15.021003) · [Full preprint, v2](https://arxiv.org/html/2401.16781v2).

Theorem 2 supplies a lattice-matching condition for simultaneous logical transmission through a beam splitter. Section III.3 and Appendix E identify output logical and gauge subsystems. Section IV studies finite-energy GKP states and coherent information; Appendix H addresses sensitivity to transmissivity. These constructions motivate engineered noise compatible with logical information. The exact thermal-marginal and bounded-mutual-information requirements are the additional constraints in the present problem.

### Voss et al. (2026)

Evelyn Voss, Bikun Li, Zhaoyou Wang, and Liang Jiang, **Passive Environment-Assisted Quantum Communication**, arXiv:2602.21549v2 (2026). [Abstract and version history](https://arxiv.org/abs/2602.21549v2) · [Full text](https://arxiv.org/html/2602.21549v2).

Sections II–IV optimize and analyze finite-dimensional encodings with non-Gaussian ancillas. They include cat/comb constructions and Fock-environment mechanisms that suppress leakage of logical information. The comparison uses arXiv version 2, dated 27 February 2026.

### Hou et al. (2025 and 2026)

Yu-Bo Hou, Xiaoan Ai, Ruizhe You, and Changchun Zhong, **Correlated noise can be beneficial to quantum transducers**, *Physical Review Research* **7**, L032042 (2025). [Publisher and full text](https://doi.org/10.1103/zq39-wzdb).

Yu-Bo Hou, Xiaoan Ai, Pengbo Li, and Changchun Zhong, **High-Performance Quantum Transduction with Correlated Noise**, arXiv:2608.06683 (2026). [Preprint](https://arxiv.org/abs/2608.06683).

The 2026 direct-conversion model uses $`\langle c^\dagger b\rangle=n_{\rm th}\chi`$, with effective thermal noise proportional to local occupations and interference terms. It extends the earlier proposal to entanglement-assisted transduction. Correlation strength $`\chi`$ is not a mutual-information cost, and the full transducer contains additional ports and tunable parameters. The Gaussian lower bound in this repository applies to the explicitly stated two-bath interface, rather than to every Gaussian transduction architecture.

## Mathematical ingredients

| Ingredient | Primary source | Use here |
|---|---|---|
| Oscillator displacement codes | [Gottesman, Kitaev, and Preskill (2001)](https://doi.org/10.1103/PhysRevA.64.012310) | The established lattice-code setting. The construction here uses normalizable packets and a subsystem decoder. |
| Modular logical/gauge decomposition | [Pantaleoni, Baragiola, and Menicucci (2020)](https://arxiv.org/html/1907.08210v3) | The parity of position bins gives a virtual qubit; tracing the complementary gauge is an inherited operation. |
| Loss, amplification, and displacement-noise coding | [Noh, Albert, and Jiang (2019), Corollary 5](https://arxiv.org/html/1801.07271v2) | The loss-followed-by-amplification displacement channel and its quadrature variance. The coherent bath displacements are then accounted for explicitly. |
| Coherent-information achievability | [Devetak (2005), Theorem 5 and Sec. 5](https://arxiv.org/html/quant-ph/0304127v6) | Applied to the finite-dimensional decoded qubit channel. The inner encoding gives every outer-code input the same oscillator energy. |
| Gaussian entanglement-breaking criterion | [Holevo (2008), Theorem 2 and Sec. 6](https://arxiv.org/html/0802.0235v1) | For $`X=\sqrt\eta I`$, the criterion depends on the determinant of the noise covariance. It includes squeezed and correlated Gaussian bath states. |
| Gaussian coherent information | [Holevo and Werner (2001)](https://arxiv.org/html/quant-ph/9912067v1) | Gaussian entropy benchmarks. The matching Gaussian feasibility proof uses the same finite-energy inner code as the main construction. |
| Relative-entropy data processing | [Müller-Hermes and Reeb (2017), Theorem 1](https://arxiv.org/html/1512.06117v3) | Valid for separable Hilbert spaces. Comparison with the product-thermal entanglement-breaking channel gives the finite-block correlation converse. |
| Environment-parametrized channels | [Wilde, Berta, Hirche, and Kaur (2020), Sec. VII.2](https://arxiv.org/html/1808.01498v2) | A common interaction converts environment-state distinguishability into bounds for adaptive channel protocols. The reference environment here is the product of the prescribed thermal marginals. |
| Conditional-entropy continuity | [Winter (2016), Lemma 2](https://arxiv.org/html/1507.07775v6) | The calibration bound is applied after qubit decoding, with a two-dimensional reference. |

The general correlation converse is an application of established data processing and a maximally entangled-state test. The Gaussian converse combines the established entanglement-breaking criterion with thermal entropy maximization and subadditivity. The project claims the resulting resource law and its explicit thermal-marginal construction, while crediting these proof mechanisms.

Complete bibliographic entries are in [references.bib](references.bib).
