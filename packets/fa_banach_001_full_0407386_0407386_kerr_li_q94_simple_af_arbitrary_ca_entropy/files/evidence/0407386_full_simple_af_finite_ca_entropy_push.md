# Attempt: Kerr--Li Question 9.4, simple AF finite nonzero CA entropy

run: `fa_banach_001`
agent: `agent_lane_10`
arxiv id: `0407386`
source: David Kerr and Hanfeng Li, *Dynamical entropy in Banach spaces*.
target: Question 9.4 asks whether a `*`-automorphism of
`M_p^{\otimes Z}`, or of any other simple AF algebra, can have finite nonzero
contractive approximation entropy.

status: serious attempt, not solved.

## What was already known in-run

The existing partial packet
`runs/fa_banach_001/solutions/partial/0407386_product_type_uhf_ca_entropy_dichotomy/`
proves a clean dichotomy for product-type UHF automorphisms induced by a
permutation of tensor factors plus local matrix automorphisms:

```text
hc(alpha)=0        if every permutation orbit is finite,
hc(alpha)=infinity if the permutation has an infinite orbit.
```

Thus the source paper's tensor shift and all similar factor-permutation UHF
automorphisms are excluded as finite-nonzero examples.

## Deeper literature search

No direct later resolution was found for exact phrases such as:

- `"finite nonzero" "CA entropy" "simple AF"`
- `"contractive approximation entropy" "simple AF" automorphism`
- `"Dynamical entropy in Banach spaces" "Question 9.4"`
- `"CA entropy" "Bunce-Deddens" "AF"`

Nearby tools found:

1. Neshveyev--Stormer, *The variational principle for a class of
   asymptotically abelian C*-algebras*, arXiv:math/0004077.
   This gives a variational principle for a broad class of AF systems and
   identifies Voiculescu topological entropy with a supremum of CNT entropies
   in that class. It is useful background but does not solve the CA question,
   because Kerr--Li's tensor shift already shows CA can be infinite while the
   matricial/operator-algebraic entropy is finite.

2. Amini--Elliott--Golestani, *The category of ordered Bratteli diagrams*,
   arXiv:1509.07246. Their abstract and introduction record the
   Cantor-minimal-system/simple-properly-ordered-Bratteli-diagram
   correspondence, giving Bratteli--Vershik models for Cantor minimal systems.

3. Høynes, *Toeplitz flows and their ordered K-theory*, arXiv:1404.4771.
   The introduction and Theorem 2.4 record that Toeplitz flows can have
   prescribed entropy `0 <= t < infinity`; in particular, finite positive
   entropy Cantor minimal systems exist in abundance.

## Promising route: Bratteli--Vershik simple AF models

Let `(X,T)` be a Cantor minimal system with `0 < h_top(T) < infinity`, for
example a Toeplitz flow of prescribed finite positive entropy. Choose a simple
properly ordered Bratteli diagram whose Vershik map is conjugate to `T`.
Let `R_AF` be the tail-equivalence AF relation on the infinite path space, and
let

```text
A = C^*(R_AF).
```

For a simple Bratteli diagram this is a simple AF algebra. Since the Vershik
map sends tail-equivalent paths to tail-equivalent paths, it induces a groupoid
automorphism of `R_AF` and hence a `*`-automorphism `alpha` of `A`. The diagonal
`D = C(X)` is `alpha`-invariant, and Kerr--Li Proposition 2.1 plus monotonicity
give

```text
hc(alpha) >= hc(alpha|D) = h_top(T) > 0.
```

So this construction gives a very natural positive-entropy simple AF
automorphism candidate.

## The missing upper bound

The unresolved point is exactly the noncommutative off-diagonal part of the AF
relation algebra. A finite stage `A_m` is a direct sum of matrix algebras
spanned by characteristic functions of basic tail-equivalence bisections
`[p,q]`, where `p` and `q` are finite paths with the same endpoint. The
automorphism sends `[p,q]` to the conjugated bisection

