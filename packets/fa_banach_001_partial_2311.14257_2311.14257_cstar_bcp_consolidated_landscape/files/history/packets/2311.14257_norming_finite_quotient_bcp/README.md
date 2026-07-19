# Norming Finite-Quotient Criterion for C*-Algebras with UBCP

Status: likely valid partial result.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

Let

```text
0 -> I -> A -> F -> 0
```

be exact, where `F` is finite dimensional and `I` is continuous trace with
separable nonzero elementary fibres. Assume:

- `Prim(I)` has a countable pi-basis;
- `I` is uniformly norming in `A`, meaning for some `gamma > 0`,
  `sup_{P in Prim(I)} ||a+P|| >= gamma ||a||` for every `a in A`.

Then `A` has UBCP. In this norming finite-quotient class,

```text
A has BCP  <=>  A has UBCP  <=>  Prim(I) has a countable pi-basis.
```

## Key Idea

This is the matrix-block version of the scalar-ballast proof. Choose a bounded
linear section `sigma:F -> A` and write

```text
a = sigma(q(a)) + k,  k in I.
```

At a norming ideal point, approximate the compact part `k(P)` by a finite-rank
operator `T`. If the lifted quotient part acts locally as `B(P)`, choose a
rank-one operator `R` aligned with a vector where `B(P)+T` almost norms. Then

```text
||B(P)+T+M R|| ≈ M + ||B(P)+T||
```

while the distance along the bump path remains about `M`.

## Why It Matters

The proof does not require a C*-splitting of the finite-dimensional quotient,
and it does not require norm-continuity of lifted multiplier fields. The only
extra hypothesis is the clean, visible one: the continuous-trace ideal must
see a uniform fraction of every norm.

## Remaining Wall

The arbitrary finite-dimensional quotient case is reduced to the non-norming
case, where norms are seen mostly at the finite quotient primitive points. The
next target is to show that this part splits off as a finite-dimensional
summand, or to build a separate quotient-point cover.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the rank-one ballast lemma;
- the use of the bump maximum point `P_1`;
- the constants involving the section norm `C`, norming constant `gamma`, and
  spike size `M=C+2`;
- the outside-support estimate.
