# Pure ell_1-SVM under independent random label flips

Status: `partial_result_likely_valid`

Run: `fa_banach_001`

Agent: `agent_lane_02`

## Source question

Anton Kolleck and Jan Vybiral, *Non-asymptotic Analysis of ell_1-norm
Support Vector Machines*, arXiv:1509.08083, Section VI (Discussion), PDF
page 15, asks for the behavior of ell_1-SVM when labels have a small
probability of disagreeing with the true Gaussian halfspace labels. The same
paragraph asks whether the sample dependence on the accuracy and Gaussian
scale is optimal.

The exact source passage is reproduced in `figures/open_problem_crop.png`.

## Candidate partial theorem

Let `a in R^d` satisfy `||a||_2=1` and `||a||_1 <= R`. Draw
`x_i = r g_i`, with `g_i` standard Gaussian, and independently flip each true
label with correct-label probability `p in (1/2,1)`:

```text
y_i = xi_i sign(<g_i,a>),   P(xi_i=1)=p.
```

Minimize the ordinary empirical hinge risk over the source's unmodified
ell_1 ball `K=R B_1^d`. Put

```text
c_p = sqrt(2 log(p/(2p-1))),   mu = 1/(r c_p).
```

If `mu ||a||_1 <= R`, then:

1. the population hinge risk has the unique global minimizer `mu a` on all of
   `R^d`, hence also on `K`;
2. every empirical minimizer over `K` converges in direction to `a`, with an
   explicit finite-sample probability bound in terms of a strictly positive,
   two-dimensional population separation modulus.

Thus independent symmetric label errors below 50 percent do not rotate the
population classifier in the Gaussian model. Once the noise-selected optimal
scale lies in the ell_1 constraint, the original pure ell_1-SVM is
directionally consistent without adding the paper's proposed ell_2
constraint.

## Proof intuition

After decomposing a candidate as `w=u a+v`, Gaussian rotation invariance turns
the signed margin into

```text
r (u |G| + ||v||_2 Z),
```

with independent standard Gaussians `G,Z`. The noisy conditional hinge loss is
convex and has kinks at `-1` and `1`. Jensen's inequality therefore says that
every nonzero orthogonal component `v` strictly raises population risk. The
remaining one-dimensional risk has an explicitly differentiable profile; its
unique critical point is `mu` above. The source paper's uniform hinge-risk
concentration proof survives random flips unchanged because every label is
still a sign and can be absorbed into the auxiliary Rademacher variables.

## Later-literature boundary

Martin Genzel and Alexander Stollenwerk, *Robust 1-Bit Compressed Sensing via
Hinge Loss Minimization*, arXiv:1804.04846, gives a stronger quantitative
`m^{-1/2}` noisy recovery theorem when the constraint set lies in the Euclidean
unit ball. Its Example 3.4(2) and Proposition 3.5 cover independent random bit
flips and compute the correlation parameter `(2p-1)sqrt(2/pi)`. The paper
explicitly cites Kolleck--Vybiral as a special case and improvement.

However, the supporting paper restricts its noisy theorem to `K subset B_2`
and says that the noisy arbitrary-convex-set extension is not straightforward.
The present theorem instead treats the source's pure `R B_1^d` constraint,
which need not lie in `B_2`, at the cost of an implicit separation modulus.

## Scope and limitations

- This is a partial answer to the broad source question, not a full noisy-SVM
  theory.
- Flips are independent and symmetric with a fixed probability below one
  half. Adversarial, feature-dependent, and asymmetric corruptions are not
  covered.
- The theorem requires the noise-selected scale `mu a` to be feasible.
- The finite-sample rate is expressed through a positive population
  separation modulus and is not claimed optimal in `p`, `r`, or accuracy.
- The source's non-Gaussian measurement-distribution question is untouched.

## Novelty search

The cheap run indexes were searched for arXiv:1509.08083, the title, ell_1-SVM,
hinge loss, label noise, and random bit flips; no existing row was found.
Bounded primary-source web searches covered exact combinations of
`random bit flips`, `ell_1-SVM`, `hinge loss`, `Gaussian`, and
`symmetric label noise`. They found arXiv:1505.07634 and arXiv:1804.04846 but
no exact pure-ell_1 population-minimizer or finite-sample theorem with the
formula above. Novelty is therefore plausible, not certified.

## Files

- `main.tex`: theorem, proof, literature boundary, and limitations.
- `solution_packet.pdf`: rendered review packet.
- `verification.md`: independent proof-structure and scope checks.
- `source_paper.pdf`: arXiv:1509.08083.
- `supporting_paper_1804.04846.pdf`: decisive later context.
- `figures/open_problem_crop.png`: source question on PDF page 15.

## Human review recommendation

Prioritize two points: confirm that the source's uniform concentration proof
indeed uses only the sign-valued nature of the labels, and search citations of
arXiv:1804.04846 for an existing arbitrary-convex noisy hinge theorem. The
population minimizer calculation itself is elementary and fully explicit.
