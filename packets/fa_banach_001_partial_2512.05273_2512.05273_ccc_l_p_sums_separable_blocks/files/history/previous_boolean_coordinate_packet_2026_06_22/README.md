# Partial solution packet: CCC for separable coordinate decompositions

Status: `partial`, likely valid, human review recommended.

## Source problem

Source: Alberto Salguero-Alarcon, Pedro Tradacete, and Nazaret Trejo-Arroyo, "Free quasi-Banach lattices", arXiv:2512.05273.

Section 7.2 asks whether, for every \(p\)-natural quasi-Banach space \(E\),
\[
C_{ph}^b(B_{E^\triangle},L_p[0,1])
\]
satisfies the countable chain condition. The paper proves this for \(E=\ell_p(\Gamma)\) and notes that the same argument also works when \(E\) is separable.

## Claimed result

This packet proves the conjectured countable chain condition for every
\(p\)-natural quasi-Banach space with a bounded separable Boolean coordinate
decomposition: a uniformly bounded family of coordinate projections
\((P_A)_{A\subseteq\Gamma}\) with finite supports dense, Boolean projection
relations, and separable one-coordinate ranges.

Consequently, it proves the conjecture for every \(\ell_r\)-sum,
\(p\le r<\infty\),
\[
E=\left(\bigoplus_{\gamma\in\Gamma} E_\gamma\right)_r
\]
where each \(E_\gamma\) is a separable \(p\)-natural quasi-Banach space. This includes \(L_r(\mu)\), \(p\le r<\infty\), whenever the measure space is a direct sum of components with separable \(L_r\)-spaces. It also proves the conjecture for the \(c_0\)-sum
\[
E=\left(\bigoplus_{\gamma\in\Gamma} E_\gamma\right)_{c_0}
\]
of separable \(p\)-natural blocks. These families may be nonseparable and include the source-paper cases: a singleton \(\Gamma\) gives the separable case, \(E_\gamma=\mathbb R\) and \(r=p\) gives \(\ell_p(\Gamma)\), \(E_\gamma=\mathbb R\) and \(p\le r<\infty\) gives \(\ell_r(\Gamma)\), and the \(c_0\)-sum gives \(c_0(\Gamma)\).

## Key mechanism

For \(p\)-sums, the unit ball \(B_{E^\triangle}\), with the weak-\(\triangle\) topology, is homeomorphic to the product \(\prod_\gamma B_{E_\gamma^\triangle}\). Each factor is separable metrizable because \(E_\gamma\) is separable, and arbitrary products of separable metrizable spaces satisfy the topological countable chain condition. A short lifting lemma then converts topological CCC of the domain into lattice CCC of the \(L_p\)-valued continuous function lattice.

For spaces with bounded separable Boolean coordinate decompositions, topological CCC can fail already in scalar-coordinate examples. The proof instead uses homogeneity: a disjoint family in \(C_{ph}^b\) yields disjoint relatively open cones in the weak-\(\triangle\) unit ball. Finite-block operators are dense up to harmless cone scaling, and a Delta-system/root-gluing argument shows that uncountably many such cones cannot be disjoint. The gluing estimate uses only uniform boundedness of the Boolean coordinate projections and separability of finite coordinate ranges.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: crop of the source conjecture.

## Review focus

The first main point to check is the homeomorphism
\[
B_{(\oplus_\gamma E_\gamma)_p^\triangle}\cong \prod_\gamma B_{E_\gamma^\triangle}.
\]
Surjectivity uses unconditional convergence in \(L_p[0,1]\); continuity of the inverse uses finite-coordinate approximation of an element of the \(p\)-sum and a uniform tail estimate.

The second main point is the coordinate-decomposition gluing lemma: after shrinking finite-block operators, two members of an uncountable family can be glued along their common Delta-system root without leaving the two prescribed weak-\(\triangle\) neighborhoods. The only norm estimate uses the uniform bound \(K=\sup_A\|P_A\|\), so three small block-supported pieces still define a norm-one operator after choosing the shrink factor small enough.
