# A finite correlation budget with exact thermal marginals

Two reservoir modes enter a balanced passive mixer. Its difference mode couples to the signal through an attenuator of fixed transmissivity $`0\lt \eta\lt 1`$; its sum mode and the outgoing environment are discarded. Each physical reservoir mode must have exactly the thermal state $`\tau_N`$, with mean occupation $`N`$. The preparation below correlates the residues of their coherent amplitudes while retaining these marginals exactly.

The signal, its reference, and both communication endpoints are initially independent of the reservoir preparation. A fresh, independent reservoir pair is supplied on each use. The preparation label is retained by neither endpoint.

## The thermal state and the residue partition

Use $`[q,p]=i`$, $`\hat a=(q+ip)/\sqrt2`$, and vacuum covariance $`I_2/2`$. For $`N\gt 0`$, the thermal state has the coherent-state representation

```math
\tau_N
=\int_{\mathbb C}\mu_N(d\alpha)\,|\alpha\rangle\langle\alpha|,
\qquad
\mu_N(d\alpha)=\frac{e^{-|\alpha|^2/N}}{\pi N}\,d^2\alpha.
```

Angular integration eliminates all off-diagonal number-basis elements; the remaining probabilities are $`N^n/(N+1)^{n+1}`$. Thus the representation gives the complete thermal density operator, including its Gaussian displacement distribution.

Set

```math
b=\sqrt\pi,
\qquad
r=\sqrt{\frac{1-\eta}{\eta}},
\qquad
L=\frac{2b}{r}.
```

Fix an integer $`M\ge2`$. For $`x\in\mathbb R`$, write $`x=L\lfloor x/L\rfloor+s_L(x)`$, where $`s_L(x)\in[0,L)`$, and define the residue-cell index

```math
\kappa(x)=\left\lfloor\frac{M s_L(x)}{L}\right\rfloor
\in\{0,\ldots,M-1\}.
```

The complex amplitude $`\alpha=x+iy`$ has label $`C(\alpha)=(\kappa(x),\kappa(y))`$. For a label $`c`$, let $`\Omega_c`$ be its cell set, and put

```math
p_c=\mu_N(\Omega_c),
\qquad
\rho_c=\frac{1}{p_c}
\int_{\Omega_c}\mu_N(d\alpha)\,|\alpha\rangle\langle\alpha|.
```

Every $`p_c`$ is positive because the Gaussian density is positive and each cell set has positive area. Each conditional state has finite mean energy for every finite $`N`$.

## Preparation and exact marginals

Draw one label $`C`$ with probabilities $`p_c`$. Conditional on that label, draw $`\alpha`$ and $`\beta`$ independently from $`\mu_N(\cdot\mid\Omega_c)`$ and prepare the corresponding product coherent state. The resulting reservoir state is

```math
\sigma_{N,M}
=\sum_c p_c\,\rho_c\otimes\rho_c.
```

This is a separable state with a positive Glauber–Sudarshan representation. Its two marginals are exactly

```math
\operatorname{Tr}_{E_2}\sigma_{N,M}
=\operatorname{Tr}_{E_1}\sigma_{N,M}
=\sum_c p_c\rho_c
=\tau_N.
```

The construction uses the actual Gaussian cell probabilities at the stated $`N`$. No replacement by a uniform label distribution or a high-temperature approximation is made.

For $`M\ge2`$ and $`N\gt 0`$, the joint amplitude distribution is non-Gaussian. It has a nonzero density on open sets where the two labels agree and vanishes on open sets where they differ. A full-dimensional Gaussian density has no such support restriction. Coherent-state preparation preserves this distinction: its Weyl characteristic function is the classical characteristic function multiplied by the nonvanishing vacuum Gaussian factor. Hence $`\sigma_{N,M}`$ itself is non-Gaussian.

## Mutual information is bounded by the finite label

All entropies and mutual informations use base-two logarithms. Consider the finite classical–quantum state

```math
\omega_{C E_2}
=\sum_c p_c |c\rangle\langle c|\otimes\rho_c.
```

Applying the local preparation channel $`|c\rangle\langle c|\mapsto\rho_c`$ to $`C`$ produces $`\sigma_{N,M}`$. Relative-entropy data processing and the classical–quantum entropy bound give

```math
I(E_1:E_2)_{\sigma_{N,M}}
\le I(C:E_2)_\omega
\le H(C)
\le\log_2(M^2)
=2\log_2 M.
```

The finite classical register is sufficient for this argument; no differential-entropy convention is needed. In the underlying classical amplitude model, $`C`$ is determined by either amplitude and the amplitudes are conditionally independent. Consequently their classical mutual information is exactly $`H(C)`$, consistent with the quantum upper bound after local preparation.

The charged quantity is the quantum mutual information of the supplied reservoir pair. The bound also exhibits a preparation with at most $`M^2`$ shared label values. It does not bound the energy, work, or complexity needed to sample and prepare the conditional states.

## Lattice noise with a bounded remainder

Write $`\alpha=x+iy`$ and $`\beta=x'+iy'`$. Because the two amplitudes have the same label, their real residues lie in the same interval of length $`L/M`$, and the same holds for their imaginary residues. Therefore

