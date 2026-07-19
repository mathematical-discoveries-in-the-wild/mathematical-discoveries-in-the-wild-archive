# Literature-Already-Answered Packet: `L_2+L_\infty` versus `L_2\cap L_\infty`

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- S. V. Astashkin and L. Maligranda, *`L_p+L_\infty` and
  `L_p\cap L_\infty` are not isomorphic for all `1<=p<infty`,
  `p != 2`*, arXiv:1704.01717; Proc. Amer. Math. Soc. 146 (2018),
  no. 5, 2181--2194.
- Local PDF: `source_paper.pdf`.
- Evidence image: `figures/open_problem_crop.png` (page 13).

Problem 2 asks whether the spaces `L_2+L_\infty` and
`L_2\cap L_\infty`, on `(0,\infty)`, are isomorphic.

## Supporting Answer Source

- S. V. Astashkin and L. Maligranda, *`L_p+L_q` and
  `L_p\cap L_q` are not isomorphic for all `1<=p,q<=infty`,
  `p != q`*, arXiv:1804.03469.
- Local PDF: `supporting_paper_1804.03469.pdf`.
- Evidence images:
  - `figures/supporting_answer_crop.png` (page 1 abstract).
  - `figures/supporting_theorem_crop.png` (page 3 Theorem 2).
  - `figures/supporting_reference_crop.png` (page 6 reference `[2]`).

## Status

The original problem is answered negatively by arXiv:1804.03469.

The supporting paper explicitly says in its abstract that
`L_2+L_\infty` and `L_2\cap L_\infty` are not isomorphic and that this is
an answer to a question formulated in reference `[2]`.  Its reference `[2]`
is the original Astashkin--Maligranda PAMS paper arXiv:1704.01717.  The
supporting paper also states the same conclusion as Theorem 2.

## Verification Notes

- Same-paper check: arXiv:1704.01717 states the `L_2` isomorphism question
  as open in Section 4 and does not answer it there.
- Separate-source check: arXiv:1804.03469 is a later and distinct paper.
  It explicitly identifies the `p=2`, `q=\infty` case as its motivation
  and as an answer to the earlier question.
- The supporting theorem is stronger than the extracted problem: Theorem 1
  proves that `L_p+L_q` and `L_p\cap L_q` are isomorphic if and only if
  `p=q` for all `1<=p,q<=infty`.  Theorem 2 isolates the needed
  `L_2+L_\infty` case.

## Search Bounds

- Checked `runs/fa_banach_001/registry.md`,
  `runs/fa_banach_001/solutions/index.tsv`,
  `runs/fa_banach_001/attempts/index.tsv`, and
  `runs/fa_banach_001/proof_gaps/index.tsv` for arXiv:1704.01717,
  `L_1+L_\infty`, `L_2+L_\infty`, and `L_2\cap L_\infty`.
- Checked local parsed source
  `data/parsed/arxiv_sources/1704.01717/source.tex` at the problem
  statement.
- Web searches on 2026-06-13 for the original title, arXiv:1704.01717,
  `L_p+L_\infty`, `L_2+L_\infty`, and `L_2\cap L_\infty` found
  arXiv:1804.03469 as the direct later answer.
- Downloaded and inspected both arXiv PDFs.

## Limitations

- This is not an original proof from the run.
- This packet records only the final `L_2+L_\infty` versus
  `L_2\cap L_\infty` problem from arXiv:1704.01717.
- It does not answer the separate Problem 1 in the original paper asking
  whether `L_1+L_\infty` is isomorphic to a dual space.  That search was
  recorded separately as
  `runs/fa_banach_001/attempts/1704.01717_l1_plus_linf_dual_status.md`.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact review packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_1804.03469.pdf`: later answer source.
- `figures/open_problem_crop.png`: original problem evidence.
- `figures/supporting_answer_crop.png`: supporting abstract evidence.
- `figures/supporting_theorem_crop.png`: supporting theorem evidence.
- `figures/supporting_reference_crop.png`: supporting reference-list evidence.
- `tmp/`: render intermediates and page images.

## Human Review Recommendation

Verify the exact-source chain:

1. arXiv:1704.01717 page 13 asks whether `L_2+L_\infty` and
   `L_2\cap L_\infty` are isomorphic.
2. arXiv:1804.03469 page 1 says the negative `L_2` answer answers the
   question in reference `[2]`.
3. arXiv:1804.03469 page 6 identifies `[2]` as the original
   Astashkin--Maligranda PAMS paper.
4. arXiv:1804.03469 Theorem 2 states the required non-isomorphism directly.
