# Partial packet: decreasing-power Orlicz spaces are not in the class X

Status: claimed partial result / negative Orlicz-family classification, likely valid, needs human review.

Source target: Sergey V. Astashkin, Konstantin V. Lykov, and Mario Milman, *Majorization revisited: Comparison of norms in interpolation scales*, arXiv:2107.11854.

Open problem addressed: Section 6 defines the class `\mathcal{X}` of rearrangement invariant spaces for which an `NP` single-crossing comparison plus `\|f\|_X >= \|g\|_X` implies the same comparison for every initial truncation. The authors state: "A complete characterization of the class `\mathcal{X}` is an open problem."

Result: for every `0 < p < q`, the Orlicz function
`M_{p,q}(u)=\int_0^u N_{p,q}(v)\,dv`, where `N_{p,q}(v)=v^q` for `0 <= v <= 1` and `N_{p,q}(v)=v^p` for `v >= 1`, gives a rearrangement invariant Orlicz space `L_{M_{p,q}}` that is not in `\mathcal{X}`. These are Delta_2 Orlicz spaces whose derivative has a decreasing power exponent across the scale break.

Mechanism: a general two-scale crossing-block lemma constructs decreasing step functions `f,g` satisfying the source paper's `NP` condition. On a prefix, the Luxemburg modular at scale `epsilon` makes `g` larger than `f`; at the global scale, the modular makes `f` larger than `g`. Adding a common low tail then forces `\|f\|_{L_M} >= \|g\|_{L_M}` while preserving the failed prefix inequality.

Files:
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2107.11854.
- `figures/open_problem_crop.png`: rendered source page containing the definition of `\mathcal{X}` and the open problem.
- `code/verify_concrete.py`: numerical sanity check for the concrete case `p=1`, `q=2`, `epsilon=1/2`.

Novelty check: on 2026-07-03, searched web phrases around `Majorization revisited`, `class \mathcal{X}`, `Orlicz`, `Nazarov-Podkorytov`, and the derivative ratio condition `M'(\varepsilon x)/M'(x)`. No later characterization or matching Orlicz negative family was found beyond the source paper itself.

Review recommendation: check the crossing-block lemma, especially the two modular-scale inequalities and the common-tail normalization. Once that lemma is accepted, the decreasing-power Orlicz family follows from the elementary limit comparison `epsilon^{q+1} < epsilon^{p+1}`.
