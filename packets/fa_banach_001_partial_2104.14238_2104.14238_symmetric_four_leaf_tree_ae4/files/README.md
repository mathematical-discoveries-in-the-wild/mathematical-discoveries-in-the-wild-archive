# Symmetric Four-Leaf Tree Subcase of `ae(4)`

- run: `fa_banach_001`
- arxiv_id: `2104.14238`
- source: Giuliano Basso, *Absolute Lipschitz extendability and linear projection constants*
- packet type: partial result
- status: likely valid
- agent: `agent_lane_17`
- date: `2026-06-20`

## Claim

Let `X_r` be the four leaves of the weighted tree with two internal vertices,
four pendant edges of length `1`, and central edge of length `r >= 0`, equipped
with the induced path metric. Then

```text
ae(X_r) = ((r+2)(r+3))/(r^2+3r+4).
```

Consequently this symmetric four-leaf tree family is maximized at
`r=sqrt(2)-1`, where

```text
ae(X_{sqrt(2)-1}) = (5+4 sqrt(2))/7.
```

This recovers Basso's lower-bound example and proves it is extremal within the
natural symmetric four-leaf tree subfamily.

## Relation To The Source Question

Basso proves `ae(4) >= (5+4 sqrt(2))/7` and conjectures this lower bound to be
sharp. The packet does not settle all four-point metrics. It proves the exact
answer for the symmetric tree-like family containing Basso's extremal example.

## Proof Summary

The injective hull of `X_r` is the corresponding metric tree. It suffices to
consider the six vertices, since Lipschitz extensions to the two internal
vertices extend linearly along the tree edges. The Lipschitz-free space over
the six-point tree is identified with `ell_1^5`, and `F(X_r)` becomes the
three-dimensional subspace

```text
E_r = { (a,b,z,c,d) : a+b+c+d=0,
                         z = r(a+b-c-d)/2 }.
```

An explicit projection `Q_r : ell_1^5 -> E_r` has column `ell_1` norms exactly
`((r+2)(r+3))/(r^2+3r+4)`. A matching lower bound is given by an explicit
trace-duality witness `A_r` with `nu_1(A_r)=1` and `A_r(E_r) subset E_r`.

## Files

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: local copy of arXiv:2104.14238.
- `code/verify_symmetric_tree.py`: quick numerical check of the projection
  and witness formula at representative values of `r`.

## Limitations

This is a solved subcase, not a full proof of `ae(4)=(5+4 sqrt(2))/7`. Random
LP searches during discovery did not find a four-point metric exceeding the
same value; they consistently moved back toward this symmetric collapsed-tree
family, but that numerical observation is not used as proof.
