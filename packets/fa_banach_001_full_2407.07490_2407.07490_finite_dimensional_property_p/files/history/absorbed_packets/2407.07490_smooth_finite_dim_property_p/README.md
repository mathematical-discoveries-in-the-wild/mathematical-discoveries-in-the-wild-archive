# Smooth finite-dimensional spaces have Property (P)

Status: partial result, likely valid.

Source target: arXiv:2407.07490, Debmalya Sain, Arpita Mal, Kalidas Mandal
and Kallol Paul, *On uniform Bishop-Phelps-Bollobas type approximations of
linear operators and preservation of geometric properties*.

The source paper asks whether every finite-dimensional Banach space satisfies
Property (P), and also asks about the infinite-dimensional case. The paper
proves Property (P) for finite-dimensional polyhedral spaces, Hilbert spaces,
and later for the special spaces `ell_p^2` with integer `p>2`.

This packet proves the following new partial answer:

> Every finite-dimensional smooth real Banach space satisfies Property (P).

This covers all real `ell_p^n` for `1<p<infty`, including the non-Hilbert and
non-polyhedral cases, and goes well beyond the source paper's two-dimensional
integer-`p` result.

What remains open:

- arbitrary finite-dimensional nonsmooth nonpolyhedral spaces;
- the infinite-dimensional question;
- the complex version, unless one separately records the real-smooth
  differentiability convention needed for the proof.

Proof mechanism:

If Property (P) failed, there would be norm-one non-isometries whose norm
attainment sets are arbitrarily dense in the sphere. Compactness forces such
operators close to the compact isometry group. After conjugating by a nearest
isometry, write them as `I+t_n C_n`. Smoothness and density of the norm
attainment sets imply that the limiting infinitesimal operator `C` satisfies
`j(x)(Cx)=0` for every unit vector `x`, where `j(x)` is the unique norming
functional. Hence `exp(sC)` is an isometry for every real `s`. But then
`exp(t_n C)` is an isometry closer to `I+t_n C_n` than the chosen nearest
isometry, a contradiction.

Novelty check:

Before promotion, the run indexes were searched for `2407.07490`, Property
`(P)`, uniform BPB/Bishop-Phelps-Bollobas, and nearby BPB terms. No duplicate
packet or attempt for this exact source question was found. A bounded web
search on 2026-06-19 for close phrases including `"Property (P)" "uniform"
"BPB" "finite-dimensional Banach"` and `"Is it true that each
finite-dimensional Banach space" "Property (P)" "BPB"` did not reveal a later
answer.

Files:

- `main.tex` - self-contained proof packet.
- `solution_packet.pdf` - compiled human-readable packet.
- `source_paper.pdf` - local copy of the source paper.
- `figures/open_problem_crop.png` - crop of the source open question.

