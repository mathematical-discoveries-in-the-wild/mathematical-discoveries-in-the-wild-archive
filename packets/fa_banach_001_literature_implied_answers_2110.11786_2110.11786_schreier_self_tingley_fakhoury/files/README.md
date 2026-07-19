# Literature-Implied Schreier Self-Sphere Case of Tingley's Problem

Status: `literature_implied_answer (partial subcase)`

Source paper: Leandro Antunes and Kevin Beanland, "Surjective isometries on Banach sequence spaces: a survey", arXiv:2110.11786.

Supporting paper: Micheline Fakhoury, "Tingley's problem for Schreier spaces and their p-convexifications", arXiv:2412.00891.

## Target

Problem 3.2 of arXiv:2110.11786 asks whether, for a regular family
`\mathcal F`, every surjective sphere isometry
`V:S_{X_\mathcal F}->S_X` extends to a linear surjective isometry
`U:X_\mathcal F->X`. The source notes that the problem is open even for
`\mathcal F=\mathcal S_1`, the classical Schreier family.

## Packet Claim

Fakhoury's Theorem 1.1 gives a positive answer to the real self-map subcase:
for the real Schreier space `X_{\mathcal S_1}`, every surjective isometry
`T:S_{X_{\mathcal S_1}}->S_{X_{\mathcal S_1}}` extends to a linear
surjective isometry of `X_{\mathcal S_1}`.

This is a literature-implied partial subcase. It does not settle the full
Mazur-Ulam property asked in the source problem, because the source problem
allows arbitrary target spaces `X`, while the supporting theorem handles the
self-sphere case `X=X_{\mathcal S_1}`. Fakhoury's paper is also stated for
real spaces.

## Evidence

- `source_paper.pdf`: arXiv:2110.11786.
- `figures/open_problem_crop.png`: Problem 3.2 and the note that it is open
  even for `\mathcal F=\mathcal S_1`.
- `supporting_paper_2412.00891.pdf`: arXiv:2412.00891.
- `figures/supporting_theorem_crop.png`: Fakhoury's Theorem 1.1.
- `main.tex` / `solution_packet.pdf`: review packet with the direct
  specialization relation.

## Verification Focus

Check that Fakhoury's notation `X_{\mathcal S_\alpha,1}` agrees with the
Schreier space `X_{\mathcal S_\alpha}` used in the source survey, and that
specializing Theorem 1.1 to `\alpha=1`, `p=1` gives exactly the self-map
subcase stated above. The packet should be classified by provenance as
`literature_implied_answers`, while retaining this partial-subcase scope.
