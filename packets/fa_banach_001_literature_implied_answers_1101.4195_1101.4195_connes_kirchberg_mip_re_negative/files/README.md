# Literature-Implied Answer: Connes--Kirchberg/QWEP problem

Run: `fa_banach_001`

Result type: `literature_implied_answer`

Status: later literature gives a negative answer to the Connes--Kirchberg
problem appearing in Pisier's arXiv:1101.4195. This packet records a
literature-status implication, not an original proof from the run.

## Original Problem Source

- Gilles Pisier, *Grothendieck's Theorem, past and present*,
  arXiv:1101.4195; Bull. Amer. Math. Soc. 49 (2012), 237--323.
- Local PDF: `source_paper.pdf`.

In the downloaded BAMS-numbered PDF, the relevant questions appear as
Problems 12.9 and 12.10. In the source TeX they are labelled
`prbl10.4` and `prbl10.4bis`. The questions ask whether, for
`A = C^*(F_N)`, `N > 1`, there is a unique C*-norm on `A tensor A`,
equivalently whether `(A,A)` is a nuclear pair, and equivalently whether
every C*-algebra is QWEP. The surrounding paragraph states the equivalence
with Connes' embedding problem.

## Supporting Sources

- Zhengfeng Ji, Anand Natarajan, Thomas Vidick, John Wright, and Henry Yuen,
  `MIP* = RE`, arXiv:2001.04383; Commun. ACM 64 (2021), no. 11, 131--138.
  Local PDF: `supporting_paper_2001.04383.pdf`.
- Isaac Goldbring, *The Connes Embedding Problem: A guided tour*,
  arXiv:2109.12682. Local PDF: `supporting_paper_2109.12682.pdf`.

The MIP*=RE paper states that its results refute Connes' embedding
conjecture. Goldbring's guide records the negative CEP solution and describes
the traditional route through Kirchberg's QWEP problem and Tsirelson's
problem.

## Status Match

Pisier's problem is one of Kirchberg's equivalent formulations of Connes'
embedding/QWEP. Since MIP*=RE gives a negative answer to Connes' embedding
problem, the equivalent Kirchberg/QWEP formulations in Problems 12.9 and
12.10 are false. Thus the answer to the tensor-norm question for
`C^*(F_N) tensor C^*(F_N)` in the nonabelian free group case is negative,
and not every C*-algebra is QWEP.

This is classified as `literature_implied_answers` rather than
`literature_already_answered` because the later theorem is identified with
the source problem through the equivalence chain stated in Pisier's paper and
standard later accounts, not because the later paper explicitly names
Problem 12.9 of arXiv:1101.4195.

## Idea Of The Answer

The source problem is deliberately formulated as an equivalent avatar of CEP.
A positive solution would collapse the minimal and maximal C*-tensor norms on
the full group C*-algebra tensor square, or equivalently make every
C*-algebra QWEP. The later MIP*=RE theorem proves a separation in quantum
correlations that refutes CEP. Transporting that negative result back through
Kirchberg's equivalence gives the negative answer to Pisier's tensor-norm and
QWEP formulations.

## Verification Notes

- Cheap duplicate search covered `1101.4195`, `2001.04383`,
  `2109.12682`, `Connes Embedding`, `QWEP`, `Kirchberg`, and `MIP*`; no
  existing run packet covered this exact implication.
- Source evidence crop: `figures/open_problem_crop.png`, page 41 of
  `source_paper.pdf`.
- Supporting evidence crops:
  `figures/mip_re_connes_refutation_crop.png`, page 1 of
  `supporting_paper_2001.04383.pdf`, and
  `figures/goldbring_cep_qwep_negative_crop.png`, page 1 of
  `supporting_paper_2109.12682.pdf`.
- No computation is involved.

## Limitations

This packet addresses only the Connes--Kirchberg/QWEP problem cluster in
Section 12 of arXiv:1101.4195. The survey contains many other open problems,
including exact Grothendieck constants, noncommutative Khintchine questions,
and later operator-space multilinear problems; they are not claimed here.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2001.04383.pdf`: MIP*=RE source.
- `supporting_paper_2109.12682.pdf`: CEP/QWEP guided-tour source.
- `figures/open_problem_crop.png`: rendered crop of Problems 12.9--12.10.
- `figures/mip_re_connes_refutation_crop.png`: rendered crop of the MIP*=RE
  abstract statement refuting CEP.
- `figures/goldbring_cep_qwep_negative_crop.png`: rendered crop of the guided
  tour abstract linking negative CEP to Kirchberg's QWEP route.

## Human Review Recommendation

Verify the equivalence chain:

1. Pisier's source states that the tensor-norm problem for
   `C^*(F_N) tensor C^*(F_N)`, `N > 1`, is equivalent to Connes' embedding
   problem and to QWEP.
2. Ji--Natarajan--Vidick--Wright--Yuen prove MIP*=RE and state that this
   refutes Connes' embedding conjecture.
3. Goldbring records the negative CEP solution and the route through
   Kirchberg's QWEP problem.

If these are accepted, the answer to Pisier's Problems 12.9 and 12.10 is
negative.
