# Additive noise and calibration

The construction tolerates a fixed amount of additional displacement noise as the reservoirs heat up. Errors in the coefficients multiplying the reservoir fields have a different effect: they multiply coherent amplitudes of typical size $`\sqrt N`$. This page gives both statements as explicit rate bounds.

The channel is fixed and known for each capacity statement. The bounds evaluate the same finite-energy inner encoder and coherent modular decoder used in the main construction; the outer code may depend on the resulting channel. All perturbations below are independent of the quantum input.

## The decoded channel for a general displacement law

Put $`b=\sqrt\pi`$. The [modular-code calculation](modular-code.md) gives the even, $`2b`$-periodic function

```math
a(v)=1-\frac{|v|}{b}
+\frac{\sin(2\pi|v|/b)}{2\pi},
\qquad -b\le v\le b.
```

For an arbitrary joint law of position and momentum displacements $`(v,w)`$, define

```math
A=\mathbb E\,a(v),
\qquad
B=\mathbb E\!\left[a(v)e^{-ibw}\right].
```

The decoded qubit channel is unital. It sends the population difference to $`(2A-1)(\rho_{00}-\rho_{11})`$ and multiplies $`\rho_{01}`$ by $`B`$. Its normalized Choi state has eigenvalues

```math
p(A,|B|)
=\left(
\frac{A+|B|}{2},
\frac{A-|B|}{2},
\frac{1-A}{2},
\frac{1-A}{2}
\right).
```

In particular, independence or symmetry of the two quadratures is unnecessary for this formula. The maximally mixed input has coherent information

```math
I_c=1-H\!\left(p(A,|B|)\right).
```

The independent symmetric law in the [main rate proof](achievable-rate.md) is the special case $`B=Ac`$ with real $`c\ge0`$.

For the nominal parameters $`\eta_0=9/10`$ and $`M=64`$, write

```math
\begin{aligned}
r_0^2&=\frac{1-\eta_0}{\eta_0}=\frac19,
&
\theta_0&=\frac{\pi r_0^2}{2},\\
c_*&=e^{-\theta_0}\cos\!\left(\frac{2\pi}{M}\right),
&
a_1&=\frac{16}{3\pi^2},\\
A_*&=\frac12+a_1c_*-\left(a_1-\frac12\right)e^{-9\theta_0},
&
B_*&=A_*c_*.
\end{aligned}
```

The nominal channel obeys $`A\ge A_*`$ and $`B\ge B_*`$ for every $`N\gt0`$. Its benchmark lower rate is the exact expression

```math
R_*=1-H\!\left(p(A_*,B_*)\right)\gt0.24259.
```

## Arbitrary additional displacement errors

Couple the nominal and perturbed noise on the same probability space, and write the new displacement as

```math
(v+\delta_q,\;w+\delta_p).
```

The perturbations may be biased and may correlate with the original noise. Suppose

```math
\mathbb E\,\delta_q^2\le d_q^2,
\qquad
\mathbb E\,\delta_p^2\le d_p^2.
```

The periodic function $`a`$ is globally $`2/b`$-Lipschitz, and $`|e^{ix}-e^{iy}|\le|x-y|`$. Consequently the perturbed parameters satisfy

```math
\begin{aligned}
A'&\ge A_{\mathrm{low}}
:=A_*-\frac{2d_q}{b},\\
|B'|&\ge B_{\mathrm{low}}
:=B_*-\frac{2d_q}{b}-bd_p.
\end{aligned}
```

For example, the coherence bound follows from

```math
\begin{aligned}
&\left|
\mathbb E\!\left[a(v+\delta_q)e^{-ib(w+\delta_p)}\right]
-\mathbb E\!\left[a(v)e^{-ibw}\right]
\right|\\
&\hspace{2em}\le
\frac2b\,\mathbb E|\delta_q|+b\,\mathbb E|\delta_p|
\le\frac{2d_q}{b}+bd_p.
\end{aligned}
```

