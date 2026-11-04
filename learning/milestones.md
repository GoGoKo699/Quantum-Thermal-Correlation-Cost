# Common understanding map

This map connects the physical model, the construction, and the comparison theorem through exactly thirty milestones. The first twelve assemble the background needed to state the problem with its resources intact. The remaining eighteen follow the new mechanism from a finite preparation label to a positive communication rate, then combine the converse, Gaussian comparison, and robustness bounds into the complete result. Each phase moves from individual objects to an integrated account.

The educational anchor is Mark M. Wilde, *Quantum Information Theory*, second edition (2017), [DOI: 10.1017/9781316809976](https://doi.org/10.1017/9781316809976). All section numbers below refer to that edition. The [anchor bridge](anchor-bridge.md) explains the notation and assumptions shared with the book. Oscillator normalization, modular subsystem extraction, the reservoir construction, and the quantitative bounds are supplied by the linked project sources. These topics extend the anchor's finite-dimensional information-theoretic framework.

| Phase | Milestones | Scientific role |
|---|---|---|
| Background and preliminaries | M01–M12 | Connect quantum states, oscillator energy, correlations, channels, and coding to the precise communication task. |
| Narrative and innovation | M13–M30 | Build the reservoir and code, establish both cost laws, and interpret their physical scope. |

The milestones identify the concepts and dependencies needed to understand the project. The [science pages](../science/README.md) contain the complete statements and proofs. A source pointer to the anchor supplies general language; a pointer to a project page supplies the particular claim made here.

## Phase I. Background and preliminaries

<a id="M01"></a>
### M01. A qubit and its coherence

**Central question:** What information in a qubit must survive a quantum communication channel?

**Understanding target:** Distinguish a coherent superposition from a classical mixture with the same measurement probabilities in one basis. Recognize the off-diagonal entries of a density operator as part of the information to preserve, including when the qubit is entangled with another system.

**Dependencies and story role:** This is the starting point. It identifies the logical system that the oscillator encoding will carry.

**Conceptual connection:** The later displacement calculation must preserve both populations and coherence. A channel that reproduces two classical labels need not transmit an unknown qubit.

**Source pointers:** Wilde §§3.2–3.3 and 4.1; [the decoded displacement channel](../science/modular-code.md#exact-decoded-displacement-channel).

<a id="M02"></a>
### M02. An oscillator as a quantum carrier

**Central question:** How does an oscillator carry a qubit while its energy remains finite?

**Understanding target:** Relate the quadratures $`\hat q,\hat p`$, coherent amplitude, and photon number through $`[\hat q,\hat p]=i`$ and $`\hat n=(\hat q^2+\hat p^2-1)/2`$. Distinguish finite mean photon number from a restriction to finitely many Fock states, and keep the vacuum quadrature variance $`1/2`$ explicit.

**Dependencies and story role:** Builds on [M01](#M01). It introduces the physical carrier and the resource that the signal encoder must control.

**Conceptual connection:** The qubit describes logical information; the oscillator provides a larger Hilbert space in which that information and an auxiliary subsystem can coexist.

**Source pointers:** Wilde §4.1 for the state formalism; [oscillator conventions](../science/model.md#oscillator-and-channel-conventions) and [finite-energy codewords](../science/modular-code.md#normalizable-codewords-and-their-exact-energy) for the oscillator-specific content.

<a id="M03"></a>
### M03. Thermal states and exact local constraints

**Central question:** What does it mean for each reservoir to be exactly thermal?

**Understanding target:** Identify $`\tau_N`$ as a full density operator with mean photon number $`N`$, and understand its Gaussian mixture of coherent states. Equality to $`\tau_N`$ fixes every local measurement distribution, beyond a mean energy or covariance matrix alone.

**Dependencies and story role:** Builds on [M02](#M02). It specifies the local constraint within which the joint reservoir state can be changed.

**Conceptual connection:** A preparation can alter correlations between reservoirs while leaving each local state unchanged. The project uses this freedom without changing either reservoir's temperature.

**Source pointers:** Wilde §§4.1 and 11.1; [thermal-state definition](../science/model.md#oscillator-and-channel-conventions) and [coherent-state representation](../science/bath-construction.md#the-thermal-state-and-the-residue-partition).

<a id="M04"></a>
### M04. Joint states, reference systems, and fidelity

**Central question:** How can identical local states conceal different correlations, and how is successful quantum transmission recognized?

**Understanding target:** Use the partial trace to distinguish a joint state from its marginals. Interpret a reference system as recording coherence that a communication protocol must preserve. Understand why entanglement fidelity tests quantum transmission more strongly than checking selected classical inputs.

**Dependencies and story role:** Builds on [M01](#M01) and [M03](#M03). It connects the reservoir's joint state to the operational goal of sending a logical system.

**Conceptual connection:** Correlations enter twice: as a resource inside the reservoir pair and as the reference-output entanglement that the protocol seeks to preserve.

**Source pointers:** Wilde §§4.3, 5.1, 9.2–9.3, and 9.5; [capacity and energy accounting](../science/model.md#capacity-and-energy-accounting); the finite-qubit example in the [anchor bridge](anchor-bridge.md).

<a id="M05"></a>
### M05. A channel from a signal and an environment

**Central question:** How does an inaccessible reservoir define the signal channel?

**Understanding target:** Connect a completely positive trace-preserving map to a joint interaction followed by a partial trace. Identify the balanced reservoir modes $`c,d`$, the attenuator coupling to $`c`$, and the outputs that are discarded. The preparation label and reservoir purification are unavailable to both endpoints.

**Dependencies and story role:** Builds on [M02](#M02) and [M04](#M04). It turns a reservoir state into a precise communication channel.

**Conceptual connection:** Changing an environment's correlations can change the induced signal channel even when all environment marginals are fixed. The allowed endpoint information is part of that channel model.

**Source pointers:** Wilde §§4.4–4.6 and 5.2; [the physical interface](../science/model.md#oscillator-and-channel-conventions) and [receiver amplification](../science/bath-construction.md#the-physical-channel-and-receiver-amplification).

<a id="M06"></a>
### M06. Entropy under an energy constraint

**Central question:** What can energy and entropy reveal about a hot oscillator?

**Understanding target:** Relate von Neumann entropy, joint entropy, and subadditivity. Understand that the thermal state maximizes entropy at fixed mean photon number, giving the bound $`S(\rho)\le g(N)`$. Recognize the logarithmic growth of $`g(N)`$ and the distinction between large energy and large entropy in a general state.

**Dependencies and story role:** Builds on [M03](#M03) and [M04](#M04). It supplies the accounting tools used to compare the two collective reservoir modes.

**Conceptual connection:** The Gaussian converse constrains entropy in the useful mode and energy in the unused mode. Their combination forces a growing correlation cost.

**Source pointers:** Wilde §§11.1–11.2 and 11.9; [thermal entropy](../science/model.md#oscillator-and-channel-conventions) and [reservoir entropy accounting](../science/gaussian-comparison.md#entropy-accounting-for-the-two-reservoirs).

<a id="M07"></a>
### M07. Classical labels and conditional preparation

**Central question:** How can a finite shared label prepare correlated quantum reservoirs?

**Understanding target:** Read a classical-quantum state and a mixture of conditionally independent product states. Understand how averaging conditional preparations produces a separable joint state. Distinguish the label's finite alphabet, its Shannon entropy, and the quantum correlations of the prepared reservoirs.

**Dependencies and story role:** Builds on [M03](#M03), [M04](#M04), and [M06](#M06). It supplies the preparation language for the main construction.

**Conceptual connection:** A shared label can coordinate two unbounded coherent amplitudes without being supplied to the receiver. The resulting bath is separable, but its induced noise can still be useful for quantum communication.

**Source pointers:** Wilde §§4.3, 10.1, and 13.3; [conditional reservoir preparation](../science/bath-construction.md#preparation-and-exact-marginals).

<a id="M08"></a>
### M08. Mutual information and data processing

**Central question:** What measure charges the reservoir correlation, and why does local processing bound it?

**Understanding target:** Connect $`I(A:B)`$ to $`D(\rho_{AB}\|\rho_A\otimes\rho_B)`$. Understand data processing as the statement that applying the same channel to two states cannot increase their relative entropy. For a shared-label preparation, connect this principle to $`I(E_1:E_2)\le H(C)`$.

**Dependencies and story role:** Builds on [M05](#M05), [M06](#M06), and [M07](#M07). It identifies the cost measure and the inequality used in both directions of the proof.

**Conceptual connection:** Local preparation gives the achievability cost bound; processing the whole communication protocol gives the converse bound.

**Source pointers:** Wilde §§11.6, 11.8–11.9; [resource charge](../science/model.md#capacity-and-energy-accounting) and [finite-label information bound](../science/bath-construction.md#mutual-information-is-bounded-by-the-finite-label).

<a id="M09"></a>
### M09. Noise that breaks entanglement

**Central question:** When does a channel destroy quantum communication regardless of the chosen code?

**Understanding target:** Interpret an entanglement-breaking channel through its action on every input jointly with a reference. Understand why local operations and classical communication cannot recover entanglement from a separable state without another entanglement resource. Distinguish this channel property from a nonpositive coherent-information value for one particular input.

**Dependencies and story role:** Builds on [M02](#M02), [M04](#M04), [M05](#M05), and [M06](#M06). It prepares the product-bath reference and the Gaussian obstruction.

**Conceptual connection:** The project needs a channel-wide impossibility statement to compare all possible endpoint codes, including non-Gaussian codes.

**Source pointers:** Wilde §§4.6–4.7 and 19.2; [product-bath comparison](../science/correlation-converses.md#the-product-bath-comparison) and [Gaussian entanglement-breaking condition](../science/gaussian-comparison.md#the-collective-mode-entanglement-breaking-condition).

<a id="M10"></a>
### M10. Coherent information and quantum communication

**Central question:** How does a calculation for one finite-dimensional channel yield an asymptotic quantum communication rate?

**Understanding target:** Interpret coherent information as $`I_c=-S(T|B)`$ for an input purified by a reference $`T`$. Connect positive coherent information to coding over independent channel uses and entanglement fidelity tending to one. Distinguish an achievable lower bound from an exact capacity formula.

**Dependencies and story role:** Builds on [M04](#M04), [M05](#M05), [M06](#M06), and [M09](#M09). It supplies the coding theorem used after oscillator decoding.

**Conceptual connection:** The proof reduces the physical oscillator channel to a qubit channel before invoking finite-dimensional unassisted coding. Energy accounting remains a separate obligation of the encoding map.

**Source pointers:** Wilde §§11.4–11.5, 13.5, 24.1, and 24.3–24.5; [lifting the qubit code](../science/achievable-rate.md#from-a-qubit-code-to-an-energy-constrained-oscillator-code).

<a id="M11"></a>
### M11. Error correction through a logical subsystem

**Central question:** How can a physical error act strongly while leaving logical information intact?

**Understanding target:** Distinguish an encoded subspace from a tensor decomposition into logical and gauge subsystems. An operation of the form $`I_L\otimes G`$ can alter the gauge state while preserving the logical state, including its entanglement with a reference. Recognize that invariance of the decoded information does not require invariant physical codewords.

**Dependencies and story role:** Builds on [M01](#M01), [M04](#M04), and [M05](#M05). It provides the structural idea behind exact removal of lattice displacements.

**Conceptual connection:** Normalizable wave packets can carry the logical state while a separate part of the oscillator Hilbert space absorbs arbitrarily large discrete shifts.

**Source pointers:** Wilde §§5.2 and 24.6 for encoding and error-correction foundations; [logical and gauge coordinates](../science/modular-code.md#logical-and-gauge-coordinates) and [lattice invariance](../science/modular-code.md#exact-invariance-under-the-displacement-lattice).

<a id="M12"></a>
### M12. The complete resource comparison

**Central question:** Which physical quantities are fixed, which are optimized, and what does a fair cost comparison require?

**Understanding target:** Assemble the task with fixed attenuation, fixed positive target rate, exact thermal marginals, and a uniform mean input-energy bound for every logical density operator. Each known channel uses one fixed bath state supplied independently across uses. The Gaussian restriction concerns the bath state; endpoint encoders and decoders remain arbitrary.

**Dependencies and story role:** Integrates [M02](#M02) through [M11](#M11). It completes the background phase by defining $`C_{\mathrm{all}}`$, $`C_{\mathrm{sep}}`$, and $`C_{\mathrm G}`$ within the same operational problem.

**Conceptual connection:** A statement uniform over known temperatures can use temperature-dependent preparations and outer codes. It does not assert one code for an unknown channel or charge preparation work as mutual information.

**Source pointers:** Wilde §§24.1 and 24.3; [capacity and energy accounting](../science/model.md#capacity-and-energy-accounting), [the three costs](../science/model.md#the-correlation-cost), and [retained resources](../science/model.md#physical-resources-retained-in-the-statement).

## Phase II. Narrative and innovation

<a id="M13"></a>
### M13. A finite label for an unbounded amplitude

**Central question:** Which limited information about a hot coherent amplitude is enough to coordinate the reservoirs?

**Understanding target:** Understand a partition of each coherent amplitude modulo a fixed period into $`M`$ cells per quadrature. The label records one of $`M^2`$ residue cells while leaving the integer period index and the amplitude itself unbounded. Its probabilities are induced by the thermal Gaussian distribution and need not be uniform.

**Dependencies and story role:** Builds on [M02](#M02), [M03](#M03), [M07](#M07), and [M12](#M12). It starts the construction with the local piece of information shared by the two preparations.

**Conceptual connection:** The desired displacement lattice determines which information is useful. Full knowledge of either thermal amplitude is unnecessary.

**Source pointers:** Wilde §§4.3 and 10.1 for the classical label; [the residue partition](../science/bath-construction.md#the-thermal-state-and-the-residue-partition) for the geometric construction.

<a id="M14"></a>
### M14. Recovering the exact thermal marginals

**Central question:** Why does coordinating the two residue labels leave both reservoirs exactly thermal?

**Understanding target:** Follow the identity that averaging conditional Gaussian amplitude laws with their actual cell probabilities recovers the original Gaussian law. Understand the resulting state $`\sigma=\sum_C p_C\rho_C\otimes\rho_C`$ as a separable preparation with both marginals equal to $`\tau_N`$ as density operators.

**Dependencies and story role:** Builds on [M03](#M03), [M07](#M07), and [M13](#M13). It verifies the physical admissibility of the construction before evaluating its communication performance.

**Conceptual connection:** Exact local thermality is compatible with a non-Gaussian joint state. The departure from a product thermal bath resides in the correlations.

**Source pointers:** Wilde §§4.1 and 4.3; [preparation and exact marginals](../science/bath-construction.md#preparation-and-exact-marginals).

<a id="M15"></a>
### M15. Charging the correlation carried by the label

**Central question:** Why does the reservoir correlation cost remain bounded as the temperature increases?

**Understanding target:** Connect conditional independence and data processing to $`I(E_1:E_2)\le H(C)\le2\log_2M`$. At $`M=64`$, the quantum mutual information is at most twelve bits for every $`N\gt0`$. Understand why this is an upper bound and need not equal either the label entropy or the preparation work.

**Dependencies and story role:** Builds on [M08](#M08) and [M14](#M14). It establishes the resource bound for the candidate bath.

**Conceptual connection:** Unbounded amplitude variation can coexist with bounded shared information because the correlation follows the finite residue label.

**Source pointers:** Wilde §§11.6, 11.9, and 13.3; [the finite-label mutual-information bound](../science/bath-construction.md#mutual-information-is-bounded-by-the-finite-label).

<a id="M16"></a>
### M16. A lattice displacement plus a bounded remainder

**Central question:** What structure appears in the difference of two amplitudes assigned the same residue cell?

**Understanding target:** Decompose each amplitude difference into an integer multiple of the chosen period and a bounded within-cell difference. After the fixed scaling to signal quadratures, the displacement has a lattice part $`2bK`$ and a residual part $`T`$ with $`|T_q|,|T_p|\le2b/M`$. The lattice index may be correlated with that remainder.

**Dependencies and story role:** Builds on [M13](#M13) and [M14](#M14). It translates the preparation rule into an error structure the code can exploit.

**Conceptual connection:** Small total noise is unnecessary if the unbounded component acts on a disposable subsystem and the remaining logical disturbance is controlled.

**Source pointers:** Wilde §4.6 for channel interpretation; [lattice noise with a bounded remainder](../science/bath-construction.md#lattice-noise-with-a-bounded-remainder) for the amplitude geometry.

<a id="M17"></a>
### M17. Converting attenuation into displacement noise

**Central question:** How does the physical attenuator become the displacement channel analyzed by the decoder?

**Understanding target:** Follow the attenuator by a quantum-limited amplifier of gain $`1/\eta`$. Understand the exact representation of the resulting noise as $`2bK+T+G`$, with independent Gaussian vacuum noise $`G`$ of variance $`(1-\eta)/\eta`$ in each quadrature. Amplifier noise is included in the channel calculation.

**Dependencies and story role:** Builds on [M02](#M02), [M05](#M05), and [M16](#M16). It connects the physical interaction to the mathematical displacement model.

**Conceptual connection:** The receiver amplifier fixes the signal gain and adds a fixed quantum noise contribution. The temperature dependence remains in a displacement component handled by the subsystem decoder.

**Source pointers:** Wilde §§4.4–4.7 for channel representations and composition; [physical channel and amplification](../science/bath-construction.md#the-physical-channel-and-receiver-amplification).

<a id="M18"></a>
### M18. Moving the lattice error into the gauge subsystem

**Central question:** Why can the decoder remove an arbitrarily large lattice displacement without learning its value?

**Understanding target:** Understand the coordinate factorization $`L^2(\mathbb R)\cong\mathbb C^2_L\otimes\ell^2(\mathbb Z)\otimes L^2([0,b))`$. Every displacement in the selected lattice acts trivially on the logical factor. Tracing the gauge factors therefore gives exact decoder invariance, even with a reference system and correlations between the lattice index and residual noise.

**Dependencies and story role:** Builds on [M11](#M11), [M16](#M16), and [M17](#M17). It removes the noise component that can grow without bound.

**Conceptual connection:** The decoder discards gauge information. The codewords themselves can change under a lattice displacement and remain normalizable.

**Source pointers:** Wilde §§5.2 and 24.6 for the encoding perspective; [logical and gauge coordinates](../science/modular-code.md#logical-and-gauge-coordinates) and [exact lattice invariance](../science/modular-code.md#exact-invariance-under-the-displacement-lattice), including the modular-bosonic subsystem references cited there.

<a id="M19"></a>
### M19. Keeping every logical state at the same finite energy

**Central question:** How does the subsystem encoding satisfy the energy constraint for arbitrary logical inputs?

**Understanding target:** Connect the compact sine packets, their square-integrable weak derivatives, and the number-operator quadratic form. Understand the identity $`V^\dagger\hat nV=E_0I`$, where $`E_0=2\pi/3-1/(4\pi)-1/2`$: populations and coherences give the same energy for every logical density operator. The product encoding consequently has energy $`mE_0`$ for every encoded block, including entangled inputs.

**Dependencies and story role:** Builds on [M02](#M02) and [M18](#M18). It verifies the precise input resource used in the theorem.

**Conceptual connection:** Exact subsystem protection and finite input energy are compatible because only decoded information is lattice invariant. Large displacements may increase gauge energy at the output.

**Source pointers:** Wilde §§5.2 and 24.1 for encodings and the transmission task; [normalizable codewords and exact energy](../science/modular-code.md#normalizable-codewords-and-their-exact-energy).

<a id="M20"></a>
### M20. Deriving the actual logical channel

**Central question:** How do the residual position and momentum displacements affect the encoded qubit?

**Understanding target:** Relate cell crossings to population errors and the surviving overlap to coherence. Understand the general decoded channel through $`A=\mathbb E a(v)`$ and $`B=\mathbb E[a(v)e^{-ibw}]`$. Independent symmetric residual quadratures produce a Pauli channel; a more general joint displacement law retains an exact finite-dimensional description.

**Dependencies and story role:** Builds on [M04](#M04), [M17](#M17), [M18](#M18), and [M19](#M19). It identifies the channel to which the coding theorem applies.

**Conceptual connection:** An exact coherence calculation is essential. Treating every packet crossing as a coherent logical bit flip would give the wrong channel.

**Source pointers:** Wilde §§4.7, 9.5, and 13.5; [exact decoded displacement channel](../science/modular-code.md#exact-decoded-displacement-channel), [general displacement law](../science/modular-code.md#a-general-random-displacement-law), and [the Pauli channel](../science/achievable-rate.md#the-decoded-channel).

<a id="M21"></a>
### M21. A rate estimate independent of temperature

**Central question:** Why does the decoded channel retain positive coherent information uniformly over thermal occupation?

**Understanding target:** Understand how an absolutely convergent Fourier expansion of the survival function combines with the fixed Gaussian noise and bounded residual displacement. The signs of the Fourier coefficients and an entropy monotonicity bound produce a common lower bound on $`1-H(p)`$, where $`p`$ is the Pauli error distribution.

**Dependencies and story role:** Builds on [M06](#M06), [M10](#M10), [M16](#M16), and [M20](#M20). It converts the controlled residual noise into the explicit positive rate.

**Conceptual connection:** The temperature-dependent distribution need not be solved exactly. Bounds on the quantities entering the finite-dimensional entropy are sufficient for a uniform guarantee.

**Source pointers:** Wilde §§11.5 and 13.5 for coherent information; [the Fourier estimate](../science/achievable-rate.md#a-uniform-fourier-estimate), [entropy bound](../science/achievable-rate.md#converting-the-scalar-bounds-into-a-rate), and [fixed-loss benchmark](../science/achievable-rate.md#explicit-fixed-loss-benchmark).

<a id="M22"></a>
### M22. Lifting a qubit code to the oscillator channel

**Central question:** Why is the logical coherent-information bound an ordinary unassisted quantum communication rate under the stated energy budget?

**Understanding target:** Compose a finite-dimensional outer code with $`V^{\otimes m}`$ and the fixed local receiver operations. The energy identity applies to every state produced by the outer encoder. At $`\eta_0=9/10`$ and the stated $`E_0`$, this gives $`R_*\gt0.24259`$ for each known $`N\gt0`$ with fresh independent bath pairs.

**Dependencies and story role:** Builds on [M10](#M10), [M12](#M12), [M19](#M19), and [M21](#M21). It completes achievability within the exact operational model.

**Conceptual connection:** The inner encoding, amplification, and subsystem decoder are independent of temperature. The outer code can depend on the known channel; the result does not require an infinite-dimensional coding theorem or imply an unknown-temperature code.

**Source pointers:** Wilde §§24.3–24.4; [qubit-to-oscillator coding argument](../science/achievable-rate.md#from-a-qubit-code-to-an-energy-constrained-oscillator-code) and [the scope of the rate](../science/achievable-rate.md#what-the-rate-establishes).

<a id="M23"></a>
### M23. Comparing an entire protocol with a product bath

**Central question:** How does replacing the bath by its product marginals constrain any communication protocol?

**Understanding target:** Hold the signal protocol fixed while comparing $`\sigma^{\otimes m}`$ with $`(\tau_N\otimes\tau_N)^{\otimes m}`$. The latter produces an entanglement-breaking thermal attenuator when $`N\ge\eta/(1-\eta)`$. Understand why its final reference-receiver state remains separable even under an adaptive protocol with two-way classical communication.

**Dependencies and story role:** Builds on [M05](#M05), [M08](#M08), [M09](#M09), and [M12](#M12). It begins the converse by defining a reference process to which the same data-processing map applies.

**Conceptual connection:** The relative entropy initially available to distinguish the two complete experiments is exactly the reservoir correlation supplied across the block.

**Source pointers:** Wilde §§11.9 and 19.2; [product-bath comparison](../science/correlation-converses.md#the-product-bath-comparison) and [the protocol comparison proof](../science/correlation-converses.md#proof).

<a id="M24"></a>
### M24. A nonzero correlation cost for every successful code

**Central question:** Why must a positive asymptotic quantum rate consume a positive amount of reservoir mutual information?

**Understanding target:** Connect the final maximally entangled-state test to the separable overlap bound $`1/d_m`$. Understand how relative-entropy data processing yields a finite-block fidelity-rate inequality and then $`Q_E\le Q_{2,E}\le I(\sigma)`$. Success probabilities and abort events are included unconditionally.

**Dependencies and story role:** Builds on [M04](#M04), [M08](#M08), [M09](#M09), and [M23](#M23). It supplies the positive lower bound on correlation cost.

**Conceptual connection:** This weak converse is independent of the particular finite-energy code and even permits two-way classical assistance. Its scope does not include a strong converse or a secret-key capacity claim.

**Source pointers:** Wilde §§9.5, 11.9, 19.2, and 24.5; [finite-block converse](../science/correlation-converses.md#a-finite-block-converse) and [asymptotic consequence](../science/correlation-converses.md#asymptotic-consequence).

<a id="M25"></a>
### M25. Why Gaussian correlations have a growing cost

**Central question:** What prevents a Gaussian reservoir with bounded correlation cost from sustaining the same positive rate at high temperature?

**Understanding target:** Connect the useful mode's symplectic eigenvalue to its Gaussian entropy and entanglement-breaking threshold. Combine bounded useful-mode entropy with the unused mode's energy bound and subadditivity to obtain a logarithmic correlation lower bound. Phase-sensitive and entangled Gaussian baths remain inside the comparison.

**Dependencies and story role:** Builds on [M02](#M02), [M06](#M06), [M09](#M09), [M12](#M12), and [M24](#M24). It identifies the restriction responsible for the Gaussian cost law.

**Conceptual connection:** Squeezing can change mean energy without changing symplectic entropy. The proof therefore bounds the relevant entropy and applies to arbitrary endpoint codes, including non-Gaussian ones.

**Source pointers:** Wilde §§11.2 and 11.9 for entropy accounting; [collective-mode Gaussian condition](../science/gaussian-comparison.md#the-collective-mode-entanglement-breaking-condition) and [two-reservoir entropy bound](../science/gaussian-comparison.md#entropy-accounting-for-the-two-reservoirs).

<a id="M26"></a>
### M26. Matching the Gaussian bound at the same signal energy

**Central question:** Can a Gaussian preparation attain the logarithmic cost order under precisely the same input-energy condition?

**Understanding target:** Understand the inverse balanced mixer applied to a vacuum useful mode and a thermal unused mode of occupation $`2N`$. It gives exact physical marginals $`\tau_N`$, a separable Gaussian bath, and correlation $`2g(N)-g(2N)`$. The resulting pure-loss channel uses the same finite-energy inner encoding with zero residue error.

**Dependencies and story role:** Builds on [M03](#M03), [M22](#M22), and [M25](#M25). It completes the Gaussian comparison with a matching upper bound in order.

**Conceptual connection:** Reusing the encoding preserves energy $`E_0`$ for every logical state. A rate computed only for a thermally averaged signal would leave the stated comparison incomplete.

**Source pointers:** Wilde §§11.2 and 24.3; [matching Gaussian preparation](../science/gaussian-comparison.md#a-matching-gaussian-preparation) and [Gaussian cost law](../science/gaussian-comparison.md#the-gaussian-cost-law).

<a id="M27"></a>
### M27. The constant-versus-logarithmic law

**Central question:** What do the construction and both converses establish together?

**Understanding target:** Combine the fixed-loss, fixed-energy bounds for any fixed $`0\lt R\lt R_*`$ and $`N\ge9`$: $`R\le C_{\mathrm{all}}\le C_{\mathrm{sep}}\le12`$, whereas $`C_{\mathrm G}=\Theta(\log N)`$. Understand that the useful collective mode of any bounded-cost family must remain highly mixed as $`N`$ grows.

**Dependencies and story role:** Integrates [M15](#M15), [M22](#M22), and [M24](#M24) through [M26](#M26). It joins the constructive rate and converse arguments into the main theorem.

**Conceptual connection:** The non-Gaussian construction organizes hot noise into correctable displacements. In a Gaussian bath, avoiding an entanglement-breaking channel constrains the useful mode's symplectic entropy and forces a growing information cost. The theorem fixes the asymptotic order without optimizing its constants.

**Source pointers:** Wilde §§11.6, 11.9, and 24.5; [main result](../science/model.md#main-result), [Gaussian cost law](../science/gaussian-comparison.md#the-gaussian-cost-law), and [the useful mode remains hot](../science/gaussian-comparison.md#the-useful-non-gaussian-mode-remains-hot).

<a id="M28"></a>
### M28. Tolerance to additional displacement noise

**Central question:** Does a positive rate survive when the ideal residual displacement law is perturbed?

**Understanding target:** Use the general logical-channel parameters $`A,B`$ to accommodate biased or correlated additional displacements. Understand how root-mean-square error bounds and Lipschitz estimates control the Choi entropy, subject to the stated comparison conditions. Independent Gaussian noise admits a separate quantitative bound.

**Dependencies and story role:** Builds on [M04](#M04), [M06](#M06), [M20](#M20), [M21](#M21), and [M27](#M27). It checks whether the positive rate is stable within a specified error model.

**Conceptual connection:** Temperature-independent tolerance to additional displacement noise concerns the residual signal disturbance. It does not by itself establish temperature-independent tolerance to every physical calibration error.

**Source pointers:** Wilde §§9.1, 11.10, and 13.5 for distance, continuity, and channel information; [general displacement errors](../science/robustness.md#arbitrary-additional-displacement-errors) and [independent Gaussian noise](../science/robustness.md#a-larger-tolerance-for-independent-gaussian-noise).

<a id="M29"></a>
### M29. Calibration precision and the meaning of its bound

**Central question:** How do errors in the physical mixer, attenuation, and amplifier enter the finite-dimensional rate guarantee?

**Understanding target:** Separate the hot displacement coefficient error, whose second moment can scale with $`N`$, from the vacuum-channel change controlled by a dilation and the finite input energy. Apply conditional-entropy continuity after decoding to a qubit. Interpret the resulting calibration inequalities as sufficient conditions for this scheme and known perturbed channel.

**Dependencies and story role:** Builds on [M02](#M02), [M05](#M05), [M12](#M12), [M19](#M19), and [M28](#M28). It connects the abstract error tolerance to explicit physical parameters.

**Conceptual connection:** An $`O(N^{-1/2})`$ calibration scale can suffice in the stated perturbation model. The analysis proves neither necessity nor zero capacity for a fixed mismatch, and a pointwise known-channel guarantee does not supply a code for unknown parameters.

**Source pointers:** Wilde §§5.2, 9.1, and 11.10; [physical calibration model](../science/robustness.md#a-physical-calibration-model), [combined rate guarantee](../science/robustness.md#a-combined-rate-guarantee), and [calibration interpretation](../science/robustness.md#interpreting-calibration-and-compensation).

<a id="M30"></a>
### M30. The complete physical meaning and its boundaries

**Central question:** What does the project establish about communication through hot correlated reservoirs, and which resources remain outside its cost law?

**Understanding target:** Integrate exact thermal marginals, fixed attenuation, the same finite energy for every logical state, ordinary positive quantum capacity, and bounded reservoir mutual information. Place the Gaussian separation and sufficient robustness bounds within that statement. Retain the growing bath and possible receiver output energy, preparation work, coherent decoding, and calibration requirements in the physical interpretation.

**Dependencies and story role:** Integrates [M12](#M12), [M22](#M22), and [M24](#M24) through [M29](#M29). It completes the narrative phase with the contribution, its inherited ingredients, and its limits.

**Conceptual connection:** Earlier environmental assistance, reservoir engineering, and modular-bosonic subsystem methods supply essential precedents. The present comparison joins those ideas into a fixed-interface high-temperature correlation-cost law under a common signal-energy constraint.

**Source pointers:** Wilde §§11.6 and 24.1–24.5; [physical interpretation](../science/interpretation.md), [resource scope](../science/model.md#physical-resources-retained-in-the-statement), and [related work and mathematical ingredients](../references/related_work.md).
