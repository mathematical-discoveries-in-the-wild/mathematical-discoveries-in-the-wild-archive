# Counterexample packet: nonclosed subspaces need not have fixed points

status: counterexample_likely_valid

source_arxiv: 2006.11500

source_problem: Open Question 3.5 of Mondal--Garai--Dey, asking about fixed points for enriched \(\mathcal A\)- and enriched \(\mathcal A'\)-contractions on subspaces, not necessarily closed, of Banach spaces.

counterexample: \(c_{00}\subset \ell_2\) with \(T x=e_1+\frac12 R x\), where \(R e_n=e_{n+1}\).

## Summary

The source wording is formally existential, in which case the answer is trivially yes: a zero map on any subspace has a fixed point. In context, however, Remark 3.3 asks whether the fixed-point theorem for Banach-space domains survives when the domain is only a linear subspace, possibly nonclosed.

This packet gives a negative answer to that nontrivial reading. Let \(Y=c_{00}\) with the norm inherited from \(\ell_2\), and let \(R:Y\to Y\) be the right shift. The affine map
\[
  T x=e_1+\frac12 R x
\]
is a self-map of \(Y\) and is a strict Banach contraction with Lipschitz constant \(1/2\). Taking \(b=0\) and \(f(r,s,t)=r/2\), the same map is both an enriched \(\mathcal A\)-contraction and an enriched \(\mathcal A'\)-contraction in the natural inherited-domain sense of the source definitions. But the fixed-point equation forces
\[
  x=(1,1/2,1/4,\ldots),
\]
which belongs to \(\ell_2\setminus c_{00}\). Hence \(T\) has no fixed point in the subspace.

## Evidence

- `source_paper.pdf`: Mondal--Garai--Dey, "On some enriched contractions in Banach spaces", arXiv:2006.11500.
- `figures/open_problem_crop.png`: crop of Remark 3.3 / Open Question 3.5 on PDF page 7.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet, once compiled.

## Novelty Check

Bounded search on 2026-07-18 found no duplicate packet or prior local run result for arXiv:2006.11500, enriched \(\mathcal A\)-contractions, enriched \(\mathcal A'\)-contractions, or the subspace fixed-point question. Local corpus search found the exact open-question text only in the source paper and target-pool copies. Web searches for exact and near phrases including `"2006.11500" "enriched A-contraction" "subspace"`, `"On some enriched contractions in Banach spaces" "open question"`, `"Does there exist a self map defined on a subspace" "enriched"`, and `"enriched A'-contraction" "subspace" "fixed point"` found the source/arXiv or bibliographic mirrors, but no later explicit resolution.

## Human Review Recommendation

Check the interpretation issue first. The counterexample is not a disproof of the literal existential grammar of Open Question 3.5, which is trivially true; it is a disproof of the contextual universal fixed-point extension suggested by Remark 3.3. Mathematically, verify that \(f(r,s,t)=r/2\) belongs to both classes \(\mathcal A\) and \(\mathcal A'\), and that the affine shift map is a self-map of \(c_{00}\) with no fixed point in \(c_{00}\).
