# Literature-Implied Answer: JL2 Refutes Problem 1 on Bounded Sequences versus Bounded Separable FU Sets

Status: `literature_implied_answer (negative answer to Problem 1; Problem 2 not claimed)`

Source paper: C. S. Barroso, O. F. K. Kalenda, and P.-K. Lin,
*On the approximate fixed point property in abstract spaces*, arXiv:1101.5274.

Supporting paper: G. Martinez-Cervantes, *Banach spaces with weak*-sequential
dual ball*, arXiv:1612.05948.

## Target

Barroso--Kalenda--Lin ask in Problem 1 whether, for an arbitrary Hausdorff
locally convex space `X`, the following are equivalent:

- every bounded sequence in `X` has a weakly Cauchy subsequence;
- each bounded separable subset of `X` is Frechet-Urysohn in the weak topology.

They note that the answer is positive when `X` admits a compatible metrizable
locally convex topology and suggest a Johnson--Lindenstrauss dual as a possible
counterexample.

## Identification

Let `Z = JL_2` be the classical Johnson--Lindenstrauss space and let
`E = (Z^*, sigma(Z^*,Z))`.

Martinez-Cervantes proves that `JL_2` has weak-star sequential dual ball of
sequential order 2. In particular, `(B_{Z^*}, w*)` is weak-star sequentially
compact but is not Frechet-Urysohn.

For the locally convex space `E`, the continuous dual is `Z`, so the weak
topology of `E` is again `sigma(Z^*,Z)`. Every `E`-bounded sequence is
pointwise bounded on `Z`, hence norm bounded by uniform boundedness; after
rescaling it lies in `B_{Z^*}` and therefore has a weak-star convergent
subsequence. Thus every bounded sequence in `E` has a weakly Cauchy
subsequence.

On the other hand, since `(B_{Z^*},w*)` is sequential but not Frechet-Urysohn,
it has a countable subspace which is not Frechet-Urysohn. That countable set is
bounded and separable in `E`. Hence the second property fails.

This gives a ZFC negative answer to Problem 1. It is recorded as
literature-implied because the supporting paper does not present the statement
as an answer to arXiv:1101.5274; the answer appears only after identifying the
locally convex space `(JL_2^*,w*)` with the properties proved in arXiv:1612.05948.

## Scope Limitations

This packet does not settle Problem 2 of the source paper, which asks whether
weak-AFPP is equivalent to the bounded-sequence weakly-Cauchy-subsequence
property for arbitrary Hausdorff locally convex spaces.

It also does not use the later CH-dependent Efremov-property constructions for
Johnson--Lindenstrauss spaces. The classical `JL_2` result from arXiv:1612.05948
already suffices for Problem 1.

## Packet Contents

- `main.tex`: compact status note with the proof of the identification.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: source/open-problem PDF, if locally available or
  downloadable.
- `supporting_paper_1612.05948.pdf`: supporting theorem PDF, if locally
  available or downloadable.

## Search Bounds

Cheap run indexes were searched for `1101.5274`, `weak-AFPP`, `approximate fixed
point property`, `Frechet-Urysohn`, `Fréchet-Urysohn`, `Johnson-Lindenstrauss`,
`JL_2`, `weak*-sequential dual ball`, and bounded separable subsets. No existing
packet for this answer was present. Existing nearby memory included a failed
ZFC attempt on the CH-sensitive Efremov-property problem for arXiv:1804.10350,
but that is a different target.

Web searches on 2026-06-28 for the source title, `weak-AFPP`, weakly Cauchy
subsequences, Johnson--Lindenstrauss weak-star sequential properties, and
bounded separable Frechet-Urysohn formulations found no more explicit later
settlement of Problem 1.

## Human Review Notes

Recommended review focus: verify the two topological translations, namely that
the continuous dual of `(Z^*,sigma(Z^*,Z))` is `Z`, and that sequential but
non-FU dual ball yields a countable bounded non-FU subspace.
