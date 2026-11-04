# Thermal marginals and the communication task

Two reservoir modes enter a balanced passive mixer. One collective mode couples to the signal through a fixed attenuator; the other mode is discarded. Each reservoir separately is exactly thermal. The freedom is the joint state of the two reservoirs, and the resource to be minimized is their quantum mutual information.

The question concerns a fixed lossy interface as the thermal occupation grows. Signal energy, attenuation, and the target communication rate remain fixed. The channel is known, and every use receives a fresh independent reservoir pair.

## Oscillator and channel conventions

Use dimensionless quadratures with $`[\hat q,\hat p]=i`$ and $`\hat a=(\hat q+i\hat p)/\sqrt2`$. The vacuum quadrature variance is $`1/2`$, and the number operator is $`\hat n=(\hat q^2+\hat p^2-1)/2`$. A thermal state of mean occupation $`N\gt0`$ is

```math
\tau_N=\frac1{N+1}\sum_{k=0}^{\infty}
\left(\frac{N}{N+1}\right)^k\lvert k\rangle\langle k\rvert.
```

Its entropy, in bits, is

```math
g(N)=(N+1)\log_2(N+1)-N\log_2N,
\qquad g(0)=0.
```

The allowed reservoir state $`\sigma_{E_1E_2}`$ satisfies

```math
\sigma_{E_1}=\sigma_{E_2}=\tau_N.
```

It is independent of the transmitted message and of the sender's reference system. The mixer and attenuator act as

```math
\hat c=\frac{\hat e_1-\hat e_2}{\sqrt2},
\qquad
\hat d=\frac{\hat e_1+\hat e_2}{\sqrt2},
\qquad
\hat a_{\mathrm{out}}
=\sqrt\eta\,\hat a_{\mathrm{in}}+\sqrt{1-\eta}\,\hat c,
\quad 0\lt\eta\lt1.
```

Tracing the unused reservoir mode and the attenuator's environment output defines the signal channel $`\mathcal N_{\eta,\sigma}`$. The sender and receiver have no access to those outputs, to a reservoir purification, or to a label used in preparing $`\sigma`$. Both reservoirs are at the same fixed mode frequency, so $`N\to\infty`$ is the high-temperature limit. No state at infinite temperature is used; every member of the family has finite $`N`$.

## Capacity and energy accounting

Let $`Q_E(\mathcal N)`$ denote the unassisted quantum communication capacity under a mean input photon budget $`E`$ per signal use. For an $`m`$-use encoder $`\mathcal E_m`$, impose the stronger uniform condition

```math
\mathrm{Tr}\!\left[
\left(\sum_{t=1}^m\hat n_t\right)\mathcal E_m(\rho)
\right]\le mE
```

for every logical input density operator $`\rho`$. A rate is achievable when there are encoders and decoders transmitting logical dimension $`d_m`$ with entanglement fidelity tending to one and $`\liminf_m m^{-1}\log_2d_m`$ at least that rate. The reservoir supply for the block is $`\sigma^{\otimes m}`$. Arbitrary endpoint quantum operations are permitted, with no preshared entanglement or extra classical communication.

The construction below has the same input energy for every logical state, so it also meets weaker average-energy conventions. Its inner encoding, receiver amplifier, and modular decoder are independent of $`N`$. The outer quantum code may depend on the known channel. A uniform lower bound over $`N`$ does not assert a single compound-channel code for unknown temperature.

The resource charge is

```math
I(\sigma):=I(E_1:E_2)_\sigma
=D\!\left(\sigma\middle\|\tau_N\otimes\tau_N\right)
=2g(N)-S(\sigma).
```

There is one reservoir pair per signal use. A classical label with $`K`$ possible values can prepare a separable bath with $`I(\sigma)\le\log_2K`$, but the label entropy is only an upper bound on the quantum mutual information. Neither quantity is identified with preparation work.

## The correlation cost

For a fixed target rate $`R\gt0`$, define

```math
C_{\mathrm{all}}(N;\eta,E,R)
=\inf_{\sigma}
\left\{I(\sigma):\ 
\sigma_{E_1}=\sigma_{E_2}=\tau_N,
\ Q_E(\mathcal N_{\eta,\sigma})\ge R\right\}.
```

The costs $`C_{\mathrm{sep}}`$ and $`C_{\mathrm G}`$ restrict the same infimum to separable and Gaussian reservoir states, respectively. The Gaussian class includes entangled and phase-sensitive states. It does not restrict the signal encoder or decoder to Gaussian operations. An empty feasible set has infinite cost.

Each cost optimizes a fixed state supplied independently on every use. There are no correlations between different reservoir pairs. Changing this supply model, the passive interface, or the information available to the endpoints changes the problem.

## Main result

Set

```math
\eta_0=\frac9{10},
\qquad
E_0=\frac{2\pi}{3}-\frac1{4\pi}-\frac12
\simeq1.5148176308.
```

The [achievable-rate theorem](achievable-rate.md) gives an explicit constant $`R_*\gt0.24259`$. For every fixed $`0\lt R\lt R_*`$ and every $`N\ge9`$, the costs at $`(\eta_0,E_0,R)`$ obey

```math
R\le C_{\mathrm{all}}(N)
\le C_{\mathrm{sep}}(N)\le12,
```

and

```math
\max\!\left\{R,\,2g(N)-g(2N)-g(9)\right\}
\le C_{\mathrm G}(N)
\le2g(N)-g(2N).
```

Consequently,

```math
C_{\mathrm{all}}(N)=\Theta(1),
\qquad C_{\mathrm{sep}}(N)=\Theta(1),
\qquad C_{\mathrm G}(N)=\Theta(\log N)
\quad(N\to\infty).
```

The constants may depend on the fixed target rate and interface. The finite-label construction actually supplies the same rate lower bound for every $`N\gt0`$. The restriction $`N\ge9`$ in the cost theorem is used by the correlation converse: the product thermal bath then makes the reference channel entanglement breaking.

### How the proof fits together

| Component | Result | Authoritative proof |
|---|---|---|
| Exact thermal preparation | A shared residue-cell label gives the two exact marginals and $`I(\sigma)\le12`$ | [Bath construction](bath-construction.md) |
| Finite-energy protection | A normalizable oscillator encoding transfers every lattice displacement to a discarded subsystem | [Modular code](modular-code.md) |
| Positive quantum rate | The decoded qubit channel has positive coherent information, uniformly in $`N`$ | [Achievable rate](achievable-rate.md) |
| Nonzero cost | Relative entropy to the product-bath channel bounds every entanglement-generation rate | [Correlation converses](correlation-converses.md) |
| Gaussian logarithmic cost | Non-entanglement-breaking Gaussian noise has bounded symplectic entropy; a vacuum collective mode attains the logarithmic order | [Gaussian comparison](gaussian-comparison.md) |

The rate and correlation constants are explicit sufficient bounds. The result does not identify the optimal constant cost, the exact channel capacity, or the best transmissivity range.

## Physical resources retained in the statement

The theorem bounds source input energy and reservoir mutual information. Reservoir energy is $`2N`$ per pair, and receiver output energy can grow with $`N`$. Endpoint processing includes a fixed quantum-limited amplifier and ideal coherent subsystem extraction. Preparation work, circuit size, detector dynamic range, and the precision of phase and coupling calibration are additional physical resources.

The [robustness analysis](robustness.md) gives explicit tolerance to additional displacement noise and a sufficient calibration scaling for a specified coupling perturbation. The [interpretation](interpretation.md) explains why the useful collective reservoir remains hot and highly mixed, and the [related-work comparison](../references/related_work.md) identifies the inherited ingredients.
