# Strong Norm Attainment Questions Answered By arXiv:1907.07698

Status: literature_already_answered.

Source/open-problem paper: Bernardo Cascales, Richard Chiclana, Luis C.
Garcia-Lirola, Manuel Martin, and Abraham Rueda Zoca, *On strongly norm
attaining Lipschitz maps*, arXiv:1807.03363.

Source signal covered here: the introduction records that it was unknown
whether the RNP of `F(M)` is necessary for density of `SA(M,Y)` in `Lip(M,Y)`
for every Banach space `Y`, and asks about the relation with Lindenstrauss
property A.

Supporting answer paper: Richard Chiclana, Luis C. Garcia-Lirola, Manuel
Martin, Abraham Rueda Zoca, and Pedro Tradacete, *Examples and applications of
the density of strongly norm attaining Lipschitz maps*, arXiv:1907.07698.

Answer status:

- Q1/RNP necessity is answered negatively by Theorem `theo:lluvia` of
  arXiv:1907.07698: the spaces `M_p` satisfy density of `SA(M_p,Y)` for every
  `Y` while containing isometric copies of `[0,1]`, so `F(M_p)` fails the RNP.
- The related expectation that an `L_1[0,1]` copy prevents density is also
  answered negatively by the same theorem.
- Q2, whether convex hull of strongly exposed points or Gromov concavity
  suffices for density of scalar strongly norm-attaining Lipschitz maps, is
  answered negatively by Theorem `theo:toro` for the Euclidean circle.
- Q3 is answered affirmatively in the compact case by Theorem
  `theorem:clcvstrepcompact` and in the boundedly compact case by Corollary
  `coro:clcvstrepbouncompact`.

Packet contents:

- `source_paper.pdf`: original arXiv:1807.03363 PDF.
- `supporting_paper_1907.07698.pdf`: supporting arXiv:1907.07698 PDF.
- `main.tex`: compact LaTeX status note.
- `solution_packet.pdf`: rendered status note.
- `tmp/`: LaTeX build outputs.

Scope:

This is not a new proof packet. It clears the RNP/density branch from
arXiv:1807.03363 that was later isolated as Q1 in arXiv:1907.07698, and it
records the related Q2--Q4 status developed in that follow-up. It does not
claim to settle the newer residual questions introduced in arXiv:1907.07698,
such as bi-Lipschitz/closed-subset variants of the RNP question or the
equivalent-metric question on `[0,1]`. It also does not record a later answer
to the octahedrality question mentioned in arXiv:1807.03363.
