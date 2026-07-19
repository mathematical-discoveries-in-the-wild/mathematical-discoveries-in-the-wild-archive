# Counterexample Packet: Non-Delta2 Orlicz-Sobolev Compact Embeddings

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `2503.19454`
- source paper: Pierre-A. Vuillermot, *On the compactness of embeddings for a class of weighted Orlicz-Sobolev sequence spaces*
- target passage: PDF page 17 / source lines 1188-1195, the remark after Theorem 4 asking whether compactness persists when `s_{k,Phi,w}` is strictly included in `l_{k,Phi,w}`, and whether compact embeddings `l_{k',Phi,w} -> l_{k,Phi,w}` exist for `k' > k`.

## Claim

For every `0 < k < k'` there is an Orlicz function `Phi` and constant
weights `w_m = 1` such that:

- `s_{k,Phi,w}` is strictly included in `l_{k,Phi,w}`;
- the continuous embedding `s_{k',Phi,w} -> s_{k,Phi,w}` is not compact;
- the continuous embedding `l_{k',Phi,w} -> l_{k,Phi,w}` is not compact.

Thus both compactness questions in the source remark have a negative answer
in general.

## Construction

Take `Phi(t)=exp(-1/t)` near zero, with `Phi(0)=0`, and extend it linearly
after a small point `a < 1/2`.  This is a convex increasing Orlicz function
which fails the `Delta_2` condition at zero.

The normalized far-out basis vectors

```text
x_n = [k' log(1+Phi(n))]^{-1} e_n
```

have `||x_n||_{k',Phi,w}=1`, but their image norms in
`l_{k,Phi,w}` and `s_{k,Phi,w}` are constantly `k/k'`.  Coordinate
projections are contractive, so these images have no Cauchy subsequence.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2503.19454.
- `source_paper.tex`: local parsed TeX source.
- `figures/open_problem_crop.png`: crop of the source remark.

## Novelty Check

Before promotion, the agent checked the run indexes for `2503.19454`,
`compactness of embeddings`, `weighted Orlicz-Sobolev sequence spaces`,
`s_{k,Phi,w}`, and `l_{k,Phi,w}`.  No duplicate or prior answer was found.

A bounded web search on 2026-07-03 for exact phrases around `2503.19454`,
the source title, `s_{k,\Phi,w}`, `l_{k,\Phi,w}`, and compact Orlicz sequence
embeddings found the source arXiv page but no later answer to this exact
question.  Human review should focus on the convexity of the chosen Orlicz
function and the Luxemburg norm computation for the far-out unit vectors.
