# Literature-already-answered packet: Carbery's Schatten almost-orthogonality question

Status: `literature_already_answered`

This packet records an exact later-literature answer. It is not claimed as a
new proof by the pipeline. The supporting paper explicitly says it
affirmatively answers Carbery's question from Section 3.3, equation (3.1), and
then proves the corresponding theorem.

## Source

- Anthony Carbery, *Almost-orthogonality in the Schatten--von Neumann classes*,
  Journal of Operator Theory 62(1):151--158, 2009.
- Local PDF: `source_paper.pdf`.

## Target question

Carbery asks whether, under the hypotheses of his Theorem 1.3, the triangle
inequality can be sharpened with the `ell_2` operator norm of
`(alpha_jk^{p'})`:

`||sum_j T_j||_p <= A_p^{1/p'} (sum_j ||T_j||_p^p)^{1/p}`.

The exact source location is shown in `figures/open_problem_crop.png`, cropped
from article page 106 / PDF page 7 of `source_paper.pdf`.

## Later answer

- arXiv:2606.04116
- Title: *Carbery's inequality in the Schatten--von Neumann classes*
- Authors: Ziang Chen, Paata Ivanisvili, Jose Madrid, and Haozhu Wang
- Local PDF: `supporting_paper_2606.04116.pdf`

The answer is affirmative. The supporting paper states that it answers the
question posed by Carbery in `[2, Section 3.3, (3.1)]` in full generality for
the Schatten--von Neumann classes, and its Theorem 1.1 proves the displayed
operator-norm inequality for all real `p >= 2` and arbitrary operators in
`S_p`.

## Files

- `solution_packet.pdf`: human-readable packet.
- `main.tex`: LaTeX source for the packet.
- `source_paper.pdf`: original PDF containing the open question.
- `supporting_paper_2606.04116.pdf`: later arXiv PDF containing the explicit answer.
- `figures/open_problem_crop.png`: full-width crop showing Carbery's question.
- `figures/supporting_answer_crop.png`: crop showing the later explicit answer and theorem.
- `code/crop_evidence.py`: reproducible crop generator after the page PNGs are rendered.
- `tmp/`: build and rendering artifacts only.

## Human review note

The human check should focus on the exact identification of Carbery's `C_p`
notation with the supporting paper's `S_p` notation, and on the fact that both
statements use the same almost-orthogonality hypotheses and the `ell_2`
operator norm of `(alpha_ij^{p'})`.
