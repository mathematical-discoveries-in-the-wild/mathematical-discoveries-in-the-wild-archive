# Weak and strong `T_{L^p}` for second countable locally compact groups

Status: `strong_partial_result_likely_valid`.

Source: Emilie Mai Elkiaer and Sanaz Pooya, *Property (T) for Banach algebras*, arXiv:2310.18136.

Target passage: Remark after Theorem 4.3 says that for countable discrete groups weak property `T_{L^p}` is equivalent to property `T_{L^p}`, but it is open whether this holds for general locally compact groups.

## Result

This packet proves the second countable locally compact case:

> If `G` is a second countable locally compact group and `1 <= p < infinity`, then weak property `T_{L^p}` is equivalent to property `T_{L^p}`.

This is a full answer in the usual lcsc setting of the source paper, but not claimed for arbitrary non-second-countable locally compact groups. Consequently, the packet is filed as a strong partial result.

## Contents

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: source arXiv paper.
- `supporting_paper_2403.05312.pdf`: discrete weak-`T_{L^p}` paper whose cocycle method is adapted.
- `figures/open_problem_crop.png`: source passage with the open locally compact gap.
- `code/render_open_problem_crop.py`: crop reproduction helper.

## Novelty Check

Cheap run indexes had no direct packet for arXiv:2310.18136. The source itself cites arXiv:2403.05312 for countable discrete groups and explicitly records the locally compact case as open. Bounded web searches on 2026-06-30 for exact phrases around `"weak property" "T_{L^p}" "locally compact"` and `"F^*_{lambda_p}" "property (T)"` found no later settlement.

## Review Recommendation

Review as a likely valid strong partial result. The main verification points are:

1. the compact-open Polish topology on locally compact cocycles;
2. the open-mapping argument proving closed coboundaries imply strong ergodicity;
3. the use of the locally compact Connes-Weiss/Schmidt strong-ergodicity characterization.
