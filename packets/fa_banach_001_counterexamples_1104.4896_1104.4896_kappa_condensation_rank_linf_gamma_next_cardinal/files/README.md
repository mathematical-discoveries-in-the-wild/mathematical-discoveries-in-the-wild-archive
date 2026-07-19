# Counterexample packet: cardinal condensation rank of `l_infty(Gamma)`

Status: `counterexample_likely_valid`

Source: Majid Gazor, *Condensation rank of injective Banach spaces*,
arXiv:1104.4896.

## Claim

The final problem in the source paper asks whether, for
`kappa = 2^{|Gamma|}`, the `kappa`-condensation rank of
`l_infty(Gamma)` is the first ordinal of cardinality `kappa`.

Under the natural nontrivial convention

```text
x is a kappa-condensation point of A
iff every neighbourhood of x meets A in at least kappa points,
```

the proposed equality is false. In fact, for every infinite `Gamma`,

```text
CR_kappa(l_infty(Gamma)) = omega_{kappa^+},
```

where `omega_mu` denotes the initial ordinal of cardinality `mu`.

## Idea

The upper bound is cardinal: a strictly decreasing derivative chain in a set of
cardinality `kappa` cannot have `kappa^+` many strict successor drops.

The lower bound uses the pairwise distance-one family `{0,1}^Gamma` in
`l_infty(Gamma)`, which has cardinal `kappa`. This lets us build rank blocks by
transfinite induction:

- a singleton has height `1`;
- separated sums over cofinal earlier ranks handle limit ordinals;
- shrinking fans with `kappa` copies of a rank-`alpha` block force a new root
  point to survive exactly one derivative longer.

Thus subsets of `l_infty(Gamma)` realize every `kappa`-condensation height
below `omega_{kappa^+}`, so the supremum is `omega_{kappa^+}`, not
`omega_kappa`.

## Files

- `main.tex` - self-contained proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv source paper.
- `figures/open_problem_crop.png` - crop of the final problem in the source
  paper.

## Novelty check

Cheap run indexes showed no prior packet for `1104.4896`. A bounded web search
for the exact cardinal condensation-rank terms found only the original arXiv
paper and no later answer.

## Review focus

The main proof points to check are:

- the separated-union derivative identity at limit ordinals;
- the fan lemma, especially that no cross-component condensation points appear
  away from the root;
- the convention for `kappa`-condensation. If one used "strictly more than
  `kappa` points" while `kappa=|l_infty(Gamma)|`, the derivative is trivially
  empty and the source equality fails for a different, degenerate reason.
