# Normal Hilbert semigroups: the range condition characterizes stability

Run: `fa_banach_001`

Source: arXiv:math/0512460, Alexander Borichev, Ralph Chill, and Yuri
Tomilov, *Uniqueness theorems for (sub-)harmonic functions with applications
to operator theory*.

## Extracted open problem

In Remark 5.11, the source paper says that its fractional-range condition is
sufficient but generally not necessary for stability, except possibly in the
Hilbert case, and asks whether condition (5.5), equivalently the stability
condition in Theorem 5.7, characterizes stability in Hilbert spaces.

For Hilbert spaces, condition (5.5) is

```tex
\bigcap_{\beta\in\mathbb R} \operatorname{Rg}(i\beta-A)^{1/2}
\text{ is dense in } H.
```

## Result

The question has an affirmative answer for bounded `C_0`-semigroups whose
generator is normal.

Let `A` be a normal generator of a bounded `C_0`-semigroup `(T(t))_{t>=0}` on
a complex Hilbert space `H`. Then the following are equivalent:

1. `(T(t))` is strongly stable;
2. the source paper's resolvent condition in Theorem 5.7 with `p=2` holds on a
   dense subset of `H`;
3. the fractional-range condition
   `cap_beta Rg(i beta - A)^{1/2}` is dense in `H`.

The implications `2 => 1` and `3 => 1` are exactly Theorem 5.7 and Corollary
5.10 of the source paper. The new observation is the converse under normality.

## Proof idea

Let `E` be the spectral measure of `A`. Boundedness gives spectral support in
the closed left half-plane. For a normal semigroup, strong stability is
equivalent to `E(iR)=0`: vectors spectrally supported on the imaginary axis
would keep constant norm, while off the imaginary axis dominated convergence
gives decay.

For `epsilon>0`, the subspace

```tex
E({z : Re z <= -epsilon})H
```

is contained in every range `Rg(i beta - A)^{1/2}`, because
`|i beta - z| >= epsilon` on that spectral set. The union over `epsilon>0` is
dense when `E(iR)=0`. The same spectral gap also gives the resolvent limit
`alpha^{1/2}R(alpha+i beta,A)x -> 0` for every beta on this dense union.

## Scope

This is a partial result. It does not solve the full Hilbert-space question for
arbitrary non-normal generators.

