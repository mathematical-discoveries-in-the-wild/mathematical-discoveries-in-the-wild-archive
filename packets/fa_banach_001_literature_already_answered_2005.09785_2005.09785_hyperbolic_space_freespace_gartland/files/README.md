# Literature Answer Packet

Status: `literature_already_answered`.

Source question: arXiv:2005.09785, Doucha--Kaufmann, "Approximation properties in Lipschitz-free spaces over groups", Question 6.

Supporting answer: arXiv:2406.10986, Gartland, "Hyperbolic Metric Spaces and Stochastic Embeddings", Theorem D / Corollary 6.4.

## Claim

For every integer `n >= 2`, the Lipschitz-free space over real hyperbolic space satisfies

`F(H^n) ~= F(R^n)`.

Consequently `F(H^n)` has a Schauder basis, because `F(R^n)` has a Schauder basis by Hajek--Pernecka.

This answers both clauses of Question 6 in Doucha--Kaufmann. The first clause follows from the second by the known Euclidean basis theorem.

## Evidence

- `source_paper.pdf`: original arXiv:2005.09785 source.
- `supporting_paper_2406.10986.pdf`: later answer source.
- `figures/open_question_crop.png`: Question 6 in arXiv:2005.09785.
- `figures/supporting_intro_crop.png`: Gartland's Theorem D announcement.
- `figures/supporting_corollary_crop.png`: Corollary 6.4 and proof.

## Scope Notes

Gartland states hyperbolic `n`-space for `2 <= n in N`, matching the nontrivial hyperbolic spaces considered in the source paper. The one-dimensional real hyperbolic line is isometric to `R`, so the same conclusion is trivial there.

The related hyperbolic-group question reiterated in the same source paper was not duplicated here; it is already recorded in `solutions/literature_already_answered/1809.09957_hyperbolic_groups_free_space_l1/`.

## Verification Notes

The chain is direct:

1. Doucha--Kaufmann ask whether `F(H^n)` has a Schauder basis and whether `F(H^n) ~= F(R^n)`.
2. Gartland proves `LF(H^n) ~= LF(R^n)` in Corollary 6.4; Gartland's `LF` is the same Lipschitz-free space notation.
3. Hajek--Pernecka prove that `F(R^n)` has a Schauder basis.
4. Schauder-basis existence is preserved by Banach-space isomorphism.

