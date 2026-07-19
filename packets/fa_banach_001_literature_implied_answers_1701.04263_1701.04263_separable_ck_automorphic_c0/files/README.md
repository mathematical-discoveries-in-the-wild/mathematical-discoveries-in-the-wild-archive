# Literature-Implied Partial Answer: Separable C(K) Automorphic Spaces

Status: `literature_implied_answer (partial subcase)`

Run: `fa_banach_001`

Source/open-problem paper: arXiv:1701.04263, Razvan Anisca, Valentin
Ferenczi, and Yolanda Moreno, "On the classification of positions and of
complex structures in Banach spaces."

Supporting paper: arXiv:0903.0658, Antonio Aviles and Yolanda Moreno,
"Automorphisms in spaces of continuous functions on Valdivia compacta."

## Claim Recorded

Question 1.1 of arXiv:1701.04263 asks whether `c_0` and `ell_2` are the only
separable automorphic Banach spaces.

The supporting paper gives a literature-implied affirmative answer on the
separable `C(K)` branch:

> If `K` is compact metrizable and `C(K)` is infinite-dimensional and
> automorphic, then `C(K)` is isomorphic to `c_0`.

This does not solve the full automorphic-space problem. It rules out all
non-`c_0` separable spaces of the form `C(K)`.

## Identification

Every compact metrizable `K` is a continuous image of the Cantor set, and the
Cantor set is Valdivia compact. Aviles--Moreno prove that if `K` is a
continuous image of a Valdivia compact and `C(K)` is extensible, then `C(K)` is
isomorphic to `c_0(Gamma)`. They also recall that automorphic spaces are
extensible. Therefore an automorphic separable `C(K)` must be isomorphic to
`c_0(Gamma)`. Separability forces `Gamma` to be countable in the
infinite-dimensional case, so the space is `c_0`.

## Evidence Locations

- arXiv:1701.04263, page 3, Question 1.1: "Are `c_0` and `ell_2` the only
  separable Banach spaces with that property?"
- arXiv:0903.0658, page 1 abstract/introduction: no automorphic `C(K)` spaces
  with `K` a continuous image of Valdivia compact except `c_0(Gamma)`.
- arXiv:0903.0658, page 2, Theorem 1: if such `C(K)` is extensible, then it is
  isomorphic to `c_0(Gamma)`.

## Search Notes

Local run searches for `1701.04263`, `automorphic`, `uniformly finitely
extensible`, `UFO`, `C(K)`, `C[0,1]`, and related position keywords found no
prior packet for this subcase. Web searches on 2026-06-15 found the source
paper and the supporting arXiv:0903.0658 paper, but no later full solution of
the broad automorphic-space question.

## Limitations

The broad question remains open outside this `C(K)` subcase. This packet does
not address arbitrary separable Banach spaces, the possible Hilbert case, UFO
classification, or the separate `E_0`-positions question for `C(0,1)`.

