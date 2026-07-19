# Smooth-phase principal-value problem answered by arXiv:2603.23238

**Status:** `literature_already_answered` (negative answer)

**Original problem.** Xing Wang and Cheng Zhang, *Sharp endpoint estimates for
eigenfunctions restricted to submanifolds of codimension 2*, arXiv:1606.09346,
Section 4, Problem 4 (bottom of PDF page 14), ask whether, for every real
`psi in C-infinity(R)`,

```text
m(lambda) = p.v. integral_{-1}^1 exp(i lambda psi(t)) dt/t
```

is bounded as a function of the real parameter `lambda`.

**Decisive later answer.** Cheng Zhang and Zhifei Zhu, *Maximal growth of the
Stein--Wainger oscillatory integral*, arXiv:2603.23238 (2026), explicitly state
in the abstract and introduction that they resolve Wang--Zhang Problem 4.
Their Theorem 1.2 constructs smooth real phases and sequences `lambda_n ->
infinity` for which

```text
|m(lambda_n)| is comparable to log(lambda_n) / log^(k)(lambda_n),  k >= 2,
```

so `m` is unbounded.  It also proves the sharp general upper bound
`m(lambda) = o(log lambda)` for every smooth phase.  A smooth phase on
`[-1,1]` can be extended to the real line without changing the integral, so
this is an exact negative answer to the source formulation.

The supporting authors explicitly cite Wang--Zhang, identify “Problem 4 in
Section 4,” and say their results give a negative answer.  This is therefore
an explicit later-literature resolution, not an agent-inferred reformulation.

A separate direct attack independently found a shorter flat-staircase
unboundedness construction before the later paper was located; it is retained
only as provenance in
`runs/fa_banach_001/attempts/1606.09346_smooth_phase_pv_integral_push.md` and
is not claimed as a new result.

Files:

- `source_paper.pdf`: arXiv:1606.09346
- `supporting_paper_2603.23238.pdf`: decisive later answer
- `main.tex`, `solution_packet.pdf`: compact review note
- ledger: `runs/fa_banach_001/ledger/results/1606.09346_smooth_phase_pv_answered_by_2603.23238.json`

