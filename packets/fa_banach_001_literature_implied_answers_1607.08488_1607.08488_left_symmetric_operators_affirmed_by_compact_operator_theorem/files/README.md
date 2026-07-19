# Literature-Implied Answer: Left Symmetric Operators In Strictly Convex Spaces

Run: `fa_banach_001`

Result type: `literature_implied_answer`

Status: later literature proves a stronger theorem that affirmatively settles
both conjectures at the end of arXiv:1607.08488. The source conjectured that
the only left symmetric operators on `l_p^n`, and more generally on any finite
dimensional strictly convex smooth real Banach space, are zero. A 2018 theorem
of Paul--Mal--Wojcik proves this under weaker finite-dimensional hypotheses:
for compact operators from a reflexive strictly convex domain into a strictly
convex range, left symmetry is equivalent to being the zero operator.

## Original Problem Source

- Debmalya Sain, *Birkhoff-James orthogonality of linear operators on finite
  dimensional Banach spaces*, arXiv:1607.08488; J. Math. Anal. Appl. 447
  (2017), 860--866.
- Local PDF compiled from the arXiv source: `source_paper.pdf`.

The source states:

- Conjecture 2.13: if `X = l_p^n`, `p > 1`, `p != infinity`, then
  `T in L(X)` is left symmetric if and only if `T = 0`.
- Conjecture 2.14: if `X` is a finite dimensional strictly convex and smooth
  real Banach space, then `T in L(X)` is left symmetric if and only if `T = 0`.

Source anchors:

- Lines 52 and 96 state the conjectural extension from `l_p^2` to all finite
  dimensional strictly convex smooth real Banach spaces.
- Lines 272--278 state Conjectures 2.13 and 2.14.
- Line 280 notes that Conjecture 2.14 implies Conjecture 2.13.

## Supporting Source

- Kallol Paul, Arpita Mal, and Pawel Wojcik, *Symmetry of Birkhoff-James
  orthogonality of operators defined between infinite dimensional Banach
  spaces*, arXiv:1807.11166.
- Local PDF compiled from the arXiv source: `supporting_paper_1807.11166.pdf`.

The supporting paper states in its introduction that it improves the finite
dimensional results of Sain et al. It proves:

- Theorem at source lines 188--190: if `X` is reflexive and strictly convex,
  `Y` is strictly convex, and `T in K(X,Y)`, then `T` is left symmetric if and
  only if `T = 0`.

## Status Match

Take `Y = X`, where `X` is a finite dimensional strictly convex smooth real
Banach space. Then:

- `X` is reflexive.
- every operator `T in L(X)` is compact, so `T in K(X,X)`;
- the range space `Y = X` is strictly convex.

The 2018 theorem therefore applies and gives exactly the conclusion of
Conjecture 2.14. Since every finite dimensional `l_p^n` with `1 < p < infinity`
is strictly convex, the same theorem also gives Conjecture 2.13.

This is classified as `literature_implied_answers`, because the supporting
paper proves a stronger theorem that subsumes the source conjectures rather
than explicitly naming Conjectures 2.13 and 2.14 of arXiv:1607.08488.

## Verification Notes

- Cheap duplicate search covered `1607.08488`, `left symmetric`,
  `Conjecture 2.13`, `Conjecture 2.14`, `l_p^n`, and Birkhoff-James operator
  symmetry terms.
- No existing packet for this implication was found in the run indexes.
- No computation is involved beyond compiling local arXiv sources.

## Limitations

This packet only addresses the left-symmetric operator conjectures 2.13 and
2.14 of arXiv:1607.08488. It does not classify right symmetric operators or
the non-strictly-convex examples discussed elsewhere in the source and
supporting papers.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original arXiv:1607.08488 source compiled locally.
- `supporting_paper_1807.11166.pdf`: supporting arXiv:1807.11166 source
  compiled locally.

## Human Review Recommendation

Verify the implication:

1. Conjecture 2.14 asks for the zero-operator-only left symmetry conclusion on
   finite dimensional strictly convex smooth real spaces.
2. Theorem 2.4 of arXiv:1807.11166 proves the same conclusion for compact
   operators from reflexive strictly convex spaces into strictly convex spaces.
3. In finite dimension, all operators are compact and the domain is reflexive.

If accepted, Conjectures 2.13 and 2.14 are affirmatively settled by later
literature.
