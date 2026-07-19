# Reduced Group C*-Algebras Have BCP Exactly for Countable Groups

Status: likely valid partial result.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

For every discrete group `G`,

```text
C*_r(G) has BCP  <=>  C*_r(G) has UBCP  <=>  G is countable.
```

## Key Idea

If `G` is countable, the reduced group C*-algebra is separable, hence UBCP.

If `G` is uncountable, any countable family of centers lies inside
`C*_r(H)` for some countable subgroup `H <= G`.  Choose `g notin H`.  The
canonical conditional expectation

```text
E_H : C*_r(G) -> C*_r(H)
```

satisfies `E_H(lambda_g)=0` and fixes every center.  Therefore

```text
||lambda_g - a_n|| >= ||E_H(lambda_g-a_n)|| = ||a_n||
```

for every center `a_n`.  The unitary `lambda_g` escapes all proposed BCP
balls.

## Why It Matters

This gives a clean non-Type-I visibility theorem.  For many uncountable
groups with simple reduced C*-algebras, it produces simple one-point-primitive
non-Type-I C*-algebras without BCP, independent of the von Neumann factor
obstruction.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- every element of `C*_r(G)` lies in `C*_r(H)` for some countable subgroup
  `H`;
- the canonical conditional expectation onto a subgroup reduced algebra;
- the final escape inequality.
