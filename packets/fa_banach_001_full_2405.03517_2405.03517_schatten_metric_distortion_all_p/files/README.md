# Sharp Schatten metric distortion for all `p >= 1`

Status: **candidate full solution -- likely valid, pending human review**.

Source: Francisco Escudero Gutierrez and Garazi Muguruza, *All `S_p`
notions of quantum expansion are equivalent*, arXiv:2405.03517v1,
Question 2 in Section 3.2 (PDF pages 4--5).

## Result

Let `D_{n,S_p}` be the least distortion sufficient to embed every `n`-point
metric space into the Schatten class `S_p`. The packet proves, with universal
implicit constants,

```text
D_{n,S_p} = Theta(max{1, log(n)/p})       for every 1 <= p < infinity.
```

This answers Question 2 throughout its stated range, including the trace-class
endpoint `p=1`.

The graph estimates used for the lower bound are

```text
h_tilde_{S_p}(G) >= (delta(G)/K)^(1/p),   1 <= p <= 2,
h_tilde_{S_p}(G) >= delta(G)/(14p),       2 <= p < infinity,
```

where `K` is universal and `delta(G)` is the normalized adjacency spectral
gap. On fixed-gap expanders the first bound is uniform on `[1,2]` and the
second has the needed `1/p` dependence.

## Proof intuition

For `p >= 2`, the lazy random walk is interpolated on the noncommutative scale
`L_p(V;S_p)`. Taking `k=O(p/delta)` makes its centered `k`-step operator a
strict contraction. Centering, Jensen, and a path estimate convert this to the
one-step graph inequality.

The endpoint range uses a different idea. Translate a map `f:V -> S_p` at a
vertex `o` chosen so that its radial `p`-moment is at most the full pairwise
energy. Apply the noncommutative Mazur map

```text
M_{p,2}(x) = u |x|^(p/2)
```

to obtain an `S_2`-valued map. Ricard's estimates give a forward Holder bound
and an inverse Lipschitz bound with radial weight `r^(2-p)`. A weighted Holder
calculation shows that, on average, the inverse-weighted squared distances
retain at least half of the original `p`-energy. Hilbert Poincare then closes
the estimate uniformly down to `p=1`.

## Packet contents and verification

- `main.tex` and `solution_packet.pdf`: complete theorem statements and proof.
- `verification.md`: independent endpoint, normalization, and dependency
  audit.
- `code/check_constants.py`: exact scalar/weighted checks and finite
  matrix-valued consistency tests. It is not used as proof.
- `source_paper.pdf`: the source paper containing Question 2.
- `supporting_paper_1407.8334.pdf`: Ricard's quantitative noncommutative
  Mazur-map theorem, the decisive external input.
- `figures/open_problem_crop_page4.png` and
  `figures/open_problem_crop_page5.png`: genuine crops from the source PDF.

Run the checks with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2405.03517_schatten_metric_distortion_all_p/code/check_constants.py
```

The most important human-review point is the uniformity of the constants in
Ricard's Mazur estimates for `M_{p,2}` and `M_{2,p}` as `p` varies in `[1,2]`.
This follows from the quantitative constants in his proof (fixed target `2`
in the forward direction and ratio `2/p <= 2` in the inverse direction).

## Scope and novelty

The metric-distortion question is fully settled by the candidate proof. The
packet does not prove the stronger graph-by-graph comparison suggested in the
source when the spectral gap tends to zero.

A bounded run-index and arXiv/web novelty search was performed on 2026-07-19
using the source arXiv id and title, `D_{n,S_p}`, Schatten distortion,
trace-class metric embedding, noncommutative Mazur maps, and graph-Poincare
terms. Ricard's arXiv:1407.8334, Mendel--Naor's arXiv:1207.4705, and related
Schatten nonembedding papers were checked. No later paper explicitly settling
Question 2 or its `S_1` endpoint was found. Novelty confidence is moderate
because the search was bounded rather than exhaustive.
