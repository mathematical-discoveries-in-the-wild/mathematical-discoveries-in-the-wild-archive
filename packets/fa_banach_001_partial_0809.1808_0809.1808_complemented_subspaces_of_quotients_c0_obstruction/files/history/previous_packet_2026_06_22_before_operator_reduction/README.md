# Complemented-Subspace Reduction for the Rosenthal/Odell Quotient Question

Status: `partial_result (complemented subspaces of quotients of strict ell_1-preduals contain c0; general WU trichotomy and c0-saturation criterion recorded)`

Run: `fa_banach_001`  
Agent: `agent_lane_08`  
Source: arXiv:0809.1808, Ioannis Gasparis, "New examples of c_0-saturated Banach spaces"

## Claim

Let `E` be a real strict `ell_1`-predual, i.e. `E^*` is isometric to `ell_1`, and let `X` be a quotient of `E`. Then every complemented infinite-dimensional subspace of `X` contains a copy of `c_0`.

In particular, if `K` is countable compact metric and `X` is a quotient of `C(K)`, every complemented infinite-dimensional subspace of `X` contains `c_0`.

## Relevance

Gasparis records Rosenthal's question asking whether every quotient of an `ell_1`-predual is `c_0`-saturated, and Odell's special case for quotients of `C(K)` with `K` countable compact. This packet does not solve the full saturation question, because saturation quantifies over all subspaces, not only complemented ones.

The result does, however, sharpen the obstruction: any counterexample to the strict `ell_1`-predual or countable `C(K)` version must contain an infinite-dimensional `c_0`-free subspace that is not complemented in the quotient.

## Final-Push Reduction

A later final-push pass did not produce a full proof or counterexample, but it narrowed the remaining countable `C(K)` case.

If `K` is countable compact metric, `X` is a quotient of `C(K)`, and `Y` is a subspace of `X`, then `Y^*` is separable: `X^*` embeds into `ell_1(K)`, and `Y^*` is a quotient of `X^*`. Hence no such `Y` contains `ell_1`.

For the first hard ordinal level `C(omega^omega)`, Odell records Schlumprecht's observation that the closed span of any normalized weakly null sequence in a quotient whose spreading model is equivalent to the `ell_1` basis contains `c_0`. Thus a hypothetical `c_0`-free subspace of a quotient of `C(omega^omega)` must have separable dual, contain no `ell_1`, and avoid weakly-null `ell_1` spreading models.

The same pass also rejected a tempting shortcut: `Y^*` being a quotient of a subspace of `ell_1` does not imply that `Y^*` has the Schur property, since quotients of `ell_1` can be arbitrary separable Banach spaces.

## Extra Push: General WU Trichotomy

The extra push sharpened the previous WU-to-reflexive reduction into a general theorem for all Banach spaces with Odell's property `(WU)`.

If `X` has `(WU)`, then every infinite-dimensional subspace of `X` contains `ell_1`, or `c_0`, or an infinite-dimensional reflexive subspace. Equivalently, every `(WU)` space containing neither `ell_1` nor `c_0` is reflexively saturated.

Proof idea: subspaces inherit `(WU)`. If a subspace `Y` contains neither `ell_1` nor `c_0` and is nonreflexive, Rosenthal's `ell_1` theorem gives a nontrivial weakly Cauchy sequence, whose normalized differences are weakly null. Property `(WU)` gives an unconditional subsequence. Since its span contains neither `ell_1` nor `c_0`, James's unconditional-basis criteria make that span reflexive.

Consequently, if `X` has `(WU)` and contains no `ell_1`, then `X` is `c_0`-saturated if and only if `X` contains no infinite-dimensional reflexive subspace. This applies in particular to quotients of spaces with shrinking unconditional FDDs, by Odell's theorem, and to any quotient of a countable compact `C(K)` space once `(WU)` is known for that quotient.

For quotients of `C(omega^omega)`, this means a hypothetical `c_0`-free subspace with no reflexive subspace must fail `(WU)` and, by Schlumprecht's observation recorded by Odell, must also avoid weakly-null `ell_1` spreading models. This is not a full solution, because Odell explicitly left quotient preservation of `(WU)` open in this neighborhood, and reflexive subspaces of quotients of countable `C(K)` spaces are not ruled out here.

## Literature-Implied Broad Answer

There is also a separate literature-implied answer to the broader isomorphic interpretation of "ell_1-predual". Argyros--Motakis, arXiv:1608.01962, construct an `L_infty` space with separable dual and no `c_0`, and their quotient section gives `ell_1`-preduals `X_1`, `X_2`, `X_3` with `X_2` a quotient of `X_1` and `X_2` containing no reflexive subspace. This gives a negative answer if "ell_1-predual" means `X^*` merely isomorphic to `ell_1`.

That literature implication is not the promoted claim of this packet and does not settle Odell's countable compact `C(K)` subproblem. It is included here to keep the target history in one place.

## Proof Inputs

- Johnson-Zippin/Pelczynski property `(V)`: real `L^1`-preduals have property `(V)`. The packet cites Krulisova arXiv:1509.06610 for a convenient reference.
- Property `(V)` passes to quotients.
- An operator fixes no copy of `c_0` iff it is unconditionally converging.
- Infinite-dimensional reflexive spaces do not embed into `ell_1`.
- Countable compact `C(K)` quotients have subspaces with separable duals; this only rules out `ell_1`, not reflexive or James-type subspaces.
- Odell's 1992 paper records Schlumprecht's `ell_1` spreading-model obstruction for quotients of `C(omega^omega)`.
- Odell's property `(WU)`, Rosenthal's `ell_1` theorem, and James's unconditional-basis criteria give the general WU trichotomy and the no-`ell_1` `c_0`-saturation criterion.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: Gasparis source paper.
- `supporting_paper_1509.06610.pdf`: supporting property `(V)` reference.
- `supporting_paper_1608.01962.pdf`: supporting Argyros--Motakis reference for the broader literature-implied answer.
- `supporting_paper_math_9201219.pdf`: Odell's quotient paper, used for the `C(omega^omega)`/Schlumprecht context.
- `supporting_paper_math_9204215.pdf`: Alspach's strict `ell_1`-predual quotient note, used as historical context.
- `supporting_paper_math_9805081.pdf`: Alspach's Bourgain--Delbaen dual paper, used as a stress-test context for low-Szlenk no-`c_0` pathologies.
- `figures/open_problem_crop.png`: source excerpt containing the Rosenthal/Odell question.

## Human Review Focus

1. Check whether the intended field is real or complex. The proof as written uses the real `L^1`-predual property `(V)` theorem.
2. Check whether there is a standard citation that already states this complemented-subspace reduction explicitly.
3. Keep the uncomplemented-subspace case separate; this packet does not solve it.
4. Keep the broad isomorphic `ell_1`-predual negative answer separate in status from the strict/countable `C(K)` partial theorem.
5. Check the final-push reduction's scope: it proves separable dual/no `ell_1`, not Schur dual/no reflexive subspace.
6. Check the extra-push trichotomy's scope: it is a standard-tool consequence for spaces with `(WU)` and does not assert quotient preservation of `(WU)` for `C(omega^omega)`.
