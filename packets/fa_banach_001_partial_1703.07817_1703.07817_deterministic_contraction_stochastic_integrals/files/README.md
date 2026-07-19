# Partial Candidate: deterministic contraction stochastic integrals

Status: candidate partial result, likely valid; human review recommended.

Source paper: Ivan Yaroslavtsev, "Fourier multipliers and weak differential
subordination of martingales in UMD Banach spaces", arXiv:1703.07817v5.

Open target: Remark 5.12 says that the analogue of Theorem 5.10 for
antisymmetric operators \(A\) remains open. Such an estimate would imply the
linear Hilbert-transform estimate
\[
\|\mathcal H_X\|_{L^p(\mathbb R;X)\to L^p(\mathbb R;X)}
\le C_p\beta_{p,X}.
\]

## Result

The packet proves the contraction estimate in the non-adapted elementary case
(and hence in the corresponding approximation closure where the stochastic
integral is defined). Let \(H\) be a real Hilbert space, \(X\) a
finite-dimensional Banach space, \(1<p<\infty\), and \(W^H\) an
\(H\)-cylindrical Brownian motion. If \(\Phi\) is deterministic, or more
generally measurable with respect to an initial sigma-field independent of
\(W^H\), then for every bounded operator \(A\in\mathcal L(H)\),
\[
\|((\Phi A)\cdot W^H)_T\|_{L^p(\Omega;X)}
\le \|A\|\,\|(\Phi\cdot W^H)_T\|_{L^p(\Omega;X)}.
\]

Thus the antisymmetric case of Remark 5.12 holds with constant \(1\), and even
for every contraction \(A\), whenever the integrand has no Brownian-path
feedback.

## Scope

This does not solve the source paper's adapted-integrand problem. The proof
uses that, after conditioning on the initial randomness, both stochastic
integrals are centered Gaussian \(X\)-valued random variables. For genuinely
adapted \(\Phi\), the terminal stochastic integrals need not be Gaussian after
freezing the past, and the covariance/Jensen argument no longer applies.

## Packet Contents

- `main.tex`: theorem, proof, and review notes.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1703.07817v5.
- `figures/open_problem_crop.png`: source crop of Remark 5.12 on page 25.

## Verification

The proof is analytic. The key checks are:

- the covariance forms of \((\Phi A)\cdot W^H\) and \(\Phi\cdot W^H\);
- positivity of the covariance difference when \(\|A\|\le 1\);
- construction of an independent Gaussian remainder in finite dimensions;
- Jensen's inequality for \(x\mapsto \|x\|^p\).

Local index search found no existing packet or attempt for arXiv:1703.07817.
Web search on June 18, 2026 found the source paper, the follow-up
arXiv:1706.01731, and related arXiv:1812.08049, but no exact packet-level
record for this deterministic/non-adapted subcase.
