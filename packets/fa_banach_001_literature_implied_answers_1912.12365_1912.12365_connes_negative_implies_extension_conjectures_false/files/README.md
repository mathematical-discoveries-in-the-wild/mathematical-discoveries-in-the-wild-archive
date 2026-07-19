# Literature-Implied Negative Answer: Burton--Juschenko Extension Conjectures

Run: `fa_banach_001`

Result type: `literature_implied_answer`

Status: later literature refutes Connes' embedding conjecture, and
arXiv:1912.12365 proves that its two main approximation/extension conjectures
would imply Connes' embedding. Therefore the half finite approximation
conjecture and the low energy extension conjecture in arXiv:1912.12365 are
false by contrapositive. This packet records a literature-status implication,
not an original construction of a finite counterexample.

## Original Problem Source

- Peter Burton and Kate Juschenko, *Extension of positive definite functions
  and Connes' embedding conjecture*, arXiv:1912.12365.
- Local PDF compiled from the arXiv source: `source_paper.pdf`.

The relevant source conjectures are:

- Conjecture 1.1, source label `thm.CEC`: Connes' embedding conjecture in the
  tensor-norm form
  `C^*(F) tensor_max C^*(F) = C^*(F) tensor_min C^*(F)`.
- Conjecture 1.3, source label `thm.half`: existence of half finite
  approximations for unitary representations of `F x F`.
- Conjecture 1.5, source label `lem.nogain`: existence of positive definite
  extensions with no energy gain for finite families in `NSPD(r,d)`.

The arXiv TeX source gives the implication chain explicitly. Lines 136--142
prove `thm.half => thm.CEC`, ending with the statement that it suffices to
prove `thm.half` in order to prove Connes' embedding. Lines 215--217 introduce
the proof of `thm.half` from `lem.nogain`.

## Supporting Sources

- Zhengfeng Ji, Anand Natarajan, Thomas Vidick, John Wright, and Henry Yuen,
  `MIP* = RE`, arXiv:2001.04383; Commun. ACM 64 (2021), no. 11, 131--138.
  Local PDF: `supporting_paper_2001.04383.pdf`.
- Isaac Goldbring, *The Connes Embedding Problem: A guided tour*,
  arXiv:2109.12682. Local PDF: `supporting_paper_2109.12682.pdf`.

The MIP*=RE paper states that its results refute Connes' embedding conjecture.
Goldbring's guide records the negative solution to CEP and its relation to the
Kirchberg/QWEP/Tsirelson problem cluster.

## Status Match

Burton--Juschenko state Connes' embedding conjecture as Conjecture 1.1 and
prove the implication

`low energy extension conjecture => half finite approximation conjecture =>
Connes' embedding conjecture`.

Since later literature gives `not Connes' embedding conjecture`, the exact
Conjecture 1.3 and Conjecture 1.5 of arXiv:1912.12365 cannot be true. Thus the
answer to both of the paper's strengthening conjectures is negative.

This is classified as `literature_implied_answers` rather than
`literature_already_answered`: the later papers refute Connes' embedding, while
the source paper supplies the implication from the Burton--Juschenko
conjectures to Connes' embedding.

## Verification Notes

- Cheap duplicate search covered `1912.12365`, the paper title, `Connes`,
  `positive definite functions`, `half finite`, and the existing
  MIP*=RE/Connes packet.
- Existing run packet
  `solutions/literature_implied_answers/1101.4195_connes_kirchberg_mip_re_negative/`
  already records the accepted negative status of CEP via MIP*=RE and
  Goldbring.
- No computation is involved.

## Limitations

This packet does not identify explicit values of `r`, `d`, or an explicit
finite family in `NSPD(r,d)` witnessing failure of Conjecture 1.5. It also does
not challenge the weak extension theorem proved inside arXiv:1912.12365. It
only records that the exact conjectures which imply Connes' embedding are
false.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original arXiv source compiled locally.
- `supporting_paper_2001.04383.pdf`: MIP*=RE source.
- `supporting_paper_2109.12682.pdf`: CEP guided-tour source.

## Human Review Recommendation

Verify the implication chain:

1. Burton--Juschenko Conjecture 1.3 implies their Conjecture 1.1.
2. Burton--Juschenko Conjecture 1.5 implies their Conjecture 1.3.
3. MIP*=RE refutes Connes' embedding conjecture.

If these are accepted, Conjectures 1.3 and 1.5 of arXiv:1912.12365 are false.
