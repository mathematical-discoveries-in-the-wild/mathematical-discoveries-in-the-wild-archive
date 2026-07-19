# A numerically norming family of uniform \(\mathcal A_{\nu}\) operators

Status: candidate partial result, likely valid

Source paper: S. Dantas, M. Jung, and O. Roldan, "Norm attaining operators which satisfy a Bollobas type theorem", arXiv:1910.05726.

Target: after Proposition 2.8, the source constructs compact operators \(T\in\mathcal A_{\nu}(H)\) on a separable infinite-dimensional real Hilbert space such that \(1=\nu(T)<\|T\|\), with a uniform Bollobas modulus independent of \(T\). The paper says it does not know whether such operators could be "norming for the whole space."

Result: under the natural numerical-radius interpretation, yes. For every nonzero finite-dimensional subspace \(F\subset H\), there is a compact operator \(T_F\) of the same type such that \(T_F|_F=I_F\). Hence the family is numerically norming:
\[
\|x\|^2=\sup_F |\langle T_Fx,x\rangle|\qquad (x\in H).
\]

## Packet Contents

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source passage.

## Verification Notes

The proof is a parameterized version of the construction in Proposition 2.8: choose the finite block \(J_3\) to be any prescribed finite-dimensional subspace \(F\), put the identity on \(F\), and put compact skew-symmetric \(2\times2\) blocks with coefficients tending to zero on \(F^\perp\). The skew part contributes zero to \(\langle Tx,x\rangle\), so the numerical-radius near-attainment condition forces \(x\) close to \(F\), with the same modulus \(\eta(\varepsilon)=\varepsilon^2/4\).

Human review should check the interpretation of "norming for the whole space." This packet proves the standard numerical-vector interpretation, not a possible operator-space-dual interpretation.
