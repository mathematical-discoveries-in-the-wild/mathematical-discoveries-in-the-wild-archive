# Partial solution packet: canonical pretree reduction for Cotlar symbols

## Source

- Paper: Adrian M. Gonzalez-Perez, Javier Parcet, and Runlian Xia,
  *Noncommutative Cotlar identities for groups acting on tree-like structures*
- arXiv: `2209.05298`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `partial`
- Target question: the source asks whether every function
  `m:G -> C` satisfying the noncommutative Cotlar identity for `G_0={e}`
  lifts to a UAC-space model of the kind in Models 1 or 2.
- Packet claim: every such `m` canonically defines a `G`-invariant pretree
  structure on the orbit `G`. At the root `e`, the pretree shadows are exactly
  the level sets of `m`.

## Result

For a group `G` and a symbol `m` satisfying the closed Cotlar formula

```text
(m(g^{-1}) - m(h))(m(gh) - m(g)) = 0,
```

define a ternary relation by saying that `b` lies between `a` and `c` if
`b=a`, `b=c`, or, for distinct `a,b,c`,

```text
m(b^{-1}a) != m(b^{-1}c).
```

Then this relation satisfies the pretree axioms `(B1)-(B3)`, and left
translation by `G` acts by pretree automorphisms. Thus the reverse-UAC problem
is reduced to realizing this canonical pretree by an equivariant UAC
topological tree while preserving root shadows.

## Relation to the torsion packet

This packet explains the structural mechanism behind the earlier torsion
collapse packet:

`solutions/partial/2209.05298_torsion_cotlar_collapse/`

The torsion result is a concrete obstruction theorem. The present packet is a
broader abstract reduction toward the full reverse construction.

## Limitations

This is not promoted as a full solution. The missing step is topological:
one must show that the canonical pretree admits a suitable equivariant
realization as a UAC space in the sense of the source paper. Standard
pretree/dendron realization results strongly suggest this is the right route,
but this packet does not claim the realization theorem in the required
generality.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/reverse_uac_question_page21_crop.png`: crop of the source question.
- `tmp/`: LaTeX build output.

## Verification notes

The proof is algebraic. The key check is axiom `(B2)`: from
`m(b^{-1}a) != m(b^{-1}c)`, apply Cotlar with
`g=c^{-1}b` and `h=b^{-1}a` to get
`m(c^{-1}a)=m(c^{-1}b)`, so `c` is not between `a` and `b`.
