# Conditional packet: Corson compacta with ell_1(omega_2) in C(K)

## Source

- Paper: Petr Hajek and Tommaso Russo, *An uncountable version of Ptak's combinatorial lemma*
- arXiv: `1805.06028`
- Published version: J. Math. Anal. Appl. 470 (2019), 1070--1080
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `conditional`
- Source question: Problem 4.3 asks whether it is consistent with ZFC that a Corson compact `K` satisfies `ell_1(omega_2) embeds C(K)`.
- Packet claim: two conditional reductions are proved.

## Conditional Dependencies

This packet does not settle the ZFC consistency question. It proves:

- Negative conditional result: if `omega_2` is a caliber of Radon measures, then no such Corson compact exists.
- Positive conditional construction: if there is a compact Radon probability space with a point-countable family of positive-measure closed sets indexed by `omega_2`, then such a Corson compact exists.

The remaining set-theoretic issue is whether the positive hypothesis is consistent, or whether a broader ZFC obstruction rules it out.

## Proof Intuition

The negative side pushes the embedding through Talagrand's theorem: `ell_1(omega_2)` in `C(K)` gives a continuous image of the dual ball onto `[0,1]^{omega_2}`. Under the measure-caliber hypothesis, the later kappa-Corson theory makes that dual ball `omega_2`-Corson, and continuous images preserve regular `kappa`-Corson compacta. But the cube `[0,1]^{omega_2}` is not `omega_2`-Corson.

The positive side adapts the adequate-compact construction used by Hajek--Russo for `omega_1`. A point-countable positive-measure family of size `omega_2` defines a Corson adequate compact. Positive measure gives the Ptak lower bound for convex means on a subfamily of size `omega_2`, and the source proposition then embeds `ell_1(omega_2)` into `C(K)`.

## Files

- `main.tex`: LaTeX source for the conditional packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `supporting_paper_2107.02513.pdf`: Marciszewski--Plebanek--Zakrzewski support paper on `kappa`-Corson compacta.
- `figures/open_problem_crop.png`: crop of Problem 4.3 in the source PDF.
- `code/crop_evidence.py`: reproduces the source crop with PyMuPDF.
- `tmp/`: LaTeX build output.

## Verification Notes

Cheap run indexes had no exact packet for `1805.06028`, `Ptak`, or the Corson/`ell_1(omega_2)` problem. Focused web and local searches for exact phrases around `"Corson compact"`, `"ell_1(omega_2)"`, `"C(K)"`, and `"Haydon"` found the source paper and later `kappa`-Corson papers, but no separate paper explicitly answering Problem 4.3.

The main reviewer focus is set-theoretic: decide whether the point-countable positive-measure family of size `omega_2` is consistent, or whether the measure-caliber obstruction can be removed.
