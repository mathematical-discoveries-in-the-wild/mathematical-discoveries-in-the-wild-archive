# 2311.15568 Polydisc Non-Atomic Equivalence Route

Status: `partial_result_likely_valid`; `candidate_full_polydisc_subcase_human_review_needed`; `symmetrized_smoothing_barrier_identified`.

Source paper: T. Bhattacharyya, M. Bhowmik, and P. Kumar, *Herglotz's representation and Caratheodory's approximation*, arXiv:2311.15568.

## Result

The source asks whether Herglotz's representation and Caratheodory's approximation are equivalent on the polydisc or on the symmetrized polydisc.

This packet proves a sharp obstruction for the polydisc part. For `d >= 2`, every positive finite Koranyi-Pukanszky determining measure on `T^d` is nonatomic. More strongly, for every mixed-sign character `chi_n(u)=u^n`, the pushforward `(chi_n)_# mu` is exactly `mu(T^d)` times Haar measure on `T`.

Consequently, the determining-measure cone used in the polydisc Herglotz representation contains no nonzero positive measure with countable support, and no finite atomic probability measures.

The packet also gives a stronger reduction: locally uniform approximation by normalized Cayley rational inner Herglotz functions is equivalent to weak-star density of their rational-inner Clark measures in the Koranyi-Pukanszky determining-measure simplex. Thus the missing replacement for the disc's point masses is not another atomic approximation scheme, but density of diffuse Clark measures.

Final push: the packet now includes a two-way route for the polydisc. Caratheodory approximation implies the normalized Koranyi-Pukanszky representation by scaling rational inner approximants and taking weak-star limits of continuous RP densities. Conversely, the Koranyi-Pukanszky representation plus the standard Pfister-Rudin-Stout finite rationalization lemma implies zero-preserving Caratheodory approximation: Fejer-smooth the representing RP measure, Cayley-transform the resulting positive-real polynomials, rationalize them by the reflected-polynomial construction, and diagonalize.

The latest stress test also records the symmetrized-polydisc barrier. Bhowmik-Kumar prove rational-inner Caratheodory approximation on quotient domains including the symmetrized polydisc, and the source paper gives the relevant Szego-kernel Herglotz representation. The same scaling argument gives the `Caratheodory => Herglotz` direction on the symmetrized polydisc. The reverse direction does not follow from the polydisc proof because the distinguished boundary is not a compact abelian group, uses the weighted Szego measure `s_*(|J|^2 dm)`, and lacks a known Fejer-type smoothing theorem preserving the quotient determining condition. An explicit `G_2` calculation now shows that ordinary torus Fejer smoothing fails to preserve the quotient annihilator even for the continuous function `q(s,p)=s^2/p-1` in `C(bG_2) cap W^\perp`.

## Why This Matters

In the disc and finitely connected planar-domain arguments, one key route from Herglotz representation to Caratheodory approximation is to approximate representing measures by finite convex combinations of point masses; the inverse Cayley transforms of the resulting extreme Herglotz functions are inner/rational-inner approximants.

The theorem here shows that this finite-atomic route cannot work on the polydisc: the Koranyi-Pukanszky moment conditions rule out positive atomic determining measures entirely. The follow-up route replaces atoms by Fejer smoothing inside the determining-measure cone and a finite rational-inner rationalization step.

## Scope

This does not solve the full open equivalence problem as stated for both the polydisc and the symmetrized polydisc. It gives a candidate full polydisc subcase, subject to human review, and rules out the direct finite-atomic/Krein-Milman mechanism for `d >= 2`.

Known positive zones are recorded: rational-inner Clark-measure density follows wherever Caratheodory approximation is already known; in particular the bidisc has a complete positive approximation statement via the Agler/Schur equality. The symmetrized-polydisc case is reduced to a quotient-boundary smoothing/density lemma not found in the checked literature, and the most obvious lift-to-`T^d` Fejer approach is ruled out already for `d=2`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: crop of the source open-problem sentence.
