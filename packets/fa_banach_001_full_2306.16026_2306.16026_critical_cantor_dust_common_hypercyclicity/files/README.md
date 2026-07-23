# Full solution: the critical Cantor dust is common hypercyclic

status: `full_solution_likely_valid`

source: Fernando Costa Jr.,
*Self-similar fractals and common hypercyclicity*,
arXiv:2306.16026, Problem 6.1 on PDF page 36.

target: decide whether the products of Rolewicz operators indexed by a
uniform four-corner Cantor dust of dissection ratio `1/4` have a common
hypercyclic vector on `c0 x c0`.

packet:
`runs/fa_banach_001/solutions/full/2306.16026_critical_cantor_dust_common_hypercyclicity/`

ledger:
`runs/fa_banach_001/ledger/results/2306.16026_critical_cantor_dust_common_hypercyclicity.json`

## Result

The answer is **yes** for the standard axis-parallel four-corner dust in the
positive quadrant. In fact, the same proof works on `ell_p x ell_p` for every
`1 <= p < infinity`.

## Main idea

Use the exact Bayart-Costa-Menet characterization of common hypercyclicity for
products of Rolewicz shifts. At level `m`, order the `4^m` dust cylinders
lexicographically. A consecutive block of `q` cylinders has total tag
variation

`O(1 + m q / 4^m)`.

At stage `j`, work at resolution `m_j = m_0 + j s` and cover the next
symbolic portion of length comparable to `tau / m_j`. The tag variation per
stage is uniformly bounded, so the required visit times grow by at most one
fixed factor. The fixed resolution increment `s` supplies that factor of
room. Since

`sum_j tau / (m_0 + j s) = infinity`,

some finite stage covers the remaining symbolic dust.

## Verification

- The source problem and the exact characterization in Theorem 2.2 of
  arXiv:2103.13152 were checked directly.
- The multiscale variation bound and the scheduling recurrence are proved
  explicitly in `main.tex`.
- `verification.md` records the proof audit and numerical smoke test.
- The exploratory computation is not used in the formal proof.

## Novelty bound

On 2026-07-23, the cheap run indexes, local arXiv source corpus, and exact
arXiv-restricted web searches were checked for the arXiv id and combinations
of `Cantor dust`, `dissection ratio 1/4`, `common hypercyclicity`, and
`Rolewicz`. No later direct answer was found. This is a bounded search, not a
priority guarantee.

## Scope

The proof treats the usual homogeneous axis-parallel four-corner Cantor dust
and its positive axis-parallel translates and scalings. It does not address
arbitrary rotated or non-corner self-similar sets or the other open problems
in arXiv:2306.16026.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2306.16026.
- `supporting_paper_2103.13152.pdf`: source of the exact characterization.
- `figures/open_problem_crop.png`: Problem 6.1 and its endpoint context.
- `code/finite_traversal_probe.cpp`: exploratory greedy stress test.
- `verification.md`: proof and rendering audit.
