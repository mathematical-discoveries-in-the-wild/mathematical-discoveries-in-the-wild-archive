# Order-continuous lattice case of the plus-minus isometry conjecture

Status: `candidate_partial_likely_valid`

Run: `fa_banach_001`  
Agent: `agent_lane_04`  
Source paper: Michael Cwikel, arXiv:1502.00986v2, *Some alternative definitions for the "plus-minus" interpolation spaces ... of Jaak Peetre*

## Result

This packet proves Cwikel's Remark 4.1 isometry conjecture under the additional hypothesis that the two endpoint Banach lattice norms are order continuous:

\[
\|\cdot\|_{\langle X_0,X_1\rangle_{\theta,(0)}}=
\|\cdot\|_{[X_0,X_1]_\theta}
\]

for complex Banach lattices of measurable functions on the same measure space.

The unrestricted conjecture for arbitrary complexified Banach lattices is not claimed.

## Proof mechanism

The proof uses a scalar moving-kernel representation. Given a Calderon product factorization written as
\[
|f|\le b,\qquad b e^{-\theta s}\in X_0,\qquad b e^{(1-\theta)s}\in X_1,
\]
place a narrow normalized kernel at the logarithmic-ratio location \(s(\omega)\). This gives a continuous plus-minus representation of \(f\) with endpoint estimates dominated by the two Calderon factors. Bounded \(s\)-bands are handled by quantizing \(s\); order continuity of \(X_0\) and \(X_1\) removes the unbounded \(s\)-tails.

## Files

- `main.tex`: full packet with statement and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1502.00986v2.
- `figures/open_problem_crop.png`: source crop of Remark 4.1.

## Verification focus

Check the completeness/limit passage in the continuous plus-minus space and the scope of the Calderon-Lozanovskii isometric product representation under the order-continuity hypothesis.
