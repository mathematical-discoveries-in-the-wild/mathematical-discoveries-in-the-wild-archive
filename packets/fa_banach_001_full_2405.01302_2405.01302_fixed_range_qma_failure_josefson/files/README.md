# Full Result: Fixed-Range QMA Failure via Josefson--Nissenzweig

Status: `full`

Source paper: Domingo Garcia, Manuel Maestre, Miguel Martin, and Oscar Roldan, *On density and Bishop-Phelps-Bollobas type properties for the minimum norm*, arXiv:2405.01302.

## Answered Question

Section 2, page 9 asks whether for every infinite-dimensional Banach space `Y` there is a Banach space `X` such that

```tex
QMA(X,Y) != L(X,Y).
```

This packet gives an affirmative answer.

## Result

For every infinite-dimensional real or complex Banach space `Y`, choose a weak-star null sequence `(y_n^*)` in `S_{Y^*}` by Josefson--Nissenzweig. For `0<a<1` and `t_n=n/(n+1)`, define an equivalent norm on the vector space `Y` by

```tex
|||y||| = max{ a ||y||, sup_n t_n |y_n^*(y)| }.
```

Let `X=(Y, |||.|||)` and let `T=Id:X -> Y`. Then `T` is an isomorphism with `m(T)=1`, but `T` is not quasi minimum-attaining. Hence `QMA(X,Y) != L(X,Y)`.

## Proof Mechanism

The identity `J:Y -> X` has norm one because the weights `t_n` tend to one. It does not attain its norm because for each fixed `y`, weak-star nullity gives `y_n^*(y) -> 0`, while every finite weight is strictly smaller than one.

Since `T^{-1}=J`, minimum attainment of `T` would force norm attainment of `J`. More strongly, if `T` were QMA, a minimizing sequence would converge through the continuous inverse and again force `J` to attain its norm.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: page 9 crop of the open question.

## Verification Notes

- The proof is analytic; no computational verifier is needed.
- External theorem used: Josefson--Nissenzweig theorem.
- The packet proves the closed-range QMA obstruction directly, rather than relying only on a cited equivalence.

## Novelty Check

Local run indexes were searched for `2405.01302`, `quasi minimum-attaining`, `QMA(X,Y)`, `minimum-attaining`, and `Josefson--Nissenzweig`; no duplicate solution or attempt was found.

External web search on 2026-06-16 used the source title, arXiv id, and close phrases around `QMA(X,Y)` and fixed infinite-dimensional range spaces. It found the source paper but no later explicit answer to this fixed-range question.

## Human Review Recommendation

Review the renorming step and the proof that `J:Y -> X` has norm one but no norm-attaining vector. If that line checks out, the QMA contradiction is immediate and the packet answers the source question literally.
