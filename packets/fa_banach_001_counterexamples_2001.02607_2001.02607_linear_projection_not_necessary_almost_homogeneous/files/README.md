# Counterexample: linear projection without almost-homogeneous difference set

Status: candidate counterexample, likely valid, pending expert review.

Source paper: Alexandros Margaris, *Almost bi--Lipschitz embeddings using
covers of balls centred at the origin*, arXiv:2001.02607.

Targeted question: Question 4.3 asks whether the condition that `X-X` is
almost homogeneous at `0` is necessary in order to have linear bi-Lipschitz
embeddings into Euclidean space.

Result: negative answer to Question 4.3 as worded. There is a compact subset
`X` of the Hilbert space `R \oplus_2 ell_2` such that the coordinate projection
`L(t,u)=t` is a linear bi-Lipschitz embedding of `X` into `R`, but `X-X` is not
almost homogeneous at `0` for any finite parameters.

## Construction

Let `m_n=2^n` and `h_n=2^{-n^3}` for `n>=2`. On disjoint intervals
`I_{n,k}` of length `h_n` inside `[0,1]`, define a 1-Lipschitz curve
`f:[0,1] -> ell_2` whose derivative is the orthonormal vector `e_{n,k}` on
`I_{n,k}` and is zero off the union of these intervals. Let
`X={(t,f(t)): 0<=t<=1}`.

The projection onto the first coordinate is bi-Lipschitz on `X`. However, for
each fixed `n`, the difference set contains `m_n=2^n` vectors
`z_{n,k}=(h_n,h_n e_{n,k})` in the ball of radius `2h_n`, and these vectors are
pairwise separated by `sqrt(2)h_n`. Taking `rho_n=h_n/4` forces any
`rho_n`-cover to use at least `2^n` balls. An almost-homogeneous-at-zero bound
with fixed parameters would allow only a power of `log(1/h_n)`, hence only a
polynomial in `n`, at this fixed ratio `r_n/rho_n=8`. This contradiction
proves that `X-X` is not almost homogeneous at the origin.

## Scope

This packet answers Question 4.3 under the literal formulation "linear
bi-Lipschitz embeddings into Euclidean space": the linear map is a bounded
operator on the ambient Banach space whose restriction to `X` is bi-Lipschitz.

It does not answer Question 4.1 about extending the embedding theorem to all
doubling subsets of Banach spaces, nor Question 4.2 about finding a nonlinear
almost bi-Lipschitz preprocessing map whose image difference set is almost
homogeneous at `0`.

## Search Evidence

The lane-1 queue selected arXiv:2001.02607. Cheap run indexes were searched for
the arXiv id, title words, `almost homogeneous at 0`, `linear bi-Lipschitz`,
`Euclidean`, `Olson Robinson`, and `Margaris`; no duplicate packet was found.
Targeted local source search and web search for the exact Question 4.3 phrase
and close variants found the source paper but no later answer.

## Files

- `main.tex` / `solution_packet.pdf`: counterexample packet.
- `source_paper.pdf`: local copy of arXiv:2001.02607.
- `figures/open_problem_crop.png`: crop of Questions 4.1--4.3 from page 16.

Review focus: verify that the standard interpretation of "linear
bi-Lipschitz embedding" in Question 4.3 is the restriction of a bounded linear
operator on the ambient Banach space to `X`. Under that reading, the
counterexample is formal.
