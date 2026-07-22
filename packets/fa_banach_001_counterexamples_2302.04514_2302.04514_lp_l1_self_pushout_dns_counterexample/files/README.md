# A self-push-out counterexample to Question 1 of arXiv:2302.04514

Status: `candidate_counterexample_likely_valid`

Source: Manuel González and Antonio Martinón, *Disjointly non-singular
operators: Extensions and local variations*, arXiv:2302.04514; Journal of
Mathematical Analysis and Applications 530 (2024), 127685, DOI
10.1016/j.jmaa.2023.127685. Question 1 is on source PDF page 8.

## Negative answer

Fix `1 < p < infinity`. Let

\[
E=L_p[0,1],\qquad Y=L_1[0,1],\qquad T=j:L_p[0,1]\hookrightarrow L_1[0,1]
\]

be the canonical inclusion used in the paper's Köthe representation.
Then `E` is order continuous and has the weak unit `1`.

The operator `T` is not disjointly non-singular. On the disjoint sets
`A_n=(2^{-n},2^{-n+1}]`, the vectors

\[
x_n=2^{n/p}\mathbf 1_{A_n}
\]

have `L_p` norm one but `||Tx_n||_1=2^{-n(1-1/p)}`. In fact, `T` is compact
on their closed span, so its restriction there is strictly singular.

For the push-out pair `(j,T)=(j,j)`,

\[
\overline\Delta=\{(g,-g):g\in L_1\}
   \subset L_1\oplus_1L_1.
\]

The map

\[
[(a,b)]\longmapsto a+b
\]

identifies the push-out isometrically with `L_1`. Under this identification,
the extension `bar(T)` is exactly the identity on `L_1`, hence is
disjointly non-singular. Thus

\[
\overline T\in DN\!\operatorname{-}S
\quad\not\Rightarrow\quad
T\in DN\!\operatorname{-}S.
\]

The other push-out arrow `bar(j)` is also the identity under this
identification, so this is a genuine extension, not a degenerate failure of
injectivity.

## Verification and novelty

- The quotient norm is exactly `||a+b||_1`: the triangle inequality gives the
  lower bound, and choosing the anti-diagonal correction `g=a` gives equality.
- The compactness calculation on `[x_n]` is explicit and included in the PDF.
- No numerical or unproved dependency is used.
- A bounded search on 2026-07-21 covered the run registry and packet indexes,
  the local source corpus, the exact wording of Question 1, the title and
  authors, and web searches for the push-out implication. The 2024 journal
  version retains Question 1, but no later answer was found. This is not an
  exhaustive novelty claim.

Recommended human review: verify only that the paper's sign convention for
`Delta` and its quotient-by-closure convention match the displayed
anti-diagonal calculation.

Ledger:
`runs/fa_banach_001/ledger/results/2302.04514_lp_l1_self_pushout_dns_counterexample.json`.

