# One-big-jump counterexample to the `p<2` subcritical MDP extension

Status: `candidate_counterexample_full_resolution_likely_valid`

Source: David Alonso-Gutiérrez, Joscha Prochno, and Christoph Thäle,
*Large deviations, moderate deviations, and the KLS conjecture*,
arXiv:2003.11442, Remark 1.1(c), page 5.

## Result

The final question in Remark 1.1(c) has a negative answer.  For every fixed
`1 <= p < 2`, take `k_n=floor(n/2)` and

`t_n = n^(1/(4-p))`.

These scales satisfy all hypotheses of the paper's subcritical Theorem C,
apart from its assumption `p>=2`.  Nevertheless, for the normalized projected
norm `X_{n,p}` from that theorem,

`lim t_n^(-2) log P(X_{n,p}/t_n >= 1) = 0`.

Thus no MDP with speed `t_n^2` and the proposed strictly positive quadratic
rate function can hold.

The mechanism is one large coordinate of the `p`-generalized Gaussian in the
paper's exact probabilistic representation.  Its cost is only
`exp(-C (t_n sqrt(n))^(p/2))`, which is subexponential on the proposed
`t_n^2` scale because `p<2`.

## Packet contents

- `main.tex` and `solution_packet.pdf`: full statement and proof.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: genuine page-5 crop of Remark 1.1(c).
- `code/check_scaling.py`: exact exponent and admissibility sanity checks.

## Human review focus

Please check the uniform-ball representation with the independent
`W ~ Exp(rate=1/p)` and the deterministic lower estimate on the event in
Step 2.  The probabilistic cost calculation is elementary and is the decisive
point.  The result resolves only the final `p<2` yes/no question in Remark
1.1(c); the two preceding supercritical/parameter-gap problems remain open.

Ledger:
`runs/fa_banach_001/ledger/results/2003.11442_p_less_than_2_subcritical_mdp_counterexample.json`.
