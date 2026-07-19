# The integral tensor space need not be the algebraic completion

Status: `candidate_counterexample_likely_valid`

Source: Eva-Maria Hekkelman, Edward McDonald, and Teun D. H. van
Nuland, *Multiple operator integrals, pseudodifferential calculus, and
asymptotic expansions*, arXiv:2404.16338 (2024).

Source location: Definition 4.1 and the paragraph after Remark 4.2, page 22.

## Result

The answer to the source paper's general completion question is **no**.

Let `Gamma` be the Banach space of bounded measurable functions on the real
line that vanish off `[1,infinity)` and are constant on every unit interval
`I_m=[m,m+1)`, with the sup norm (repeated as every seminorm).  Thus `Gamma`
is isometric to `ell_infinity`.  The block-diagonal kernel

```text
phi(x,y) = 1  if x and y belong to the same I_m,
           0  otherwise
```

belongs to the integral-representation space `Gamma boxtimes_i Gamma`.
Indeed, on the product Rademacher probability space, put
`a(x,omega)=omega_m` on `I_m` and zero elsewhere.  Then
`phi(x,y)=E[a(x,omega)a(y,omega)]`, and both factors have norm one.

However, `phi` is not in the completion of `Gamma tensor Gamma` for the
seminorm of Definition 4.1.  That seminorm dominates the uniform norm.  On
sampling one point from each interval, `phi` becomes the infinite identity
matrix, whereas every algebraic tensor becomes a finite-rank infinite matrix.
No finite-rank matrix can approximate the identity matrix entrywise uniformly
to error below `1/2`: its rows lie in a bounded subset of one finite-dimensional
space and hence contain two arbitrarily close rows, while two distinct rows of
the identity are distance one apart.

Thus the algebraic tensor product has distance at least `1/2` from `phi` in
the paper's own seminorm.

## Scope

This is a full negative answer to the phrase "in general" in the source
question.  It does not say that algebraic tensors fail to be dense for the
particular symbol spaces used later in the paper, such as the spaces
`S^beta(R)` or `T^beta(R)`, nor does it change the paper's multiple operator
integral results.

## Verification and novelty

The proof is elementary and non-computational.  The main adversarial checks
are recorded in `verification.md`: joint measurability of the Rademacher
factor, domination of the uniform norm by the integral seminorm, and the
finite-rank row separation lemma.

The run indexes were searched for arXiv:2404.16338 and the core completion,
integral-projective-tensor, Rademacher, and diagonal terms.  A bounded web and
arXiv search used the exact question sentence, the source title/id, and close
integral projective tensor-product phrases.  No separate resolution was found.
Most significantly, Eva-Maria Hekkelman's 2026 thesis repeats the question
verbatim in Remark 3.2.2 as unanswered.  This is strong recent status evidence,
but not an exhaustive novelty claim.

## Packet contents

- `main.tex`: self-contained counterexample and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv source paper.
- `figures/open_problem_crop.png`: full-width source crop containing the
  definition, seminorm, algebraic inclusion, and question.
- `verification.md`: adversarial verifier report.
- `attempt_log.md`: proof-development history and repaired false start.

Human review recommendation: **send for focused functional-analysis review**.
The highest-value check is that "completion under the given seminorms" has the
ordinary density meaning used in the proof; the uniform separation then makes
the conclusion immediate.

