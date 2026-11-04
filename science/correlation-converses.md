# Correlation bounds for arbitrary reservoirs

The product of the two thermal marginals is a useful comparison state. Above the ordinary thermal entanglement-breaking threshold, that product bath cannot transmit entanglement. Replacing it by the actual correlated bath changes the entire output of any communication protocol by at most the relative entropy supplied in the bath. A final entanglement test converts this statement into a rate bound.

This argument permits arbitrary reservoir states and arbitrary endpoint operations. In particular, its lower bound on the required correlation does not assume a Gaussian or separable bath.

## The product-bath comparison

Use the [channel and energy conventions](model.md), and fix a finite occupation $`N`$ and a transmissivity $`0\lt\eta\lt1`$. Write

```math
\omega_N=\tau_N\otimes\tau_N,
\qquad
I(\sigma)=D(\sigma\|\omega_N).
```

All logarithms are base two. Both marginals of $`\sigma`$ are exactly $`\tau_N`$, so

```math
D(\sigma\|\omega_N)
=2g(N)-S(\sigma)
=I(E_1:E_2)_\sigma.
```

These quantities are finite for every finite $`N`$. The product thermal state is invariant under the passive balanced mixer. Its difference mode is therefore thermal with occupation $`N`$, and the reference signal channel is the ordinary thermal attenuator.

That attenuator is entanglement breaking when

```math
N\ge N_{\mathrm{EB}}(\eta):=\frac{\eta}{1-\eta}.
```

This is the established Gaussian entanglement-breaking boundary; see [Holevo (2008), Section 6](https://arxiv.org/html/0802.0235v1). The [Gaussian comparison](gaussian-comparison.md) also derives the corresponding condition for a phase-sensitive collective mode.

## A finite-block converse

Consider a protocol using exactly $`m`$ fresh copies of $`\sigma`$. It starts without entanglement shared between the sender and receiver, and it aims to create a maximally entangled state $`\Phi_d`$ of Schmidt rank $`d`$ between their final logical registers. Arbitrary local quantum operations and unrestricted two-way classical communication may occur between channel uses. All failure and abort branches are included in the final state.

Let $`F=\operatorname{Tr}(\Phi_d\rho_{AB})=1-\epsilon`$ be the unconditional entanglement fidelity, with $`0\le\epsilon\le1/2`$. If $`N\ge N_{\mathrm{EB}}(\eta)`$, then

```math
\boxed{
m I(\sigma)\ge (1-\epsilon)\log_2d-h_2(\epsilon).
}
```

Here $`h_2(x)=-x\log_2x-(1-x)\log_2(1-x)`$ is the binary entropy, with the usual endpoint convention.

### Proof

Fix the protocol, including its code, auxiliary states, classical randomness, adaptive operations, and final decoder. Its complete execution is a quantum channel $`\mathcal P_m`$ from the collection of bath input registers to the final logical registers. The protocol may have been designed using the known $`\sigma`$; the comparison holds its operations fixed and changes only the supplied bath state. Thus

```math
\rho_{AB}=\mathcal P_m(\sigma^{\otimes m}),
\qquad
\zeta_{AB}=\mathcal P_m(\omega_N^{\otimes m}).
```

The comparison protocol uses an entanglement-breaking channel on every call. Its final state $`\zeta_{AB}`$ is separable across the sender–receiver cut, even with adaptive two-way classical communication.

Relative-entropy data processing and additivity give

```math
D(\rho_{AB}\|\zeta_{AB})
\le D(\sigma^{\otimes m}\|\omega_N^{\otimes m})
=m I(\sigma).
```

Measure the two-outcome test $`\{\Phi_d,\mathbb I-\Phi_d\}`$ on both final states. Every separable state satisfies

```math
q:=\operatorname{Tr}(\Phi_d\zeta_{AB})\le\frac1d.
```

Indeed, the overlap bound is immediate for a product pure state and extends by convexity and closure. Another application of data processing yields

```math
\begin{aligned}
m I(\sigma)
&\ge D_{\mathrm{bin}}(F\|q)\\
&=-h_2(F)-F\log_2q-(1-F)\log_2(1-q)\\
&\ge F\log_2d-h_2(F)\\
&=(1-\epsilon)\log_2d-h_2(\epsilon).
\end{aligned}
```

The same statement holds when $`\epsilon`$ is an upper bound on the actual infidelity, provided $`\epsilon\le1/2`$: the target overlap is then at least $`1-\epsilon`$, and the displayed lower bound is monotone over that range.

Only the final logical systems have to be finite dimensional. The bath and all intermediate oscillator systems may be infinite dimensional. Relative-entropy data processing applies on separable Hilbert spaces; see [Müller-Hermes and Reeb (2017), Theorem 1](https://arxiv.org/html/1512.06117v3). No continuity estimate on a hot oscillator state is needed.

The fixed-program comparison is a standard use of relative entropy. For the broader environment-parametrized channel framework, see [Wilde, Berta, Hirche, and Kaur (2020), Section VII.2](https://arxiv.org/html/1808.01498v2). The new resource restriction here is the exact product of the prescribed thermal marginals.

## Asymptotic consequence

Let $`Q_{2,E}`$ denote the corresponding entanglement-generation capacity with two-way classical assistance and mean input energy at most $`E`$. The converse did not use the input-energy bound, so it applies to that constrained capacity and to weaker energy conventions. Taking a sequence of codes with vanishing infidelity gives

```math
Q_E(\mathcal N_{\eta,\sigma})
\le Q_{2,E}(\mathcal N_{\eta,\sigma})
\le I(\sigma),
\qquad N\ge N_{\mathrm{EB}}(\eta).
```

A fixed positive quantum rate therefore requires a nonzero amount of reservoir mutual information per fresh pair. This is a weak converse for vanishing error. It makes no strong-converse claim for a fixed nonzero error, no secret-key claim, and no expected-use claim for variable-length protocols.

The inaccessible-bath condition matters. The reference channel is entanglement breaking after the unused reservoir mode and the environment outputs have been discarded. The argument would have to be changed if those systems, a purification, or the preparation label were supplied to an endpoint.

## Constant correlation cost

Set $`\eta_0=9/10`$ and

```math
E_0=\frac{2\pi}{3}-\frac1{4\pi}-\frac12.
```

The [finite-label preparation](bath-construction.md) and [achievable-rate theorem](achievable-rate.md) give a separable reservoir state for every $`N\gt0`$ satisfying

```math
I(\sigma_N)\le12,
\qquad
Q_{E_0}(\mathcal N_{\eta_0,\sigma_N})\ge R_*,
\qquad R_*\gt0.24259.
```

For every fixed target $`0\lt R\lt R_*`$, the costs defined in the [model](model.md) consequently obey

```math
\boxed{
R\le C_{\mathrm{all}}(N;\eta_0,E_0,R)
\le C_{\mathrm{sep}}(N;\eta_0,E_0,R)
\le12,
\qquad N\ge9.
}
```

The first inequality is the finite-block converse in the asymptotic limit. The middle inequality follows from inclusion of the separable class in the unrestricted class. The upper bound uses the explicit separable construction.

Thus both unrestricted and separable correlation costs are $`\Theta(1)`$ as $`N\to\infty`$, for each fixed target rate in this range. This identifies the asymptotic order, rather than the optimal constant. The bath state and outer code may depend on the known $`N`$; the inner encoder, receiver amplifier, and modular decoder in the construction do not.

