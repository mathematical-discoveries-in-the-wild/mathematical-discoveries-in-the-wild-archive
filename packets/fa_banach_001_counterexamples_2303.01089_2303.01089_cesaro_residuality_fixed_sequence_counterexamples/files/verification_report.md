# Verification report

## Verdict

candidate_counterexample_likely_valid

The packet gives complete negative answers to Questions 5.6 and 5.9 exactly
as printed. The proof is definitional and has no external dependency.

## Source audit

- Published source checked: Discrete Analysis 2024:10, arXiv:2303.01089v3.
- Question 5.6, article page 29, quantifies over every strictly increasing
  integer sequence and asks whether \(G''_{p,(c_n)}\) is residual.
- Question 5.9, article page 29, quantifies over every pair of nonsingular
  integer matrices and asks whether \(G''_{A,B}\) is residual.
- Neither question includes multiplicative independence, coprimality, or a
  requirement that the acting dynamics differ from the invariance dynamics.

## Proof audit

1. \(c_n=p^n\) is strictly increasing for every integer \(p\geq2\).
2. Pushforwards compose as \(T_aT_b=T_{ab}\).
3. If \(T_p\mu=\mu\), induction gives \(T_{p^n}\mu=\mu\) for all \(n\).
4. Therefore every displayed Cesaro average equals \(\mu\), so convergence
   to \(\mathrm{Leb}\) occurs exactly for \(\mu=\mathrm{Leb}\).
5. Thus the questioned set is the singleton \(\{\mathrm{Leb}\}\). It is not
   dense in the Hausdorff space \(\mathcal P_p(\mathbb T)\), which also
   contains \(\delta_0\), and hence it is not residual under the source
   definition.
6. For Question 5.9, \(A=B=2I_d\) satisfies all printed hypotheses.
   \(A\)-invariance gives \(T_{B^n}\mu=T_{A^n}\mu=\mu\).
7. The same reasoning yields \(G''_{A,B}=\{\mathrm{Leb}_d\}\); the distinct
   invariant point mass \(\delta_0\) shows this singleton is not dense.

## Scope audit

- The result is only against the universal literal formulations.
- The multiplicatively independent case highlighted immediately after
  Question 5.6 remains open.
- Matrix variants with independence/coprimality assumptions remain open.
- Questions 5.5 and 5.8 concern non-Cesaro convergence and are not answered.

## Computational status

No numerical or symbolic computation is needed for the proof. The only code
in the packet reproduces the source-page crops.

## Literature check

Cheap indexes and bounded exact-phrase web searches on 2026-07-22 found no
existing answer to these two literal formulations. Because the obstruction is
elementary, the novelty claim should be read with moderate confidence pending
author or specialist review.

