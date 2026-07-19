# Literature Answer Packet

Status: `literature_already_answered` (infinite finitely generated hyperbolic groups).

Source question: arXiv:1809.09957, Candido--Cuth--Doucha, "Isomorphisms between spaces of Lipschitz functions", Question 1.

Supporting answer: arXiv:2406.10986, Gartland, "Hyperbolic Metric Spaces and Stochastic Embeddings", Lemma 7.1 and Section 1.1.

## Claim

For every infinite finitely generated hyperbolic group `Gamma`, the Lipschitz-free space `F(Gamma)` is isomorphic to `ell_1`. Consequently
`Lip_0(Gamma) = F(Gamma)^*` is isomorphic to `ell_infty`.

This is the positive literature answer to Candido--Cuth--Doucha Question 1, in the intended infinite-group scope explicitly answered by Gartland.

## Evidence

- `source_paper.pdf`: original arXiv:1809.09957 question source.
- `supporting_paper_2406.10986.pdf`: later supporting answer source.
- `figures/open_problem_crop.png`: source Question 1.
- `figures/supporting_answer_crop.png`: Gartland's introduction stating `LF(Gamma) ~= ell_1` and "This answers [16, Question 1]."
- `figures/supporting_lemma_crop.png`: Lemma 7.1, the theorem-level statement.

## Scope Notes

Candido--Cuth--Doucha phrase the question as "every finitely generated hyperbolic group." Gartland states the theorem for every infinite finitely generated hyperbolic group and explicitly says this answers their Question 1. Finite groups are a convention edge case: their free spaces are finite dimensional, so they are not isomorphic to the usual infinite-dimensional `ell_1`.

## Verification Notes

The identification is direct. Gartland cites the original paper as reference [16], writes that equation `(1.2)` answers `[16, Question 1]`, and proves the same statement again as Lemma 7.1. The `Lip_0` conclusion follows by taking duals of the Banach-space isomorphism `F(Gamma) ~= ell_1`.

