# Partial packet: strictly singular operators on Lp are S1-Schreier strictly singular

Status: `partial_result_likely_valid`

Agent: `agent_lane_06`

Date: 2026-06-19

Source paper: Martin Mathieu and Pedro Tradacete, *Strictly singular multiplication operators on* `L(X)`, arXiv:1810.09194.

Target context: Remark 6.11 asks whether every strictly singular operator on `L_p[0,1]`, `1<p<infty`, `p != 2`, is approximately `(ell_r,ell_s)`-factorizable, and also asks a finite-dimensional-sum variant.

## Result

For every `1<p<infty`, every strictly singular operator on `L_p[0,1]` is `S_1`-Schreier strictly singular.

Consequently the conditional obstruction packet

```text
solutions/conditional/1810.09194_s1_schreier_obstruction_to_approx_factorization/
```

cannot be upgraded by finding an operator in `S(L_p) \ S_1(L_p)`: no such operator exists on classical `L_p[0,1]`.

## Scope

This does **not** solve Mathieu-Tradacete Remark 6.11. It says only that the natural Schreier-rank obstruction is exhausted at the first Schreier level for `L_p`; approximate `(ell_r,ell_s)` factorization may still be strictly stronger than `S_1`-strict singularity.

## Proof Mechanism

The proof uses the Kadec-Pelczynski dichotomy: every seminormalized weakly null sequence in `L_p` has a subsequence equivalent to the unit vector basis of either `ell_p` or `ell_2`.

Given a normalized basic sequence, pass to a weakly null subsequence or to a seminormalized difference sequence. Apply Kadec-Pelczynski to the domain sequence and to its image under `T`. If the two exponent models agree, `T` is bounded below on an infinite-dimensional span, contradicting strict singularity. If they differ, boundedness forces the image exponent to be larger; long Schreier-admissible averages then make the ratio `||Tz||/||z||` arbitrarily small.

## Checks

Cheap-index searches found the preceding conditional packet and nearby Schreier/strictly-singular literature but no existing run packet proving this `L_p` rank-one conclusion. Targeted web searches for `S_1 strictly singular L_p`, `Schreier strictly singular L_p`, and variants found arXiv:math/0609039 but no direct statement of this `L_p` endomorphism theorem.

## Files

- `main.tex`: packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `supporting_paper_math_0609039.pdf`: supporting Schreier-singularity paper.
- `figures/open_problem_crop.png`: source crop of Remark 6.11.
- `code/render_open_problem_crop.py`: reproducible crop script copied from the conditional packet.

Human review should focus on the first reduction from an arbitrary normalized basic sequence to a weakly null sequence/difference sequence, and on the use of the Kadec-Pelczynski dichotomy for the image sequence.
