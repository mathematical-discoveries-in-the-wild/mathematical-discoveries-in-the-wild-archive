# Literature-Implied Partial Subcase: Countably Branching Trees and Szlenk Index

Status: `literature_implied_answer (partial subcase)`

Source problem paper: F. Baudier, N. J. Kalton, and G. Lancien,
*A new metric invariant for Banach spaces*, arXiv:0912.5113.

Supporting paper: Y. Perreau, *On the embeddability of the family of
countably branching trees into quasi-reflexive Banach spaces*,
arXiv:1906.02046.

## Target

After Corollary 3.4, Baudier--Kalton--Lancien ask whether condition `(iii)`
implies `(i)` for general Banach spaces. In their notation:

- `(i)` is `Sz(X) > omega` or `Sz(X*) > omega`.
- `(iii)` is the existence of a constant `C >= 1` such that each finite
  countably branching tree `T_N` admits a `C`-distortion Lipschitz embedding
  into `X`.

The original corollary proves the equivalence for separable reflexive spaces.
The general Banach-space question remains open in this packet.

## Result

Perreau's Theorem 1.1 proves the missing contrapositive in the quasi-reflexive
setting: if `X` is quasi-reflexive and both `Sz(X) <= omega` and
`Sz(X*) <= omega`, then the family `(T_N)` does not equi-Lipschitz embed into
`X`.

Therefore, for quasi-reflexive Banach spaces, Baudier--Kalton--Lancien's
condition `(iii)` implies condition `(i)`.

## Proof Summary

Assume `X` is quasi-reflexive and condition `(iii)` holds. A uniformly bounded
distortion family of embeddings `T_N -> X` can be rescaled tree by tree to give
uniform lower and upper Lipschitz constants, hence an equi-Lipschitz embedding
of the family `(T_N)` into `X`. If both Szlenk indices were at most `omega`,
Perreau's theorem would rule out such a family. Thus at least one of
`Sz(X)` and `Sz(X*)` is larger than `omega`.

## Evidence

- `figures/open_problem_crop.png`: Corollary 3.4 and the following remark in
  the source paper.
- `figures/supporting_theorem_crop.png`: abstract and Theorem 1.1 in Perreau's
  paper.
- `source_paper.pdf`: local copy of arXiv:0912.5113.
- `supporting_paper_1906.02046.pdf`: local copy of arXiv:1906.02046.

## Search Bounds

Before packaging, the cheap run indexes were searched for `0912.5113`,
`1906.02046`, `Perreau`, `countably branching trees`, `quasi-reflexive`,
`Szlenk`, and `T_N` keywords. No prior packet or attempt for this exact
0912.5113 quasi-reflexive tree/Szlenk subcase was found. A web/arXiv search on
2026-06-14 identified Perreau's later theorem as the relevant supporting
source.

## Human Review Notes

Recommended review focus:

- Check that Baudier--Kalton--Lancien's `C`-distortion notation and Perreau's
  equi-Lipschitz notation are being identified correctly via rescaling.
- Check whether Perreau's theorem requires any hidden separability hypothesis.
  The introduction notes that the earlier separability assumptions can be
  removed by Szlenk-index properties, and Theorem 1.1 is stated for
  quasi-reflexive `X`.
- Confirm the packet is counted only as a literature-implied partial subcase,
  not as a full answer to the source paper's general Banach-space remark.

