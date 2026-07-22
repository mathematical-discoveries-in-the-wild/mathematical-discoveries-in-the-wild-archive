# Verification Report

Candidate: `2205.14385_dir_preserves_compact_operators_without_ap`

## Claim Checked

For arbitrary Banach spaces \(X,Y\), every compact operator \(T:X\to Y\)
induces a compact operator
\[
\operatorname{Dir}(T):\operatorname{Dir}(X)\to\operatorname{Dir}(Y).
\]
In particular, the approximation-property assumption in Hypothesis 2.14 of
arXiv:2205.14385 can be omitted.

## Verdict

`likely valid`

This is a candidate full solution. No missing hypothesis or false direction of
inclusion was found.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | PDF page 11 states Hypothesis 2.14 exactly as transcribed. The source proves the AP case just before it and does not answer the hypothesis later in the paper. |
| Goldstine net | valid | For each \(z\in B_{E^{**}}\), Goldstine supplies a net from \(B_E\), not merely from a larger ball. Nets are necessary in the nonseparable case and are used correctly. |
| Naturality of the bidual | valid | \(S^{**}\kappa_E=\kappa_F S\), so the transformed Goldstine net consists of points in \(\kappa_F(K)\). |
| Weak-star closedness of \(\kappa_F(K)\) | valid | \(K=\overline{S(B_E)}\) is norm compact. Its canonical image is compact for the weak-star topology because the norm-to-weak-star identity is continuous. Weak-star topology is Hausdorff, hence that compact image is closed. |
| Compact-image lemma | valid | Weak-star continuity of \(S^{**}\) forces \(S^{**}(B_{E^{**}})\subseteq\kappa_F(K)\). In particular, \(S^{**}\) is compact. |
| Induction through tower stages | valid | Applying the lemma to \(T_n\) gives \(K_{n+1}\subseteq\kappa^Y_{n,n+1}(K_n)\), and also supplies compactness needed for the next induction step. |
| Passage to the direct limit | valid | The relation \(\iota_{n+1}^Y\kappa^Y_{n,n+1}=\iota_n^Y\) collapses every \(\iota_n^Y(K_n)\) into the fixed compact set \(\iota_0^Y(K_0)\). |
| Density inside the unit ball | valid | A dense linear subspace need not have its raw approximants in the unit ball, but normalization by \(\max\{1,\|a_j\|\}\) repairs this and preserves convergence to every point of the closed unit ball. |
| Completion and compactness | valid | Continuity of \(\operatorname{Dir}(T)\) and closedness of \(\iota_0^Y(K_0)\) extend the containment to the completed unit ball. Containment in a compact set gives relative compactness. |
| `Inv` corollary | valid/external | For self-maps, the source's Theorem 2.9 identifies \(\operatorname{Inv}(T)\) with the adjoint of \(\operatorname{Dir}(T)\). Schauder's theorem then gives compactness. This corollary is not needed to answer Hypothesis 2.14. |

## Counterexample Search

Small cases checked: not applicable. The proof is a general topological
argument, including nonseparable spaces through nets. Reflexive spaces,
finite-dimensional spaces, and spaces without the approximation property all
fall under the same lemma; none introduces a separate case.

Result: no counterexample found. No computational search was performed because
finite computation cannot test the weak-star/direct-limit claim.

## External Dependencies

- Goldstine's theorem: standard; used in its unit-ball form.
- Schauder's theorem: standard; used only for the optional `Inv` corollary.
- Source Theorem 2.9: inspected locally; supplies the adjoint identification
  for `Inv`.
- Definitions and naturality identities for `Dir`: inspected in the local
  source and reproduced in the packet.

## Gaps

- No mathematical gap identified.
- Novelty is not certified. A bounded search found no explicit later answer,
  but this is not an exhaustive literature review and supports no priority
  claim.

## Confidence

Score: **97/100**

Reason: the proof reduces the claim to one standard compact-image lemma, whose
topological details and induction direction were independently rechecked. The
remaining uncertainty is chiefly literature novelty and ordinary human-review
risk, not a known mathematical dependency.

## Human Review Recommendation

`send to human`

The fastest audit is to check the lemma
\(S^{**}(B_{E^{**}})\subseteq\kappa_F(\overline{S(B_E)})\), then verify that
the direct-limit identities put every stage image in one fixed compact set.
