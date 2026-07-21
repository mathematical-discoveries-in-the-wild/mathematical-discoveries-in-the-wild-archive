# A density-two sheared hyperbolic-secant Gabor nonframe

Status: `candidate counterexample - likely valid; computer-assisted zero existence; human review requested`

Source: Markus Faulhuber and Irina Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, page 13, Section 5. The paper says that sufficient density conditions for the hyperbolic secant on general lattices are unknown and that its lattice frame set should first be determined.

## Result

Let

\[
g(t)=\sqrt{\pi/2}\,\operatorname{sech}(\pi t).
\]

There are numbers

\[
\left|a_*-\frac1{\sqrt{28}}\right|\le 10^{-6},\qquad
\left|c_*-\frac{15}{28}\right|\le 10^{-6},\qquad
q_*=\frac{c_*}{a_*^2},
\]

for which the density-two lattice

\[
\Lambda_*=\mathbb Z(a_*,-q_*a_*)+\mathbb Z\left(0,\frac1{2a_*}\right)
\]

does **not** generate a Gabor frame with window (g). Thus the rectangular criterion “density (>1)” does not extend to arbitrary lattices for the hyperbolic secant.

The proof chirps (g), uses the density-two Zak criterion, and certifies a simultaneous Zak zero. One of the two zeros is forced by evenness. Existence of the other is proved with Poincare--Miranda on a (2\times10^{-6}) box. The numerical part is a directed-interval certificate with an analytic bound for the infinite tail and for every Taylor remainder.

This does not determine the complete lattice frame set and does not rule out stronger sufficient hypotheses involving lattice shape as well as density.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: page-13 source evidence.
- `code/verify_zero_box.py`: reusable interval certificate.
- `verification_report.md`: command, certified output summary, and review focus.

## Reproduction

From the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2204.02917_density_two_sheared_sech_nonframe/code/verify_zero_box.py
```

Expected first line: `CERTIFIED`.

## Bounded novelty check

Checked on 2026-07-21:

- the run registry, solution index, and attempts index for arXiv:2204.02917 and the phrases `hyperbolic secant`, `general lattice`, `sheared lattice`, and `lattice frame set`;
- arXiv searches for exact and close variants of `hyperbolic secant general lattices Gabor frame`, `sech Gabor sheared lattice non-frame`, and `hyperbolic secant lattice frame set`;
- Janssen--Strohmer, arXiv:math/0301134 (rectangular lattices);
- Baranov--Belov, arXiv:2312.10174 (half-irregular product sets);
- Faulhuber--Shafkulovska--Zlotnikov, arXiv:2403.10503 (Hermite windows, not the sech general-lattice problem).

No matching general-lattice sech counterexample or solution was found. Novelty confidence is moderate because this was a bounded arXiv-centered search rather than an exhaustive bibliographic review.

## Human-review recommendation

Priority: high. Check (i) the interval library's outward-rounding behavior, (ii) the density-two Zak criterion normalization, and (iii) the sign in the chirp/shear covariance. The packet proves the criterion and covariance explicitly, so these checks are short.

