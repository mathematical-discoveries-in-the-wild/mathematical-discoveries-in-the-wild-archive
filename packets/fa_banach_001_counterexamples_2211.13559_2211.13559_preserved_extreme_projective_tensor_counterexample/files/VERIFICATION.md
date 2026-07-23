# Verification report

Status: `candidate_counterexample_likely_valid`

## Mathematical checks

- Checked that the proposed closed symmetric convex set contains
  `(1/2)B_ell2` and is contained in `sqrt(2)B_ell2`, so its Minkowski
  functional is an equivalent norm.
- Checked that `e_0` belongs to the new unit ball as the norm limit of the
  midpoints `(p_n^++p_n^-)/2=(1-epsilon_n)e_0`.
- Checked the weak slice estimate generator by generator. For any fixed
  Hilbert functional, the high-index positive generators converge weakly to
  `e_0`, while all remaining generators have a uniform positive deficit in
  the exposing functional. Thus every net in the unit ball on which the
  exposing functional tends to one converges weakly to `e_0`.
- Checked the implication from this net-level weak exposure to preserved
  extremality using Goldstine approximation of each term in a hypothetical
  bidual midpoint decomposition.
- Checked that both tensor sequences consist of points of the projective unit
  ball and admit simultaneous weak-star cluster points in the product of two
  bidual balls.
- Checked the midpoint identity against an arbitrary bounded bilinear form.
  The only off-diagonal term is `A(e_0,e_n)`, which tends to zero because
  `(e_n)` is weakly null under any equivalent norm on `ell_2`.
- Checked distinctness using the original Hilbert inner product, which is a
  bounded bilinear form for the equivalent norm. Its values tend to `2` on
  the first tensor sequence and `0` on the second.

No numerical or symbolic computation is needed; all formulas are exact.

## Literature check

A bounded arXiv search on 22 July 2026 used:

- the exact phrase `Is x tensor y a preserved extreme point`;
- arXiv id `2211.13559` together with `Question 3.9`;
- `preserved extreme`, `projective tensor`, and `counterexample`;
- `weak-strongly exposed` together with tensor-product terminology.

The search found the source paper and arXiv:2510.21234, *Almost preserved
extreme points*, whose projective-tensor result is a different positive partial
answer under compact-operator and approximation-property hypotheses. No
counterexample or later full answer was located. This is bounded evidence, not
a novelty certification.

## Rendering check

The packet was compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error -outdir=tmp main.tex`. The final log has no warnings,
undefined references, or overfull/underfull boxes. All four pages were rendered
at 150 DPI and visually inspected. The title block, source-question crop,
displayed formulas, page transitions, references, and margins are readable and
free of clipping or overlap.

## Human-review recommendation

Review as a likely valid full counterexample to Question 3.9. The two
highest-value checks are the uniform weak slice argument in Lemma 2 and the
passage to simultaneous weak-star cluster points in the tensor bidual.
