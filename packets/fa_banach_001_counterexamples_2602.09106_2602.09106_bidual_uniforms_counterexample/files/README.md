# Counterexample to Bidual Stability of Uniform Property `(S)`

Result type: `counterexample`

Status: human reviewed; correct, but already known to the authors in a
yet-unpublished new version.

Source paper:

- William B. Johnson and Tomasz Kania, "Uniform Property (S)",
  arXiv:2602.09106.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Open Problem (5) asks whether `X**` must have uniform property `(S)` when
`X` has uniform property `(S)`.

The packet gives a negative answer in the real Banach-space category:

`X = L_1[0,1]`

has uniform property `(S)` by Theorem 1.2 of the source paper. However,

`X** = (L_infty[0,1])*`

is isometric to a measure space `M(K)` for the Stone/Gelfand compact
space `K` of `L_infty[0,1]`. Since `K` has at least two points, `X**`
contains two disjoint atoms, say `delta_s` and `delta_t`.

The two norm-one positive measures

`u = (3/4) delta_s + (1/4) delta_t`,
`v = (1/4) delta_s + (3/4) delta_t`

satisfy `||u-v|| = 1`, but for every real signed measure `z` with
`||z|| <= 1/8`, one has `||u+z|| = ||v+z||`. Hence
`U_{X**}(1;1/8)=0`, so `X**` does not have uniform property `(S)`.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `human_review.tex`: human verification note.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: rendered packet followed by the human review.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of the
  open-problem list containing Problem (5).
- `code/check_atomic_band.py`: numerical sanity check for the atomic
  total-variation calculation.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Human Review Notes

The proof uses only standard representation facts:

- `L_infty[0,1]` is a commutative unital Banach lattice/algebra
  represented as `C(K)` for a compact Hausdorff space `K`.
- `(C(K))*` is the space of regular signed measures on `K`.
- Dirac measures at two distinct points are disjoint atoms.

The obstruction is not merely that `X**` contains a bad subspace; the two
atoms form a band, and the total-variation norm calculation survives all
small perturbations in the full bidual.

Author follow-up note: after reaching out to the authors, they indicated that
they had already found the same example for a new version that has not yet
been published. Therefore this packet should be archived as a correct
rediscovery/check, not as a novel contribution.
