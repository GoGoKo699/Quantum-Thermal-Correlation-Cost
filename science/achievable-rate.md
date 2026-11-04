# A positive rate at fixed loss and fixed input energy

The [thermal-marginal reservoir](bath-construction.md) and the [finite-energy modular code](modular-code.md) define a qubit channel at the receiver. This reduction makes the communication rate an ordinary finite-dimensional coding statement. The estimates below are uniform in the reservoir occupation $`N`$.

## The decoded channel

For fixed $`\eta`$ and $`M`$, let $`\mathcal N_{\eta,\sigma_{N,M}}`$ denote the physical oscillator channel. Its decoded qubit channel is

```math
\Lambda_N
=\mathcal R\circ\mathcal A_{1/\eta}
 \circ\mathcal N_{\eta,\sigma_{N,M}}\circ\mathcal V.
```

The reservoir preparation and amplifier give a random displacement $`2bK+T+G`$, where $`b=\sqrt\pi`$, $`|T_q|,|T_p|\le2b/M`$, and $`G_q,G_p`$ are independent centered Gaussians with variance

```math
s=\frac{1-\eta}{\eta}.
```

The decoder removes the lattice part exactly, even though $`K`$ and $`T`$ can be correlated. The remaining coordinates

```math
v=T_q+G_q,
\qquad
w=T_p+G_p
```

are independent and symmetric. The decoded channel is therefore Pauli, with

```math
\begin{aligned}
A_N&=\mathbb E[a(v)],\\
c_N&=\mathbb E[\cos(bw)],\\
p_I&=\frac{A_N(1+c_N)}2,\\
p_Z&=\frac{A_N(1-c_N)}2,\\
p_X=p_Y&=\frac{1-A_N}2.
\end{aligned}
```

Its coherent information at the maximally mixed qubit input is

```math
I_c(I_2/2,\Lambda_N)=1-H(p_I,p_Z,p_X,p_Y).
```

The formula is exact; the bounds below estimate its two scalar parameters without evaluating the conditional reservoir distributions.

## A uniform Fourier estimate

The survival function from the decoder has the absolutely convergent Fourier series

```math
a(v)=\frac12+
\sum_{\substack{k\ge1\\k\text{ odd}}}
\kappa_k\cos\!\left(\frac{k\pi v}{b}\right),
\qquad
\kappa_k=\frac{16}{\pi^2k^2(4-k^2)}.
```

These coefficients follow by integrating the linear and sine terms in $`a(v)`$ on $`[0,b]`$. For odd $`k`$, their contributions are $`4/(\pi^2k^2)`$ and $`4/[\pi^2(4-k^2)]`$, respectively. Every coefficient with positive even index is zero, including $`k=2`$. The coefficients decay as $`k^{-4}`$, so averaging the series term by term is justified.

The first coefficient is positive, all subsequent nonzero coefficients are negative, and evaluation at $`v=0`$ gives

```math
\kappa_1=\frac{16}{3\pi^2},
\qquad
\sum_{\substack{k\ge3\\k\text{ odd}}}\kappa_k
=\frac12-\kappa_1.
```

Set $`\theta=\pi s/2`$. Gaussian averaging multiplies Fourier frequency $`k\pi/b`$ by $`e^{-k^2\theta}`$. Because $`|T_q|\le2b/M`$ and $`M\ge2`$,

```math
\mathbb E\!\left[\cos\!\left(\frac{\pi T_q}{b}\right)\right]
\ge\cos\frac{2\pi}{M}.
```

The identical estimate for $`T_p`$ gives

```math
c_N\ge c_*
:=e^{-\theta}\cos\frac{2\pi}{M}.
```

For the negative Fourier coefficients, each residual characteristic factor is at most one. Moreover $`e^{-k^2\theta}\le e^{-9\theta}`$ for $`k\ge3`$. Multiplying these inequalities by the negative coefficients reverses the direction and yields

```math
\begin{aligned}
A_N
&=\frac12+
  \sum_{\substack{k\ge1\\k\text{ odd}}}
  \kappa_k e^{-k^2\theta}
  \mathbb E\!\left[
    \cos\!\left(\frac{k\pi T_q}{b}\right)
  \right]\\
&\ge\frac12+\kappa_1 c_*
        -\left(\kappa_1-\frac12\right)e^{-9\theta}
=:A_*.
\end{aligned}
```

Only the bounded residue is used. Neither estimate depends on $`N`$.

## Converting the scalar bounds into a rate

For $`A\in[1/2,1]`$ and $`c\in[0,1]`$, the entropy of the corresponding Pauli distribution can be written as

```math
H(A,c)
=h_2(A)+A h_2\!\left(\frac{1-c}{2}\right)+(1-A).
```

Here $`h_2(x)=-x\log_2x-(1-x)\log_2(1-x)`$, with $`0\log_2 0=0`$. The entropy decreases in both arguments on this domain, as its interior derivatives show:

