# Weighted tensor-grid subcase of the Schatten linear-KS question

Status: `candidate_partial_likely_valid`

Source: Assaf Naor and Gideon Schechtman, *Pythagorean powers of hypercubes*, arXiv:1501.05213v2; Annales de l'Institut Fourier 66 (2016), 1093-1116, DOI 10.5802/aif.3032.

Source location: arXiv PDF pages 3-4, equations (8) and (10), and the paragraph after Theorem 1.7. The authors ask whether the Schatten trace class \(S_1\) is a KS metric space, or even a linear KS space.

## Claimed contribution

The packet proves both source linear inequalities uniformly for every weighted tensor-grid array
\[
z_{jk}=a_{jk}u_jv_k^*\in S_1,
\]
where \((u_j)_{j=1}^n\) and \((v_k)_{k=1}^n\) are orthonormal families and the scalar weights \(a_{jk}\) are arbitrary.

- The original permutation inequality (source equation (8)) holds with constant \(1\).
- The modified linear-KS inequality (source equation (10)) holds with constant \(e\).

This is a solved noncommutative subcase, not a proof that all of \(S_1\) is linear KS. General arrays do not share the tensor-grid singular-vector structure used in the proof.

## Idea of the proof

Every within-row signed sum is rank one, so its trace norm is the Euclidean norm of that row of coefficients. A permutation transversal is a weighted partial isometry and its trace norm is the sum of the selected absolute weights. For the modified inequality, a selector with collisions decomposes into orthogonal column blocks; its singular values are the Euclidean norms of the occupied blocks. Keeping only the largest selected entry in each block and ordering the column weights gives a Bernoulli first-hit estimate. Since \((1-1/n)^{n-1}\ge e^{-1}\), this lower-bounds the selector average by \((en)^{-1}\sum_{j,k}|a_{jk}|\), which dominates \(e^{-1}\) times the row average.

## Verification

The proof is fully elementary after the singular-value formulas are established. The verifier report checks each step and isolates the scope limitation. `code/verify_tensor_grid.py` enumerates all selectors for \(1\le n\le5\) on randomized weighted grids, checks the two claimed bounds, and directly compares the selector formula with matrix SVDs in small dimensions. This code is a regression check, not part of the proof.

Run:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1501.05213_s1_tensor_grid_linear_ks/code/verify_tensor_grid.py
```

The broader heuristic search in `code/search_s1_ratio.py` optimized exact finite-dimensional KS ratios for unrestricted real matrix arrays at \(n=2,3,4,5\). The best ratios were approximately 1.401, 1.395, 1.397, and 1.418; this is only counterexample screening and gives no proof for general \(S_1\).

## Novelty and literature bounds

On 2026-07-19, the run searched its four lightweight indexes for arXiv:1501.05213, `linear KS`, `Schatten trace class`, and the embedding variants, with no matching packet or attempt. Exact web/arXiv phrase searches and a Semantic Scholar forward-citation query for DOI 10.5802/aif.3032 found no paper claiming to resolve the \(S_1\) linear-KS question. A 2018 Naor-Schechtman preprint cited as *Obstructions to metric embeddings of Schatten classes* and the authors' 2017-2018 slides concern the distinct upper-property-\(\alpha\) obstruction; they do not state the KS conclusion proved here. This was a bounded search, so novelty is not certified.

## Human-review recommendation

Review the selector singular-value formula and the first-hit estimate. If valid, retain as a narrow partial result and use it to rule out weighted matrix-unit grids as a source of counterexamples. The main \(S_1\) linear and metric KS questions remain open in this packet.

