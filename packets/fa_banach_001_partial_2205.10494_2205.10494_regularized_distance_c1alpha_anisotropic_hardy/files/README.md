# Regularized-distance C1,alpha anisotropic Hardy inequality

Status: **candidate substantial partial, likely valid; human review required**

Model: GPT5.6  
Agent: agent_lane_11  
Date: 2026-07-23

## Source question

Gheorghe Nenciu and Irina Nenciu, *Weak anisotropic Hardy inequality:
essential self-adjointness of drift-diffusion operators on domains in
\(\mathbb R^d\), revisited*, arXiv:2205.10494 [math.AP] (2022).

In Section 5, PDF page 17, the authors ask whether Theorem 3.1 remains true
when \(\partial\Omega\) is \(C^{1+\epsilon}\), \(0<\epsilon<1\).

## Result

The packet proves two statements.

1. The full anisotropic inequality extends to bounded \(C^{1,\epsilon}\)
   domains after replacing the possibly nonsmooth Euclidean distance
   \(\delta\) by a normalized regularized distance \(t\), and formulating the
   coefficient factorizations and normal/tangential block decomposition
   relative to \(t\). The logarithmic coefficient may be any
   \(\lambda<1\). Using any \(\lambda>1/2\), the polynomially small
   comparison error can be absorbed to recover the exact source conclusion
   for all the anisotropic data:
   \[
   \frac14(1-q)a\delta^{\beta-2}
   \left[(\beta+\gamma-1)^2+
   \frac1{2\log^2(1/\delta)}\right].
   \]

2. In particular, for \(D=I\) and \(\rho=1\), this becomes
   \[
   \frac1{4\delta^2}\left(1+
   \frac1{2\log^2(1/\delta)}\right).
   \]
   Thus the open question has a positive answer, without reformulation, in
   the classical unweighted Laplacian subcase.

The key device is
\[
N=\frac{\nabla t}{|\nabla t|^2},
\qquad N\cdot\nabla t=1.
\]
It preserves the one-dimensional Hardy calculation exactly. The new
geometric terms are
\[
O\!\left(t^{1-s}(1+|\log t|)+t^\epsilon\right)
=o\!\left(\log^{-2}(1/t)\right)
\]
and are absorbed by the logarithmic reserve.

## Why the packet is classified as partial

The conclusion now has the exact Euclidean-distance barrier for general
anisotropic data. The remaining issue is in the hypotheses. At
\(C^{1,\epsilon}\) regularity, the Euclidean distance need not be
differentiable in an entire boundary collar because the cut locus can
accumulate at the boundary. The source assumptions use \(\nabla\delta\) to
define anisotropic normal blocks, so the literal general statement is not
well posed on every such domain. The packet gives a complete natural
regularized-distance theorem with the exact \(\delta\)-barrier, but does not
claim that arbitrary a.e. \(\delta\)-based anisotropic coefficient data can
be converted to the \(t\)-based hypotheses.

## Files

- `main.tex`: complete theorem, proof, limitations, novelty check, and
  references.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:2205.10494.
- `figures/open_problem_crop.png`: source PDF page 17 crop containing the
  exact question.
- `figures/theorem_3_1_crop.png`: source PDF page 5 crop containing Theorem
  3.1.
- `code/verify_algebra.py`: symbolic check of the central scalar identity and
  numerical asymptotic sanity checks.
- `code/make_source_crops.py`: reproducible source-page rendering and crop.
- `verification_report.md`: commands, outputs, and review focus.

## Reproduction

From the repository root:

```sh
cd runs/fa_banach_001/solutions/partial/2205.10494_regularized_distance_c1alpha_anisotropic_hardy
conda run --no-capture-output -n sandbox python code/verify_algebra.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

## Human-review recommendation

Review the normalized regularized-distance lemma first, especially the
boundary normalization and \(D^2t\) estimate. Then check the displayed error
term \(E\) in the vector-field computation and the final comparison from
\(t\) to \(\delta\) in the Laplacian corollary. The symbolic checker confirms
the central cancellation, but is not a proof of the analytic estimates.
