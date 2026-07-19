# Full Packet: The Qubit Four-Measurement Lower Bound is Not Optimal

Run: `fa_banach_001`
Agent: `agent_lane_13`
Status: claimed full negative answer to Question 12.1; needs human review

## Source

- Paper: Andreas Bluhm, Anna Jencova, Ion Nechita, "Incompatibility in general probabilistic theories, generalized spectrahedra, and tensor norms"
- arXiv: `2011.06497`
- Source target: Question 12.1 asks whether the lower bound `gamma(g; QM_2) >= 1/2` is optimal for finite `g >= 4`, equivalently whether equality already occurs at `g = 4`.

## Result

The lower bound is not attained at `g = 4`, and there is an explicit sharper upper bound:

```text
1/2 < gamma(4; QM_2) <= 2/sqrt(13) < 1/sqrt(3).
```

Thus the pointwise equality scenario in Question 12.1 is false.  This is a full negative
answer to the stated equality/optimality question.  The exact value of `gamma(4; QM_2)` is
still not determined by this packet, though the hard-push numerics strongly suggest the
candidate value `2/sqrt(13)`.

## Idea

For the Bloch-ball/qubit GPT, the source paper reduces `gamma(4; QM_2)` to a Banach-space
tensor-norm ratio for `ell_2^3`.  Equivalently,

```text
gamma(4; QM_2)
 = inf max_{eps_i = +/-1} ||sum eps_i z_i||_2 / sum ||z_i||_2,
```

where the infimum ranges over nonzero four-tuples in `R^3`.

If equality `1/2` were attained, then after normalizing `sum ||z_i||_2 = 1`, the Rademacher
second-moment identity would force all four vectors to have length `1/4` and every signed
sum to have norm exactly `1/2`.  Expanding the squared signed sums then forces all pairwise
inner products to vanish, i.e. four nonzero pairwise orthogonal vectors in `R^3`, impossible.

For the upper bound, take three vectors of length `3/(2 sqrt(13))` in a plane at angles
`0, 120, 240` degrees, and take a fourth orthogonal vector of length `2/sqrt(13)`.  The
largest signed sum has norm `1`, while the total generator length is `sqrt(13)/2`, giving
`gamma(4; QM_2) <= 2/sqrt(13)`.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: compiled packet
- `source_paper.pdf`: original arXiv PDF
- `figures/question_12_1_crop.png`: crop of the source question

## Scope

This answers the finite-attainment/equality part of Question 12.1 negatively at `g=4`.
It does not compute the exact value of `gamma(4; QM_2)`, nor does it rule out finite `g>4`
having values arbitrarily close to `1/2`.  The source already proves that the infimum over
all `g` and the limit as `g -> infinity` equal `1/2`.

Separate attempt note:

- `../../../attempts/2011.06497_qubit_gamma4_exact_value_push.md`: literature/direct-attack log
  for the conjectural exact value `2/sqrt(13)`.

## Literature and Novelty Check

Bounded index and web/literature searches covered the arXiv id, source title, `QM_2`,
`gamma(4)`, compatibility degree phrases, four-qubit joint measurability phrases, vector
balancing, four-generator zonotopes in the Euclidean ball, and the corresponding
projective/injective tensor-norm phrasing.  No later explicit resolution of Question 12.1
or exact computation of `gamma(4; QM_2)` was found.

## Verification

Build command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

Human review should focus on the reduction from the source paper's Theorem 10.3/Equation
for centrally symmetric GPTs to the four-vector sign-sum formula.
