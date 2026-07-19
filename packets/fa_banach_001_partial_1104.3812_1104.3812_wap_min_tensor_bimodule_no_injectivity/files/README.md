# Weakly compact slice tensors form a minimal-tensor bimodule without injectivity

Status: `partial_result_likely_valid`.

Source: Volker Runde, *Factorization of completely bounded maps through
reflexive operator spaces with applications to weak almost periodicity*,
Journal of Mathematical Analysis and Applications 385 (2012), 477--484,
arXiv:1104.3812, DOI: 10.1016/j.jmaa.2011.06.073.

## Source question

On PDF page 11, the source asks whether, for every Hopf--von Neumann algebra
\((M,\Gamma)\), the space \(\operatorname{WAP}(M_*)\) is a \(C^*\)-subalgebra
of \(M\).  The exact statement is preserved in
`figures/open_problem_crop.png`.

## Partial result

For arbitrary von Neumann algebras \(M,N\), put
\[
  \mathcal W(M\bar\otimes N)
  =\{u\in M\bar\otimes N:(f\otimes\mathrm{id})(u),\ f\in M_*,
      \text{ defines a weakly compact map }M_*\to N\}.
\]
Then
\[
  (M\otimes_{\min}N)\,\mathcal W(M\bar\otimes N)
  +\mathcal W(M\bar\otimes N)\,(M\otimes_{\min}N)
  \subseteq \mathcal W(M\bar\otimes N).
\]
Equivalently, \(\mathcal W(M\bar\otimes N)\) is a bimodule over the spatial
minimal tensor product for **all** von Neumann algebras.  Corollary 2.3 of the
source proves this with the additional assumptions that \(M,N\) are injective.

Consequently, for every Hopf--von Neumann algebra define
\[
  A_\Gamma=\{y\in M:\Gamma(y)\in M\otimes_{\min}M\}.
\]
This is a unital \(C^*\)-subalgebra of \(M\), and
\(\operatorname{WAP}(M_*)\) is an \(A_\Gamma\)-bimodule, without an
injectivity assumption.

## Idea of the proof

For an elementary tensor \(a\otimes b\), multiplication can be moved through
the slice map.  If \(T_u(f)=(f\otimes\mathrm{id})(u)\), then
\[
  T_{u(a\otimes b)}(f)=T_u(f\circ R_a)b,
  \qquad
  T_{(a\otimes b)u}(f)=bT_u(f\circ L_a).
\]
The maps surrounding \(T_u\) are bounded, so weak compactness is preserved.
Finite sums follow by linearity, and arbitrary elements of
\(M\otimes_{\min}N\) follow by norm approximation because weakly compact
operators form a norm-closed operator ideal.

## Scope

This does not settle the source question.  If \(x,y\in\operatorname{WAP}(M_*)\),
both slice maps associated with \(\Gamma(x)\) and \(\Gamma(y)\) are weakly
compact, but neither coproduct need lie in \(M\otimes_{\min}M\).  The theorem
therefore controls a canonical multiplier subalgebra, not arbitrary products
of two WAP elements.

## Novelty check

The run's lightweight indexes contained no match for arXiv:1104.3812 or this
injectivity removal.  Bounded searches on 2026-07-19 used the exact source
title, `WAP(M_*)`, `bimodule`, `spatial/minimal tensor product`, and
`injective`.  The source itself states the result only for injective von
Neumann algebras.  Daws's later arXiv:1409.7302 still describes the full Hopf
question as unresolved and constructs a non-algebra example only for the
unconstrained two-fold weak-slice class, not for a Hopf coproduct.  No exact
statement of the theorem in this packet was found.  This is therefore labeled
`likely valid`, not literature-certified novel.

## Human-review recommendation

Promote as a substantial partial theorem after checking the four identities
and closures highlighted in `verification_report.md`.  The argument is short
and removes a published hypothesis, so independent expert comparison with
Corollary 2.3 is especially appropriate.

## Files

- `main.tex` and `solution_packet.pdf`: full review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: exact source-question crop.
- `verification_report.md`: adversarial proof audit.
- `attempt_log.md`: successful and failed routes.