```text
(x,y) |-> (T x, T y).
```

The diagonal orbit is controlled by the clopen partition complexity of `T`,
and hence by `h_top(T)`. What is not yet proved is a uniform CA upper bound
for the orbit of these off-diagonal bisections. A full positive answer would
follow from the following concrete lemma.

### Needed lemma

For the Bratteli--Vershik AF automorphism above, for every finite stage
`A_m`, finite set `Omega subset A_m`, and `delta>0`, there is a constant
`C(Omega,delta)` such that

```text
rc(Omega union alpha(Omega) union ... union alpha^{n-1}(Omega), delta)
    <= C(Omega,delta) exp(C n)
```

with a universal finite `C` independent of `m` and `Omega`, preferably
`C` comparable to `h_top(T)`. This would give `0 < hc(alpha) < infinity`.

The natural way to try to prove this is to refine the clopen partition
`vee_{i=0}^{n-1} T^{-i} P_m` and decompose the conjugated bisections into
basic AF bisections over that refinement. The diagonal count grows like
`exp((h_top(T)+eps)n)`. The issue is that CA rank for noncommutative matrix
blocks can scale with the Banach-space geometry of the off-diagonal span, not
merely with the number of clopen atoms.

## Obstruction found during the push

The following criterion explains why many finite-VB-entropy AF systems still
do not answer Question 9.4.

### Positive-density tensor-independence criterion

Let `A` be a C*-algebra, `alpha in Aut(A)`, and suppose there is a unital copy
`B congruent M_2` with self-adjoint Pauli generators `u,v` such that, for a
set `S subset N` of positive lower density, the subalgebras
`alpha^s(B)`, `s in S`, are pairwise commuting and tensor-independent: for
each finite `F subset S`, the multiplication map from the minimal tensor
product `tensor_{s in F} alpha^s(B)` into `A` is isometric.

Then `hc(alpha)=infinity`.

Proof sketch: for any finite subset `Omega` of the unit sphere of
`span{u,v}`, the tensor-independence hypothesis gives the same `ell_1`-sum
norm identity used by Kerr--Li for the UHF tensor shift, along the times in
`S`. Applying the proof of Kerr--Li Lemma 9.1 on the positive-density time set
gives

```text
hc(alpha, Omega) >= density(S) log |Omega|.
```

Since the unit circle in `span{u,v}` contains arbitrarily large finite sets
with pairwise sums of norm strictly below `2`, the supremum over `Omega` is
infinite.

This criterion covers tensor shifts and many localized/noncommutative AF
shifts whose ordinary Voiculescu-Brown entropy is finite. It also shows why
Neshveyev--Stormer type finite-entropy AF systems are not enough by themselves:
one must rule out positive-density tensor-independent noncommutative orbit
pieces, or else CA jumps to infinity.

## Current verdict

No full solution or counterexample was obtained in this loop.

The Bratteli--Vershik construction is the best positive route found:
finite positive entropy on the diagonal is immediate, and the algebra is simple
AF. The full problem is now concentrated in a precise off-diagonal CA upper
bound for conjugated tail-equivalence bisections.

The best negative/obstruction route is the positive-density
tensor-independence criterion above. Proving that every positive-entropy
simple AF automorphism contains such a tensor-independent `M_2` orbit would
give a full negative answer. Conversely, proving the Bratteli--Vershik
off-diagonal upper bound for a finite-entropy Toeplitz model would give a full
positive answer.

## References searched/used

- Kerr--Li source paper, arXiv:math/0407386:
  https://arxiv.org/abs/math/0407386
- Neshveyev--Stormer, arXiv:math/0004077:
  https://arxiv.org/abs/math/0004077
- Amini--Elliott--Golestani, arXiv:1509.07246:
  https://arxiv.org/abs/1509.07246
- Høynes, arXiv:1404.4771:
  https://arxiv.org/abs/1404.4771
