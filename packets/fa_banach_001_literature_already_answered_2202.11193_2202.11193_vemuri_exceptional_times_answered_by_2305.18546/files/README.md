# Vemuri Exceptional Times Answered in Dimension One

Status: `literature_already_answered (one-dimensional exceptional-time completion)`.

Original/source paper: Aleksei Kulikov, Lucas Oliveira, and Joao P. G. Ramos,
"On Gaussian decay rates of harmonic oscillators and equivalences of related
Fourier uncertainty principles," arXiv:2202.11193 (published in Revista
Matematica Iberoamericana 40 (2024), 481--502).

Supporting paper: Danylo Radchenko and Joao P. G. Ramos, "Sharp Gaussian
decay for the one-dimensional harmonic oscillator," arXiv:2305.18546
(published in Proceedings of the AMS 153 (2025), 1985--1991).

## Identification

The source paper states Vemuri's conjecture on PDF page 3 and proves it in
Theorem 1.1 on PDF page 4 except at the arithmetic progression
`t=(2k+1)/16`. Radchenko--Ramos explicitly say that their main purpose is to
prove the conjecture in those remaining cases, and their Theorem 1 gives the
endpoint Gaussian bound for all real times in one dimension.

The supporting authors knew they were completing the source result: they cite
Kulikov--Oliveira--Ramos and name precisely the exceptional times left there.

## Scope Limitations

This packet records only the one-dimensional completion of Vemuri's original
uniform endpoint conjecture. It does not settle:

- the exceptional-time extension of the source's higher-dimensional theorem;
- the stronger time-dependent exponent conjecture (Conjecture 3.1 in the
  published numbering / `conjecture:upgraded-vemuri` in the arXiv source);
- the source's general `L^2`-to-`L^infinity` endpoint question.

## Files

- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: arXiv:2202.11193.
- `supporting_paper_2305.18546.pdf`: the completing paper.
- `tmp/`: LaTeX build intermediates and rendered QA pages.
