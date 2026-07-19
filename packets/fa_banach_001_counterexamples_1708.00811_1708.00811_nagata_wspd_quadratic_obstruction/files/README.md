# Nagata Dimension Does Not Give Linear-Size WSPD

Status: `counterexample_likely_valid`.

Run: `fa_banach_001`  
Agent: `agent_lane_08`  
Date: 2026-07-19

## Source

- arXiv:1708.00811
- Charles Fefferman and Pavel Shvartsman, "Sharp finiteness principles for Lipschitz selections: long version"
- Source location: Introduction, paragraph following the discussion of Whitney extension and efficient computation for finite metric spaces.

The source asks whether Har-Peled and Mendel's results on well-separated pair decompositions for doubling metrics can be extended from doubling metrics to metrics of bounded Nagata dimension.

## Claimed Result

The usual fixed-separation, linear-size WSPD conclusion cannot be extended from
doubling metrics to bounded Nagata dimension.

For every \(n\), the \(n\)-point equilateral metric has Nagata dimension \(0\)
with uniform constants. However, for every separation parameter \(s>1\), every
\(s\)-well-separated pair decomposition of this metric has at least
\(\binom n2\) pairs.

Thus bounded Nagata dimension alone cannot support a Har-Peled--Mendel style
WSPD theorem with \(O(n)\) pairs for fixed separation.

## Packet Contents

- Main proof: `main.tex`
- Rendered PDF: `solution_packet.pdf`
- Source paper copy: `source_paper.pdf` when available
- Source excerpt crop: `figures/open_problem_crop.png`
- Ledger record: `runs/fa_banach_001/ledger/results/1708.00811_nagata_wspd_quadratic_obstruction.json`

## Scope

This is not a negative answer to every possible algorithmic replacement for
WSPD in bounded Nagata dimension. It rules out the direct extension that keeps
the standard WSPD covering requirement and the linear-size bound for a fixed
separation parameter \(s>1\).

## Novelty Check

Cheap run indexes were searched for `1708.00811`, the title, Lipschitz
selections, finiteness principles, WSPD, Har-Peled--Mendel, doubling metrics,
and Nagata dimension. No exact packet was found.

A bounded web search on 2026-07-19 for `"well-separated pair decomposition"
"Nagata dimension"`, `"bounded Nagata dimension" "well separated pair
decomposition"`, `"WSPD" "Nagata dimension" equilateral`, and `"Har-Peled"
"Mendel" "Nagata dimension"` found the source paper and general Nagata
dimension references, but no exact WSPD obstruction.

## Human Review Recommendation

This should be quick to verify. Check only the definition of WSPD intended by
Har-Peled--Mendel and whether the source question specifically requires a
linear-size decomposition. Under the standard definition, the equilateral
metric lower bound is immediate.

