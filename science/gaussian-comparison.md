# Why Gaussian reservoirs need logarithmically more correlation

For a Gaussian reservoir, a large entropy of the mode coupled to the signal forces the channel to become entanglement breaking. A bounded correlation budget cannot keep that entropy finite when both physical marginals become arbitrarily hot. This gives a lower bound on all Gaussian bath preparations, including entangled and phase-sensitive states.

Throughout, the passive interface, signal-energy constraint, and endpoint access are those in the [model](model.md). Gaussianity restricts the reservoir only. The signal encoder and decoder remain arbitrary.

## The collective-mode entanglement-breaking condition

Let $`\sigma`$ be a two-mode Gaussian state with both marginals $`\tau_N`$. Apply the balanced mixer and denote its outputs by $`c,d`$. The signal interacts with $`c`$ only. Tracing $`d`$ before or after the signal interaction gives the same signal channel, so only the reduced state $`\sigma_c`$ determines that channel.

Write $`V_c`$ for the covariance matrix of $`c`$ in the convention with vacuum covariance $`\mathbb I_2/2`$. Its one-mode symplectic eigenvalue is

```math
\nu_c=\sqrt{\det V_c}\ge\frac12,
```

and its entropy is

```math
S(c)=g\!\left(\nu_c-\frac12\right).
```

The signal channel has Gaussian matrices

```math
X=\sqrt\eta\,\mathbb I_2,
\qquad
Y=(1-\eta)V_c.
```

To evaluate its entanglement-breaking property, write the Williamson decomposition $`V_c=S(\nu_c\mathbb I_2)S^{\mathsf T}`$. An input Gaussian unitary with symplectic matrix $`S`$ and an output unitary with matrix $`S^{-1}`$ transform the channel to

```math
X'=\sqrt\eta\,\mathbb I_2,
\qquad
Y'=(1-\eta)\nu_c\mathbb I_2.
```

These unitary changes preserve whether a channel is entanglement breaking. Their input-energy cost is irrelevant to this step, because they are being used to classify the channel, not to construct an energy-constrained code.

The transformed channel is the thermal attenuator with environment occupation $`\nu_c-1/2`$. The standard one-mode criterion of [Holevo (2008), Section 6](https://arxiv.org/html/0802.0235v1) therefore gives

```math
\mathcal N_{\eta,\sigma}\text{ is entanglement breaking}
\quad\Longleftrightarrow\quad
\nu_c\ge\frac{1+\eta}{2(1-\eta)}.
```

In particular, any positive unassisted or two-way assisted quantum rate requires

```math
S(c)\le g\!\left(\frac{\eta}{1-\eta}\right).
```

The strict non-entanglement-breaking condition gives a strict inequality; the weak form above suffices for the cost bound. It constrains the symplectic entropy, not the mean energy. This distinction keeps arbitrarily squeezed Gaussian collective modes within the converse.

## Entropy accounting for the two reservoirs

The mixer preserves the joint entropy and total photon number. Consequently,

```math
\begin{aligned}
S(cd)&=S(E_1E_2)=2g(N)-I(\sigma),\\
\langle\hat n_c\rangle+\langle\hat n_d\rangle&=2N.
\end{aligned}
```

A one-mode thermal state maximizes entropy at a fixed mean photon number. Since $`\langle\hat n_d\rangle\le2N`$,

```math
S(d)\le g(2N).
```

Subadditivity then gives

```math
2g(N)-I(\sigma)=S(cd)\le S(c)+S(d).
```

Combining this with the non-entanglement-breaking entropy bound proves

```math
\boxed{
I(\sigma)\ge
2g(N)-g(2N)-g\!\left(\frac{\eta}{1-\eta}\right)
}
```

for every Gaussian bath that supports a positive quantum rate through the specified interface. No standard-form ansatz for the two-mode covariance matrix was imposed, and the argument did not assume separability.

## A matching Gaussian preparation

Prepare the collective modes in

```math
\sigma_{cd}^{\mathrm G}
=\lvert0\rangle\langle0\rvert_c\otimes\tau_{2N,d},
```

and apply the inverse balanced mixer. Each physical output mode $`E_1,E_2`$ is exactly thermal with occupation $`N`$. The resulting two-mode state is Gaussian and separable. For example, its positive coherent-state representation is

```math
\sigma_{E_1E_2}^{\mathrm G}
=\int_{\mathbb C}\frac{d^2\alpha}{\pi N}\,
e^{-|\alpha|^2/N}
\lvert\alpha\rangle\langle\alpha\rvert
\otimes
\lvert\alpha\rangle\langle\alpha\rvert.
```

The coupled mode is vacuum, so the signal sees the pure-loss channel. The mutual information is exactly

```math
I(\sigma^{\mathrm G})=2g(N)-g(2N).
```

At $`\eta_0=9/10`$, this channel supports at least the rate $`R_*`$ with the same uniform input-energy budget $`E_0`$ used by the non-Gaussian construction. To see this without invoking an additional oscillator coding theorem, use the same finite-energy encoder, amplifier, and modular decoder. Their noise is the Gaussian displacement term from the [achievable-rate proof](achievable-rate.md), with the residue error set to zero. The lower bounds in that proof can only improve when the residue characteristic factor $`\cos(2\pi/64)`$ is replaced by one.

Thus the Gaussian upper construction meets the same signal-energy and target-rate constraints. It does not rely on an input-energy limit that grows with $`N`$.

## The Gaussian cost law

For every fixed $`0\lt R\lt R_*`$ and every $`N\ge9`$, the Gaussian correlation cost satisfies

```math
\boxed{
\max\!\left\{
R,\,
2g(N)-g(2N)-g(9)
\right\}
\le C_{\mathrm G}(N;\eta_0,E_0,R)
\le2g(N)-g(2N).
}
```

The first term in the lower bound comes from the [general correlation converse](correlation-converses.md). The second comes from the Gaussian entropy argument. The upper bound is achieved by the separable Gaussian preparation above, so allowing entangled Gaussian baths cannot improve the logarithmic order.

Because

```math
2g(N)-g(2N)
=\log_2N+\log_2e-1+O(N^{-1}),
```

the minimum Gaussian cost is $`\Theta(\log N)`$. Together with the constant-cost separable non-Gaussian construction, this is the claimed separation.

## The useful non-Gaussian mode remains hot

The entropy bookkeeping before the Gaussian entanglement-breaking step applies to every allowed bath state. It gives

```math
\boxed{
S(c)\ge2g(N)-g(2N)-I(\sigma).
}
```

If the mutual information remains bounded as $`N\to\infty`$, then the coupled mode's entropy diverges as at least $`\log_2N-O(1)`$. Its mean energy must also diverge, since an oscillator with bounded mean photon number has bounded entropy.

The non-Gaussian construction therefore does not obtain a bounded-energy vacuum mode from the hot reservoirs. It makes large, high-entropy noise compatible with the logical subsystem through its displacement structure. Gaussian reservoirs face the additional restriction that non-entanglement-breaking noise has bounded symplectic entropy.

The proof uses established Gaussian normal forms, the entanglement-breaking boundary, and the entropy maximum of a thermal state. The resource comparison follows by imposing the exact local marginals and minimizing their mutual information at a fixed positive communication rate.

