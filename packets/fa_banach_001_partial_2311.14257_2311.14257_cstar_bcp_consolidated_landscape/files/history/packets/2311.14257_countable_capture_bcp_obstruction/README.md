# Countable-Capture Obstruction for BCP

Status: likely valid partial result / reusable obstruction criterion.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

Let `X` be a normed space. Suppose that for every countable set `C subset X`
there are a normed space `Y`, a contraction `E:X -> Y`, and a unit vector
`u in X` such that

```text
E(u)=0
and
||E(c)|| = ||c|| for every c in C.
```

Then `X` fails BCP.

Equivalently, no countable family of proposed BCP centers can work: applying
the hypothesis to the center set gives a unit vector `u` satisfying

```text
||u - x_n|| >= ||x_n||
```

for every center `x_n`.

## C*-Algebra Use

For a C*-algebra `A`, it is enough to find, after seeing any countable family
of centers, a contractive linear "capture" map which preserves the norms of
those centers while killing a fresh unit vector.

This is the exact mechanism behind the packet
`2311.14257_reduced_group_cstar_bcp_countable`: for uncountable discrete
groups, the subgroup expectation

```text
E_H : C*_r(G) -> C*_r(H)
```

fixes all centers contained in the countable subgroup algebra `C*_r(H)` and
kills a fresh group unitary `lambda_g`.

## Scope

This packet does not classify all non-Type-I C*-algebras. It isolates a
negative visibility mechanism. Positive non-Type-I examples remain, including
separable C*-algebras and positive von Neumann algebra cases covered by the
source paper.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the equivalent BCP test using balls `B(x_n, ||x_n||)`;
- the contraction escape inequality;
- the specialization to C*-algebra conditional expectation/capture maps.
