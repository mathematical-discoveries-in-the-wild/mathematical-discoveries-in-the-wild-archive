# Uncountable Tensor Products Have Countable Capture

Status: likely valid partial result.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

Let `(A_gamma)_{gamma in Gamma}` be unital C*-algebras, and suppose
uncountably many factors are nontrivial. Then the unital minimal infinite
tensor product

```text
A = tensor_min,gamma in Gamma A_gamma
```

has countable capture. Therefore `A` fails BCP.

In particular, for every uncountable set `Gamma`,

```text
tensor_gamma in Gamma M_2
```

fails BCP. This gives simple one-point-primitive examples where primitive
topology is not the obstruction.

## Key Idea

Every element of an infinite tensor product has countable support: it lies in
the subproduct over some countable subset of `Gamma`. A countable family of
centers therefore lives in a countable subproduct.

Choose a fresh nontrivial tensor factor and a self-adjoint contraction `v`
whose spectrum contains `-1` and `1`. For a center `b` in the old subproduct
and any scalar `lambda`,

```text
||b - lambda (1 tensor v)||
  >= max(||b-lambda 1||, ||b+lambda 1||)
  >= ||b||.
```

Thus `dist(b, span(1 tensor v)) = ||b||` for every center `b`, which is
exactly the quotient-line characterization of countable capture.

## Scope

This does not classify all countable-pi-base C*-algebras. It handles a large
and important internal-size mechanism: countably many centers cannot see an
unused tensor coordinate.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the countable-support lemma for unital infinite tensor products;
- the construction of a two-state self-adjoint contraction in a nontrivial
  unital C*-algebra;
- the tensor-factor distance inequality;
- the simple uncountable UHF corollary.
