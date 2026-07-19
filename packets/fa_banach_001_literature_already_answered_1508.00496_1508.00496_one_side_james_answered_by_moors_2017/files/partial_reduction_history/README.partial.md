# Partial result: positive families for the remaining one-sided James conjecture

- Source paper: B. Cascales, J. Orihuela, and A. Pérez, *One-side James' Compactness Theorem*, arXiv:1508.00496.
- Source signal: final remarks, asking whether Theorems 2 and 10 are valid for arbitrary Banach spaces.
- Supporting paper: J. Orihuela, *Conic James' Compactness Theorem*, arXiv:1610.02763.
- Packet status: consolidated partial result plus literature-status clarification, likely valid.

## Result

The 2016 conic James paper explicitly extends Theorem 10 of the source paper to arbitrary Banach spaces and states that Theorem 2 remains unknown for arbitrary Banach spaces.

For the remaining Theorem 2, this packet records the exact one-set reduction and proves four positive families.

First, the arbitrary two-set statement is equivalent to the one-set assertion:

> If `C` is bounded, closed, convex, `dist(0,C)>0`, and every `x*` with `sup_C x*<0` attains `sup_C x*`, then `C` is weakly compact.

Second, the affine-slice subcase holds. Let `E` be a Banach space and let `A,B` be nonempty bounded closed convex subsets of `E` with `d(A,B)>0`. Assume:

1. every `x* in E*` with `sup(x*,B) < inf(x*,A)` attains its supremum on `B` and its infimum on `A`;
2. there is `phi in E*` and real numbers `gamma < delta` such that `phi(B)={gamma}` and `phi(A)={delta}`.

Then `A` and `B` are weakly compact.

Equivalently, after reducing to `C=closure(B-A)`, the one-sided James assertion holds whenever the test set `C` is contained in an affine hyperplane strictly separated from `0`.

Third, a literature-assisted conic-dominated family follows from Orihuela's conic James theorem: if the negative cone `{x*: sup_C x*<0}` contains the positive cone of some weakly compact direction set `D` with `0 notin D`, then `C` is weakly compact.

Fourth, a direct frustum family holds. If `Y` is any Banach space, `S subset Y` is bounded closed convex with `0 in S`, `0<alpha<beta`, and

`C = co( { (alpha,0) } union ( {beta} x S ) ) subset R oplus_infty Y`,

then the one-sided condition for `C` forces every `y* in Y*` to attain its supremum on `S`; hence `S` is weakly compact by James' theorem and `C` is weakly compact. Thus this broad family cannot supply a counterexample: any non-weakly-compact base produces a nonattaining negative separator.

Fifth, a finite-dimensional cylinder family holds. If `F` is finite-dimensional, `P subset F` is compact convex with `dist(0,P)>0`, `S subset Y` is bounded closed convex, and

`C = P x S subset F oplus_infty Y`,

then the one-sided condition for `C` forces every `y* in Y*` to attain its supremum on `S`; hence `S` and `C` are weakly compact. This includes genuine non-singleton finite-dimensional bases, not just affine slices.

## Proof mechanism

For `C=closure(B-A)`, the hypothesis says every functional strictly negative on `C` attains its supremum on `C`. The affine-slice assumption gives a functional `phi` that is constant and negative on `C`.

Given any `y* in E*`, choose `lambda>0` so that `y* + lambda phi` is strictly negative on `C`. By the one-sided hypothesis it attains its supremum on `C`. Since `phi` is constant on `C`, the same point also maximizes `y*`. Thus every functional in `E*` attains its supremum on `C`; James' compactness theorem gives weak compactness of `C`, and then `A` and `B` are weakly compact as closed convex subsets of translates of `C`.

For the frustum family, a scalar functional on the `R` coordinate can be tuned so that a chosen `y*` exposes the far slice `{beta} x S` while the whole functional remains strictly negative on `C`. If the one-sided hypothesis holds, that tuned functional must attain its maximum on `C`, forcing `y*` to attain on `S`.

For the cylinder family, first choose a finite-dimensional separator `phi` with `sup_P phi<0`. Given `y*`, scale `phi` so that `lambda phi + y*` is strictly negative on `P x S`. Attainment of this product functional, with the `P` coordinate fixed, forces `y*` to attain on `S`.

## Full-push notes

The arbitrary two-set conjecture is equivalent to the one-set assertion for bounded closed convex `C` with `dist(0,C)>0`: if every `x*` with `sup_C x*<0` attains `sup_C x*`, then `C` is weakly compact. The affine-slice proof works because a constant negative functional on `C` lets us shift every `y*` into the negative cone without changing its maximizers.

Without such a constant shift, the natural perturbation by an arbitrary separator need not preserve nonattainment, and the 2016 conic theorem applies only when a fixed weakly compact direction set sits inside the strict separating cone. The frustum and cylinder computations show that two simple base-hiding counterexample templates fail for the opposite reason: the negative cone sees the base strongly enough to force James norm-attainment on the base itself. The remaining hard core is to decide whether every non-weakly-compact `C` away from `0` admits a nonattaining functional inside its strict negative cone.

## Verification notes

- Local indexes had no prior packet for arXiv:1508.00496.
- Literature check: arXiv:1610.02763 explicitly says it extends Theorem 10 for arbitrary Banach spaces and that Theorem 2 remains unknown.
- New web searches on exact title/arXiv id/counterexample phrases found the source paper and the 2016 conic paper as the relevant direct hits, with no later exact resolution found in this bounded search.
- The direct family proofs use only classical James compactness theorem, Orihuela's conic theorem, and elementary support-function computations.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `supporting_paper_1610.02763.pdf`: supporting conic James paper.
- `figures/open_question_crop.png`: crop of the source final-remarks question.
