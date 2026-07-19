# Literature-implied status for the Heisenberg `L_1` compression exponent

Status: `literature_implied_answer (scoped compression exponent)`.

Source/open-problem signal: arXiv:0910.2026, J. Cheeger, B. Kleiner, and
A. Naor, *Compression bounds for Lipschitz maps from the Heisenberg group to
`L_1`*.

Supporting theorem source: arXiv:2004.12522, A. Naor and R. Young,
*Foliated corona decompositions*.

## Identification

The source paper proves a quantitative central-collapse theorem for Lipschitz
maps from the Heisenberg group to `L_1`; its proof gives a very small explicit
exponent `delta`. Immediately after Theorem 1.1, the source states that finding
the best possible `delta` remains open. In the compression subsection,
Corollary 1.6 gives, for every 1-Lipschitz map
`f : H(Z) -> L_1`, an upper compression estimate
`omega_f(t) <= C t/(1+log t)^delta`, and the following remark asks for the
correct compression exponent.

Naor--Young, arXiv:2004.12522, supply the exponent-level answer. Their
Theorem 1.10 constructs a Lipschitz map from the three-dimensional integer
Heisenberg group `H_Z` to `ell_1` whose compression satisfies
`omega_f(s) >= c s/((log s)^(1/4)(log log s)^2)` for all `s >= 3`. Their
Remark 23 then states that the lower-order factor cannot be removed: no
Lipschitz map from `H_Z` to `ell_1`, for the word metric, has compression
`omega_f(s) >= c s/(log s)^(1/4)` for all `s >= 2`.

Thus the main logarithmic compression exponent is `1/4`, up to lower-order
factors. This is an agent-identified implication of the later theorem and
remark, not an original proof produced by this run.

## Scope

This packet does not claim a full characterization of all possible compression
rates. Naor--Young explicitly say that such a characterization would require
more work. The durable status is therefore scoped: the exponent in the
Heisenberg-to-`L_1` compression problem is pinned down at `1/4` modulo
necessary lower-order loss, while the precise lower-order profile remains
open.

This is separate from the finite-ball distortion packets already recorded in
this run for nearby Heisenberg questions. Those packets record the
`c_1(B_n) ~ (log n)^(1/4)` consequence; this packet records the corresponding
compression-rate status for the arXiv:0910.2026 signal.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: local copy of arXiv:0910.2026.
- `supporting_paper_2004.12522.pdf`: local copy of arXiv:2004.12522.

## Search Evidence

Cheap run indexes were searched for `0910.2026`, the source title, Heisenberg
`L_1` compression, central collapse, Naor--Young, `2004.12522`, and
`sqrt[4]{log}`. No exact prior packet for arXiv:0910.2026 was found. Nearby
rows for arXiv:1003.4261, arXiv:1007.4238, arXiv:1212.2107, and arXiv:2207.11305
point to arXiv:2004.12522 for related Heisenberg finite-ball distortion or
step-two nilpotent consequences, confirming this target should be recorded as
literature-status memory rather than pursued as a new proof.

Human review recommendation: accept as a scoped literature-implied answer for
the `H_Z -> L_1` compression exponent, not as a new result and not as a full
lower-order characterization.
