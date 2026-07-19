# Candidate Full Result: Random-Semigroup SLLN on All Banach Spaces

- **Run:** `fa_banach_001`
- **Agent:** `agent_lane_11`
- **arXiv:** `2507.07658`
- **Source paper:** S. V. Dzhenzher and V. Zh. Sakbaev, *The Strong Law of Large Numbers for random semigroups on uniformly smooth Banach spaces*
- **Source location:** Conjecture 2.6, page 4
- **Status:** `candidate_full_solution_likely_valid_needs_human_review`

## Claim

Conjecture 2.6 is true.  If `X` is any Banach space and
`A, A_1, A_2, ...` are i.i.d. bounded Bochner-measurable random elements of
`L(X)`, then for every `x in X` and `T > 0`,

```tex
\sup_{0\le t\le T}
\|(e^{A_1t/n}\cdots e^{A_nt/n}-e^{(\mathbb E A)t})x\|
\to 0
```

almost surely.  Uniform smoothness of `X` is not needed.

## Proof Sketch

The proof replaces the exponential product by the Euler product
`prod_j (I + (t/n)A_j)`, with `O(1/n)` error uniformly on compact `t`
intervals.  The Euler product is compared to the deterministic Euler product
for `\bar A = E A`.  The error recursion is driven by mean-zero terms
`(t/n)(A_j-\bar A)y_{n,j}` where the deterministic points `y_{n,j}` stay on a
compact curve.  A finite partition of that curve reduces the noise estimate to
finitely many ordinary Banach-valued SLLNs on intervals of indices.  Abel
summation then turns small noise partial sums into small product error, and a
uniform Lipschitz estimate in `t` upgrades rational-time convergence to
uniform convergence on `[0,T]`.

## Files

- `main.tex` - source for the solution packet
- `solution_packet.pdf` - compiled packet
- `source_paper.pdf` - downloaded arXiv source paper
- `figures/open_problem_crop.png` - crop of page 4 containing Conjecture 2.6
- `code/matrix_smoke.py` - finite-dimensional numerical smoke check

## Verification

- Compiled with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

- Smoke check command:

```sh
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/full/2507.07658_random_semigroup_slln_all_banach/code/matrix_smoke.py
```

Observed grid errors:

```text
n=  50 grid_sup_error=0.118950
n= 100 grid_sup_error=0.116373
n= 200 grid_sup_error=0.059650
n= 400 grid_sup_error=0.014226
n= 800 grid_sup_error=0.018669
```

The numerical check is not used as evidence for the proof; it only checks the
finite-dimensional scaling and product orientation.

## Novelty Check

Local lightweight indexes were searched for `2507.07658`, the title, `random
semigroups`, `strong law of large numbers`, `SOT`, and related Banach-space
phrases.  No prior packet or attempt for this conjecture was found.

Web searches on 2026-06-26 for the exact title, `Conjecture 2.6 random
semigroups Banach space`, `SLLN in SOT random semigroups Banach space`, and
nearby variants found the source arXiv paper and a 2026 follow-up by the same
authors on unbounded generators in uniformly smooth Banach spaces, but no
paper resolving the bounded-generator conjecture for arbitrary Banach spaces.

## Review Notes

Human review should focus on:

- Lemma 2, the compact-curve interval SLLN, especially the reversed-index
  interval reduction;
- Lemma 3, the Abel summation estimate for the Euler-product error.

The packet does not address the separate question in the source discussion of
whether the i.i.d. assumption can be weakened to merely independent uniformly
bounded generators with a common expectation.
