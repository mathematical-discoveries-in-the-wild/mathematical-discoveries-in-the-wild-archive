# Countable-Capture Characterization and Topological Sources

Status: likely valid partial result / characterization of the obstruction
mechanism.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

The countable-capture obstruction from
`2311.14257_countable_capture_bcp_obstruction` has an exact Banach-space
form.

For a nonzero normed space `X`, the following are equivalent:

```text
For every countable C subset X there are a contraction E:X -> Y
and u in S_X such that E(u)=0 and ||E(c)||=||c|| for c in C.
```

and

```text
For every countable C subset X there is u in S_X such that
dist(c, span(u)) = ||c|| for every c in C.
```

Equivalently, every countable set admits norming functionals whose common
kernel contains a nonzero vector.

## C*-Algebra Consequence

If `Prim(A)` has no countable pi-base, then `A` has countable capture. Thus
the primitive-space obstruction is not merely a diagonal BCP obstruction: it
is exactly a countable-capture source.

## Exact Model Classifications

- For nonzero locally compact Hausdorff `K`, `C_0(K)` has countable capture
  iff `K` has no countable pi-base.
- For Hilbert spaces, countable capture holds iff the Hilbert space is
  nonseparable.
- For discrete groups, `C*_r(G)` has countable capture iff `G` is
  uncountable.

## Scope

This does not classify all C*-algebras with countable capture. The remaining
hard case is the norm-visible obstruction inside algebras whose primitive
ideal space already has a countable pi-base, such as simple nonseparable
algebras and atomless von Neumann factors.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the factorization through `X / span(u)`;
- the Hahn-Banach dual characterization;
- the primitive-ideal proof that lack of countable pi-base gives capture;
- the exact commutative, Hilbert, and reduced-group corollaries.
