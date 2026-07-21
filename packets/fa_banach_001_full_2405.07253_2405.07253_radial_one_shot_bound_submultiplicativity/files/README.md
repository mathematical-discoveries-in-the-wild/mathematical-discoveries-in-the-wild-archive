# Full-result packet: sharp radial one-shot bound by submultiplicativity

Status: `candidate_full_solution_likely_valid`

Source: Silouanos Brazitikos and Giorgos Chasapis, *Sharp estimates for the
Cramér transform of log-concave measures and geometric applications*,
arXiv:2405.07253, Advances in Mathematics 478 (2025), 110407.

## Result

Let `E_n` be the isotropic radial exponential law on `R^n` and set

`A_n = E exp(-Lambda^*_{E_n}(E_n))`.

The packet proves the new submultiplicativity inequality

`A_{n+m} <= A_n A_m` for all integers `n,m >= 1`.

The source paper's Theorem 4.13 then gives, for every full-dimensional
rotationally invariant log-concave random vector `X` in `R^n`,

`E exp(-Lambda_X^*(X)) <= A_n <= A_1^n`.

This completely answers the explicit question on source PDF page 23 asking
whether the one-dimensional double-exponential bound remains true without a
product assumption. The base `A_1 ~= 0.7872717101` is sharp across all
dimensions because equality occurs in dimension one.

The stronger Conjecture 2—that `A_n^(1/n)` is non-increasing at every
consecutive integer—is not claimed. Submultiplicativity proves the motivating
sharp bound but does not logically imply that stronger sequence statement.

## Proof mechanism

The explicit Cramér formula reduces `A_n` to

`A_n = E exp(-F_n(S_n))`,

where `S_n ~ Gamma(n,1)` and

`F_n(s) = (n+1)/2 h(s/(n+1))`.

For independent Gamma variables of shapes `n` and `m`, condition on their sum.
The split proportion is `Beta(n,m)`. A Beta size-bias identity and the strict
concavity of `h'` show that the mean split energy is at most `F_{n+m}`. Jensen
for the convex function `exp(-x)` then gives submultiplicativity.

## Packet contents

- `main.tex`: self-contained proof packet with proof intuition, theorem,
  corollary, limitations, and novelty check.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: readable full-width crop of source PDF page
  23 containing the question and Conjecture 2.
- `code/check_submultiplicativity.py`: finite numerical smoke test; no
  computation is used as proof.
- `tmp/`: build intermediates and rendered-page QA images.

## Verification focus

1. Check the scaling `sqrt(n+1)|E_n| ~ Gamma(n,1)` and the formula for `F_n`.
2. Check both Beta size-bias laws and their means.
3. Check the direction of Jensen for `exp(-x)`.
4. Check that source Theorem 4.13 has the radial log-concave scope used in the
   final corollary.

Current verdict: the proof is elementary after the explicit source formula and
is likely valid. Human review is recommended, with special attention to the
four normalization points above.

## Novelty check

The cheap run indexes were searched for `2405.07253`, `one-shot
separability`, `radial exponential`, and `submultiplicativity`, with no
overlap found. A bounded web search on 2026-07-21 used the paper title, the
exact one-shot phrase, `Conjecture 2`, and combinations of `Cramér transform`,
`radial exponential`, and `monotonicity`; it found the source/published paper
but no later resolution. This supports, but does not prove, novelty.
