# Least-Atom Hypercontractivity Conjecture

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Jie Cao, Shilei Fan, Yong Han, Yanqi Qiu, and Zipeng Wang, “The optimal
  hypercontractive constants for Z_3 and biased Bernoulli random variables,”
  arXiv:2602.17248v2 (2026).
- Conjecture location: page 8, after Figure 3.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The packet proves that the exact biased Bernoulli constant
`sigma_{p,q}(lambda)` is strictly increasing for every `1 < p < q < infinity`
and `0 < lambda <= 1/2`. Wolff’s Theorem 3.1 then collapses his general
finite-space sandwich to equality: every finite probability measure with
least atom `lambda` has constant exactly `sigma_{p,q}(lambda)`.

The key new identity is the envelope derivative

```text
d/da log sigma = (K_p(x) - K_q(y))/a,
a = lambda/(1-lambda).
```

After logarithmic coordinates, `K` is controlled by
`h(u) = (u/2)coth(u/2)`. The second critical equation forces the two
coordinates to cross, and the fact that `h` is increasing and convex gives
the strict sign. Duality handles exponents below 2.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: the source arXiv paper.
- `supporting_paper_wolff_2007.pdf`: the decisive Wolff theorem used in the
  last step.
- `figures/open_problem_crop.png`: full-width crop of the source conjecture.
- `code/verify_derivative.py`: symbolic identity checks and numerical stress
  tests; these are not part of the proof.
- `verification.md`: verifier output and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

Bounded web searches on July 21, 2026 used the exact source title and close
variants of “sigma p q lambda monotonicity,” “biased Bernoulli
hypercontractivity,” and “least atom conjecture.” They found the source paper,
Wolff’s paper, and background material, but no independent proof of the
monotonicity or the finite-space conjecture. The run’s cheap indexes also had
no prior result for arXiv:2602.17248. Novelty confidence is moderate pending a
specialist search.

## Human review focus

Please check:

- the envelope/Danskin passage from the source paper’s exact critical formula
  to strict global monotonicity;
- the algebraic derivative identity in Lemma 1;
- the coordinate-crossing implication `A > C` and `B < D`;
- the reversal of exponent order when translating Wolff’s Theorem 3.1.
