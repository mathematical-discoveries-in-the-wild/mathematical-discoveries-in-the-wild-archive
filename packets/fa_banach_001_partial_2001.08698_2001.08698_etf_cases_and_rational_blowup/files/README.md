# ETF Cases and a Rational Blow-Up Reduction for Basso's Orthogonal Projection Question

Status: `partial_result_likely_valid`

Run: `fa_banach_001`  
Agent: `agent_lane_13`  
Source paper: Giuliano Basso, *Almost minimal orthogonal projections*, arXiv:2001.08698.

## Result

Basso's Question 1.1 asks whether, for every integer `n >= 1`, there is an
`n`-dimensional subspace `E subset ell_1^d` whose orthogonal projection is
minimal and has norm equal to the maximal real projection constant `Pi_n`.

This packet proves two partial advances:

1. If a real maximal equiangular tight frame exists in `R^n`, then Question 1.1
   has a positive answer for that `n`.
2. Consequently the question is positive for the concrete dimensions
   `n = 1, 2, 3, 7, 23`.
3. More generally, if Basso's weighted Chalmers-Lewicki maximizer can be chosen
   with rational diagonal weights, then Question 1.1 has a positive answer for
   that `n`.

The general all-`n` question is not solved here. The remaining obstruction is
exactly the arithmetic one: Basso's proof approximates the positive diagonal
weights by rational vectors; rationality would make the approximation an exact
finite blow-up.

## Files

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2001.08698.
- `supporting_paper_2206.09454.pdf`: local copy of the Deregowska-Lewandowska supporting paper.
- `figures/open_problem_crop.png`: crop of Basso's Question 1.1.

## Verification

The proof is algebraic. The ETF theorem reduces the question to Basso's
Proposition 1.4 by explicitly constructing an unweighted sign matrix that
attains Basso's supremum `A = Pi_n`. The rational-weight theorem checks that a
block blow-up of a weighted sign matrix has the scaled weighted matrix as its
nonzero block-constant compression, so Basso's unweighted supremum is attained.

Bounded novelty/literature checks:

- Cheap run indexes searched for `2001.08698`, `Almost minimal orthogonal projections`,
  `Pi_n`, `orthogonal projection`, and `maximal projection constants`.
- Local parsed source was inspected for Basso's Question 1.1, Theorem 1.3,
  Proposition 1.4, Lemma 3.7, and the blow-up argument in Section 5.
- Web searches used exact title and question phrases, plus `maximal ETF`,
  `Deregowska Lewandowska`, and `projection constants`.

Novelty confidence: modest. The ETF subcases are an explicit combination of
known ETF projection-constant results with Basso's Proposition 1.4. The
rational-weight reduction appears to be a clean exact version of the
approximation mechanism in Basso's proof.

## Limitations

This is not a full solution of Question 1.1. It proves an infinite-form
criterion and the known maximal-ETF dimensions, but does not prove that the
weighted maximizers have rational weights for every `n`, nor that a real
maximal ETF exists in every dimension.
