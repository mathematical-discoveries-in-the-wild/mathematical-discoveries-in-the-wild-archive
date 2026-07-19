# Literature-Already-Answered Packet: bounded multipliers on quantum tori

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: a separate later paper gives a negative answer to the bounded
multiplier question asked in Section 7 of arXiv:1206.3358. This packet records
literature status only; it is not an original proof from the run.

## Original Problem Source

- Z. Chen, Q. Xu, and Z. Yin, *Harmonic analysis on quantum tori*,
  arXiv:1206.3358.
- Local source inspected: `data/parsed/arxiv_sources/1206.3358/source.tex`,
  lines 1544--1552.
- Local PDF: `source_paper.pdf`.

The source asks whether, for `2 < p <= infinity`, ordinary bounded Fourier
multipliers on the quantum torus agree with those on the classical torus:
`M(L_p(T^d_theta)) = M(L_p(T^d))`. The authors conjecture that the answer is
negative and give only an infinite-generator `p = infinity` model example.

## Supporting Answer Source

- E. Ricard, *L_p-Multipliers on Quantum Tori*, arXiv:1512.01142; J. Funct.
  Anal. 270 (2016), 4604--4613.
- Local supporting source inspected from arXiv e-print:
  `tmp/supporting_source_1512.01142.tar`, source lines 191--196, 498--517,
  and 604--612.
- Local PDF: `supporting_paper_1512.01142.pdf`.

## Status Match

Ricard's abstract states that the completely bounded multiplier spaces are
theta-independent by Chen--Xu--Yin, but that bounded multipliers behave
differently. Theorem `ex1` in the arXiv source proves that for every irrational
`theta` and every `1 < p != 2 < infinity` there is a symbol `phi` bounded as an
`L_p(T^2)` Fourier multiplier but unbounded as an `L_p(T^2_theta)` multiplier.
This gives a negative answer throughout the finite part of the source range,
in particular for `2 < p < infinity`.

For the endpoint `p = infinity`, Proposition `ex3` in Ricard's arXiv source
constructs, for every irrational `theta`, a symbol bounded on
`L_infinity(T^2_theta)` whose completely bounded norm is infinite. Since the
same paper recalls the Chen--Xu--Yin equality identifying this cb norm with the
classical `L_infinity(T^2)` multiplier norm, this yields a bounded quantum
multiplier that is not a classical bounded multiplier. Thus the endpoint is
also answered negatively.

## Scope Limitations

This packet clears the ordinary bounded multiplier equality question for the
source range `2 < p <= infinity`, by negative examples on irrational
two-dimensional quantum tori. It does not attempt to classify all bounded
multiplier spaces for rational theta, nor does it produce a new proof beyond
the literature identification.

## Verification Notes

- Same-paper check: arXiv:1206.3358 asks the bounded multiplier equality
  question and supplies only an infinite-generator illustration, not a finite
  quantum-torus answer.
- Separate-source check: arXiv:1512.01142 is a later paper whose abstract and
  main theorems explicitly contrast bounded multipliers with the Chen--Xu--Yin
  completely bounded equality.
- Local duplicate check: the cheap run indexes had no exact packet for
  arXiv:1206.3358 or Ricard's arXiv:1512.01142 multiplier answer before
  creation.
- Literature search evidence: arXiv and ScienceDirect metadata identify the
  supporting paper as *L_p-Multipliers on Quantum Tori* and state that bounded
  multipliers behave differently from the cb case.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_1512.01142.pdf`: decisive supporting answer source.
- `tmp/supporting_source_1512.01142.tar`: downloaded arXiv e-print payload
  used to inspect theorem labels and statements.

## Human Review Recommendation

Verify the exact source chain:

1. arXiv:1206.3358, Section 7 asks whether
   `M(L_p(T^d_theta)) = M(L_p(T^d))` for `2 < p <= infinity`.
2. arXiv:1512.01142, Theorem `ex1` gives a finite-dimensional irrational
   two-torus counterexample for every `1 < p != 2 < infinity`.
3. arXiv:1512.01142, Proposition `ex3` gives the corresponding negative
   endpoint information at `p = infinity`, using the cb/classical equality.
