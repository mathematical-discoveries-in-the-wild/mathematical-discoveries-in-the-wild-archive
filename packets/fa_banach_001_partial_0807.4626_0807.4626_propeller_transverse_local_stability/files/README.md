# Transverse local stability of the Gaussian propeller optimizer

Run: fa_banach_001

Source: arXiv:0807.4626, Subhash Khot and Assaf Naor, *Approximate
kernel clustering*.

Status: candidate_partial_result_likely_valid_needs_human_review

## Source question

On page 20 the source asks whether its Gaussian partition constants satisfy

    C(k) <= C(3) = 9/(8*pi)  for every k >= 2.

Lemma 3.7 equivalently maximizes
(E max_j g_j)^2 / sum_j E[g_j^2] over centered Gaussian vectors. The
conjectured optimizer has only three active coordinates, coming from a planar
120-degree propeller.

## New partial result

Fix the three equilateral coefficient vectors of the propeller in a plane.
Adjoin any fixed finite, nonzero cloud of coefficient vectors in an orthogonal
space, scale that cloud by epsilon, and center the entire enlarged list of
coefficients. Then for every sufficiently small nonzero epsilon, its
Gaussian-max quotient is strictly less than 9/(8*pi).

Thus the propeller is a strict local maximum against arbitrary finite purely
transverse extensions, even when those extensions use arbitrarily many new
orthogonal dimensions.

## Proof idea

The three-blade maximum M dominates half the planar Gaussian radius, so
P(M <= t) = O(t^2). A transverse coordinate of size epsilon can improve the
maximum only on that small-ball event; its gain is therefore O(epsilon^3).
Centering the coefficient list shows that every nonzero added cloud incurs a
strictly positive A*epsilon^2 increase in total variance. The quadratic loss
beats the cubic gain.

## Scope and novelty

This does not solve the global propeller conjecture. It does not control
longitudinal or mixed perturbations, nor configurations far from the
propeller. A bounded primary-source search on 2026-07-22 found the known
three-dimensional solution arXiv:1112.2993 and related later conditional work,
but no exact transverse-extension theorem. Novelty confidence is moderate.

## Human review focus

Check the centered denominator identity and the conditional small-ball bound
that turns the numerator improvement into O(epsilon^3). No computational claim
is used.

Ledger: runs/fa_banach_001/ledger/results/0807.4626_propeller_transverse_local_stability.json
