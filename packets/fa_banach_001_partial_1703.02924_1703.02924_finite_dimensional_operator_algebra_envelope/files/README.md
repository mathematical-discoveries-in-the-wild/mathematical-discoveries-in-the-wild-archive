# Finite-Dimensional Operator-Algebra Envelope Case

Source paper: Raphael Clouatre and Christopher Ramsey, "A completely
bounded non-commutative Choquet boundary for operator spaces",
arXiv:1703.02924.

Status: `partial_result_likely_valid`.

## Target

The source paper conjectures that for every operator space `M`, completely
isometric representation `mu`, and `r >= 1`, the C*-algebras
`C^*_{e,1}(M,mu)` and `C^*_{e,r}(M,mu)` are *-isomorphic. This packet proves
the conjecture for the operator-algebra subcase in which the ordinary
`C^*_{e,1}` envelope is finite-dimensional.

## Result

Let `A` be a unital operator algebra and let
`alpha: A -> B(H_alpha)` be a unital completely isometric homomorphism. If
`C^*_{e,1}(A,alpha)` is finite-dimensional, then for every `r >= 1` the
comparison map

```text
Gamma_r: C^*_{e,1}(A,alpha) -> C^*_{e,r}(A,alpha)
```

constructed in Theorem 8.9 of the source paper is injective. Hence
`C^*_{e,1}(A,alpha)` and `C^*_{e,r}(A,alpha)` are *-isomorphic.

## Proof Mechanism

If `Gamma_r` had a nonzero kernel, it would kill a simple summand of the
finite-dimensional `C^*_{e,1}` envelope. Finite-dimensional boundary/peaking
theory gives a matrix over the operator algebra that peaks on this summand.
Because the source object is an operator algebra, tensor powers of that matrix
remain matrices over the same algebra and amplify the strict peak ratio below
`1/r`. But Corollary 8.1 of Clouatre--Ramsey says `epsilon_{alpha,r}` is
bounded below by `1/r` on every matrix level of the represented algebra. This
contradiction forces `Gamma_r` to be injective.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1703.02924.
- `supporting_paper_clouatre_thompson_2022_download_blocked.html`: publisher
  challenge page from the attempted download of the peaking reference.
- `figures/source_conjecture_page43_crop.png`: crop of the source conjecture
  and surrounding known cases.
- `tmp/`: LaTeX and rendering intermediates.

## Limitations

This is not a full proof of the Clouatre--Ramsey conjecture. It uses two
features absent from the general operator-space problem: multiplication in the
source operator algebra, and finite-dimensional peaking of the ordinary
C*-envelope.

## Human Review Recommendation

Review as a genuine partial theorem. The main checks are the quoted
finite-dimensional peaking input and the tensor-power amplification step.
