# Ordinary C-numerical range: positive finite-kernel case

Status: `partial_result_likely_valid`

Source: J. Loreaux and S. Patnaik, *Convexity of the orbit-closed
C-numerical range and majorization*, arXiv:2009.01300. The abstract and
Introduction restate Dirr--vom Ende's Open Problem (b): is the ordinary
infinite-dimensional `C`-numerical range convex for selfadjoint trace-class
`C`, without taking closure?

## Result

If `C >= 0` is trace class with finite-dimensional kernel, then `W_C(A)` is
convex for every bounded operator `A`. No normality, compactness, or
diagonalizability assumption is imposed on `A`.

The proof has two mechanisms. First, every point in the planar interior of
`closure(W_C(A))` is attained: finitely many orbit elements can be approximated
simultaneously by orbit elements with one common infinite-dimensional tail,
leaving a finite-dimensional head whose numerical range is convex. Second,
any two ordinary maximizers on a supporting face are conjugate by a unitary in
the commutant of the supporting selfadjoint part. A logarithm path through that
commutant fills the whole face segment.

## Scope

This is a substantial partial answer, not a solution of the full selfadjoint
problem. The positive infinite-rank case with infinite-dimensional kernel and
arbitrary `A` remains outside the proof. Finite rank was already known by
Westwick. The finite-kernel hypothesis is used to fix the residual kernel
multiplicity in the equality decomposition of a boundary maximizer.

A bounded search on 2026-07-22 found the source papers and the orbit-closed
follow-up arXiv:2106.11205, but no later theorem with this conclusion. This is
novelty evidence rather than a definitive certification.

Human review recommendation: **verify and retain as a substantial partial
theorem**. The two high-value checks are Lemma 1's common-tail construction and
the residual kernel count in the maximizer classification.

Ledger: `ledger/results/2009.01300_positive_trace_class_finite_kernel_convexity.json`

