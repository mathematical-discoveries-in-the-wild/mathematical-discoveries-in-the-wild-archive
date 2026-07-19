# Counterexample Packet: `0004049_nn_bounded_not_closed_under_nn_convergence`

Status: candidate counterexample to an author-labeled question.

Source paper: Vladimir G. Troitsky, "Spectral Radii of Bounded Operators on Topological Vector Spaces", arXiv:math/0004049.

## Target

In the operator-topologies subsection, after defining `nn-convergence`,
Troitsky asks:

```text
Is the class of all nn-bounded operators closed relative to nn-convergence?
```

## Result

The answer is negative.

Let `X = R^N` with the topology of coordinatewise convergence, and let
`L` be the left shift

```text
L(x_0,x_1,x_2,...) = (x_1,x_2,x_3,...).
```

For `N >= 0`, let `P_N` keep coordinates `0,...,N` and kill the rest, and
put `S_N = P_N L`. Each `S_N` is finite rank and nb-bounded, hence
nn-bounded. But `S_N` nn-converges to `L`: on any basic neighborhood
constraining finitely many coordinates, the tail `L-S_N` is eventually zero
on all constrained coordinates. The limit `L` is not nn-bounded, as shown
in the source paper's Example 2.5 and reproduced in the packet.

## Evidence

- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of the arXiv PDF.
- `main.tex`: self-contained proof source.
- `figures/open_problem_crop.png`: crop of the nn-convergence definition and displayed question.
- `figures/source_left_shift_crop.png`: crop of Example 2.5, the left shift is continuous but not nn-bounded.
- `code/README.md`: notes that no computational verifier is needed.

## Novelty Check

Local registry, solution packets, attempts, and proof gaps were searched for
`0004049`, `Spectral Radii`, `nn-bounded`, `nn-convergence`, `left shift`,
`product topology`, and `Troitsky`; no prior local artifact covered this
target. Web searches for the exact displayed question and close phrases
`nn-bounded nn-convergence left shift` and `Spectral radii of bounded
operators nn-convergence` did not reveal a separate known answer.

Human review recommendation: high confidence. The construction is a direct
finite-truncation closure counterexample around the source paper's own
non-nn-bounded left shift.
