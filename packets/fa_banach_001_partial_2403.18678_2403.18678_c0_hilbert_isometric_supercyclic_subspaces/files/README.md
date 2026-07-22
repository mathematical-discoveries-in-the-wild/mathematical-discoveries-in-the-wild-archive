# Isometric classical subspaces of supercyclic operators on c0 and Hilbert space

Status: `candidate_partial_solution_likely_valid_needs_human_review` for
Question 3.1 of arXiv:2403.18678.

## Results

The packet gives two complete positive theorems beyond the source's `X=ell_1`
example.

1. If `B` is the unweighted backward shift on `c_0`, then

   ```text
   Phi(lambda) = sum_(k>=1) lambda_k B^k
   ```

   is a linear isometry from `ell_1` into `L(c_0)`, and every nonzero
   `Phi(lambda)` is supercyclic. Thus the supercyclic operators on `c_0`,
   together with zero, contain a closed isometric copy of `ell_1`. This works
   over both the real and complex scalar fields.

2. On every infinite-dimensional separable complex Hilbert space, the
   supercyclic operators together with zero contain a closed isometric copy
   of the disk algebra `A(D)`. On `H^2`, the embedding is

   ```text
   f in A_0(D)  ->  M_(f#)^*,   f#(z)=conjugate(f(conjugate(z))).
   ```

   Here `A_0(D)=z A(D)` is isometric to `A(D)`. Every nonzero image becomes
   hypercyclic after multiplication by a suitable nonzero scalar, by the
   Godefroy--Shapiro eigenvector criterion, and is therefore supercyclic.

## Why the c0 proof is short

For nonzero `lambda`, factor `Phi(lambda)=B^p A`, where `p` is the first
nonzero coefficient and `A=lambda_p I+N`, with `N` strictly lowering finite
supports. On `c_00`, the finite Neumann series for `A^(-1)` is exact. Combining
it with the forward shift gives a right inverse `S` of `Phi(lambda)` on
`c_00`. Powers of `Phi(lambda)` eventually kill each vector in `c_00`, while
`Phi(lambda)^n S^n=I`. This is precisely the Supercyclicity Criterion.

## Scope

Question 3.1 asks broadly which spaces admit such isometric copies. The two
theorems completely resolve the named cases `c_0` and separable complex
Hilbert space but do not classify all separable Banach spaces. The packet is
therefore filed as a substantial partial solution, not a full classification.

## Packet contents

- `solution_packet.pdf`: standalone theorem statements, proofs, verification,
  limitations, and novelty notes.
- `source_paper.pdf`: arXiv:2403.18678.
- `figures/open_problem_crop.png`: Question 3.1 on source PDF page 4.
- `VERIFICATION.md`: separate structural proof audit.
- `tmp/`: LaTeX build artifacts.

Bounded searches by arXiv id, title, authors, exact question, `c_0`, Hilbert
space, disk algebra, and isometric-copy terminology found no later answer.
The one indexed citing paper studies a different frequent-supercyclicity
criterion. This is evidence rather than an exhaustive novelty guarantee;
independent mathematical and literature review is recommended.