To turn these two lower bounds into an entropy bound, require

```math
0\le B_{\mathrm{low}}\le A_{\mathrm{low}}\le1,
\qquad
A_{\mathrm{low}}\ge\frac{1+B_{\mathrm{low}}^2}{2}.
```

These conditions hold for the numerical examples below. On the physical domain,

```math
\frac{\partial H(p(A,B))}{\partial B}
=\frac12\log_2\frac{A-B}{A+B}\le0.
```

First lowering $`|B'|`$ to $`B_{\mathrm{low}}`$ therefore increases the entropy. At this fixed value of $`B`$,

```math
\frac{\partial H(p(A,B))}{\partial A}
=\log_2\frac{1-A}{\sqrt{A^2-B^2}}\le0
\quad\text{when}\quad
A\ge\frac{1+B^2}{2}.
```

Lowering $`A'`$ to $`A_{\mathrm{low}}`$ also increases the entropy along this path. It follows that

```math
\boxed{
Q_{E_0}\ge
\max\!\left\{
0,\,
1-H\!\left(p(A_{\mathrm{low}},B_{\mathrm{low}})\right)
\right\}.
}
```

The resource bounds of the bath preparation are unchanged: its local marginals remain exactly thermal, and its mutual information is still at most 12 bits.

For equal root-mean-square bounds $`d_q=d_p=d`$, denote the displayed coherent-information bound by $`\mathcal R(d)`$. Direct evaluation of the exact formulas gives

| Additional displacement bound in each quadrature | Guaranteed rate, qubits per use |
|---|---:|
| $`d=0.01`$ | $`\mathcal R(d)\gt0.1586`$ |
| $`d=0.02`$ | $`\mathcal R(d)\gt0.0794`$ |

These bounds are uniform in $`N`$. They do not require a zero perturbation mean, Gaussian noise, independence between quadratures, or independence from the original bath displacement.

## A larger tolerance for independent Gaussian noise

A sharper expression is available when the extra noise is a centered Gaussian displacement with independent quadratures, each of variance $`\Delta\ge0`$, added after the receiver amplifier. It combines with the amplifier's Gaussian noise, so the [Fourier proof](achievable-rate.md) applies with

```math
\theta_\Delta=\frac{\pi}{2}(r_0^2+\Delta).
```

Define

```math
\begin{aligned}
c_\Delta&=e^{-\theta_\Delta}\cos\!\left(\frac{2\pi}{M}\right),\\
A_\Delta&=\frac12+a_1c_\Delta
-\left(a_1-\frac12\right)e^{-9\theta_\Delta},\\
R_\Delta&=1-H\!\left(p(A_\Delta,A_\Delta c_\Delta)\right).
\end{aligned}
```

Whenever $`A_\Delta\ge1/2`$ and $`c_\Delta\ge0`$, the same monotonicity argument as in the main rate proof gives $`Q_{E_0}\ge\max\{0,R_\Delta\}`$. In particular,

```math
\boxed{
\Delta=0.05
\quad\Longrightarrow\quad
Q_{E_0}\gt0.0217
\quad\text{for every }N\gt0.
}
```

The noise variance here is specified in the quadrature convention $`[\hat q,\hat p]=i`$ and at the input to the modular decoder. Noise added at an earlier port must first be propagated to this location.

## A physical calibration model

Retain the bath prepared for the nominal $`\eta_0`$ and the same inner encoder and modular decoder. Let the actual interface and receiver amplifier instead be

```math
\hat a_{\mathrm{out}}'
=\sqrt{\eta'}\,\hat a_{\mathrm{in}}
+\sqrt{1-\eta'}\,(u\hat e_1+v\hat e_2),
\qquad
|u|^2+|v|^2=1,
```

with $`0\lt\eta'\lt1`$, followed by a quantum-limited amplifier of gain $`g'\ge1`$. The nominal values are

