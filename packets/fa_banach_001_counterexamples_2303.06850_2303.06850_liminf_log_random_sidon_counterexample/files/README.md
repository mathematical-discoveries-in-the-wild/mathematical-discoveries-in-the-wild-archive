# Counterexample: bounded liminf does not force random Sidonicity

Status: `counterexample_likely_valid`

Source: Aihua Fan, Herve Queffelec, and Martine Queffelec, *Old and new
results on the Furstenberg sets*, arXiv:2303.06850v1.

Target: Problem 8 in Section 6 asks whether, in Theorem 5.12, the hypothesis
`m_N = O(log N)` can be weakened to
`liminf_{N -> infinity} m_N/log N < infinity`.

Result: No. There is a nonincreasing selector mean sequence
`delta_n` for which `liminf m_N/log N < infinity`, but the associated
independent random set is almost surely not Sidon. Hence the proposed
liminf-only replacement is insufficient for the Sidon conclusion of
Theorem 5.12.

Mechanism: build long plateaus at level `1/N_j`. At the plateau endpoint
`H_j`, the expected count `m_{H_j}` is at least a constant times
`j log H_j`; after that, drop the selector means and wait to a much larger
endpoint `N_j` so that `m_{N_j} <= log N_j`. Chernoff plus Borel-Cantelli
forces the random counting function to violate the Sidon mesh bound along
the `H_j` endpoints.

Files:

- `main.tex` - proof packet source.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - source paper PDF.
- `figures/open_problem_crop.png` - page crop containing Problem 8.
- `code/make_open_problem_crop.py` - reproducible crop renderer.

Novelty check: cheap run indexes were searched for arXiv:2303.06850 and
phrases around `liminf m_N/log N`, `Bourgain random condition`, and random
Sidon sets; no prior packet was found. Web searches on 2026-07-03 for exact
and close phrases found the source paper but no later exact resolution.
