# Partial result: the SOT Calkin quotient topology is indiscrete

Status: `partial_result_likely_valid`

Source problem paper: Jarno Talponen, *Convex-transitivity of Banach algebras via ideals*, arXiv:1106.1292.

## Target

On page 13, after Theorem 3.4, the source paper says that it is not known whether the Calkin algebra

```text
C(L^\infty) = B(L^\infty) / K(L^\infty)
```

is `(SOT-)convex-transitive`.

## Result

The SOT part has a general positive answer under the paper's quotient-topology convention.

For every Banach space `X`, the finite-rank operators are SOT-dense in `B(X)`. Since finite-rank operators are compact, `K(X)` is SOT-dense in `B(X)`. Therefore the SOT quotient topology on `B(X)/K(X)` is indiscrete. Consequently, if the quotient is nonzero, every nonempty orbit has SOT closure equal to the whole quotient, so `B(X)/K(X)` is SOT-convex-transitive in the formal topological sense.

In particular, `C(L^\infty)` is SOT-convex-transitive.

## Scope

This does **not** settle the norm convex-transitivity of `C(L^\infty)`. It only settles the parenthetical SOT formulation as written, and shows that this SOT formulation is topologically degenerate for Calkin quotients.

## Evidence

- `source_paper.pdf`: local copy of arXiv:1106.1292.
- `figures/open_problem_crop.png`: crop of the source question on page 13.
- `solution_packet.pdf`: proof packet.

## Human Review Notes

Recommended review focus:

- Confirm that the source's SOT quotient convention is the one stated in its preliminaries: quotient neighborhoods are of the form `U + Y`, even when `Y` is not SOT-closed.
- Confirm that the intended SOT question was not meant to pass to a Hausdorff quotient or another nontrivial operator topology.
- Treat the norm convex-transitivity question for `C(L^\infty)` as still open.
