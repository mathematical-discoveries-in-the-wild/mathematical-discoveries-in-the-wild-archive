# Order-Reversing Convex-Function Operators Answered by Cheng--Luo

Source paper: Alfredo N. Iusem, Daniel Reem, and Benar F. Svaiter, "Order
preserving and order reversing operators on the class of convex functions in
Banach spaces", arXiv:1212.1120, published in J. Funct. Anal. 268 (2015),
73--92.

Status: literature_already_answered (self-map branch). The source paper leaves
open the characterization and even existence of fully order reversing operators
on \(\mathscr C(X)\), the cone of proper lower semicontinuous convex functions
on a Banach space \(X\). Cheng and Luo, arXiv:1708.06548, explicitly cite this
Iusem--Reem--Svaiter question and answer the self-map branch.

## Original Question

In Section 3 ("The order reversing case"), after proving the weak-star
codomain theorem for maps

```text
S: C(X) -> C_{w*}(X*)
```

the source says that the issue of characterizing fully order reversing
operators

```text
S: C(X) -> C(X)
```

and, in the nonreflexive case, maps \(S:C(X)\to C(X^*)\), is left as an open
problem deserving future research.

## Supporting Answer

Cheng--Luo, "On order preserving and order reversing mappings defined on cones
of convex functions", arXiv:1708.06548, quote the Iusem--Reem--Svaiter open
problem in their introduction. Their Theorem 1.5 states that a fully order
reversing self-map

```text
S: conv(X) -> conv(X)
```

exists if and only if \(X\) is reflexive and linearly isomorphic to \(X^*\).
Their Theorem 1.6 gives the corresponding Artstein--Avidan--Milman normal form:
for every such \(S\), there are a linear isomorphism \(U:X\to X^*\),
\(x_0^*,\varphi_0\in X^*\), \(\alpha>0\), and \(r_0\in\mathbb R\) such that

```text
(Sf)(x) = alpha (F f)(U x + x_0^*) + <phi_0, x> + r_0.
```

Here \(F\) is the Fenchel transform. Thus the self-map existence and
representation questions from the source paper are already answered in the
later literature.

## Scope

This packet records an explicit later-paper answer, not a new proof by this
run. The classification above fully covers the self-map branch
\(\mathscr C(X)\to\mathscr C(X)\). The source paper itself already treats
\(\mathscr C(X)\to\mathscr C_{w^*}(X^*)\), and notes that when \(X\) is
reflexive this is the same as the norm-lower-semicontinuous codomain
\(\mathscr C(X^*)\). This packet does not claim a separate new result beyond
the Cheng--Luo identification.

## Files

- `source_paper.pdf`: the original Iusem--Reem--Svaiter paper.
- `supporting_paper_1708.06548.pdf`: the Cheng--Luo paper answering the
  self-map branch.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