```math
u_0=\frac1{\sqrt2},
\quad
v_0=-\frac1{\sqrt2},
\quad
\eta'=\eta_0,
\quad
g'=g_0:=\frac1{\eta_0}.
```

The signal coefficient is real and positive in the chosen phase convention. This model includes errors in the relative bath phase, the passive mixing ratio, attenuation, and amplifier gain.

### The hot displacement error

For the bath's coherent preparation variables $`\alpha,\beta`$, the actual complex quadrature displacement after amplification is

```math
z'=\sqrt{2g'(1-\eta')}\,(u\alpha+v\beta).
```

The nominal displacement is $`z_0=r_0(\alpha-\beta)`$. Hence

```math
z'-z_0=k_1\alpha+k_2\beta,
```

where

```math
k_1=\sqrt{2g'(1-\eta')}\,u-r_0,
\qquad
k_2=\sqrt{2g'(1-\eta')}\,v+r_0.
```

For the rectangular residue-cell construction,

```math
\begin{aligned}
\mathbb E|\alpha|^2=\mathbb E|\beta|^2&=N,\\
\mathbb E\alpha^2=\mathbb E\beta^2
=\mathbb E(\alpha\beta)&=0,\\
\kappa_N:=\mathbb E(\alpha\overline\beta)
=\mathbb E\!\left|\mathbb E(\alpha\mid C)\right|^2
&\in[0,N].
\end{aligned}
```

The vanishing nonconjugated moments follow because the two quadrature preparations are independent and identical. Conditional independence of $`\alpha,\beta`$ given the same cell label gives the formula for $`\kappa_N`$.

It follows that both real and imaginary parts of $`z'-z_0`$ have the same second moment,

```math
d_{\mathrm{exact}}^2
=\frac N2\left(|k_1|^2+|k_2|^2\right)
+\kappa_N\mathrm{Re}(k_1\overline{k_2}),
```

and therefore obey the conservative bound

```math
d_{\mathrm{exact}}
\le d_N:=
\sqrt{\frac N2}\left(|k_1|+|k_2|\right).
```

This is the source of the temperature dependence. The perturbation is a coefficient error multiplying the hot coherent amplitudes.

### The vacuum-channel error

Changes in $`\eta'`$ or $`g'`$ also change the signal's vacuum loss and amplification channel. Their effect on the finite-energy encoded input can be bounded separately.

Use the beam-splitter and amplifier parameters

```math
\vartheta(\eta)=\arccos\sqrt\eta,
\qquad
s(g)=\mathrm{arcosh}\sqrt g.
```

The half trace distance, including any reference, between the actual vacuum channel and the nominal vacuum channel on the encoded qubit is at most

```math
t_{\mathrm{vac}}=
\min\!\left\{
1,\,
\sqrt{E_0}\,
|\vartheta(\eta')-\vartheta(\eta_0)|
+
\sqrt{\eta_0E_0+1}\,
|s(g')-s(g_0)|
\right\}.
```

For completeness, the beam-splitter dilation has a vacuum ancillary mode and generator $`H=i(\hat a^\dagger\hat v-\hat a\hat v^\dagger)`$. Its squared norm on the encoded input and ancillary vacuum is $`\langle H^2\rangle=E_0`$. The spectral inequality

```math
\|(e^{-itH}-e^{-isH})|\psi\rangle\|
\le|t-s|\,\|H|\psi\rangle\|
```

gives the first term. The amplifier's two-mode-squeezing generator has squared norm $`\langle\hat n+1\rangle`$ when its idler is vacuum. Applied after the nominal loss channel, this is $`\eta_0E_0+1`$, giving the second term. A triangle inequality and trace-distance contraction under the remaining channels give the displayed bound. The same argument applies to an input entangled with a reference.

### A combined rate guarantee

