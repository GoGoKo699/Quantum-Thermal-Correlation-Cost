# A finite-energy qubit inside one oscillator

The [reservoir construction](bath-construction.md) produces arbitrarily large displacements on the lattice $`(2\sqrt\pi\mathbb Z)^2`$. A modular subsystem decomposition places those displacements entirely in a discarded gauge subsystem. Two ordinary wavepackets then encode a qubit with fixed finite energy.

The logical–gauge framework is inherited from [Pantaleoni, Baragiola, and Menicucci, *Modular Bosonic Subsystem Codes*, *Physical Review Letters* **125**, 040501 (2020)](https://doi.org/10.1103/PhysRevLett.125.040501). The definitions below specify the shifted coordinate convention and packet used in this construction.

## Logical and gauge coordinates

Set $`b=\sqrt\pi`$. Apart from endpoints of measure zero, every position coordinate has a unique decomposition

```math
q=2bm+(j-1)b+u,
\qquad
j\in\{0,1\},\quad m\in\mathbb Z,\quad 0\le u\lt b.
```

Define

```math
W:L^2(\mathbb R)
\longrightarrow
\mathbb C^2_L\otimes\ell^2(\mathbb Z)\otimes L^2([0,b))
```

by

```math
(W\psi)_j(m,u)
=\psi\bigl(2bm+(j-1)b+u\bigr).
```

The intervals indexed by $`(j,m)`$ partition the real line, so $`W`$ preserves the norm. Any square-integrable family on the right defines a wavefunction by the inverse piecewise assignment, proving that $`W`$ is unitary. The label $`j`$ is the logical qubit; $`(m,u)`$ is the gauge subsystem.

The decoding channel is

```math
\mathcal R(\rho)
=\operatorname{Tr}_{m,u}[W\rho W^\dagger].
```

This is a coherent extraction of a subsystem followed by a partial trace. Measuring $`j`$ would destroy the coherence that the channel must preserve.

## Exact invariance under the displacement lattice

Use $`D(v,w)=e^{i(wq-vp)}`$, with position-space action

```math
(D(v,w)\psi)(q)
=e^{iw(q-v/2)}\psi(q-v).
```

For integers $`s,t`$, substitution of $`v=2bs`$ and $`w=2bt`$ gives

```math
\bigl(WD(2bs,2bt)\psi\bigr)_j(m,u)
=e^{i2bt u}(W\psi)_j(m-s,u).
```

Every additional phase is an integer multiple of $`2\pi`$ because $`b^2=\pi`$. Consequently

```math
WD(2bs,2bt)W^\dagger
=I_L\otimes G_{s,t},
\qquad
(G_{s,t}f)(m,u)=e^{i2bt u}f(m-s,u).
```

Taking the gauge trace proves the channel identity

```math
\mathcal R\circ\operatorname{Ad}_{D(\ell)}
=\mathcal R
\qquad
\text{for every }\ell\in(2b\mathbb Z)^2.
```

It holds on the entire oscillator trace class, and therefore also when an external reference is present. Weyl multiplication introduces only a scalar phase, which disappears under conjugation. Hence

```math
\mathcal R\circ\operatorname{Ad}_{D(\ell+z)}
=\mathcal R\circ\operatorname{Ad}_{D(z)}
```

for every lattice vector $`\ell`$ and every residual displacement $`z`$. The equality requires no independence between the lattice and residual parts of a random error.

Large lattice shifts change the gauge state and the physical energy. Logical invariance follows because the decoder discards that gauge state; the encoded wavepackets themselves do not have to be invariant under translation.

## Normalizable codewords and their exact energy

Let

```math
f(u)=
\begin{cases}
\sqrt{2/b}\,\sin(\pi u/b),&0\lt u\lt b,\\
0,&\text{otherwise},
\end{cases}
```

and define the isometry $`V:\mathbb C^2\to L^2(\mathbb R)`$ by

```math
(V|0\rangle)(q)=f(q+b),
\qquad
(V|1\rangle)(q)=f(q).
```

The two packets have unit norm and disjoint supports. In the subsystem coordinates,

```math
WV|j\rangle
=|j\rangle_L\otimes|0\rangle_m\otimes|f\rangle_u.
```

Writing $`\mathcal V(\rho)=V\rho V^\dagger`$, this proves $`\mathcal R\circ\mathcal V=\operatorname{id}_2`$.

The zero extension of $`f`$ is continuous and has a square-integrable weak first derivative. Both codewords therefore lie in the quadratic-form domain of the oscillator number operator

```math
\hat n=\frac{q^2+p^2-1}{2}.
```

For either codeword, elementary integration gives

```math
\begin{aligned}
\lVert qV|j\rangle\rVert^2
&=\frac{b^2}{3}-\frac{b^2}{2\pi^2}
=\frac{\pi}{3}-\frac{1}{2\pi},\\
\lVert pV|j\rangle\rVert^2
&=\frac{\pi^2}{b^2}
=\pi.
\end{aligned}
```

The quadratic-form cross terms between the two codewords vanish. For the position contribution this follows from disjoint packet supports; for the momentum contribution it follows from disjoint supports of the weak first derivatives. Thus, as a quadratic-form identity on the logical qubit,

```math
V^\dagger\hat n V=E_0 I_2,
\qquad
E_0=\frac{2\pi}{3}-\frac{1}{4\pi}-\frac12
\approx1.5148176308472478.
```

Every encoded logical state has exactly $`E_0`$ mean photons. This includes mixed states and marginals of logical states entangled with other channel inputs or a reference. For any state $`\rho`$ of $`k`$ logical qubits,

```math
\operatorname{Tr}\!\left[
  \left(\sum_{i=1}^k\hat n_i\right)
  V^{\otimes k}\rho(V^\dagger)^{\otimes k}
\right]
=kE_0.
```

No hard photon-number cutoff is imposed. The finite mean-energy statement follows directly from the number-operator quadratic form.

## Exact decoded displacement channel

Define the even, $`2b`$-periodic function

```math
a(v)=1-\frac{|v|}{b}
     +\frac{\sin(2\pi|v|/b)}{2\pi},
\qquad -b\le v\le b.
```

For a position shift $`0\le v\le b`$, the portion of either packet that remains in its original logical bin has probability

```math
\int_0^{b-v}|f(u)|^2du=a(v).
```

The same probability applies to negative $`v`$ by reflection symmetry. Periodic extension accounts for arbitrary $`v`$ through the lattice-invariance identity.

The surviving parts of the two packets have the same gauge coordinates. A momentum shift $`w`$ supplies the relative phase $`e^{-ibw}`$, since their physical positions at equal gauge coordinates differ by $`b`$. The two crossing parts occupy different integer gauge cells, so tracing the gauge removes their mutual coherence. Any crossed and uncrossed pieces in the same integer cell have disjoint $`u`$ support, which removes the remaining possible cross terms.

The resulting channel is therefore exactly

```math
\left(\mathcal R\circ\operatorname{Ad}_{D(v,w)}
       \circ\mathcal V\right)(\rho)
=
\begin{pmatrix}
a(v)\rho_{00}+[1-a(v)]\rho_{11}
&a(v)e^{-ibw}\rho_{01}\\
a(v)e^{ibw}\rho_{10}
&[1-a(v)]\rho_{00}+a(v)\rho_{11}
\end{pmatrix}.
```

This formula gives the full logical channel, including phase coherence. It also shows directly that each fixed-displacement channel is unital.

## A general random displacement law

For any joint law of $`(v,w)`$, define

```math
A=\mathbb E[a(v)],
\qquad
B=\mathbb E[a(v)e^{-ibw}].
```

Averaging the fixed-displacement formula gives the same population map with coefficient $`A`$ and multiplies $`\rho_{01}`$ by $`B`$. Since $`|B|\le A`$, the four eigenvalues of its normalized Choi state are

```math
\left(
\frac{A+|B|}{2},\,
\frac{A-|B|}{2},\,
\frac{1-A}{2},\,
\frac{1-A}{2}
\right).
```

The maximally mixed input remains maximally mixed. Its coherent information is consequently one minus the Shannon entropy of these four eigenvalues. This statement allows correlations between the two residual coordinates and is useful when analyzing imperfect couplings.

For the exact reservoir construction, $`v`$ and $`w`$ are independent and symmetric. With $`c=\mathbb E[\cos(bw)]`$, the multiplier reduces to $`B=Ac`$. In the parameter regime used below, $`c\ge0`$, and the decoded channel is a Pauli channel with probabilities

```math
p_I=\frac{A(1+c)}{2},
\qquad
p_Z=\frac{A(1-c)}{2},
\qquad
p_X=p_Y=\frac{1-A}{2}.
```

The [achievable-rate proof](achievable-rate.md) bounds $`A`$ and $`c`$ uniformly in reservoir occupation. The code and decoder use ordinary normalizable states and an ideal coherent subsystem operation; their circuit complexity and required receiver dynamic range are separate implementation resources.
