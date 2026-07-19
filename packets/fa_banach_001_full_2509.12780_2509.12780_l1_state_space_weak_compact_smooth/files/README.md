# Full Solution Packet: arXiv:2509.12780 Problem 3.18

Status: `full_solution_likely_valid`.

## Target

Soumitra Daptari and Saurabh Dwivedi, "A study on state spaces in classical Banach spaces," arXiv:2509.12780, to appear in Colloquium Mathematicum.

The target is Problem 3.18 on page 18: after Theorem 2.5 characterizes norm compactness of the state space \(S_f\) for \(f \in S(L^1([0,1],X))\), the authors state that the analogous weak compactness result is not known.

## Result

Under the same separable-dual setting used in Theorems 2.3 and 2.5, weak compactness gives no larger class:

For a real or complex Banach space \(X\) with \(X^*\) separable and \(f\in S(L^1([0,1],X))\), the state space \(S_f\subset L^\infty([0,1],X^*)\) is weakly compact if and only if \(f\) is a smooth point of \(L^1([0,1],X)\). Equivalently, \(f(t)\ne 0\) a.e. and \(f(t)/\|f(t)\|\) is smooth in \(X\) a.e.

Thus the weak compactness analogue of Theorem 2.5 is affirmative and coincides with the norm compactness characterization.

## Proof Mechanism

If \(f\) vanishes on a set of positive measure, \(S_f\) contains a Rademacher sequence supported on that zero set. If \(f\) is nonzero a.e. but is not smooth, then on a positive-measure set of fibres there are two measurably selectable, uniformly separated pointwise states. Alternating between them with Rademacher signs gives a sequence in \(S_f\). A bounded evaluation map sends this sequence to a translate of the Rademacher sequence in \(L^\infty\). Since the Rademacher sequence spans an isometric \(\ell_1\) basis, it has no weakly Cauchy subsequence. Eberlein--Smulian then rules out weak compactness of \(S_f\).

## Contents

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2509.12780.
- `figures/open_problem_crop.png`: crop of Problems 3.18 and 3.19 from page 18.
- ledger: `runs/fa_banach_001/ledger/results/2509.12780_l1_state_space_weak_compact_smooth.json`.

## Scope

This solves Problem 3.18 in the setting of the paper's Theorems 2.3 and 2.5. It does not solve Problem 3.19, which asks what happens when \(X^*\) is not separable.
