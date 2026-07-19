# Counterexample packet: the symmetry assumption is necessary

status: counterexample_likely_valid

source_arxiv: 1311.6624

source_problem: Section 3.5 of Jean Van Schaftingen, "Limiting
Bourgain-Brezis estimates for systems: theme and variations", asks whether
the symmetry assumption in the higher-order nilpotent-group endpoint estimate
is necessary.

counterexample: the literal extension from symmetric \(k\)-tensors to arbitrary
\(k\)-tensors fails already on the Euclidean step-one group \(G=\mathbb R^2\)
with \(k=2\).

## Summary

Let \(A=e_1\otimes e_2-e_2\otimes e_1\) be a nonzero antisymmetric 2-tensor.
For a compactly supported mollifier \(\rho_m\), put
\[
  f_m=\rho_m A .
\]
Then \(f_m\) satisfies the higher-order annihilation condition because every
Hessian \(D^2\psi\) is symmetric and hence \(\langle D^2\psi,A\rangle=0\).

If the source inequality remained true for arbitrary, not necessarily
symmetric, test tensors \(\varphi\), we could test it on
\[
  \varphi_m=h_m A,
\]
where \(h_m\) is a logarithmic cutoff equal to \(1\) near the support of
\(\rho_m\) and satisfying \(\|\nabla h_m\|_{L^2(\mathbb R^2)}\to0\). The left
side is fixed, while the right side tends to \(0\), a contradiction.

Equivalently, the antisymmetric component is invisible to the source
annihilation condition. Removing symmetry would force a false critical
\(\dot W^{1,2}(\mathbb R^2)\to L^\infty\) point-control estimate.

## Scope

This answers the literal question of whether one can simply replace
\(\operatorname{Sym}^k(T_bG)\) by the full tensor bundle in the displayed
inequality. It does not address possible repaired variants that add a separate
condition controlling antisymmetric components, nor does it address the Besov
or Sobolev-Lorentz open problems earlier in the paper.

## Evidence

- `source_paper.pdf`: Jean Van Schaftingen, "Limiting Bourgain-Brezis estimates
  for systems: theme and variations", arXiv:1311.6624.
- `figures/open_problem_crop.png`: crop of the symmetry-assumption sentence on
  PDF page 16.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet, once compiled.

## Novelty Check

Bounded local search on 2026-07-18 found no existing packet or attempt for
arXiv:1311.6624, the phrase "symmetry assumption", `Sym^k`, `D_b^k`, or the
Chanillo--Van Schaftingen higher-order group estimate. The only local
`antisymmetric` hits concerned unrelated martingale/operator-space targets.
Web searches for the exact sentence and close variants returned the source
paper and bibliographic mirrors, but no explicit counterexample to the literal
symmetry-removal extension.

## Human Review Recommendation

Check interpretation first. The packet treats the source sentence as asking
whether the test section \(\varphi\) can range over all horizontal \(k\)-tensors
instead of symmetric \(k\)-linear maps. Under that literal reading, the
counterexample is immediate and likely valid. If the intended open problem was
instead a subtler symmetry question with an added constraint on the
antisymmetric component, then this packet should be cited as the obstruction to
the naive formulation.
