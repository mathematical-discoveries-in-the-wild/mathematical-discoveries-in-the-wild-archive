# Full candidate: Donoho--Stark minimizers are bishifts

Status: `candidate_full_solution_likely_valid`, pending expert review.

Source: Zhengwei Liu, Sebastien Palcoux, and Jinsong Wu, *Fusion
Bialgebras and Fourier Analysis*, arXiv:1910.12059, Advances in Mathematics
390 (2021), 107905.

Target: Question 6.15 on PDF page 22 asks whether every minimizer of the
Donoho--Stark uncertainty principle is a bishift of a biprojection. The
source proves this when the dual has Young's property.

## Claimed answer

Yes. For every canonical fusion bialgebra, in arbitrary finite dimension,
every Donoho--Stark minimizer is a bishift of a biprojection. No simplicity,
integrality, self-duality, subfactor realization, dual Schur property, or
dual Young property is assumed.

The conclusion is invariant under product-one gauges
`(F,d,tau) -> (lambda F,lambda d,lambda^{-1}tau)`. These are exactly the
gauges preserving the sharp constant-one support inequality. An unrestricted
two-parameter gauge changes that numerical constant and should first be
canonicalized, as in the source's normalization theorem.

## Main mechanism

Write a normalized minimizer as

```text
w = sum_{j in J} eps_j p_j,   |eps_j|=1,
D = sum_{j in J} d_j^2,
F(w) = D V,
```

where `V` is a partial isometry. Equality in the operator-norm triangle
inequality is termwise rigid. Every fusion-basis element in the support acts
with maximal norm and a prescribed phase between the initial and final
spaces of `V`.

The basis elements acting by scalar phases on the Fourier range projection
form a fusion subalgebra `H`. Positivity of the fusion coefficients forces
every constituent of every pairwise quotient `x_j x_k*` into `H`. A phased
regular-element calculation proves

```text
sum_{s in H} d_s^2 = sum_{j in J} d_j^2 = D.
```

A second saturation argument gives `HJ subset J`, so `J` is an `H`-coset in
the weighted fusion sense. Frobenius reciprocity then proves the support
projection is a right shift of the biprojection associated with `H`. The
explicit phased regular projection is a shift of its Fourier support. These
two identities give the required bishift factorization of `w`.

## Files

- `main.tex`: self-contained full proof and normalization audit.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: real full-width crop of Question 6.15 and
  the source's conditional theorem.
- `code/verify_stabilizer_group_cases.py`: exact/numerical finite-group
  sanity checks, including noncommutative group algebras.
- `code/verify_rank_three_identities.py`: retained checker for the earlier
  complete rank-three route that this packet supersedes.
- `verification.md`: proof audit, commands, results, and reviewer focus.
- `tmp/`: LaTeX and page-render intermediates.

## Novelty check

On 2026-07-22 the cheap run indexes and bounded arXiv web searches were
checked using arXiv:1910.12059, the exact wording of Question 6.15, and the
terms `fusion bialgebra`, `Donoho-Stark`, `bishift`, `biprojection`,
`extremal bi-partial isometry`, and `dual Young property`. The search found
the source paper but no later paper claiming to answer the question. This is
a bounded novelty check, not a claim of publication priority.

## Human review recommendation

Review these four points first:

1. termwise saturation in the positive fusion expansion;
2. the two-sided definition of the Fourier stabilizer;
3. the coefficient calculation equating stabilizer and support dimensions;
4. the order of the inverse Fourier factors in the dual shift equation.

If these pass, the packet settles Question 6.15 in the source's normalized
setting.