```math
\begin{aligned}
x-x'&=L K_q+\Delta_q,\\
y-y'&=L K_p+\Delta_p,
\end{aligned}
\qquad
K_q,K_p\in\mathbb Z,
\qquad
|\Delta_q|,|\Delta_p|\le\frac{L}{M}.
```

Multiplication by $`r`$ gives

```math
r\bigl(\operatorname{Re}(\alpha-\beta),
        \operatorname{Im}(\alpha-\beta)\bigr)
=2bK+T,
\qquad
|T_q|,|T_p|\le\frac{2b}{M}.
```

The integer vector $`K`$ can be arbitrarily large. It may also be correlated with $`T`$. The [modular decoder](modular-code.md) is invariant under every displacement in $`(2b\mathbb Z)^2`$, so neither property affects the decoded logical channel.

The two coordinates of $`T`$ are independent and have symmetric distributions. To see the independence, write

```math
\mu_N(d\alpha)=g_N(x)g_N(y)\,dx\,dy,
\qquad
g_N(x)=\frac{e^{-x^2/N}}{\sqrt{\pi N}}.
```

The cell partition factors into one partition for each coordinate, and its probabilities satisfy $`p_{jk}=p_jp_k`$. The complete joint sampling law of $`(x,x',y,y')`$ therefore factors into an $`(x,x')`$ law and an identical $`(y,y')`$ law. Within either coordinate, exchanging the two conditionally independent samples reverses $`\Delta`$ while preserving its law. This proves symmetry without assuming that the residue is uniformly distributed within a cell.

## The physical channel and receiver amplification

Let the mixer outputs be

```math
\hat c=\frac{\hat e_1-\hat e_2}{\sqrt2},
\qquad
\hat d=\frac{\hat e_1+\hat e_2}{\sqrt2},
```

and let the signal output obey

```math
\hat a_{\mathrm{out}}
=\sqrt\eta\,\hat a+\sqrt{1-\eta}\,\hat c.
```

For a coherent product component $`|\alpha\rangle|\beta\rangle`$, mode $`c`$ is coherent with amplitude $`(\alpha-\beta)/\sqrt2`$. Its signal channel is the vacuum pure-loss channel $`\mathcal L_\eta`$ followed by quadrature displacement

```math
\sqrt{1-\eta}\,
\bigl(\operatorname{Re}(\alpha-\beta),
      \operatorname{Im}(\alpha-\beta)\bigr).
```

Apply a quantum-limited amplifier $`\mathcal A_{1/\eta}`$ at the receiver. It rescales this displacement by $`1/\sqrt\eta`$. The attenuator–amplifier composition supplies an additional independent Gaussian displacement with covariance $`r^2 I_2`$.

For completeness, define the Weyl operator and characteristic function by

```math
D(z_q,z_p)=e^{i(z_pq-z_qp)},
\qquad
\chi_\rho(z)=\operatorname{Tr}[\rho D(z)].
```

The vacuum factor is $`e^{-\lVert z\rVert^2/4}`$. The two Gaussian channels act as

```math
\begin{aligned}
\chi_{\mathcal L_\eta(\rho)}(z)
&=\chi_\rho(\sqrt\eta z)
  e^{-(1-\eta)\lVert z\rVert^2/4},\\
\chi_{\mathcal A_g(\rho)}(z)
&=\chi_\rho(\sqrt g z)
  e^{-(g-1)\lVert z\rVert^2/4}.
\end{aligned}
```

At $`g=1/\eta`$, their composition multiplies $`\chi_\rho(z)`$ by $`e^{-r^2\lVert z\rVert^2/2}`$. This is the characteristic multiplier of a classical quadrature displacement $`G\sim\mathcal N(0,r^2 I_2)`$. Displacement covariance of the amplifier then yields the exact channel representation

```math
\mathcal A_{1/\eta}\circ\mathcal N_{\eta,\sigma_{N,M}}(\rho)
=\mathbb E\!\left[
  D(2bK+T+G)\rho D(2bK+T+G)^\dagger
  \right].
```

Here $`G`$ is independent of the reservoir sampling. The residual coordinates $`T_q+G_q`$ and $`T_p+G_p`$ remain independent and symmetric. The noise representation is exact for every finite $`N\gt 0`$.

Attenuation–amplification conversion is established bosonic-channel machinery; see [Noh, Albert, and Jiang, *IEEE Transactions on Information Theory* **65**, 2563–2582 (2019)](https://doi.org/10.1109/TIT.2018.2873764). The explicit calculation above fixes the normalization used here. The role of the residue coupling is to make the reservoir-dependent part of this noise equal to a harmless lattice displacement plus a uniformly bounded remainder.

The construction at $`N=0`$ can be defined separately as the product vacuum state. Its reservoir displacement is zero, and the same rate bound follows from the Gaussian displacement term alone.

## Fixed and temperature-dependent resources

At fixed $`\eta`$ and $`M`$, the period $`L`$, the label alphabet, the amplifier gain, and the logical encoder and modular decoder are independent of $`N`$. The conditional distributions and their probabilities depend on $`N`$ to preserve the thermal marginals exactly. The reservoir energy is $`2N`$, and the receiver must accept an output with growing energy. A calibrated quadrature convention and mixer are assumed. The [rate proof](achievable-rate.md) concerns a known channel for each $`N`$ and charges the signal input energy and the supplied reservoir mutual information.
