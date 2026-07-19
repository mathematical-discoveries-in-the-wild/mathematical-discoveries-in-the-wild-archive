# 2605.12930 inductive-limit reduction

Status: `partial_result`

Source paper: Geng Tian and Guoliang Yu, *Embedding complexity into Banach spaces and the strong Novikov conjecture*, arXiv:2605.12930.

Extracted question: after proving the strong Novikov conjecture for groups with finite complexity rate, the paper asks whether every countable discrete group is an inductive limit of groups with finite complexity rates.

Result in this packet: for the injective/direct-union interpretation of "inductive limit", the question for all countable groups is equivalent to the same question for finitely generated groups. More precisely, a countable group is a directed union of finite-complexity-rate subgroups if and only if each finitely generated subgroup has finite complexity rate. This follows from subgroup heredity of the complexity-rate condition and the standard direct-union description of a countable group by its finitely generated subgroups.

Scope and caveat: this does not prove that every countable group has the requested representation. It shows that the direct-union formulation does not reduce the problem below the finitely generated case. A naive attempt to use direct limits of free groups is also ruled out in the packet: filtered colimits of torsion-free groups are torsion-free, so finite cyclic groups already cannot arise that way.

Novelty/literature check: searched on 2026-06-16 for `2605.12930 finite complexity rates`, `Embedding complexity into Banach spaces inductive limit`, and `finite complexity rates inductive limit countable discrete group`; no later answer to the exact question was found. The packet claims only the elementary reduction stated above.

Files:
- `main.tex` / `solution_packet.pdf`: review packet.
- `source_paper.pdf`: local copy of arXiv:2605.12930.
- `figures/open_problem_crop.png`: crop of the source question from page 6.
