# 2606.02040 - ZFC continuum-sized almost disjoint family on N*

Status: candidate partial result, likely valid.

Source paper: Chris Lambie-Hanson and David Schrittesser, "Generalized almost disjoint families and injective Banach spaces", arXiv:2606.02040.

## Source Question

Question 4.3 asks whether ZFC proves the existence of an almost disjoint family on \(\mathbb N^*\) of cardinality \(2^{\aleph_1}\), or even \(2^{2^{\aleph_0}}\), in the generalized sense of Definition 2.1 of the source paper.

## Partial Result

ZFC always proves the existence of such a family of cardinality \(2^{\aleph_0}\).

This does not settle the requested \(2^{\aleph_1}\) or \(2^{2^{\aleph_0}}\) bounds in all models. It gives a baseline lower bound and, in models where \(2^{\aleph_0}=2^{\aleph_1}\), answers the first cardinal target of Question 4.3.

## Proof Summary

Start with the standard branch almost disjoint family on \(\omega\): identify \(2^{<\omega}\) with \(\omega\), and for each \(x\in2^\omega\), let \(A_x=\{x{\upharpoonright}n:n<\omega\}\). Partition each \(A_x\) into infinite blocks \(A_{x,n}\), set \(b_{x,n}=\bigcup_{m<n}A_{x,m}\), and define
\[
U_x=\bigcup_{n\ge 1}N_{b_{x,n}}\subseteq\mathbb N^*,
\]
where \(N_a=\{p\in\mathbb N^*:a\in p\}\).

The \(U_x\)'s are pairwise disjoint because the \(A_x\)'s are almost disjoint. Each \(U_x\) is open, regular open, and noncompact. Regularity follows by thinning any basic neighborhood outside \(U_x\): either outside \(A_x\), or to one point in infinitely many tail blocks of the partition of \(A_x\). Thus \(\{U_x:x\in2^\omega\}\) is a generalized almost disjoint family on \(\mathbb N^*\) of size \(2^{\aleph_0}\).

## Files

- `main.tex` - full partial-result packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:2606.02040.
- `figures/open_problem_crop.png` - crop of Question 4.3.

