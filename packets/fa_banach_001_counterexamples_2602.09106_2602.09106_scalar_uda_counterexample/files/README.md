# Scalar Counterexample to the `U(d,a) <= C da` Question

Result type: `counterexample`

Status: human reviewed; rejected as a solution to the intended problem.

Source paper:

- William B. Johnson and Tomasz Kania, "Uniform Property (S)",
  arXiv:2602.09106.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Open Problem (3) asks:

> Is `U(d,a)` always smaller than `da` (up to a constant)?

As written, the answer is no in the real Banach-space category, even if
one restricts to spaces that have uniform property `(S)`.

Take the real one-dimensional Banach space `X = R`. Its unit sphere is
`{-1,1}`. This space has uniform property `(S)`, since the formula below
is always positive. For every `0 < d < 2`, the only admissible pair in
the infimum defining `U_R(d;a)` is the antipodal pair. For `0 < a <= 1`,

`U_R(d;a) = sup_{|z| <= a} ||1+z| - |-1+z|| = 2a`.

If a universal constant `C` satisfied `U_X(d;a) <= C d a` for all real
Banach spaces with uniform property `(S)`, all `0 < d < 2`, and all
`a > 0`, then the scalar example would give `2a <= C d a`, hence
`2 <= C d`, for every `d in (0,2)`. Letting `d` tend to zero is
impossible.

Thus no dimension-free universal bound of the form `C d a` can hold
without an additional hypothesis excluding the one-dimensional scalar
case or requiring genuine small-distance pairs in the unit sphere.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `human_review.tex`: human verification note.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: rendered packet followed by the human review.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of the
  open-problem list containing Problem (3).
- `code/check_scalar_modulus.py`: numerical sanity check for the scalar
  formula.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Human Review Notes

This candidate has been manually reviewed and should be rejected as a
solution to the intended problem. The obstruction is the trivial
one-dimensional scalar edge case, certainly not what was intended by the
authors. A meaningful version would require genuine small-distance geometry,
for example by considering spaces whose unit sphere has nontrivial pairs at
every small distance, or infinite-dimensional spaces with uniform property
`(S)`.

Follow-up note: `research/strengthened_Uda_memo.md` records a partial
proof-level boundary. In particular, the source paper's Theorem C already
implies the desired `U_X(d;a) <= C d a` upper bound for all
non-superreflexive Banach spaces, so any infinite-dimensional
counterexample must be superreflexive.
