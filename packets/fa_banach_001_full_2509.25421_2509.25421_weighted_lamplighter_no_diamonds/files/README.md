# Full solution packet: weighted lamplighter trees do not contain diamonds

## Source

- Paper: Charlotte Melby and Beata Randrianantoanina, *Bi-Lipschitz embedding
  properties of lamplighter graphs on weighted and unweighted trees*
- arXiv: `2509.25421`
- Source location: page 5 of the arXiv PDF, after Theorem 1.8.

## Classification

- Status: `full_solution_likely_valid`
- Result type: full positive answer to the weighted-tree follow-up question.
- Scope: the question whether Theorem 1.8 remains true for
  `Lam(WB_{theta,n})` when `theta >= 3`.

## Result

For every integer `theta >= 3`, the sequence of diamond graphs `(D_k)` does not
equi-bi-Lipschitzly embed into the sequence of lamplighter graphs on the
weighted complete binary trees `(Lam(WB_{theta,n}))`.

This answers the source's explicit question affirmatively: the no-diamonds
theorem does extend from the subdivided trees `W_{theta,n}` to the weighted
complete binary trees `WB_{theta,n}`.

## Proof Idea

The weighted case has a simple obstruction that the subdivided case lacks.
The top edge of `WB_{theta,n}` has weight `theta^{n-1}`. If every edge of a
connected source graph maps to distance smaller than this top weight, then the
image cannot cross a top-edge cut and cannot change any lamps on the other side
of that cut. Hence, after toggling a fixed lamp set, the whole image lies in one
principal copy of `Lam(WB_{theta,n-1})`.

For a minimal-depth embedding this is impossible, so the image of some diamond
edge must have length at least `theta^{n-1}`. On the other hand, for
`theta >= 3`, the diameter of `Lam(WB_{theta,n})` is at most `6 theta^n`. If
`D_k` embeds with distortion `D` and scaling `lambda`, then

```text
D lambda >= theta^{n-1}
lambda 2^k <= 6 theta^n
```

so `2^k <= 6 D theta`. Thus, for fixed distortion, the diamond level `k` is
bounded.

## Files

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: crop of the source question.
- `code/verify_scale_bounds.py`: sanity checker for the scale inequalities.
- `tmp/pdfs/`: render/build intermediates.

## Novelty Check

Cheap run indexes had no exact prior packet for `2509.25421`. The adjacent
`1902.07098` attempt concerned the older stretched-tree counterexample problem,
which the present source paper already settles. A bounded web search on
July 18, 2026 for exact phrases around `Lam(WB)`, weighted complete binary
trees, lamplighter graphs, and diamonds found the source paper but no later
answer to the weighted no-diamonds follow-up.

