# Explicit Gaussian constants for unconditional multiplier rescaling

Status: `partial_result_likely_valid`; `quantitative_strengthening_of_literature_answer`; `human_review_recommended`.

Source paper: Peter Balazs, Daniel Freeman, Roxana Popescu, and Michael
Speckbacher, *Quantitative bounds for unconditional pairs of frames*,
arXiv:2212.00947. Conjecture 1.2 is on PDF page 3.

Later literature boundary: Anton Tselishchev, *Rescaling of unconditional
Schauder frames in Hilbert spaces and completely bounded maps*,
arXiv:2508.02802. Theorem 2.2 resolves the finite quantitative conjecture
qualitatively. Its proof gives `K=2`; Remark 2.6(1) says Gaussian variables
give a better constant but does not evaluate it.

## Result

For complex Hilbert spaces and nonzero rank-one terms, the finite rescaling
conjecture holds with the explicit Bessel constant

```text
kappa = 4/pi.
```

For completely general finite data, including irrelevant terms with one zero
vector and a nonzero symbol, it holds with every `kappa > 4/pi`; in particular
`kappa = 3/2` is valid. The analogous real-Hilbert-space constant is `pi/2`
for nonzero terms and every larger constant in general.

The equivalent operator-space formulation receives the same explicit
improvement: every map `Phi: l_infinity^N -> B(H)` whose coordinate images
have rank at most one satisfies

```text
||Phi||_cb <= (4/pi) ||Phi||.
```

The proof has two ingredients. Complex Gaussian averaging converts the
unconditional multiplier estimate into

```text
sum_j sqrt(Tr(rho P_j) Tr(sigma Q_j)) <= (4/pi) C
```

for all density matrices `rho,sigma`. A coercive convex minimization over
logarithmic weights then produces maximizing density matrices for which the
two quantities under each square root balance coordinate by coordinate. At
that minimizer, both Bessel bounds are exactly the same Hellinger-type sum and
are therefore at most `(4/pi)C`.

This is not presented as a new qualitative solution: arXiv:2508.02802 already
settles the original conjecture. The candidate contribution is the explicit
constant and direct convex-balancing proof. The supporting paper itself flags
the Gaussian improvement but leaves the value and optimal constant beyond its
scope, so novelty confidence is moderate rather than high.

## Files

- `main.tex`: complete proof and literature-boundary note.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original open-problem paper.
- `supporting_paper_2508.02802.pdf`: later qualitative solution.
- `figures/open_problem_crop.png`: source screenshot of Conjecture 1.2.
