# Literature-Implied Answer: continuous bounded trace selection

Status: literature_implied_answer for the weaker continuity alternative in
Remark 4.3(2); not claimed as an original new formula.

Source paper: Daniel Azagra and Carlos Mudarra, "\(C^{1,\omega}\)
extension formulas for \(1\)-jets on Hilbert spaces", arXiv:1912.13317.

## Target

Remark 4.3(2), on PDF page 26 and source line 1405, asks whether the bounded
extension results can be improved so that the extension operator is continuous
from \((\mathcal J_b^{1,\omega}(E),\rho)\) into
\((C_b^{1,\omega}(X),\|\cdot\|_{1,\omega,b})\).

## Identification

The paper's bounded extension theorem makes the trace map
\[
T:C_b^{1,\omega}(X)\to \mathcal J_b^{1,\omega}(E),\qquad
T(F)=(F|_E,\nabla F|_E),
\]
a surjective bounded linear map once the target is given the norm \(\rho\).
The quotient norm induced by \(T\) is equivalent to \(\rho\), so the trace
space is Banach. The Bartle--Graves selection theorem then gives a continuous
nonlinear right inverse \(S\) of \(T\). This \(S\) is the desired continuous
extension operator.

## Scope

This answers the "or at least" continuity alternative in the remark. It also
implies the natural \(A\)-seminorm convergence for differences of the selected
extensions. It does not give an explicit paraconvex-envelope formula and does
not prove that the specific formula constructed in the source paper has this
stronger continuity.

## Files

- `main.tex`: compact proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1912.13317.
- `figures/open_problem_crop.png`: crop of Remark 4.3(2).

## Search And Duplication Check

Local index search for `1912.13317`, `C^{1,omega}`, `1-jets`, `Whitney`,
`continuous extension operator`, and `Bartle-Graves` found no existing packet
for this target. Nearby packets for arXiv:2305.19995 and arXiv:2403.14317
concern different Whitney-extension questions. Web search on 2026-06-19 found
the source arXiv page and general Bartle--Graves references, but no paper
explicitly identifying this implication for Remark 4.3(2).
