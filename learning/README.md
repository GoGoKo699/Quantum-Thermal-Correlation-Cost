# Learning the correlation-cost result

Two reservoirs can have the same local thermal states while producing very different noise when their amplitudes are combined. This project asks how much correlation between them is needed to preserve quantum communication through a fixed lossy interface. The signal energy and target rate stay fixed as the reservoirs become hotter.

The [main theorem](../science/model.md#main-result) gives a constant correlation cost for a suitable separable non-Gaussian preparation and a logarithmically growing cost for every feasible Gaussian preparation. The distinction concerns the structure of the reservoir state. Both classes permit arbitrary signal encoders and decoders.

## Choose a route

| Reader's aim | Route |
|---|---|
| Understand the physical idea | Read the [scientific overview](../science/README.md), the [worked two-bit environment example](anchor-bridge.md#a-worked-example-with-two-classical-environment-bits), and the [physical interpretation](../science/interpretation.md). |
| Build the prerequisites and follow the whole argument | Start with the [anchor bridge](anchor-bridge.md), then follow the [30-milestone map](milestones.md). Its source pointers connect each understanding target to the book and the relevant scientific account. |
| Check the theorem and its assumptions | Start with the [operational model](../science/model.md), then follow its proof table to the construction, rate, general converse, and Gaussian comparison. |
| Reproduce the finite calculations | Use the [verification guide](../verification/README.md). It distinguishes the numerical observations from the analytic statements that hold at every temperature. |
| Check attribution and inherited methods | Use the [related-work comparison](../references/related_work.md) and [bibliography](../references/references.bib). |

## One educational anchor

The anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition, Cambridge University Press, 2017**, [DOI: 10.1017/9781316809976](https://doi.org/10.1017/9781316809976).

The [bridge](anchor-bridge.md#the-selected-edition-and-the-open-text) identifies the relevant sections using the publisher's 2017 contents. It also links Wilde's open version of the same work, *From Classical to Quantum Shannon Theory*, explicitly pinned to arXiv:1106.1445v8 from 14 July 2019. Section references in this learning route belong to the selected 2017 edition; page numbers from the later open text are not substituted for them.

Use the selected sections when their ideas become relevant. Reading the entire book is not a prerequisite for reading this project. The bridge supplies the notation changes, a complete finite-system example, and the missing connections to the oscillator model.

## How the milestone map fits together

The [map](milestones.md) contains exactly 30 project-defined understanding targets in two phases.

**[M01 to M12, background and preliminaries](milestones.md#phase-i-background-and-preliminaries)**, connect states, channels, correlations, information measures, coding, and oscillator conventions into the communication task. The phase ends with the matched physical model and resource accounting.

**[M13 to M30, narrative and innovation](milestones.md#phase-ii-narrative-and-innovation)**, follow the finite-label reservoir preparation through coherent decoding and the positive-rate proof, then combine the general and Gaussian converses with robustness and physical interpretation. The final synthesis explains what the correlation-cost separation establishes and which resources remain outside its accounting.

This allocation gives the project-specific mechanism and its limitations most of the space while retaining the foundations needed to read them. The map covers the complete scientific story; the canonical science pages retain the detailed derivations.

## Distinctions to keep visible

- **Local thermality and independence differ.** Both reservoir marginals are exactly $`\tau_N`$. The joint state is the variable being optimized.
- **Preparation information and receiver information differ.** A finite classical label creates the correlations, but neither communication endpoint receives that label.
- **A code can tolerate large noise without making that noise cold.** The useful collective mode remains hot. The decoder transfers lattice displacements to a discarded subsystem.
- **The energy condition applies to every logical input.** The inner encoder has the same finite oscillator energy for all qubit states, including reduced states of an entangled outer code.
- **An achievable rate is a lower bound.** Positive coherent information supplies a code. A zero value for a chosen input would not prove zero capacity.
- **Gaussianity restricts the bath.** The Gaussian converse permits entangled and phase-sensitive reservoirs and arbitrary endpoint operations.

The [bridge's source layers](anchor-bridge.md#foundations-local-derivations-and-research-dependencies) separate textbook foundations, explicit oscillator calculations, and imported research theorems. The [model](../science/model.md) remains the authoritative statement of the task and its scope.
