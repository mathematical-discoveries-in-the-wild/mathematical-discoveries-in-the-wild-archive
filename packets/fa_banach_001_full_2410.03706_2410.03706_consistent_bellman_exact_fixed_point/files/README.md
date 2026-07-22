# Exact fixed-point formula for the consistent Bellman operator

Status: `full` (claimed exact quantitative answer; human review required).

Source: Krame Kadurha David, *Topological Foundations of Reinforcement
Learning*, arXiv:2410.03706 (2024), Chapter 5, Section 5.1.2, printed page 34
(PDF page 38).

The source asks how the unique fixed point of the consistent Bellman operator
relates to the classical Bellman fixed point. For a finite discounted MDP, let
`Q*` be the classical optimal Q-function, `V*(s)=max_a Q*(s,a)`, let `Qc` be
the consistent fixed point, and put `d(s,a)=P(s|s,a)`. The packet proves

`V*(s)-Qc(s,a) = (V*(s)-Q*(s,a))/(1-gamma*d(s,a))`.

This completely determines `Qc` from `Q*` and the self-transition
probabilities. In particular:

- `max_a Qc(s,a)=V*(s)`;
- `argmax_a Qc(s,a)=argmax_a Q*(s,a)` exactly, including ties;
- each action gap is multiplied by `1/(1-gamma*d(s,a))`;
- `Qc(s,a)<=Q*(s,a)`, with strict inequality precisely for a suboptimal
  action having positive self-loop probability.

The proof introduces a value-level ``self-loop-eliminated'' operator. Its
actionwise Lipschitz coefficient is
`gamma*(1-d)/(1-gamma*d)<=gamma`, hence it is a contraction. The classical
optimal value is its fixed point, which identifies the maximum of `Qc`; the
coordinate formula then follows by isolating the self-loop term.

Literature boundary: Bellemare, Ostrovski, Guez, Thomas, and Munos,
*Increasing the Action Gap: New Operators for Reinforcement Learning*,
arXiv:1512.04860 / AAAI 2016, Corollary 3, already prove the qualitative
optimality-preserving and gap-increasing properties. The inspected paper does
not state the coordinatewise formula above. The novelty claim is deliberately
limited to this explicit identity and its exact consequences; the search was
bounded, not exhaustive.

Artifacts:

- `solution_packet.pdf`: full proof packet;
- `source_paper.pdf`: original target paper;
- `supporting_paper_1512.04860.pdf`: qualitative predecessor;
- `figures/open_problem_crop.png`: mandatory source-question screenshot;
- `code/check_random_mdps.py`: 400-instance randomized finite-MDP check.

The randomized check passed with worst direct formula error
`1.08e-11`, worst consistent fixed-point residual `2.07e-13`, and exact
max-value agreement to displayed floating-point precision.

Human review should focus on the value-level contraction reduction and on the
scope: the theorem is stated for finite state and action spaces, matching the
source's tabular sums and attained maxima.

