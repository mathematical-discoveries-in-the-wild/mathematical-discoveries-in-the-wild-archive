# Literature-Implied Answer: Finite Games Requiring Infinite-Dimensional Entanglement

Status: `literature_implied_answer (Open Problem 5.2)`

Source question: Carlos Palazuelos and Thomas Vidick, "Survey on Nonlocal Games
and Operator Space Theory", arXiv:1512.00419. Section 5.4.1, page 42, Open
Problem 5.2 asks whether there exists a multiplayer game `G` whose entangled
value `omega^*(G)` is attained only in the limit of infinite-dimensional
entanglement.

Identification: the question is answered by later finite nonlocal-game
constructions.

- William Slofstra, "The set of quantum correlations is not closed",
  arXiv:1703.08618, constructs a finite linear-system nonlocal game that can be
  played perfectly as a limit of finite-dimensional quantum strategies but not
  perfectly by any finite-dimensional Hilbert-space strategy, or even any
  tensor-product strategy. Theorem 1.1 states the corresponding finite
  nonlocal-game separation.
- Zhengfeng Ji, Debbie Leung, and Thomas Vidick, "A three-player coherent state
  embezzlement game", arXiv:1802.04926, gives an especially direct finite
  three-player classical-question-answer game. Its abstract and Theorem 1 state
  that the optimal success probability 1 is achievable only in the limit of
  strategies using arbitrarily high-dimensional entangled states.

Why this is `literature_implied_answers`: the later papers do not appear, from
the checked abstracts and local excerpts, to explicitly label their result as a
resolution of Palazuelos--Vidick Open Problem 5.2. The implication is direct
after identifying their games as standard finite nonlocal games.

Scope limitations:

- This packet answers only Open Problem 5.2 from arXiv:1512.00419.
- It does not answer Open Problem 5.3, which asks for an explicit uniform
  dimension bound `d(epsilon,n)` for approximating the entangled value of
  arbitrary games with at most `n` questions and answers per player.
- This is not a new proof or counterexample produced by the run; it is a
  literature-status packet to prevent repeating an already-settled target.

Packet contents:

- `main.tex` and `solution_packet.pdf`: compact status note.
- `source_paper.pdf`: Palazuelos--Vidick source survey.
- `supporting_paper_1703.08618.pdf`: Slofstra answer source.
- `supporting_paper_1802.04926.pdf`: Ji--Leung--Vidick answer source.
- `figures/open_problem_crop.png`: source-page crop of Open Problems 5.2 and
  5.3.

Ledger: `runs/fa_banach_001/ledger/results/1512.00419_finite_game_infinite_entanglement_slofstra_jlv.json`.
