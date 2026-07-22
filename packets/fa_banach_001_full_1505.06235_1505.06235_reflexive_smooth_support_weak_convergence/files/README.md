# Reflexive smooth support preserving weak convergence

**Status:** claimed full solution, likely valid, pending human review.

This packet answers concluding open question C of E. Ostrovsky and L. Sirota,
*Strengthening of weak convergence for Radon measures in separable Banach
spaces* ([arXiv:1505.06235](https://arxiv.org/abs/1505.06235)).

If `mu_n => mu` are Borel probability measures on a separable Banach space
`X`, there is one separable reflexive Banach subspace `Y`, compactly embedded
in `X`, such that all the measures are concentrated on `Y`, the weak
convergence holds on `Y`, and `Y` has an equivalent Fréchet-differentiable
norm.

The proof uses a Skorokhod coupling and regards the complete difference
sequence `(xi_n-xi)` as a single `c_0(X)`-valued random variable. Buldygin's
support theorem places that variable on a reflexive space compactly embedded
in `c_0(X)`. A new finite-block/outer-`ell_2` factorization assembles all
coordinate ranges in one reflexive compactly embedded subspace of `X`, with
the coordinate norms tending to zero. This produces almost-sure convergence
in `Y`, and therefore weak convergence of the lifted laws.

A bounded literature search through 22 July 2026 found the cited single-measure
support theorem and related results with extra integrability hypotheses, but no
later exact resolution. Novelty confidence is moderate, not exhaustive.

## Files

- `solution_packet.pdf` - typeset proof and review notes
- `main.tex` - LaTeX source
- `VERIFICATION.md` - detailed proof audit and novelty record
- `source_paper.pdf` - arXiv:1505.06235
- `figures/open_problem_crop.png` - concluding question C on page 8
- `code/crop_source_evidence.py` - reproducible crop helper

The theorem covers probability sequences, exactly as asked. It does not claim
an extension to arbitrary nets of sigma-finite measures.
