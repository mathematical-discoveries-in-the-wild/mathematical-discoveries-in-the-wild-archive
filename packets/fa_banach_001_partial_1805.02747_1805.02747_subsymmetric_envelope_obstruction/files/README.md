# Partial result: subsymmetric envelope obstruction

- run: `fa_banach_001`
- source arXiv id: `1805.02747`
- source paper: R. M. Causey, *Three and a half asymptotic properties*
- source question: Question 6.1 asks whether `\mathfrak{T}_{\xi,p}` and `\mathfrak{A}_{\xi,p}` are distinct for all ordinals.
- packet status: `partial_result`
- verdict: likely valid, human review recommended

## Result

The packet proves that an `A_{0,p}` estimate on a normalized shrinking subsymmetric basis forces ordinary `\ell_p` domination of that basis, with `c_0` in the case `p=\infty`. The same argument applies to normalized shrinking symmetric unordered coordinate bases.

Consequently, the natural "long symmetric/subsymmetric envelope" route to extend Causey's countable-cofinality witness cannot work: an envelope with enough symmetry to make every countable coordinate subsequence look like the bad Tsirelson-dual model is already forced by `A_{0,p}` to have all coordinate subsequences dominated by `\ell_p` (or `c_0`).

## Scope

This does not settle Causey's full Question 6.1. It rules out a substantial class of envelope constructions suggested by the prior attempt, namely symmetric or subsymmetric replacements for the countable `T_q^*` envelope in the uncountable-cofinality case.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered proof packet
- `source_paper.pdf`: local copy of arXiv:1805.02747
- `figures/open_problem_crop.png`: rendered crop of Question 6.1
- `code/make_open_problem_crop.py`: crop-generation script

## Novelty and duplicate checks

Local registry checks on `2026-06-18` found only the prior attempt note for `1805.02747` and no promoted solution packet for this result. Web searches for the exact question, the paper title with `uncountable cofinality`, and the symbols `\mathfrak{T}_{\xi,p}` and `\mathfrak{A}_{\xi,p}` found the source arXiv page but no later exact closure of Question 6.1.