Consider an intermediate channel with the actual coherent displacement $`z'`$ and the nominal vacuum loss-and-amplification channel. The displacement result applies to it with $`d=d_N`$. Its decoded Choi state differs from the actual decoded Choi state by half trace distance at most $`t_{\mathrm{vac}}`$.

Define

```math
\chi(t)=2t+(1+t)h_2\!\left(\frac{t}{1+t}\right).
```

The conditional-entropy continuity bound of [Winter (2016), Lemma 2](https://arxiv.org/html/1507.07775v6), applied to the two-dimensional reference, then yields

```math
\boxed{
Q_{E_0}(\mathcal N_{\mathrm{actual}})
\ge
\max\!\left\{
0,\,
\mathcal R(d_N)-\chi(t_{\mathrm{vac}})
\right\},
}
```

whenever the parameter conditions defining $`\mathcal R(d_N)`$ above hold. Here the actual receiver amplifier is part of the exhibited decoder, so an achievable rate for the resulting decoded qubit channel is also achievable through the original perturbed signal channel.

For example,

```math
d_N\le0.01,\qquad t_{\mathrm{vac}}\le0.005
\quad\Longrightarrow\quad
Q_{E_0}(\mathcal N_{\mathrm{actual}})\gt0.10.
```

The continuity estimate is taken after decoding to a qubit. It requires no uniform entropy or energy bound on the hot oscillator output.

## Interpreting calibration and compensation

For a pure relative-phase error, set

```math
u=\frac1{\sqrt2},
\qquad
v=-\frac{e^{i\phi}}{\sqrt2},
\qquad
\eta'=\eta_0,\quad g'=g_0.
```

Then $`t_{\mathrm{vac}}=0`$, and the exact displacement root-mean-square error in each quadrature is

```math
d_\phi
=r_0\sqrt{\frac N2}\,|e^{i\phi}-1|.
```

Thus the following explicit sufficient condition gives a temperature-uniform positive rate:

```math
|e^{i\phi}-1|
\le\frac{3\sqrt2}{50\sqrt N}
\quad\Longrightarrow\quad
Q_{E_0}\gt0.0794.
```

Likewise, for a balanced bath mixer with attenuation or amplifier-gain drift, put $`u=u_0,v=v_0`$. The displacement coefficients are opposite, and $`\kappa_N\ge0`$ gives the sharper bound

```math
d_{\mathrm{exact}}
\le\sqrt N\,
\left|
\sqrt{g'(1-\eta')}-r_0
\right|.
```

This combines with $`t_{\mathrm{vac}}`$ to give a sufficient tolerance for uncorrected attenuation and gain errors. A passive mixing-ratio error is covered by the general $`k_1,k_2`$ formula.

These are sufficient error budgets for the specified encoder and decoder. They establish that small coefficient errors of order $`N^{-1/2}`$ can preserve a fixed rate. They do not prove that this precision is necessary for every encoding, every error model, or every physical implementation. When a fixed nonzero mismatch makes the bound uninformative at large $`N`$, that alone is not a proof of zero capacity.

If calibration parameters are unknown to the endpoints, these are pointwise bounds for the possible memoryless channels. A single outer code for an unknown or drifting channel requires its own coding and estimation argument.

Known calibration changes can sometimes be absorbed exactly into the preparation. A known relative phase can be canceled by rotating the second coherent amplitude in the bath recipe; thermal marginals and mutual information are unchanged. For a known balanced attenuator of transmissivity $`\eta'`$, choose the residue period $`2b/\sqrt{(1-\eta')/\eta'}`$ and receiver gain $`1/\eta'`$. The rate formula then uses the actual $`\eta'`$, and the hot displacement mismatch disappears. A known mixing-ratio change requires restoring the specified balanced interface or a separate preparation analysis.

The main correlation-cost theorem uses an exactly specified interface. This robustness analysis makes the additional calibration resource explicit while retaining a nonzero, temperature-independent tolerance to additive noise.

