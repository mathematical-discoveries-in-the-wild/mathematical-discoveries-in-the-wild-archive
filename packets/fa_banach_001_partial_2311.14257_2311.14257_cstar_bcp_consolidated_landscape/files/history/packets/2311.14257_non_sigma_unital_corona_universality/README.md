# Non-Sigma-Unital Coronas Are Universal

Status: `partial_result_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_non_sigma_unital_corona_universality/`

## Result

For every nonzero unital C*-algebra `B`, there is a nonunital non-sigma-unital
C*-algebra `A` such that

`M(A) / A` is isomorphic to `B`.

One can take

`A = C0([0, omega_1), B)`.

Consequently the sigma-unital hypothesis in the packet
`2311.14257_sigma_unital_coronas_fail_bcp` is essential: non-sigma-unital
multiplier coronas need not fail BCP. For example,

`M(C0([0, omega_1))) / C0([0, omega_1))` is isomorphic to `C`,

so it has UBCP.

## Why This Matters

This blocks the hoped-for blanket theorem that all nonunital multiplier
coronas fail BCP. More sharply, it says that non-sigma-unital coronas can
realize arbitrary unital C*-algebras, so their BCP behavior is as complicated
as the original unital part of Question 3.

## Proof Intuition

The locally compact ordinal space `[0, omega_1)` is not sigma-compact, but it
has a strong rigidity property: every continuous map from `[0, omega_1)` into a
metric space is eventually constant. Since every C*-algebra is a metric space
in norm, each bounded continuous `B`-valued function on `[0, omega_1)` has an
eventual value in `B`. Functions vanishing at infinity are exactly those whose
eventual value is zero. Thus the corona quotient is precisely the eventual
value algebra `B`.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a structural partial theorem and sharpness result for the
sigma-unital corona obstruction. The key checks are the eventual-constancy
lemma for norm-continuous functions on `[0, omega_1)`, the multiplier
identification `M(C0(X,B)) = C_b(X,B)` for unital `B`, and the proof that
`C0([0, omega_1),B)` is not sigma-unital.
