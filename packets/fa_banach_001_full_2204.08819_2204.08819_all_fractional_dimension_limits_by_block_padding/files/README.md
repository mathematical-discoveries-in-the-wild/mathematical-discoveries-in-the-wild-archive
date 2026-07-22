# All fractional-dimension limits by block padding

**Source:** G. Chiribella, K. R. Davidson, V. I. Paulsen, and M. Rahaman, *Counterexamples to the extendibility of positive unital norm-one maps*, arXiv:2204.08819.

**Status:** `candidate_full_solution_likely_valid`

## Outcome

The source paper asks whether the fractional dimension of an operator system supporting one of its non-extendible positive maps is subject to bounds. In the unrestricted formulation, there is no nonzero universal lower bound and no universal upper bound below one. More strongly, every number in \([0,1]\) is an asymptotic fractional-dimension limit.

The construction starts with the paper's complex example

\[
\Gamma_2:\mathcal T_2\longrightarrow M_4(\mathbb C),
\qquad \dim_{\mathbb C}\mathcal T_2=7,
\]

which is a positive unital isometry with no positive extension to \(M_4(\mathbb C)\). For integers \(r\geq 1\) and \(k\geq 0\), take \(r\) block-diagonal copies of \(\mathcal T_2\), append one unrestricted \(M_k(\mathbb C)\) block, and apply \(\Gamma_2\) on the first \(r\) blocks and the identity on the last. The new map remains a positive unital isometry and remains non-extendible. Its fractional dimension is

\[
\delta_{r,k}=\frac{7r+k^2}{(4r+k)^2}.
\]

- With \(k=0\) and \(r\to\infty\), \(\delta_{r,0}\to0\).
- With \(r=1\) and \(k\to\infty\), \(\delta_{1,k}\to1\).
- Given \(0<\theta<1\), put \(\lambda=4\sqrt\theta/(1-\sqrt\theta)\) and \(k_r=\lfloor\lambda r\rfloor\). Then \(\delta_{r,k_r}\to\theta\).

Any positive extension of the padded map would, after embedding into and compressing out of the first \(4\times4\) corner, give a positive extension of \(\Gamma_2\), which is impossible.

## Why this is a full answer

Both the arXiv manuscript and the published journal version ask the question without imposing irreducibility, generation, indecomposability, or a fixed ambient size. The construction meets every stated requirement: its domain is an operator system in a full matrix algebra; its map is positive, unital, and norm one (indeed isometric); and it has no positive extension. Since the resulting densities have all of \([0,1]\) as their limit-point set, only the trivial universal asymptotic bounds remain. This is therefore a complete negative answer to the question as stated.

The block-diagonal nature of the construction suggests a separate strengthened problem: require the operator system to generate its entire ambient matrix algebra, act irreducibly, or satisfy a fixed finite-dimensional extremal condition. Those hypotheses do not occur in the source question and are not needed for the full result recorded here.

## Files

- `solution_packet.pdf` — review-ready statement, proof, scope analysis, and novelty search.
- `main.tex` — packet source.
- `figures/open_problem_crop.png` — source-paper crop showing the question and its dimension context.
- `code/check_density_limits.py` — numerical sanity check for the limiting formula.
- `source_paper.pdf` — the arXiv source used for page verification.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python code/check_density_limits.py
```

The script is only a numerical check; the proof is the block-compression argument in the packet.
