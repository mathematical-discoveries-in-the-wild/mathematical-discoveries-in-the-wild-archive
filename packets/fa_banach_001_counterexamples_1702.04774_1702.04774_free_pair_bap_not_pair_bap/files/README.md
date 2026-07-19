# Counterexample Packet: Free-Space Pair BAP Need Not Imply Pair BAP

Status: `counterexample_likely_valid`

Source: Javier Alejandro Chavez-Dominguez, "An Ando-Choi-Effros lifting theorem respecting subspaces", arXiv:1702.04774.

Target: Section 7 says that the Godefroy-Kalton theorem equates BAP, Lipschitz BAP, and BAP of the Lipschitz-free space for a single Banach space, and asks whether a similar result holds for BAP for pairs.

Claim: Under the natural Banach-pair interpretation, the implication

```text
(F(X), F(Y)) has BAP  =>  (X,Y) has BAP
```

is false.

## Construction

Use the source paper's Proposition 6.11. It constructs a separable pair `(X,Y)` with the Lipschitz BAP but without the BAP. In the proof, `X=c(E_n)` and `Y=c_0(E_n)` for a paving of a separable Banach lattice `Z` without the approximation property. The source also notes that `X` and `Y` have BAP individually and that there is a Lipschitz retraction `P:X->Y`.

Since `X` has BAP, the Godefroy-Kalton theorem gives BAP for `F(X)`. The Lipschitz retraction `P` linearizes to a bounded projection `\widehat P:F(X)->F(Y)`. A standard complemented-subspace lemma then yields BAP for the pair `(F(X),F(Y))`.

Thus `(F(X),F(Y))` has BAP while `(X,Y)` does not.

## Scope

This packet disproves the free-space-to-original-pair implication for Banach-space pairs. It does not challenge the source paper's compact/separable metric-pair characterizations in Section 7, and it does not claim to settle every possible formulation of a "similar result" for arbitrary metric pairs.

## Verification

- `figures/open_problem_and_example_crop.png` captures the source's Proposition 6.11 and the Section 7 question sentence.
- `solution_packet.pdf` contains the formal proof.

## Novelty Check

Cheap run indexes were searched for `1702.04774`, the title, `Ando-Choi-Effros lifting`, `BAP for pairs`, `Lipschitz-free`, and nearby terms. No exact prior packet for this arXiv id or target was found.

External web searches on 2026-06-20 for phrases including `"BAP for pairs" "Lipschitz-free spaces"`, `"F(X), F(Y)" "BAP" "pair"`, and `"free-space pair" "BAP" "without the BAP"` returned the source paper or no direct answer.

## Human Review Recommendation

Review the intended reading of the source phrase "similar result". The counterexample is targeted at the natural implication from BAP of the free-space Banach pair back to BAP of the original Banach pair.
