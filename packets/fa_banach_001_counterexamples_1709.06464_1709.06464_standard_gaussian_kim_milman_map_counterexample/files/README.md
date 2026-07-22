# Standard-Gaussian Kim--Milman map: candidate counterexample

**Status:** candidate counterexample, likely valid, awaiting human review.

## Result

There is a smooth convex globally Lipschitz function
\(F:\mathbb R^2\to\mathbb R\) such that, for all sufficiently small
\(\varepsilon>0\), the Kim--Milman reverse-heat-flow map transporting the
standard Gaussian measure \(\gamma_2\) to
\[
  d\nu_\varepsilon=Z_\varepsilon^{-1}e^{-\varepsilon F}\,d\gamma_2
\]
is not the Brenier map.

This supplies a rigorous positive answer to the numerical suggestion in the
final section of Anastasiya Tanana's arXiv:1709.06464: even with standard
Gaussian source, the two maps can differ for a non-Gaussian log-concave
target. The general comparison question originated in Kim--Milman,
arXiv:1002.0373; Tanana settled it for non-standard Gaussian sources but left
the standard-source/non-Gaussian case at the level of numerical evidence.

## Mechanism

Let \(P_t\) be the standard Ornstein--Uhlenbeck semigroup and let
\(S_t^\varepsilon\) be the inverse Kim--Milman flow. For
\(J_\varepsilon(x)=DS_\infty^\varepsilon(x)\), a second-order expansion gives
\[
 J_\varepsilon(x)-J_\varepsilon(x)^T
 =\varepsilon^2\int_0^\infty\!\int_0^t
   [D^2P_tF(x),D^2P_sF(x)]\,ds\,dt+o(\varepsilon^2).
\]
All local second-order terms are Hessians and hence symmetric; only the
time-ordering commutator can create skewness.

For the model
\(F_0(x)=x_1^4+(x_1+x_2)^4\) and \(x_0=(0,1)\), the double integral is exactly
\[
 -6[P,Q]=
 \begin{pmatrix}0&6\\-6&0\end{pmatrix}\neq0,
 \quad
 P=\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
 Q=\begin{pmatrix}3&2\\2&2\end{pmatrix}.
\]
A smooth convex globally Lipschitz truncation of the scalar fourth power
preserves this nonzero coefficient by dominated convergence. Thus
\(DS_\infty^\varepsilon(x_0)\) is nonsymmetric for all small positive
\(\varepsilon\). If the forward map were Brenier, its inverse would be the
gradient of the convex conjugate and would have symmetric derivative, a
contradiction.

## Packet contents

- `main.tex` and `solution_packet.pdf`: full statement and proof.
- `source_paper.pdf`: Tanana, arXiv:1709.06464, containing the standard
  Gaussian numerical question on page 5.
- `background_paper_1002.0373.pdf`: Kim--Milman, arXiv:1002.0373.
- `figures/open_problem_crop.png`: full-width crop of the page-5 source
  passage.
- `code/verify_commutator.py`: exact symbolic check of the matrix and scalar
  integral computation.
- `VERIFICATION.md`: proof, computation, novelty, and rendering checks.

## Novelty bounds

A bounded search was performed through 2026-07-22 using the run's cheap
indexes and arXiv/web searches for the exact paper ids and phrases
`Kim-Milman map standard Gaussian Brenier`, `heat flow interpolation Brenier
standard Gaussian`, and close variants. The search found Tanana's 2017 note
and later papers using Kim--Milman/Langevin flows, but no rigorous resolution
of the standard-Gaussian/non-Gaussian comparison. This is not an exhaustive
bibliographic guarantee; novelty confidence is **medium**.

## Human-review recommendation

Check first the parameter-dependent ODE expansion in Lemma 2 of the packet,
especially uniform integrability as \(t\to\infty\). Then check the dominated-
convergence passage from the quartic model to smooth convex Lipschitz
truncations. The finite-dimensional commutator calculation is exact and is
independently reproduced by the verifier.
