# Constant-one finite determination for classical `L_p[0,1]`

Status: `partial_result_likely_valid`

Source paper: Sofiya Ostrovska and Mikhail I. Ostrovskii, *Distortion in the finite determination result for embeddings of locally finite metric spaces into Banach spaces*, arXiv:1510.05974, Glasg. Math. J. 61 (2019), 33-47.

Source question: Problem 5.1 asks whether there exist Banach spaces `X` with `D(X)>1^+`.

## Result

For every `1 <= p < infinity`,

```text
D(L_p[0,1]) = 1.
```

Equivalently, if `M` is locally finite and all finite subsets of `M` embed into `L_p[0,1]` with distortion at most `C`, then `M` itself embeds into `L_p[0,1]` with distortion at most `C`, with no additional `1+epsilon` loss.

This is a partial negative result for Problem 5.1: classical nonatomic `L_p` spaces do not witness a strict finite-determination gap. It does not settle the existence of some other Banach space `X` with `D(X)>1^+`.

## Proof Idea

The finite-subset embeddings give, by the standard ultraproduct argument, a `C`-bilipschitz embedding of `M` into an ultrapower of `L_p[0,1]`. Ultrapowers of `L_p` spaces are again `L_p` spaces. Since a locally finite metric space is countable, the closed linear span of the image is separable, hence sits inside a separable `L_p` subspace. Every separable `L_p` space over a finite measure algebra embeds linearly isometrically into `L_p[0,1]`. Composing these maps brings the ultrapower embedding back to `L_p[0,1]` without changing distances.

## Packet Contents

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: local copy of arXiv:1510.05974.
- `figures/open_problem_crop.png`: crop of Problem 5.1 from page 15 of the source PDF.

## Novelty Check

Local cheap-index search found only the prior failed attempt `attempts/1510.05974_D_gt_one_plus_attempt.md` and no existing solution packet for this `L_p[0,1]` subcase. The old attempt identified the ultrapower-return obstruction but did not exploit separable `L_p` representability.

Web searches for exact/near phrases including `"D(X)>1^+" "L_p" "finite determination"`, `"D(L_p" "finite determination" "locally finite metric spaces"`, and `"finite determination" "L_p[0,1]" "locally finite metric"` did not reveal a later explicit answer to this subcase. The 2023 Catrina--Ostrovskii paper improves the general constant to `3+epsilon` and restates the `1+epsilon` problem, but does not record this constant-one `L_p[0,1]` pullback.

## Human Review Recommendation

Review as a likely valid partial result. The main audit point is the standard representation step: a separable subspace of an ultrapower of `L_p[0,1]` lies in a separable `L_p` space that embeds linearly isometrically into `L_p[0,1]`.
