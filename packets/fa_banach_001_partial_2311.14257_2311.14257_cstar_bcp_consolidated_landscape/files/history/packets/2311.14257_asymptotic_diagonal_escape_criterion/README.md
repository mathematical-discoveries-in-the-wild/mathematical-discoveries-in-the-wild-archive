# Asymptotic Diagonal Escape Criterion for Quotients

Status: `partial_criterion_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_asymptotic_diagonal_escape_criterion/`

## Result

This packet upgrades the previous exact adaptive diagonal criterion to a
quotient/asymptotic form.

Let `X = Y/J`. If every countable family of lifted centers `y_i` admits local
contractive maps `L_k : Y -> E_k`, assigned infinitely often to the centers,
such that:

- `L_k y_{pi(k)}` almost norms the quotient center;
- `J` vanishes along the assigned local maps;
- there is one global unit quotient class `q(y)` whose local images approximate
  chosen local escape vectors `u_k`;
- each `u_k` is locally far from `L_k y_{pi(k)}`;

then `X` fails BCP.

## Why This Matters

The exact criterion captured atomless von Neumann corners. This asymptotic
criterion captures the shape of quotient arguments, where the local maps are
not well-defined on the quotient but become well-defined along tails because
the ideal terms vanish.

This is the abstraction behind:

- sigma-unital multiplier coronas, via approximate-unit annuli;
- Hilbert-module coronas, via compact-vanishing block projections;
- reduced products, via disjoint positive coordinate refinements.

## Files

- `main.tex`: self-contained criterion packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a reusable quotient-level diagonal tool. The formal proof is short;
the key review point is whether the hypotheses isolate exactly the reusable
part of the sigma-unital corona and reduced-product arguments without hiding
the hard local construction inside the conclusion.
