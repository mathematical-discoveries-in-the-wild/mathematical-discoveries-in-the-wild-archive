# Literature status: RV06 L-infinity entropy exponent question

Status: literature already answered.

Source paper: arXiv:math/0404192, Mark Rudelson and Roman Vershynin, *Combinatorics of random processes and sections of convex bodies*.

Later paper: arXiv:2605.13684, Shashaank Aiyer, Yishay Mansour, Shay Moran, Han Shao, and Tom Waknine, *Scale-Sensitive Shattering: Learnability and Evaluability at Optimal Scale*.

## Question identified

In Section 4 of the source paper, after Theorem 4.4 and the comparison with the Alon et al. L-infinity entropy bound, Rudelson and Vershynin state that their theorem improves the known `O(log^2 n)` behavior to `O(log^{1+epsilon} n)` and then ask whether the logarithmic exponent can be made `1`.

Local evidence:

- PDF page 21 of `source_paper.pdf`.
- TeX source line 1459 in `data/parsed/arxiv_sources/0404192/source.tex`.

## Resolution by later literature

The later paper explicitly says that its empirical `ell_infty` covering-number bounds resolve open questions by Alon et al. and Rudelson--Vershynin. The decisive theorem is Theorem 2: for a bounded real-valued function class, if

```text
gamma* = inf { gamma > 0 : fat_gamma(F) < infinity },
```

then the empirical metric entropy satisfies an `O(log n)` upper bound for scales `gamma in (2 gamma*, R)`, while the `O(log^2 n)` regime is sometimes tight below the critical scale. Immediately after Theorem 2, the authors explicitly identify the Rudelson--Vershynin `O(log^{1+epsilon} n)` question and state that their result resolves it.

Thus this is not a new proof by the run. It is an exact later-literature answer whose authors knew they were addressing the Rudelson--Vershynin question.

## Scope notes

This packet only clears the L-infinity empirical entropy exponent-one question following Theorem 4.4 of arXiv:math/0404192. It does not claim to settle any unrelated open question or conjectural direction in the source paper.

The later theorem gives the sharp scale-sensitive picture: the exponent-one `O(log n)` upper bound is available above the threshold stated in Theorem 2, while a near-`log^2 n` lower bound survives in the lower regime. That scale distinction is part of the answer.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source paper arXiv:math/0404192.
- `supporting_paper_2605.13684.pdf`: later paper giving the answer.
- `tmp/source_page21.png`: rendered source evidence page.
- `tmp/support_page3.png`: rendered supporting theorem page.
