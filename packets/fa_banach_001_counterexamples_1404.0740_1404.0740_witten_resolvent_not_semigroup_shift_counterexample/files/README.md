# Witten Resolvent Not Semigroup Shift Counterexample

status: counterexample_likely_valid

source_arxiv_id: 1404.0740

source_title: On the Witten index in terms of spectral shift functions

target: Definition 3.3 equivalence question after Remark 3.5.

## Claim

There is a bounded operator `T` such that both the resolvent and semigroup
differences for `T*T` and `TT*` are trace class, the resolvent regularized
Witten index exists and equals `0`, but the semigroup regularized Witten index
does not exist.

## Contents

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1404.0740.
- `figures/open_problem_page16.png`: rendered source page containing the open question.
- `code/finite_difference_probe.py`: numerical sanity check for the log-kernel separation mechanism.

## Review Focus

The main review point is the log-kernel separation lemma in the packet,
especially the saddle-point estimate for the high-order integer finite
differences. Once that lemma is accepted, the direct-sum constant-weight shift
construction gives the counterexample.

## Novelty Check

Cheap run indexes were searched for `1404.0740`, `Witten index`,
`resolvent regularized`, `semigroup regularized`, `spectral shift`, and the core
author names. A bounded web search on 2026-07-19 found the original paper and
model-operator follow-ups but no later unrestricted answer to the Definition
3.3 reverse implication.
