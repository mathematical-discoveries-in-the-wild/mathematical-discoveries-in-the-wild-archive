# Literature-Already-Answered Packet: `c_0` Spreading Models and `K^s`

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is an exact later-literature answer to Problem 5.11 from
Hajek--Kania--Russo, not a new proof from this run.

## Source Problem

- Petr Hajek, Tomasz Kania, Tommaso Russo, *Symmetrically separated sequences
  in the unit sphere of a Banach space*, arXiv:1711.05149.
- Local PDF: `source_paper.pdf`.
- Evidence image:
  - `figures/open_problem_crop.png` (page 17, Problem 5.11).

Problem 5.11 asks whether every Banach space admitting a spreading model
isomorphic to `c_0` must satisfy `K^s(X)=2`.

## Supporting Literature

- Tommaso Russo, *A note on symmetric separation in Banach spaces*,
  arXiv:1904.12598.
- Local PDF: `supporting_paper_1904.12598.pdf`.
- Evidence images:
  - `figures/supporting_negative_identification_crop.png` (page 2, explicit
    statement that Theorem B solves `[HKR, Problem 5.11]` negatively).
  - `figures/supporting_theorem_b_crop.png` (page 3, Theorem B).
  - `figures/supporting_tsirelson_theorem_crop.png` (page 7, Theorem 4.2 and
    the direct-consequence note).

## Literature Status

The answer is negative. Russo explicitly identifies `[HKR, Problem 5.11]` and
states that Theorem B solves it negatively. Theorem B gives, for every
`epsilon > 0`, a Banach space `X` all of whose spreading models are isomorphic
to `c_0` and with `K(X) <= 1 + epsilon`. Since `K^s(X) <= K(X)`, taking
`epsilon < 1` yields `K^s(X) < 2`.

Russo's Theorem 4.2 supplies the concrete model: for the original Tsirelson
space `T^*_theta`, every spreading model is isomorphic to `c_0`, and
`K(T^*_theta)=K^s(T^*_theta)=1/theta` when `theta in (1/2,1)`.

## Proof Idea

The source question asks whether the familiar `c_0` long-support construction
forcing symmetric `2`-separation transfers through the weaker information that
`c_0` appears only as a spreading model. Russo shows that it does not. The
original Tsirelson spaces have only `c_0` spreading models, but their asymptotic
`c_0` geometry still bounds ordinary separated sequences from above. For
`theta > 1/2`, the bound is `1/theta`, strictly below `2`.

## Limitations

- This is a status packet, not an original solution from this run.
- It answers Problem 5.11 only. It does not answer the broader Problem 5.12
  asking whether `K^s(X) >= K^s(Z)` for arbitrary spreading models `Z` of `X`.
- It does not claim a new estimate beyond Russo's published theorem.

## Files

- `README.md`: this packet summary.
- `main.tex`: literature-status packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original open-problem paper.
- `supporting_paper_1904.12598.pdf`: later paper answering the problem.
- `figures/open_problem_crop.png`: source Problem 5.11 crop.
- `figures/supporting_negative_identification_crop.png`: explicit negative
  identification crop.
- `figures/supporting_theorem_b_crop.png`: Theorem B crop.
- `figures/supporting_tsirelson_theorem_crop.png`: Theorem 4.2 crop.
- `tmp/`: LaTeX build intermediates.

## Verification And Search Notes

Before packaging, the run lightweight indexes were searched for
`1711.05149`, the title phrase, `symmetrically separated`, `spreading model`,
`c_0`, and `Kottman`; no existing exact packet or attempt for this problem was
found. A primary-source arXiv/web search for `Kottman constant spreading model
c0` found Russo's arXiv:1904.12598 as an exact match.

## Human Review Recommendation

Treat Problem 5.11 from arXiv:1711.05149 as already answered negatively by
arXiv:1904.12598. Do not count this as a new run proof; keep it as
literature-status memory to avoid duplicate work on the same question.
