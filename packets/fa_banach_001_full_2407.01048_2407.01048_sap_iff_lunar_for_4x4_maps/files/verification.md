# Verification report

## Claim checked

For every coordinatewise-injective `Phi:[4]x[4]->L`, the associated Hankel
system has SAP if and only if `Phi` is lunar.

## Verdict

Likely valid full result. Confidence: 97/100. The mathematical proof is exact
but computer-assisted, and novelty remains subject to author/expert review.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Source scope | valid | The associated Hankel system is defined in the source for coordinatewise-injective maps; the theorem uses that standing hypothesis. |
| Proper-coloring model | valid | Every color class is a matching in `K_4,4`, and conversely. |
| Directed normal forms | valid after two repairs | Unequal overlapping solution sets yield two distinct non-loop directed edges with neither a common initial nor a common terminal. Reverse, the two crossed orientations, and disjoint incidence give four types per coordinate and sixteen combined types. |
| Restricted-growth enumeration | valid | Row-major first-occurrence labeling gives one representative for every unlabeled proper coloring and explores every compatible old color plus the next new color. |
| Full census | valid | The classifier obtains 17,427,192 canonical proper colorings and 15,667,716 non-lunar colorings, matching the independent earlier census. |
| Orbit quotient | valid | Minimization runs over all 24 row permutations, 24 column permutations, transposition, and canonical color relabeling. The resulting non-lunar orbit count is 14,828. |
| Symmetry transfer | valid | Row/column permutations and color relabeling are unitary/permutation equivalences. Under transposition, replacing each coefficient `C_l` by `C_l^T` fully transposes both source and absorbed operators, preserving norm. |
| Certificate coverage | valid | The scalar and matrix index sets are disjoint and their union is exactly `{0,...,14827}`: 7,331 scalar and 7,497 matrix records. |
| Component compression | valid | Tensor support components are orthogonal row/column blocks. A certified component norm is bounded above by the full absorbed norm, so a component larger than the source suffices. |
| Exact norm gate | valid | Integer Gram matrices have exact characteristic polynomials. Rational thresholds are not roots; exact Sturm counts give zero source eigenvalues and at least one target eigenvalue above the threshold. |
| Lunar implies SAP | cited | This is Theorem B of arXiv:2407.01048v1. |

## Adversarial repairs retained in the record

Three attractive but invalid shortcuts were found and removed before
promotion:

1. A witness for a merged minimal non-lunar core does not automatically lift
   to a refinement, because tensoring the merged color creates cross terms.
2. Coordinatewise injectivity does not force all four row indices or all four
   column indices in a lunar failure to be distinct. The earlier 6,301-class
   disjoint/disjoint census was therefore incomplete.
3. A nine-type quotient silently lost the relative orientation when both
   coordinates were crossed. The final classifier keeps a redundant directed
   4-by-4 list, adding 403 genuine orbits.

None of these discarded reductions appears in the final theorem proof.

## Exact verifier result

The clean packet verifier run rebuilds the classifier and ends with:

```text
classification: 17,427,192 proper canonical colorings; 15,667,716 non-lunar; 14,828 symmetry orbits
exact certificates: 7,331 scalar; 7,497 at matrix level 2
PASS: every non-lunar coordinatewise-injective 4x4 map fails SAP
```

NumPy is used to assemble integer arrays. SymPy characteristic polynomials and
Sturm root counts are the acceptance gate. The classification itself uses
only integer C++ code.

SHA-256 fingerprints of the verified artifacts:

```text
69616586712acfa3e4254b4e5c2f2fdbf9e62a0211e8e91c048b308c316ebfe5  classify_all_failure_orbits.cpp
f77a619e06496ab972abb2dbae2bda4dcb528d6ab53880f32e3e07c581c3f0ee  verify_full_problem7.py
68f17f6e0ac938296bba552af04e86899bb2324e0180f703cc9c3dce24b92904  directed_failure_scalar_certificates.json
38882f176bfa8c73182b1327c3800ebcb9794aadedfe25a980f49d6ef21a4503  directed_failure_matrix_certificates.json
```

## Remaining limitations

- This is a computer-assisted finite proof, not a conceptual hand proof.
- The certificate files are about 12 MB in total and should remain attached to
  the packet for auditability.
- The bounded novelty search found no public resolution, but a 2024 talk
  announcement mentions unspecified progress. Contact the source authors.

## Human review recommendation

Send to an operator-space/functional-analysis expert and a second reviewer
comfortable auditing finite classification code. Priority checks are the
directed normal-form lemma, transposition invariance for matrix coefficients,
and random independent replay of certificate records.
