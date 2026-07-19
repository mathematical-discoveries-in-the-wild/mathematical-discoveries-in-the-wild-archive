# Proper Purely Unrectifiable Spaces and Locally Flat Separation

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- R. J. Aliaga, "Lipschitz-free spaces and purely 1-unrectifiable metric
  spaces", arXiv:2606.02918.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

The source asks whether every purely `1`-unrectifiable metric space `M` has
`lip(M)` separating points uniformly.

This packet proves an affirmative answer for every proper purely
`1`-unrectifiable metric space, where proper means closed bounded balls are
compact. The proof runs the compact Bate/AGPP approximation argument along a
closed-ball exhaustion. After each compact-ball improvement, McShane extends
the function back to the whole space. The one-sided slope estimate in Bate's
lemma keeps earlier balls locally flat up to a summable error tail.

This is not a full answer for arbitrary purely `1`-unrectifiable metric
spaces; the proof uses compact neighborhoods essentially.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: rendered local copy of the original arXiv source.
- `figures/open_problem_crop.png`: full-width crop from page 6 showing the
  open question.
- `tmp/`: LaTeX build intermediates.

## Human Review Notes

The main points to verify are:

- the diagonal construction of the global function from compact-ball
  restrictions;
- preservation of old small-scale slope bounds under later compact
  approximations;
- the final local-flatness argument at an arbitrary point using the fact that
  the point is eventually interior to an exhaustion ball;
- the rescaling from Lipschitz constant `1+S` to `1` without losing the desired
  separation.
