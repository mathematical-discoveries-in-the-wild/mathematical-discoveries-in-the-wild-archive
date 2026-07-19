# Literature-Implied Answer: Average Distortion Does Not Preserve the Dimension-Refined Bound

Status: `literature_implied_answer (negative answer to Discussion item 3, dimension-refined extension)`

Source target: Alexandros Eskenazis, *Some geometric applications of the discrete heat flow*, arXiv:2310.01868.

Supporting theorem: Alan Chang, Assaf Naor, Kevin Ren, *Random zero sets with local growth guarantees*, arXiv:2410.21931, Proposition `\ref{prop:Rn more genral}`.

## Identification

Discussion item 3 of arXiv:2310.01868 asks whether the lower bound of Theorem `\ref{thm:main}` can be extended from bi-Lipschitz distortion of the Hamming cube to average-distortion embeddings.  Theorem `\ref{thm:main}` gives

```tex
c_X({-1,1}^n) \gtrsim
\sup_{1 \le p \le 2}
\frac{n}{T_p(X)\min\{n,\dim X\}^{1/p}}.
```

The answer to this dimension-refined extension is negative already for the one-dimensional Hilbert target `X = R` and quadratic average distortion.

## Reason

For `X = R`, `dim X = 1` and `T_2(R) = 1`, so the `p=2` term in the Theorem 1 bound is order `n`.  If the same bound extended to quadratic average distortion, then the Hamming cube would have quadratic average distortion at least `c n` into `R`.

However, Proposition `\ref{prop:Rn more genral}` of arXiv:2410.21931 says that for `1 <= q <= 2`, the least `D` such that `ell_q^n` embeds into `R` with `p`-average distortion `D` is of order `sqrt(max{1,n/p})`.  Taking `q=1` and `p=2` gives an embedding of `ell_1^n` into `R` with quadratic average distortion `O(sqrt n)`.  Restricting that embedding to the sign cube gives the same order for `{-1,1}^n` with the Hamming metric, up to the harmless factor between `ell_1` distance on signs and Hamming distance.

Thus the proposed dimension-refined average-distortion analogue would demand order `n`, while the actual quadratic average distortion is at most order `sqrt n`.

## Scope

This does not contradict the IVV-style average lower bound mentioned in the source paper.  For `X=R` and type `2`, that lower bound is only order `sqrt n`, matching the later proposition.  What fails is precisely the extra low-dimensional improvement supplied by Theorem `\ref{thm:main}` in the bi-Lipschitz setting.

The supporting paper does not appear to state that it is answering Discussion item 3 of arXiv:2310.01868; this packet records the agent-identified implication.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2310.01868.
- `supporting_paper_2410.21931.pdf`: arXiv:2410.21931.

