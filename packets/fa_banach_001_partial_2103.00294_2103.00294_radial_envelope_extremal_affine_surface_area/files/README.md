# Radial-envelope extension for extremal general affine surface area

Status: `candidate_partial_likely_valid`

Source: Steven Hoehner, *Extremal general affine surface areas*, Journal of
Mathematical Analysis and Applications 505 (2022), article 125506,
arXiv:2103.00294v4.

Source location: Section 7.4, page 21. The source asks for extensions of the
article's results beyond the two classes for which
`phi(t)/sqrt(t)` is globally monotone. The exact source evidence is in
`figures/open_problem_crop.png`.

## Claimed contribution

For `h_phi(t)=phi(t)/sqrt(t)`, put

```text
L_phi = limsup_{t -> infinity} h_phi(t),
H_phi(a) = sup_{t >= a} h_phi(t).
```

If `L_phi` is finite and `H_phi(a) > L_phi` for every `a > 0`, then the inner
maximal general affine surface area `IS_phi(K)` is finite, is attained, and is
Hausdorff-continuous on centered convex bodies. It also satisfies the sharp
radial-envelope inequality

```text
IS_phi(K) <= n |B_n| H_phi(vrad(K)^(-2n)),
```

with equality for every centered Euclidean ball.

This tail-gap class contains Hoehner's entire decreasing-ratio class and is
strictly larger. In particular, it contains `phi(t)=log(1+t)`, whose ratio is
first increasing and then decreasing and hence lies in neither source class.
For this explicit function the packet gives the exact envelope and the unique
critical equation `log(1+t_*) = 2t_*/(1+t_*)`, with
`t_* approximately 3.9215536346`.

## Scope and limitations

This is a substantial partial answer, not a full solution of the source's
broad request for all results of the article. It extends finiteness,
attainment, continuity, and the affine-isoperimetric radial bound for the inner
maximal functional. The source's endpoint ball identity and its
Blaschke-Santalo equality characterization do not extend verbatim: for
`phi(t)=log(1+t)`, a smaller concentric ball maximizes inside `B_n`.

The proof also repairs the non-collapse step in the source existence proof.
Global strict decrease of `h_phi` does not force its limit to be zero (for
example, `phi(t)=sqrt(t)+t^(1/4)`); the needed fact is the strict gap between
the tail limit and an admissible finite-radius value.

## Novelty check

- Searched all four local run indexes by arXiv id, title, and the terms
  `extremal general affine surface area`, `inner maximal`, and `richer class of
  functions`; no duplicate result was found.
- Searched arXiv/web exact-title and exact-phrase variants through 2026-07-19.
- Inspected the journal page's three listed citing works: *Volume product*
  (2023), *Floating bodies for ball-convex bodies* (2025), and *New fiber and
  graph combinations of convex bodies* (2025). None states this tail-envelope
  extension.
- Inspected arXiv:2402.16130, *Extremal affine surface areas in a functional
  setting*; it studies a different functional construction and fixed
  power-parameter affine surface areas.

This is a bounded search, so absolute novelty is not certified.

## Packet contents

- `main.tex`: self-contained review note with theorem, proof, example, and
  verification notes.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: page-21 source crop.
- `verification.md`: explicit adversarial verification report.
- `code/check_log_example.py`: reproducible numerical check of the logarithmic
  critical point; it is not used as proof.

Human review recommendation: **send to a convex-geometric analyst**. The main
focus should be the use of the general affine isoperimetric inequality in the
non-collapse argument and whether the source's phrase "the results" warrants
promoting this as a partial rather than a full answer.

