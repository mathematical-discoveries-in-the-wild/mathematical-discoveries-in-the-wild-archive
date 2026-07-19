# Endpoint Failure for Haase's Unbounded-Group Transference Principle

Status: `counterexample_likely_valid`.

Run: `fa_banach_001`  
Agent: `agent_lane_08`  
Date: 2026-07-19

## Source

- arXiv:0807.3906
- Markus Haase, "A Transference Principle for General Groups and Functional Calculus on UMD Spaces"
- Source location: Section 3, Theorem 3.2 and Remark 3.3.

Haase proves the unbounded-group transference estimate with a strict gap
\(\omega_0<\omega\). Remark 3.3 says the proof essentially uses strictness
and the endpoint \(\omega=\omega_0\) is not expected.

## Claimed Result

The strict gap is genuinely necessary. For every positive growth parameter
\(\alpha>0\), the endpoint transference estimate at \(\omega=\omega_0=\alpha\)
fails already for the scalar Hilbert space \(X=\mathbb C\), \(p=2\), and the
one-dimensional group \(U(s)=e^{\alpha s}\).

The counterexample uses finite absolutely continuous measures whose Fourier
multiplier norms on scalar \(L^2(\mathbb R)\) are at most one, but whose endpoint
transferred operators grow like \(\log N\).

## Proof Packet

- Main proof: `main.tex`
- Rendered PDF: `solution_packet.pdf`
- Source paper copy: `source_paper.pdf` when available
- Source excerpt crop: `figures/open_problem_crop.png`
- Ledger record: `runs/fa_banach_001/ledger/results/0807.3906_endpoint_transference_failure.json`

## Novelty Check

Before promotion, the lightweight run indexes were searched for
`0807.3906`, the source title, `endpoint transference`, `omega_0`, and related
phrases. No duplicate packet was found.

A bounded web search on 2026-07-19 for phrases including `"omega = omega_0"
"transference"`, `"A transference principle for general groups" "endpoint
counterexample"`, and `"unbounded groups" "transference principle" "endpoint"`
found later interpolation and functional-calculus uses of Haase's transference
principle, but no exact endpoint counterexample.

## Human Review Recommendation

Review the distributional Fourier-transform computation for
\(\tanh(\alpha s)\) and the reduction from an endpoint transference estimate
to the scalar \(L^2\) multiplier bound. These are the only substantive moving
parts.
