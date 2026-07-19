# Counterexample: Lip0 almost-invariant approximation

status: candidate_counterexample_likely_valid

arxiv_id: 2506.06770

source: Tomas Raunig, "Almost-invariant elements of group actions on Lip0 spaces"

target: Question 1.3, the Lip0 reformulation of the Kazhdan--Yom Din approximation question.

## Claim

Question 1.3 has a negative answer for arbitrary pointed metric spaces and
isometric group actions.  Take a group with no real characters but with a
nonzero homogeneous quasimorphism, for instance `PSL(2,Z)`.  If `q` is such a
quasimorphism with defect `D`, define a left-invariant metric by

```text
d(x,y) = 0,                         x = y,
d(x,y) = B + |q(x^{-1}y)| + D,      x != y,
```

with `B = 100D`.  Then `q` is a norm-one element of `Lip0(G,d)`, and under
left translations it is `1/20`-invariant in the source's norm.  For
`delta = 1/2` this is exactly `delta/10`-invariance.  However invariant
`Lip0` functions for left translations are homomorphisms, and
`Hom(PSL(2,Z),R)=0`, so the only invariant function is zero.  The distance
from `q` to zero is one, larger than `delta`.

## Scope

This refutes the arbitrary-metric version of Question 1.3.  It does not
contradict the paper's positive results for free or finitely presented groups
equipped with word metrics, nor the known positive amenable-group case.  The
counterexample uses a left-invariant metric engineered from the quasimorphism.

## Novelty Check

Local index search on 2026-07-18 found no exact `2506.06770` packet.  Nearby
hits concern fixed points, amenability, property (T), invariant means, and
Lipschitz-free extension questions, but not this Lip0/quasimorphism metric
counterexample.

Web search on 2026-07-18 checked the exact arXiv id and title, "Question 1.3",
"Lip0 almost invariant quasimorphism", and counterexample variants.  I found
the source preprint, the Glasner background paper, and quasimorphism existence
literature, but no later paper explicitly answering this Lip0 question.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: page-2 crop of Question 1.3.

## Human Review Recommendation

Review as a likely valid counterexample.  The key checks are the triangle
inequality for the metric, the defect estimate for the translated
quasimorphism, and the cited existence of a nonzero homogeneous quasimorphism
on a group with finite abelianization such as `PSL(2,Z)`.
