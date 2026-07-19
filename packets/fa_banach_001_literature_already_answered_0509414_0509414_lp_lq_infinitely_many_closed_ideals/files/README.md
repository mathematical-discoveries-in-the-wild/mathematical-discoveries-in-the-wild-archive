# Literature-Already-Answered Packet: Infinitely Many Closed Ideals in `L(ell_p oplus ell_q)`

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- B. Sari, Th. Schlumprecht, N. Tomczak-Jaegermann, V. G. Troitsky,
  *On norm closed ideals in L(ell_p oplus ell_q)*, arXiv:math/0509414.
- Local PDF: `source_paper.pdf`.
- Evidence image: `figures/open_problem_crop.png` (page 1).

The 2005 paper frames the next question after the classical `ell_p` and `c_0`
operator-algebra cases as the problem of describing all closed ideals of
`L(ell_p oplus ell_q)`, equivalently the closed ideals in
`L(ell_p,ell_q)` for `p<q`. It proves that for `1<p<2<q<infty` there are at
least four distinct proper closed ideals in `L(ell_p,ell_q)`.

## Supporting Answer Sources

- Th. Schlumprecht and A. Zsak, *The algebra of bounded linear operators on
  ell_p oplus ell_q has infinitely many closed ideals*, arXiv:1409.3480.
  Local PDF: `supporting_paper_1409.3480.pdf`.
- D. Freeman, Th. Schlumprecht, A. Zsak, *Banach spaces for which the space
  of operators has 2^c closed ideals*, arXiv:2006.15415.
  Local PDF: `supporting_paper_2006.15415.pdf`.

Evidence images:

- `figures/supporting_pietsch_problem_crop.png`: arXiv:1409.3480 states
  Pietsch's Problem 5.3.3 and says the paper solves it.
- `figures/supporting_main_theorem_crop.png`: arXiv:1409.3480 Theorem A gives
  a continuum-sized chain in `L(ell_p,ell_q)` for `1<p<q<infty`.
- `figures/supporting_exact_cardinality_crop.png`: arXiv:2006.15415 Corollary
  9 gives exact cardinality `2^c` for `L(ell_p oplus ell_q)`.

## Status

The infinite-many/cardinality part of the closed-ideals question is already
answered in the literature.

Schlumprecht--Zsak explicitly formulate Pietsch's Problem 5.3.3:

```text
For 1 <= p < q, does L(ell_p,ell_q) have infinitely many closed ideals?
```

They then prove that for every `1<p<q<infty` there is a chain of size the
continuum of closed ideals in `L(ell_p,ell_q)`.

Freeman--Schlumprecht--Zsak later prove the stronger exact-cardinality result:
for every `1<p<q<infty`, the set of closed ideals in
`L(ell_p oplus ell_q)` has cardinality exactly `2^c`.

## Verification Notes

- Same-paper check: arXiv:math/0509414 asks for the closed-ideal structure and
  proves finite progress, but it does not answer the infinite-many question in
  the reflexive range.
- Separate-source check: arXiv:1409.3480 is a later separate paper. Its
  abstract explicitly says it solves Pietsch's Problem 5.3.3, and the
  introduction restates the problem before Theorem A.
- Strengthening check: arXiv:2006.15415 gives a later stronger exact
  cardinality result, not just infinitely many ideals.
- Identification: Pietsch's theorem, quoted in both the 2005 and 2014 papers,
  gives a correspondence between the non-maximal proper closed ideals of
  `L(ell_p oplus ell_q)` and closed ideals in `L(ell_p,ell_q)`.

## Search Bounds

- Checked the active run indexes and registry for `0509414`, `1409.3480`,
  `2006.15415`, `closed ideals`, `ell_p oplus ell_q`, `Pietsch`, and
  `Schlumprecht Zsak`.
- Read the original source passages in
  `data/parsed/arxiv_sources/0509414/source.tex`.
- Web searches on 2026-06-14 located arXiv:1409.3480 and arXiv:2006.15415 as
  later answer sources.
- Downloaded and inspected the arXiv PDFs and TeX sources for all three papers.

## Limitations

- This is not an original proof from the run.
- This packet does not claim a full classification of the closed-ideal lattice
  of `L(ell_p oplus ell_q)` or `L(ell_p,ell_q)`.
- The exact-cardinality statement recorded here is restricted to
  `1<p<q<infty`.
- Endpoint cases involving `ell_1`, `c_0`, or `ell_infty` are not claimed here.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact review packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original/source paper PDF.
- `supporting_paper_1409.3480.pdf`: later explicit answer source.
- `supporting_paper_2006.15415.pdf`: later exact-cardinality source.
- `figures/`: evidence crops from the source and supporting papers.
- `code/crop_evidence.py`: reproducible crop generator.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Verify the identification between Pietsch's `L(ell_p,ell_q)` problem and the
`L(ell_p oplus ell_q)` algebra via the quoted maximal-ideal correspondence.
Treat the infinite-many and exact-cardinality status as literature-known; keep
the full lattice-classification problem separate.
