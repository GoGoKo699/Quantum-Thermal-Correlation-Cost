# From Wilde's foundations to thermal correlation cost

The practical question is how to send an unknown quantum state through a lossy interface whose environment becomes increasingly hot. The sender cannot reduce the two reservoirs' prescribed local thermal occupations. The available freedom is to correlate the reservoirs before they interact with the signal.

Wilde's book supplies the language for states, channels, information, and coding. This bridge connects that language to the [specific model](../science/model.md), where oscillator energy and reservoir correlations must be accounted for separately.

## The selected edition and the open text

**Educational anchor:** Mark M. Wilde, *Quantum Information Theory*, **second edition**, Cambridge University Press, **2017**, [DOI: 10.1017/9781316809976](https://doi.org/10.1017/9781316809976). The publisher's [full frontmatter and contents](https://assets.cambridge.org/97811071/76164/frontmatter/9781107176164_frontmatter.pdf) identify this edition and its chapter and section numbering.

**Open version of the same work:** Wilde, *From Classical to Quantum Shannon Theory*, [arXiv:1106.1445v8](https://arxiv.org/abs/1106.1445v8), revised **14 July 2019**, with [full HTML text](https://arxiv.org/html/1106.1445v8). The author's [book page](https://www.markwilde.com/) connects this open work to the Cambridge second edition. The open version contains later corrections and is not the 2017 typeset book.

All section numbers below refer to the **2017 second edition**, checked against its publisher contents. The topic descriptions are a guide to their use here. No page number from the 2019 text is presented as 2017 pagination. These are two access forms of one educational anchor.

## Sections to use when they become relevant

| Foundation needed | Sections in the 2017 edition | Connection to this project |
|---|---|---|
| Qubits, composite systems, and entanglement | 3.2, 3.3, 3.5, 3.6 | Distinguish the logical qubit from the oscillator carrying it and from a reference used to test transmission. |
| Mixed states, local states, and classical labels | 4.1, 4.3 | Read the thermal marginals and the conditional preparation $`\sum_c p_c\rho_c\otimes\rho_c`$. |
| Channels, discarded systems, and dilations | 4.4 to 4.6; 5.1, 5.2 | Combine bath preparation, passive mixing, attenuation, amplification, and coherent subsystem extraction into a channel. |
| Distance and transmission accuracy | 9.1 to 9.3, 9.5 | Interpret entanglement fidelity and the normalized trace distance used in robustness. |
| Entropy, conditional entropy, and correlation | 10.1; 11.1, 11.2, 11.4 to 11.8 | Separate label entropy, reservoir mutual information, and coherent information of the decoded channel. |
| Information inequalities and continuity | 11.9, 11.10 | Understand the data-processing and entropy-accounting steps before checking their oscillator-domain hypotheses. |
| Communication tasks and coding | 13.5; 24.1, 24.3 to 24.6 | Turn a positive coherent-information value for a qubit channel into asymptotic transmission. The code discussion provides context for protecting logical degrees of freedom. |
| Local operations and separable comparisons | 19.2 | Understand why the product-bath comparison cannot create sender-receiver entanglement. |

The [milestone map](milestones.md) selects these foundations at the points where they enter the scientific argument. The oscillator construction below requires additional local derivations; its exact decoder is not obtained by citing the book's code examples.

## A worked example with two classical environment bits

Consider an unknown signal qubit $`A`$ and two environment bits $`E_1,E_2`$. A bit value $`x=1`$ applies the phase flip $`Z`$ to the signal, while $`x=0`$ does nothing. Here $`Z|0\rangle=|0\rangle`$ and $`Z|1\rangle=-|1\rangle`$. Let both environment bits act once, and discard them afterward.

For fixed bit values $`x,y`$, the signal transformation is

```math
\rho\longmapsto Z^{x+y}\rho Z^{x+y}.
```

Because $`Z^2=I`$, two phase flips cancel. The resulting channel depends on the parity of the two bits. Neither the sender nor the receiver learns either bit value.

Compare two preparations with **exactly the same local states**:

```math
\sigma^{\mathrm{ind}}_{E_1E_2}
=\frac14\sum_{x,y=0}^{1}|xy\rangle\langle xy|,
\qquad
\sigma^{\mathrm{corr}}_{E_1E_2}
=\frac12|00\rangle\langle00|
 +\frac12|11\rangle\langle11|.
```

Each environment bit is $`I_2/2`$ in both cases. The correlated state is separable: it is a mixture of two product states.

For the independent preparation, even and odd parity each have probability $`1/2`$. Thus

```math
\mathcal N_{\mathrm{ind}}(\rho)
=\frac12\rho+\frac12Z\rho Z.
```

If $`\rho=\begin{pmatrix}a&z\\z^*&1-a\end{pmatrix}`$, the result is $`\mathrm{diag}(a,1-a)`$. The off-diagonal entries, which carry phase coherence, vanish. This is the same channel as measuring in the $`|0\rangle,|1\rangle`$ basis and preparing the measured basis state, so it is entanglement breaking.

For the correlated preparation, the bits always agree. The parity is always even, and

```math
\mathcal N_{\mathrm{corr}}(\rho)=\rho.
```

The information accounting is equally explicit. Each marginal has entropy one bit. The independent joint state has four equal eigenvalues and entropy two bits; the correlated joint state has two equal nonzero eigenvalues and entropy one bit. Therefore

```math
I(E_1:E_2)_{\mathrm{ind}}=1+1-2=0,
\qquad
I(E_1:E_2)_{\mathrm{corr}}=1+1-1=1.
```

One shared random bit is sufficient to prepare the correlated environment. It is used at preparation, not sent to the receiver as side information.

To see the difference at the output, send $`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$ and measure in the $`|+\rangle,|-\rangle`$ basis. The independent bath gives either outcome with probability $`1/2`$; the correlated bath gives $`+`$ with probability one. A stronger quantum test sends half of $`|\Phi\rangle_{TA}=(|00\rangle+|11\rangle)/\sqrt2`$, keeping reference $`T`$ at the sender. The correlated bath preserves the Bell state. The independent bath yields the separable state $`(|00\rangle\langle00|+|11\rangle\langle11|)/2`$.

This example isolates the distinction between local noise and joint environmental structure. It is a finite-bit illustration, with a controlled-phase interaction. It does not establish the oscillator result, which must preserve exact thermal marginals at every finite occupation, use the specified passive interface, and satisfy a uniform signal-energy budget.

## Notation and assumption translation

| Book language | Repository convention and meaning |
|---|---|
| A state $`\rho_A`$ and its local states | The transmitted state and the reservoir state are separate objects. The latter is $`\sigma_{E_1E_2}`$, with both marginals fixed to $`\tau_N`$. |
| Quantum entropy written $`H(A)_\rho`$ | The science pages write $`S(\rho_A)`$. Classical Shannon entropy is $`H(C)`$ or $`H(p)`$. All logarithms are base two. |
| Quantum mutual information written with a semicolon | $`I(E_1:E_2)_\sigma=S(E_1)+S(E_2)-S(E_1E_2)`$. A colon is a notational choice, not a different information measure. |
| Coherent information of a state or channel | For a purification on reference $`T`$ and input $`A`$, let $`\omega_{TB}=(\mathrm{id}_T\otimes\Lambda)(\psi_{TA})`$. Then $`I_c(\rho_A,\Lambda)=S(B)_\omega-S(TB)_\omega`$. |
| Trace norm and fidelity | The robustness variable is $`t=\frac12\lVert\rho-\sigma\rVert_1`$. For a pure target $`\lvert\Phi\rangle`$, the fidelity is the test probability $`\langle\Phi\rvert\rho\lvert\Phi\rangle`$, not its square root. |
| An environment in an isometric description | The physical reservoirs, unused mixer output, environment output, and mathematical purification are not additional information supplied to either endpoint. |
| Repeated independent channel uses | Each use receives one fresh pair in the same state $`\sigma`$, so an $`m`$-use block consumes $`\sigma^{\otimes m}`$. |
| A reference system often denoted $`R`$ | The scalar $`R`$ in the cost definition is the target rate. This example uses $`T`$ for the reference to keep those roles distinct. |
| A channel symbol $`\mathcal N`$ and block length | The scalar $`N`$ is reservoir occupation; the block length is $`m`$. They describe different limits. |
| Energy of the physical carrier | Here $`[\hat q,\hat p]=i`$, vacuum variance is $`1/2`$, and $`\hat n=(\hat q^2+\hat p^2-1)/2`$. The budget $`E_0`$ counts input photons per use. |

The definitions of the information measures and distance conventions can be compared directly with Chapters 9 and 11 of the [version-qualified open text](https://arxiv.org/html/1106.1445v8). The physical conventions and capacity task are specified in the [model](../science/model.md#oscillator-and-channel-conventions).

Two assumption changes require particular care. First, a finite mean energy does not make an oscillator finite dimensional. The proof supplies an explicit two-dimensional inner code before applying a finite-dimensional coding theorem. Second, the code must meet the energy budget for **every** logical input. Evaluating the energy of only one convenient average input would not establish that requirement.

## The steps from the book to the oscillator result

### Exact thermal states from a finite label

In the [reservoir construction](../science/bath-construction.md), a label $`C`$ identifies a small cell of a coherent amplitude's residue modulo a fixed period. Given $`C=c`$, the two amplitudes are sampled independently from the actual thermal distribution restricted to that cell. Summing the conditional states with their actual probabilities recovers the thermal state exactly.

The preparation has the form

```math
\sigma_{E_1E_2}=\sum_c p_c\,\rho_c\otimes\rho_c.
```

Applying a preparation channel to the classical register and using data processing gives

```math
I(E_1:E_2)_\sigma\le I(C:E_2)\le H(C).
```

For $`64`$ cells in each of two quadratures there are $`64^2`$ label values, giving the upper bound $`H(C)\le12`$ bits. The label distribution need not be uniform. Quantum mutual information need not equal label entropy because different conditional oscillator states can be nonorthogonal.

### A logical subsystem inside the oscillator

The two coherent amplitudes can differ by a large integer number of periods while their residues remain close. After the specified receiver amplifier, the resulting quadrature shift is a lattice displacement plus a bounded residue error and a fixed Gaussian noise term.

The [modular code](../science/modular-code.md) coherently identifies a qubit inside the oscillator and traces a complementary subsystem. Every displacement on the chosen lattice acts only on that complementary subsystem. This is an operator statement about the decoder, including inputs entangled with a reference. It does not require translation-invariant finite-energy codewords, and it does not measure the logical qubit's position-bin parity.

The codewords are normalizable sine packets. Their weak derivatives are square integrable, which permits the energy calculation in the number operator's quadratic-form domain. This local calculation is the extra ingredient that an abstract finite-dimensional code theorem does not provide.

### A finite-dimensional coding theorem with physical energy attached

Let $`V`$ be the qubit-to-oscillator encoding, $`\mathcal A_{1/\eta}`$ the receiver amplifier, and $`\mathcal R`$ the modular decoder. The effective qubit channel is

```math
\Lambda_N
=\mathcal R\circ\mathcal A_{1/\eta}
 \circ\mathcal N_{\eta,\sigma_N}\circ\mathcal V,
\qquad
\mathcal V(\rho)=V\rho V^\dagger.
```

For the prepared bath, this is a Pauli channel. With maximally mixed input, its output entropy is one bit and its reference-output state is diagonal in the Bell basis with probabilities $`p`$. Consequently its coherent information is $`1-H(p)`$. The [rate proof](../science/achievable-rate.md) bounds these probabilities using an absolutely convergent Fourier series and supplies the temperature-uniform lower bound.

The [same proof](../science/achievable-rate.md#from-a-qubit-code-to-an-energy-constrained-oscillator-code) applies the quantum coding theorem to independent uses of $`\Lambda_N`$. Lifting that outer code through $`V^{\otimes m}`$ is justified by

```math
V^\dagger\hat nV=E_0I_2,
\qquad
E_0=\frac{2\pi}{3}-\frac1{4\pi}-\frac12.
```

The equality is a quadratic-form identity. It gives total input energy $`mE_0`$ for every outer-code state, including entangled states. The oscillator claim therefore uses a finite-dimensional coding theorem together with an explicit physical embedding, rather than assuming that an average thermal input meets the stronger energy convention.

### Converse arguments with different domains of validity

The [general converse](../science/correlation-converses.md) compares the actual reservoir with $`\tau_N\otimes\tau_N`$, holding the complete communication protocol fixed. For $`\eta=0.9`$ and $`N\ge9`$, the comparison channel is entanglement breaking. Relative-entropy data processing bounds the distinguishability of the two final outputs by the total reservoir mutual information. A final test for a maximally entangled state then bounds the communication rate.

The [Gaussian comparison](../science/gaussian-comparison.md) adds a restriction on the reservoir state. For Gaussian noise, avoiding an entanglement-breaking signal channel bounds the coupled mode's symplectic entropy. Entropy conservation through the mixer and subadditivity then require a correlation cost of order $`\log N`$.

That Gaussian entropy restriction is not applied to the non-Gaussian construction. Its useful collective mode remains hot and has diverging entropy. The decoder can tolerate that mode's structured displacement noise. A vanishing coherent-information lower bound for one input would not replace either converse.

## Foundations, local derivations, and research dependencies

| Layer | What it supplies | Where to check it |
|---|---|---|
| The selected textbook | Density operators, channels, purifications, entropy and information measures, fidelity, coding tasks, and finite-dimensional quantum capacity foundations. | The section map above and the [30 milestones](milestones.md). |
| Explicit oscillator calculations | Exact thermal marginals, finite-label correlation bound, displacement normalization, modular decoder, finite-energy packets, Fourier estimates, and the composition with an outer qubit code. | [Bath construction](../science/bath-construction.md), [modular code](../science/modular-code.md), and [achievable rate](../science/achievable-rate.md). |
| Imported coding and structural results | Coherent-information achievability; the modular logical/gauge framework; attenuation followed by amplification as displacement noise. | The accounts credit Devetak, Pantaleoni–Baragiola–Menicucci, and Noh–Albert–Jiang in the [mathematical attribution table](../references/related_work.md#mathematical-ingredients). |
| Research-level converse ingredients | Relative-entropy data processing on separable Hilbert spaces; the environment-program comparison; the one-mode Gaussian entanglement-breaking criterion. | [Correlation converse](../science/correlation-converses.md) and [Gaussian comparison](../science/gaussian-comparison.md), citing Müller-Hermes–Reeb, Wilde–Berta–Hirche–Kaur, and Holevo. |
| A quantitative stability ingredient | Conditional-entropy continuity applied after qubit decoding, with a two-dimensional reference. | [Robustness](../science/robustness.md), citing Winter's bound. |

The research papers support attribution and exact theorem hypotheses. They are proof dependencies, not additional educational anchors. In particular, the universal converse still depends on an infinite-dimensional data-processing theorem; an accessible opening example does not remove that requirement.

The next step is the [milestone map](milestones.md). For a direct check of the final statement, use the [model and main theorem](../science/model.md#main-result); for finite computational checks, use [verification](../verification/README.md).
