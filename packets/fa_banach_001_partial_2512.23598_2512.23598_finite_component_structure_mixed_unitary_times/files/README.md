# Partial Solution Packet: Finite-Component Structure of Mixed-Unitary Times

- status: candidate partial result, likely valid
- run: `fa_banach_001`
- model: `GPT5.6`
- agent: `agent_lane_10`
- source arXiv id: `2512.23598`
- source paper: B. V. Rajarama Bhat and Repana Devendra, *On regions of mixed unitarity for semigroups of unital quantum channels*
- target passage: arXiv PDF page 21, the remark following Theorem 5.4

## Result

Let `Phi_t = exp(tL)` be any unital quantum dynamical semigroup on `M_d`, and
let

```text
S_L = {t >= 0 : Phi_t is mixed unitary}.
```

Then `S_L` is a closed additive subsemigroup of the nonnegative real line and
has only finitely many connected components. Equivalently, it is a finite
union of isolated points and closed intervals, one interval being a final ray
`[tau,infinity)`.

The source paper asks whether the first re-entry time `t0` must equal the
eventual threshold `t1`, and speculates that if `t0<t1`, the mixed-unitary
times in `[t0,t1]` might be discrete. The theorem here does not decide whether
such a gap exists, but proves that any discrete intermediate set must be
**finite**. Infinite oscillation between mixed and non-mixed unitarity before
the eventual regime is impossible.

There is also a quantitative additive consequence. If
`[a,b] subset S_L` with `0<a<b`, then

```text
[n a,infinity) subset S_L
for n = ceil(a/(b-a)).
```

Thus any nontrivial interval of mixed-unitary times forces a concrete final
ray.

## Method

The proof uses only finite-dimensional real algebraic geometry and elementary
one-variable analyticity.

1. In real coordinates, the unitary group is semialgebraic and
   `U -> Ad_U` is polynomial.
2. Caratheodory's theorem bounds the number of unitary conjugations needed in
   a convex representation. Tarski-Seidenberg then shows that the set of
   mixed-unitary channels is semialgebraic.
3. After quantifier elimination, membership is determined by the signs of
   finitely many polynomials in the channel coordinates.
4. Along `Phi_t=exp(tL)`, each such polynomial becomes a real-analytic
   function of `t`. On any compact interval it has finitely many zeros unless
   it vanishes identically.
5. The membership sign pattern can therefore change only finitely many times.
   Eventual mixed unitarity, proved in the source, supplies the final ray.

## Files

- `main.tex`: theorem and complete proof
- `solution_packet.pdf`: rendered proof packet
- `source_paper.pdf`: local copy of arXiv:2512.23598
- `figures/open_problem_crop.png`: genuine crop of the source remark
- `verification.md`: dependency and edge-case audit

## Novelty Check

The run indexes were searched for arXiv id `2512.23598`, the exact title,
`mixed-unitary times`, `regions of mixed unitarity`, `finite union of
intervals`, `semialgebraic mixed unitary`, and quantum-channel semigroups. No
overlapping result was found.

Bounded external searches on 2026-07-23 used:

```text
"mixed-unitary times" semigroup finite union intervals
"mixed unitary" semigroup o-minimal
"mixed unitarity" semialgebraic quantum channels
"On regions of mixed unitarity for semigroups" citations
```

They found the source preprint and adjacent mixed-unitarity work, but no
statement of this finite-component theorem or answer to the `t0=t1` question.
This is evidence rather than a guarantee of novelty.

## Human Review Focus

The key review point is the semialgebraicity step: Caratheodory gives a
uniform finite number of unitaries, so the convex hull is the projection of a
finite-dimensional semialgebraic set. Once this is accepted, the analytic
zero-set argument is elementary. The result must remain labeled partial
because it does not construct a semigroup with `t0<t1` or prove that no such
semigroup exists.