```math
\begin{aligned}
\frac{\partial H}{\partial A}
&=\log_2\frac{1-A}{A}
  +h_2\!\left(\frac{1-c}{2}\right)-1
\le0,\\
\frac{\partial H}{\partial c}
&=\frac{A}{2}\log_2\frac{1-c}{1+c}
\le0.
\end{aligned}
```

Thus, whenever the explicit bounds satisfy $`A_*\ge1/2`$ and $`c_*\ge0`$, substituting them gives

```math
I_c(I_2/2,\Lambda_N)
\ge 1-H(A_*,c_*).
```

The parameters below lie strictly inside that domain.

## Explicit fixed-loss benchmark

Take

```math
\eta=\frac9{10},
\qquad
M=64,
\qquad
\theta=\frac\pi{18}.
```

Define the exact constants

```math
\begin{aligned}
c_*&=e^{-\pi/18}\cos\frac\pi{32},\\
A_*&=\frac12+\frac{16}{3\pi^2}c_*
     -\left(\frac{16}{3\pi^2}-\frac12\right)e^{-\pi/2},\\
R_*&=1-H\!\left(
\frac{A_*(1+c_*)}{2},
\frac{A_*(1-c_*)}{2},
\frac{1-A_*}{2},
\frac{1-A_*}{2}
\right).
\end{aligned}
```

Their numerical values are

| Quantity | Value |
|---|---:|
| $`A_*`$ | $`0.94325795939704928875\ldots`$ |
| $`c_*`$ | $`0.83580509811181884799\ldots`$ |
| $`R_*`$ | $`0.24259452381736871250\ldots`$ |
| $`E_0=2\pi/3-1/(4\pi)-1/2`$ | $`1.51481763084724782442\ldots`$ photons |
| Reservoir mutual information | At most $`12`$ bits per pair |

The exact expressions define the bounds; the displayed decimals are evaluations. In particular, $`R_*\gt 0.24259`$ and $`E_0\lt 1.514818`$.

## From a qubit code to an energy-constrained oscillator code

The finite-dimensional quantum coding theorem makes every rate below $`I_c(I_2/2,\Lambda_N)`$ achievable for independent uses of $`\Lambda_N`$ with vanishing entanglement-transmission error. This is the standard coherent-information achievability theorem; see [Devetak, *The private classical capacity and quantum capacity of a quantum channel*](https://arxiv.org/abs/quant-ph/0304127), Theorem 5, Proposition 7, and the direct entanglement-transmission construction in Appendix D.

Take such a $`k`$-use qubit encoder $`\mathcal E_k`$ and decoder $`\mathcal D_k`$. An oscillator protocol uses

```math
\widetilde{\mathcal E}_k
=\mathcal V^{\otimes k}\circ\mathcal E_k,
\qquad
\widetilde{\mathcal D}_k
=\mathcal D_k\circ
  (\mathcal R\circ\mathcal A_{1/\eta})^{\otimes k}.
```

The complete logical channel of this protocol equals the original qubit code's channel exactly. The signal energy also transfers directly: every marginal of $`\mathcal E_k(\rho)`$ is a logical qubit state, and the quadratic-form identity $`V^\dagger\hat nV=E_0I_2`$ therefore gives exactly $`kE_0`$ total mean photons for every input $`\rho`$. Correlations between code symbols or with an external reference do not change that identity.

The encoder uses no reservoir label and the receiver uses only local amplification and decoding. The code requires neither preshared entanglement nor classical communication. Consequently

```math
Q_{E_0}(\mathcal N_{9/10,\sigma_{N,64}})
\ge Q(\Lambda_N)
\ge R_*
\gt 0.24259
\qquad\text{for every }N\gt 0.
```

The proof invokes a coding theorem only for the decoded qubit channel. An independent infinite-dimensional coding theorem is unnecessary for this lower bound because the physical encoding and its energy are explicit.

The result is uniform in $`N`$ in the following sense: for every known occupation $`N`$, a memoryless channel with the specified reservoir state admits every rate below $`R_*`$. The packet encoder, amplifier, and modular decoder are the same for all $`N`$. An outer qubit code may depend on the channel, and the statement does not require one code to work for an unknown or varying temperature.

## What the rate establishes

At a fixed ten-percent loss, a separable reservoir pair with exact thermal marginals supports a fixed positive unassisted quantum rate under a fixed signal energy budget. The mutual-information budget is independent of temperature. The [Gaussian comparison](gaussian-comparison.md) and [correlation converse](correlation-converses.md) place this construction within the asymptotic correlation-cost law.

The reservoir and signal output can carry growing energy, and the coherent modular decoder is an ideal allowed operation. Those resources, along with calibration accuracy and conditional-state preparation complexity, must be accounted for in any implementation claim. The theorem above is a communication and correlation-resource statement with those operational boundaries explicit.
