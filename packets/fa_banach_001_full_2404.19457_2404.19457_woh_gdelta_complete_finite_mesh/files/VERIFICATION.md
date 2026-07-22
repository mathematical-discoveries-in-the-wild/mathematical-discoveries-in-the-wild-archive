# Verification report

Verdict: `full_solution_likely_valid`

## Mathematical interfaces checked

1. **Tail estimates.** For `t <= epsilon/4`, `1-t` dominates
   `(1-epsilon)(1+t)`. For `t >= 2/epsilon`, `t-1` dominates the same
   expression. Both estimates are uniform in `c in [0,1]`.
2. **Middle mesh.** The loss from moving by at most
   `h=epsilon^2/64` is less than `2h`. Since
   `c+t >= epsilon/4`, the available loss between factors
   `1-epsilon/2` and `1-epsilon` is at least `epsilon^2/8`, four times the
   required bound.
3. **Dense-point transfer.** Approximating each sphere point within
   `epsilon^2/64` loses less than twice that amount, while every mesh scale is
   at least `epsilon/4`. This preserves the factor `1-epsilon/2` needed by the
   mesh lemma.
4. **Finite dual trace.** The inequalities
   `|sum q_i alpha_i| <= ||sum q_i x_i||` for rational `q` are necessary and
   sufficient for a norm-one functional on the span. Zero-norm relations are
   forced to receive value zero; Hahn–Banach supplies the extension.
5. **Varying quotient kernels.** The trace graph is used only on the open set
   where the fixed rational directions have positive seminorm. Joint
   continuity of finite-dimensional seminorm evaluation follows from
   equi-Lipschitz control by the finitely many coordinate seminorms.
6. **Compact co-projection.** The bad/inadmissible alternative and every
   strict finite-mesh witness alternative are open. Universal quantification
   over the compact cube `[-1,1]^n` therefore produces an open set by the tube
   lemma.
7. **Boundary of the positive-norm domain.** Adding the closed complement of
   the open domain produces a union of one closed and one open set, which is
   `G_delta` in a metrizable space. Countable intersection over rational
   tuples remains `G_delta`.
8. **Completeness.** The source's non-`F_sigma` proposition applies to the
   same WOH isometry class in both `P_infinity` and `B`. Combined with the new
   `G_delta` upper bound, the cited Hurewicz theorem gives completeness.

## Adversarial edge cases

- `f(x_i)=0`: the lower mesh endpoint is positive, so density-transfer slack
  does not vanish.
- `t` near zero or infinity: handled independently of the mesh and of `f`.
- linearly dependent or quotient-zero combinations of the selected vectors:
  the Hahn–Banach inequalities enforce consistency.
- selected rational vector killed by the seminorm: the tuple is ignored via
  the closed complement of the positive-norm domain; surviving normalized
  rational directions are still dense in the sphere.
- non-attainment of a dual supremum: irrelevant, because the proof quantifies
  over actual finite evaluation vectors of all functionals and characterizes
  them by extension inequalities.

## Non-computational status

No numerical search or symbolic computation is used in the proof. The crop
script only prepares source evidence and has no mathematical role.

## Recommended human review

Focus on Lemma 5 (the closed finite dual trace) and the passage from the open
relation to the compact universal co-projection. Once those two interfaces are
accepted, the remaining argument is elementary quantitative bookkeeping.

