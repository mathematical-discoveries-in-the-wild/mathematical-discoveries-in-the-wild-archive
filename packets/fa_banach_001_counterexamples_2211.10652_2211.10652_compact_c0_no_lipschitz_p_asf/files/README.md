# Counterexample: a compact c0 subset with no Lipschitz p-ASF

Status: `counterexample`

Source problem paper: K. Mahesh Krishna and P. Sam Johnson, *Lipschitz p-Approximate Schauder Frames*, arXiv:2211.10652.

## Target

Problem 3.1(1) asks for a classification of subsets of Banach spaces that have a Lipschitz p-approximate Schauder frame for some `1 <= p < infinity`, and in particular asks whether every subset of a Banach space has one.

## Result

No. There is a compact subset `M` of a Banach space isometric to `c0` such that `M` has no Lipschitz p-ASF for any finite `p`.

## Construction

Let `E_n = ell_infty^n` and let

```text
X0 = (direct sum_n E_n)_{c0}.
```

This is isometric to `c0`. Put `r_n = 2^{-n}` and place the compact ball `r_n B_{E_n}` in the `n`th coordinate block. Define

```text
M = {0} union union_n r_n B_{E_n}.
```

The radii tend to zero, so `M` is compact.

## Obstruction

If `M` had a Lipschitz p-ASF, its analysis map would be a bi-Lipschitz embedding of `M` into `ell^p`: the frame map is `theta_tau theta_f`, the synthesis operator is bounded, and the frame map has a Lipschitz inverse.

But `M` does not bi-Lipschitz embed into any `ell^p`, `1 <= p < infinity`. A hypothetical embedding restricts to uniformly distorted embeddings of all balls `B_{ell_infty^n}` into the same `ell^p`. Differentiating on the relative interior gives linear embeddings `ell_infty^n -> ell^p` with uniform distortion. Cotype `max(p,2)` of `ell^p` forces that distortion to grow at least like `n^{1/max(p,2)}`.

## Evidence

- `figures/open_problem_crop.png`: source Problem 3.1, PDF page 10.
- `source_paper.pdf`: local copy of arXiv:2211.10652.
- `solution_packet.pdf`: full proof packet.

## Scope

This answers the universal question in Problem 3.1(1) negatively, even for compact subsets of `c0`.

It does not classify all subsets with Lipschitz p-ASFs and does not settle Problem 3.1(2), whose representation property is weaker than the Lipschitz p-ASF structure.

## Novelty check

Local run indexes were searched for arXiv:2211.10652 and the core title/keyword phrases. External web/arXiv searches on June 16, 2026 found the source and adjacent frame papers, but no later solution to Problem 3.1 and no compact `c0` counterexample of this form.

## Human review notes

Recommended review focus:

- Check the lemma that Lipschitz p-ASFs force bi-Lipschitz embeddability into `ell^p`.
- Check compactness of the shrinking block bouquet.
- Check the Rademacher plus cotype obstruction for all finite `p`.
