# Operator-valued Schur classes satisfy Sun's Wiener lemma

Status: `candidate_full_likely_valid`

This packet gives a full operator-valued analogue of Qiyu Sun's
inverse-closedness theorem for weighted Schur classes.  It answers the future
work request in Remark 3.11(2) of Köhldorfer--Balazs, arXiv:2407.16416, under
the same `(p,2)`-admissibility hypothesis as the cited scalar theorem.

The key move is to use Sun's admissibility interpolation with auxiliary
exponent `r=infinity`.  A block is a coordinate compression of the global
operator, so its norm is bounded by the global operator norm.  This avoids the
scalar `r=2` delta-vector step, which does not extend to arbitrary operator
blocks.  The resulting differential norm inequality yields equality of
spectral radii and inverse-closedness by Hulanicki's lemma.

Main files:

- `solution_packet.pdf` -- compiled review packet
- `main.tex` -- full proof
- `source_paper.pdf` -- original arXiv paper
- `supporting_paper_sun_2007.pdf` -- decisive scalar theorem and proof
- `figures/open_problem_crop.png` -- source passage on page 18

No computational evidence is used.  The primary human-review target is the
translation of Sun's `(p,r)` interpolation notation at `r=infinity`.

Ledger: `runs/fa_banach_001/ledger/results/2407.16416_operator_valued_schur_p_wiener.json`.
