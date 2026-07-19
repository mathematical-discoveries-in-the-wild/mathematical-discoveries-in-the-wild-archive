# A numerically norming family of uniform \(\mathcal A_{\nu}\) operators

Status: candidate full result, likely valid

Source paper: S. Dantas, M. Jung, and O. Roldan, "Norm attaining operators which satisfy a Bollobas type theorem", arXiv:1910.05726.

Target: after Proposition 2.8, the source constructs compact operators \(T\in\mathcal A_{\nu}(H)\) on a separable infinite-dimensional real Hilbert space such that \(1=\nu(T)<\|T\|\), with a uniform Bollobas modulus independent of \(T\). The paper says it does not know whether such operators could be "norming for the whole space."

Result: under the numerical-radius interpretation used in the source paragraph, yes. Let \(\eta_0(\varepsilon)=\min\{\varepsilon^2/4,1/4\}\), and let \(\mathscr U_{\eta_0}(H)\) be the class of compact operators \(T\) with \(1=\nu(T)<\|T\|\), numerical-radius attainment, and the \(\mathcal A_{\nu}(H)\) property with the common modulus \(\eta_0\). Then \(\mathscr U_{\eta_0}(H)\) is numerically norming:
\[
\|x\|^2=\sup_{T\in\mathscr U_{\eta_0}(H)} |\langle Tx,x\rangle|\qquad (x\in H).
\]

The proof uses the stronger concrete fact that for every nonzero finite-dimensional subspace \(F\subset H\), there is \(T_F\in\mathscr U_{\eta_0}(H)\) with \(T_F|_F=I_F\).

## Packet Contents

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source passage.
- `history/partial_packet_2026-06-18/`: previous partial packet, kept only as provenance after the full upgrade.

## Verification Notes

The proof is a parameterized version of the construction in Proposition 2.8: choose the finite block \(J_3\) to be any prescribed finite-dimensional subspace \(F\), put the identity on \(F\), and put compact skew-symmetric \(2\times2\) blocks with coefficients tending to zero on \(F^\perp\). The skew part contributes zero to \(\langle Tx,x\rangle\), so the numerical-radius near-attainment condition forces \(x\) close to \(F\), with the same modulus \(\eta(\varepsilon)=\varepsilon^2/4\).

Human review should check only the interpretation of "norming for the whole space." This packet is full for the source-local numerical-radius interpretation; it does not claim to solve a separate operator-space-dual problem not formulated in the paper.
