# Partial Packet: Root-Split Height `omega_2` Trees Are Valdivia

Run: `fa_banach_001`

Result type: `partial`

Status: superseded by the full packet in
`solutions/full/2305.11737_height_omega2_scattered_r_tree_valdivia/`.
Kept here as proof-development history.

## Source Problem

- Tommaso Russo and Jacopo Somaglia, *Banach spaces of continuous functions
  without norming Markushevich bases*, arXiv:2305.11737.
- Source location: page 15, Problem 5.9.
- Local PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

Problem 5.9 asks whether every scattered compact `r`-tree `T` with
`ht(T)=omega_2` must be Valdivia.

## Partial Result

Yes under a root-splitting hypothesis. If `T` is a rooted scattered compact
`r`-tree with `ht(T)=omega_2` and every immediate successor subtree `V_s`,
`s in ims(0_T)`, has height strictly below `omega_2`, then `T` is Valdivia.

Equivalently, this covers the boundary case where the only reason `T` has
height `omega_2` is that the root carries a cofinal family of lower-height
clopen subtrees.

## Proof Mechanism

Russo--Somaglia prove that every scattered compact `r`-tree of height less
than `omega_2` is Valdivia. Under the root-splitting hypothesis each clopen
branch `V_s` is therefore Valdivia. The whole tree is the one-point
compactification of the topological disjoint sum of these `V_s`, with the root
as the point at infinity. A direct coordinate embedding shows that this
one-point compactification of any disjoint family of Valdivia compacta is
again Valdivia.

## Limitations

This does not solve Problem 5.9 in full. The remaining hard case is when,
after passing below the root, at least one immediate successor subtree still
has height `omega_2`; more generally, the unresolved issue is a height-`omega_2`
core that cannot be decomposed into lower-height clopen pieces at a finite
root cut.

## Files

- `README.md`: this summary.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source Problem 5.9 crop.
- `code/check_packet_assets.py`: lightweight asset/proof-scope checker.
- `tmp/`: LaTeX build intermediates and rendered page image.

## Verification Notes

The cheap run indexes were searched for `2305.11737`, `norming M-basis`,
`Valdivia`, `omega_2`, `compact r-tree`, and tree-height keywords. No existing
packet for this exact source paper or this root-split subcase was found.

Web searches on 2026-06-16 for exact phrases around arXiv:2305.11737, Problem
5.9, `scattered compact r-tree height omega_2 Valdivia`, and `C(T) norming
M-basis tree height omega_1` found the source paper but no later resolution of
Problem 5.9 or this subcase.

## Human Review Recommendation

Check the one-point compactification identification and the stability lemma
for Valdivia compacta under arbitrary topological sums plus one point. If those
are accepted, the partial result follows immediately from Russo--Somaglia
Corollary 5.7.
