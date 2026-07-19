# Literature-implied answer: real \(p=3/2\) SOT hypercyclicity

Status: `literature_implied_answer (partial real-scalar variant)`.

Source/open-problem paper: Sophie Grivaux, Etienne Matheron, and Quentin Menet, *Does a typical \(\ell_p\)-space contraction have a non-trivial invariant subspace?*, arXiv:2012.02016.

Supporting paper: Sophie Grivaux, Etienne Matheron, and Quentin Menet, *Generic properties of \(l_p\)-contractions and similar operator topologies*, arXiv:2207.07938.

## Identified question

In Section 7, Question 5 of arXiv:2012.02016 asks whether, for \(X=\ell_p\), \(1<p<2\), or \(X=c_0\), every fixed \(M>1\) has the property that a typical \(T\in(\mathcal B_1(X),\mathrm{SOT})\) satisfies that \((MT)^*\) is hypercyclic. In the \(\ell_p\) case it also asks, at least, whether the typical SOT contraction has no eigenvalue.

## Implied answer

For the real space \(X=\ell_{3/2}\), the answer to the hypercyclicity part is positive for every fixed \(M>1\). Hence a typical SOT contraction on real \(\ell_{3/2}\) has no eigenvalue.

The implication is:

1. The 2012 paper records in Proposition `monsteraide` that for \(1<p<\infty\) and every \(M>1\), the set of contractions \(T\) such that \((MT)^*\) is hypercyclic is dense \(G_\delta\) for the strong-star topology. This is the standard hypercyclic-density argument; the real scalar version is the same argument.
2. The 2022 paper proves in Theorem C / Theorem `toutcapourca` that for real \(\ell_p\) with \(p=3\) or \(p=3/2\), all operator topologies between WOT and SOT* on the contraction ball are similar.
3. Since SOT lies between WOT and SOT*, SOT and SOT* have the same comeager sets on real \(\ell_{3/2}\). The SOT*-comeager hypercyclicity set from (1) is therefore SOT-comeager.

The supporting authors explicitly prove the topology-similarity theorem, but they do not present this as an answer to arXiv:2012.02016 Question 5. The relation is an agent-identified implication.

## Scope limitations

This packet does not answer the original complex \(1<p<2\) case, the \(c_0\) case, or the main invariant-subspace Question 4 from arXiv:2012.02016. It also does not settle whether all \(1<p<2\) spaces have SOT/SOT* comeager transfer. The 2022 paper explicitly says the complex \(1<p<2\) no-eigenvalue question remains out of reach of Theorem A, and its full all-topologies result is only for the real \(p=3\) and \(p=3/2\) cases.

## Direct-attack note

I also checked the apparent \(c_0\) cone route coming from Proposition `conec0` in the 2012 paper. The source proof gives a non-supercyclic vector using moving dominant coordinates and has a commented observation that the projective-orbit closure would be a nonconvex invariant cone. Turning that into a closed convex cone by a fixed separating functional is blocked by the moving-marker mechanism: for the active marker \(k\), a fixed \(\ell_1\) functional would need its \(k\)-th marker weight to dominate too much of the remaining marker mass. A modified damping strategy may still exist, but no complete convex-cone proof was found in this loop.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2012.02016.
- `supporting_paper_2207.07938.pdf`: arXiv:2207.07938.

## Verification

Cheap indexes were searched for `2012.02016`, `typical ell_p contraction`, `SOT*`, `hypercyclic`, and related invariant-subspace keywords. The only close durable hit was the existing attempt note for arXiv:2207.07938. Web searches on 2026-07-03 for the exact 2012 title, the 2022 topology paper, and the \(p<2\) hypercyclic/no-eigenvalue phrases did not reveal a newer complex-case resolution.
