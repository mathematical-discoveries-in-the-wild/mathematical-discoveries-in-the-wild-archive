# Pure Transition Pi-Bases Calibrate the Boundary Cases

Status: likely valid partial result for the arXiv:2311.14257 C*-algebra BCP
classification program.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
C*-algebra version of the commutative `C(K)` BCP/UBCP criterion.

## Main Result

Let

```text
T(A) = ext(B_{A*})
```

with the relative weak-star topology.  Think of `T(A)` as the pure transition
functional space.

This packet proves two boundary calibrations.

1. If `A=C(K)` is unital commutative, then `T(A)` has a countable pi-base iff
   `K=P(A)` has a countable pi-base.  Hence the transition formulation is
   exactly the source paper's Corollary 3.9 in the commutative case.
2. If `M` is a von Neumann algebra and `T(M)` has a countable pi-base, then
   `M` is atomic and separably represented.  Hence `M` has BCP and UBCP by
   the source paper's Theorem 3.8.

Equivalently, every von Neumann algebra failing BCP in the source theorem has
pure transition functional space with no countable pi-base.

## Why This Is Not a Duplicate

The source paper proves:

- von Neumann algebras have BCP/UBCP iff they are atomic and separably
  represented;
- unital commutative C*-algebras have BCP/UBCP iff their pure state space has
  a countable pi-base.

It does not formulate or prove the transition-functional statement above.  The
new content is that the proposed noncommutative replacement invariant
`T(A)=ext(B_{A*})` reduces to the known commutative invariant and excludes the
negative von Neumann cases.

## Proof Idea

For `C(K)`, the extreme points of the dual unit ball are exactly
`lambda delta_x`, so `T(C(K))` is homeomorphic to `T x K`; countable pi-base is
unchanged by product with the metrizable circle.

For atomless von Neumann algebras, every pure transition functional has a
singular pure state as absolute value.  A countable family of transition-open
sets can therefore be hit by functionals whose absolute values are all
annihilated by one nonzero projection.  The open set of transition
functionals that see this projection is nonempty, but none of the proposed
pi-basic sets lies inside it.

Atomic nonseparable von Neumann algebras fail by uncountably many disjoint
transition-open sets, coming either from central summands or from orthogonal
rank-one projections in a nonseparable Hilbert summand.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source Question 3.

## Remaining Wall

This packet supports the transition-functional route but does not close the
arbitrary C*-case.  The missing positive mechanism is still:

```text
countable transition pi-base
  -> countable local coefficient/rank-one/scalar bump devices
  -> UBCP.
```

The split-interval counterexample shows why those devices cannot be replaced
by separable principal right ideals.

## Review Focus

Check:

- the identification `T(C(K)) ~= T x K`;
- the use of polar decomposition for pure functionals on von Neumann algebras;
- the common projection argument for countably many singular absolute values;
- the uncountable disjoint-open-set arguments in atomic nonseparable cases.

