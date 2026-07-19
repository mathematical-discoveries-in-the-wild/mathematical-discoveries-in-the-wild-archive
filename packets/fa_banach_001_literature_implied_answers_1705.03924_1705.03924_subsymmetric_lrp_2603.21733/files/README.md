# Literature-Implied Partial Answer: Subsymmetric Bases With LRP

Status: `literature_implied_answer (partial subcase)`

Run: `fa_banach_001`

Source/open-problem paper: arXiv:1705.03924, Fernando Albiac, Jose L.
Ansorena, and Ben Wallis, "1-Greedy renormings of Garling sequence spaces."

Supporting paper: arXiv:2603.21733, Fernando Albiac, Jose L. Ansorena, Miguel
Berasategui, and Pablo M. Berna, "Isometric renormings for greedy bases in
Banach spaces, with applications to the Haar System in L_p[0,1], 1<p<infty."

## Claim Recorded

Problem 3.3 of arXiv:1705.03924 asks:

> Does every Banach space with a subsymmetric basis admit a `1`-greedy
> renorming?

The supporting paper gives a strong positive partial answer:

> If a Banach space has a subsymmetric basis whose upper superdemocracy
> function, equivalently fundamental function in this setting, has the lower
> regularity property (LRP), then the space admits an equivalent norm for which
> that basis is isometrically greedy, isometrically bidemocratic, and
> isometrically subsymmetric.

In particular, the same supporting paper proves this for subsymmetric bases in
Banach spaces with nontrivial cotype.

## Evidence Locations

- arXiv:1705.03924, page 11, Problem 3.3: the broad subsymmetric-basis
  renorming question.
- arXiv:2603.21733, page 23, Theorem 5.2: the LRP/fundamental-function
  subcase.
- arXiv:2603.21733, page 23, Theorem 5.3: the nontrivial-cotype subcase.
- arXiv:2603.21733, page 26: the authors state that the general answer for
  subsymmetric bases is still absent and point to the remaining no-LRP regime.

## Identification

Subsymmetric bases are greedy and bidemocratic in the framework of the
supporting paper. Theorem 5.2 of arXiv:2603.21733 applies exactly to a
Banach space with a subsymmetric basis once its fundamental function has LRP.
The resulting equivalent norm makes the basis isometrically greedy; this is
the `1`-greedy renorming requested by Problem 3.3 in the source paper.

The connection is recorded as `literature_implied_answer`, not
`literature_already_answered`, because the supporting paper does not state that
it solves Problem 3.3 of arXiv:1705.03924 in full. It explicitly leaves the
general problem open.

## Search Notes

Cheap run-index searches for `1705.03924`, `Garling sequence spaces`,
`subsymmetric basis`, `1-greedy renorming`, `1-GUR`, `Property (A)`, and
`greedy basis` found no prior packet for this exact subcase. Web searches on
2026-06-15 found arXiv:2603.21733 as the decisive recent supporting paper, but
no full solution of the broad Problem 3.3.

## Limitations

This packet does not settle all subsymmetric bases. The remaining territory is
the no-LRP regime, highlighted explicitly in arXiv:2603.21733, including the
question about the canonical basis of the dual Schlumprecht space.

