# Weak-Norm Inner Product Counterexample for Problem 13.1

Status: `counterexample_likely_valid`

Source: Ron Blei, "The Grothendieck inequality revisited", arXiv:1111.7304.

## Problem

Problem 13.1 asks whether the inclusions

```tex
\tilde V_2(X\times Y) \subset C_b(X\times Y)\cap \tilde{\mathcal V}_2(X\times Y),
\qquad
G_2(X\times Y) \subset C_b(X\times Y)\cap \mathcal G_2(X\times Y)
```

are proper for topological spaces `X` and `Y`.

## Counterexample

Let `H = ell_2`. Let `X` be the closed unit ball
`B_H` with the weak topology, let `Y` be the same unit ball with the norm
topology, and define

```tex
f(x,y)=\langle x,y\rangle.
```

Then `f` is bounded and jointly continuous on `X x Y`. It belongs to the
set-theoretic Hilbert-factorization class `\mathcal G_2`; by the discrete
Grothendieck theorem in the source paper, it also belongs to
`\tilde{\mathcal V}_2`.

However `f` is not in the topological class `G_2(X x Y)`. If it had a
topological Hilbert factorization `f(x,y)=<g(x),h(y)>` with `g` continuous from
the weak topology on `B_H` into Hilbert norm, then

```tex
\|x-x'\| = \sup_{y\in B_H}|\langle x-x',y\rangle|
        \le M\|g(x)-g(x')\|.
```

Thus the identity map from the weak unit ball to the norm unit ball would be
continuous. An orthonormal sequence converges weakly to `0` but not in norm,
contradiction.

Since `\tilde V_2 \subset G_2`, the same example is outside `\tilde V_2` as
well. Therefore both inclusions in Problem 13.1 are proper.

## Files

- `source_paper.pdf`: source paper arXiv:1111.7304.
- `figures/open_problem_crop_page92.png`: display (13.1).
- `figures/open_problem_crop_page93.png`: Problem 13.1 statement.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.

## Novelty Check

Cheap run indexes were searched for `1111.7304`, `Grothendieck inequality
revisited`, `Problem 13.1`, `proper inclusions`, and the relevant
`tilde V_2/G_2` phrases; no exact prior packet was found. Local parsed-source
searches and web searches for the exact Problem 13.1 wording and close
weak-topology/norm-topology variants did not find a separate answer. Novelty
confidence is moderate pending human literature review, but the counterexample
is elementary and self-contained.

## Human Review

Recommended review focus: verify the definitions of `G_2`, `\mathcal G_2`,
`\tilde V_2`, and `\tilde{\mathcal V}_2` used in Sections 2, 3.1, and 13.1 of
the source paper, especially that the explicit probability-space
representation in the packet gives membership in `\mathcal G_2` and hence in
`\tilde{\mathcal V}_2`.
