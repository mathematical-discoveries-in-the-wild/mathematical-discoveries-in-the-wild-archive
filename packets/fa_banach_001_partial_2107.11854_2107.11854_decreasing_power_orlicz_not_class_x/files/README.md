# Partial packet: an Orlicz-space characterization for the class X

Status: claimed partial result, likely valid, needs human review.

Source target: Sergey V. Astashkin, Konstantin V. Lykov, and Mario Milman, *Majorization revisited: Comparison of norms in interpolation scales*, arXiv:2107.11854.

Open problem addressed: Section 6 defines the class `\mathcal{X}` of rearrangement invariant spaces for which an `NP` single-crossing comparison plus `\|f\|_X >= \|g\|_X` implies the same comparison for every initial truncation. The authors state: "A complete characterization of the class `\mathcal{X}` is an open problem."

Result: within the Delta_2 Orlicz spaces considered in the source paper, membership in `\mathcal{X}` is characterized by a scaled secant-ratio monotonicity condition. For each `0 < epsilon < 1`, define

`Q_epsilon(u,v) = (M(epsilon v)-M(epsilon u))/(M(v)-M(u))`, `0 < u < v`.

Then, for a strictly increasing Delta_2 Orlicz function `M`, `L_M` belongs to `\mathcal{X}` if and only if

`Q_epsilon(u,v) >= Q_epsilon(v,w)` for every `0 < u < v < w` and every `epsilon in (0,1)`.

Consequences:
- The source paper's differentiable sufficient condition follows because `M'(epsilon x)/M'(x)` decreasing makes these secant ratios decrease.
- The previous decreasing-power family is now a corollary: if `M'(u)` behaves like `u^q` near zero and `u^p` at infinity with `0 < p < q`, then the secant condition fails, so `L_M notin \mathcal{X}`.

Files:
- `main.tex`: upgraded proof packet.
- `solution_packet.pdf`: rendered upgraded packet.
- `source_paper.pdf`: local copy of arXiv:2107.11854.
- `figures/open_problem_crop.png`: rendered source page containing the definition of `\mathcal{X}` and the open problem.
- `code/verify_concrete.py`: numerical sanity check for the decreasing-power corollary.
- `history/previous_packet_2026_07_03/`: the initial narrower packet before the Orlicz-characterization upgrade.

Novelty check: on 2026-07-03, searched web phrases around `Majorization revisited`, `class \mathcal{X}`, `Orlicz`, `Nazarov-Podkorytov`, and the derivative ratio condition `M'(\varepsilon x)/M'(x)`. No later characterization or matching Orlicz criterion was found beyond the source paper itself.

Review recommendation: focus on the interval-ratio averaging lemma and the Luxemburg normalization step under Delta_2. The necessity direction is the explicit crossing-block construction from the earlier packet; the sufficiency direction is the source paper's Orlicz proof with the derivative-ratio hypothesis replaced by the exact secant-ratio condition.
