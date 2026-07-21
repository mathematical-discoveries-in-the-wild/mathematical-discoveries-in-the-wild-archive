# Counterexample: the critical Allen--Cahn energy supremum has infinite mean

Status: `candidate_counterexample_likely_valid`.

Source target: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and maximal
regularity: an extended survey*, arXiv:2501.18561v5, Problem 4 on page 92.

The source asks whether the critical variational estimate

```text
E sup_{0<=t<=T} ||u(t)||_H^2 <= C_T(1+E||u_0||_H^2)
```

holds, and singles out the one-dimensional periodic Allen--Cahn equation

```text
du = (Delta u + u-u^3)dt + gamma u^2 dW
```

at `gamma^2=2` as an unknown model case.

This packet gives a negative answer. For every deterministic constant
`u_0=x_0>0` and every `T>0`, the spatially constant solution at
`gamma=sqrt(2)` satisfies

```text
E sup_{0<=t<=T} ||u(t)||_L2(T)^2 = infinity.
```

The scalar mode solves

```text
dX=(X-X^3)dt+sqrt(2)X^2dW.
```

After the reciprocal transform, `R=1/(sqrt(2)X)` is the radius of a
four-dimensional Ornstein--Uhlenbeck process `Z`. Hence
`X_t=1/(sqrt(2)|Z_t|)`. A self-contained occupation-time estimate gives

```text
P(inf_{T/2<=t<=T}|Z_t| <= epsilon) >= c_T epsilon^2.
```

Consequently the squared supremum has a `c/y` lower tail, and its expectation
diverges by the layer-cake formula. The paths themselves remain finite on each
compact time interval.

Files:

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered packet.
- `verification.md`: independent audit checklist and novelty-search record.
- `source_paper.pdf`: current source paper (arXiv v5).
- `figures/open_problem_crop.png`: source crop containing Problem 4 and the
  critical model example.
- `code/verify_reduction.py`: exact symbolic checks of the Itô transforms and
  the occupation-integral scaling.

Human-review focus:

1. Check the second-moment bound for the small-ball occupation time, especially
   the transition-density estimate at time lag `h`.
2. Check that the constant spatial mode is covered by the source model and
   that uniqueness identifies it with the variational solution.
3. Check the scope claim: the packet refutes the proposed general energy bound
   and resolves the highlighted critical model negatively, but it does not
   address the neighboring continuity question (Problem 5).

Bounded novelty check: the run indexes, the current arXiv record, exact-title
and exact-model web searches, and nearby 2026 reaction--diffusion search hits
were inspected on 2026-07-21. No later proof or counterexample to this exact
critical `L^2`-supremum question was found. This is a bounded search, not a
claim of exhaustive priority.
