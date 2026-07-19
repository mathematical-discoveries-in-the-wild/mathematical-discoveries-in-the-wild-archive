# Partial Result: Hilbert-Pair Norm-Attaining Tensors

status: likely_valid_partial_result

## Source Target

- Source paper: S. Dantas, M. Jung, O. Roldan, A. Rueda Zoca,
  *Norm-attaining tensors and nuclear operators*, arXiv:2006.09871.
- Target location: Question 6.1, page 23 of the source PDF.
- Source question: if `X` and `Y` are reflexive Banach spaces, is the set of
  norm-attaining tensors dense in `X \hat{\otimes}_\pi Y`?

## Result

This packet records a positive exact-norm-attainment subcase.

1. If `H_1` and `H_2` are complex Hilbert spaces, then every tensor in
   `H_1 \hat{\otimes}_\pi H_2` attains its projective norm.
2. Equivalently, every nuclear operator between two complex Hilbert spaces
   attains its nuclear norm.
3. More generally, if
   `X = H_1 \oplus_1 ... \oplus_1 H_m` is a finite `ell_1`-sum of complex
   Hilbert spaces and `K` is a complex Hilbert space, then every tensor in
   `X \hat{\otimes}_\pi K` attains its projective norm.

Since finite sums of Hilbert spaces are reflexive, item 3 gives a small
positive family for Question 6.1.  The source paper already proves the diagonal
case `H \hat{\otimes}_\pi H`; the packet makes explicit that the same
singular-value argument works for arbitrary Hilbert pairs and then passes
through finite `ell_1`-sums.

## Scope

This does not solve Question 6.1.  It gives equality
`NA_pi(X \hat{\otimes}_\pi Y)=X \hat{\otimes}_\pi Y` only for Hilbert-pair and
finite Hilbert `ell_1`-sum cases.  It does not address general reflexive
spaces, nor Question 6.2 on non-density for nuclear operators in arbitrary
Banach spaces, nor Question 6.3 on property `alpha` or quasi-`alpha`.

## Files

- [main.tex](main.tex): proof packet source.
- [solution_packet.pdf](solution_packet.pdf): rendered packet.
- [source_paper.pdf](source_paper.pdf): arXiv:2006.09871 source paper.
- [figures/open_questions_page.png](figures/open_questions_page.png): rendered
  page containing Question 6.1.
- [code/crop_open_questions.py](code/crop_open_questions.py): reproducible
  page-render script.

## Checks

Cheap run indexes were searched for `2006.09871`, `Norm-attaining tensors`,
`nuclear operators`, `norm-attaining tensors`, and `projective tensor`
phrases.  No prior packet or attempt covered this source target.

Bounded web searches on 2026-06-16 for exact phrases around
`norm-attaining tensors`, `reflexive Banach spaces`, `projective tensor`, and
`norm-attaining nuclear operators not dense` found the source paper but no
later exact answer to Question 6.1.  Novelty confidence is modest: the Hilbert
pair step is an immediate standard trace-class/SVD extension of the source
paper's diagonal Hilbert case.

## Human Review Recommendation

Review as a likely valid but modest partial result.  The main checks are the
isometric identification of `H_1 \hat{\otimes}_\pi H_2` with nuclear operators
from `H_1^*` to `H_2`, the singular-value decomposition for trace-class
operators between two Hilbert spaces, and the finite `ell_1`-sum tensor
decomposition.
