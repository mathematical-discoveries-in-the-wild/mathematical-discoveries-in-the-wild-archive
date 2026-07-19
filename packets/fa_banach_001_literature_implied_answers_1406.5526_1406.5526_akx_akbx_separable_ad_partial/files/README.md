# Literature-Implied Partial Answer: `AK(X)` versus `AK(B_X)`

Status: `literature_implied_answer (partial subcase)`

Source problem paper: A. Aviles, G. Plebanek, and J. Rodriguez,
*Tukey classification of some ideals in omega and the lattices of weakly
compact sets in Banach spaces*, arXiv:1406.5526v3.

Supporting theorem source: the same paper, especially Proposition 3.2,
Proposition 3.7, Theorem 4.3, Theorem 6.1, and Theorem 8.1.

## Target

Problem 8.1 in the source asks:

> Is it true that `AK(X) ~ AK(B_X)` for every non-reflexive `X`?

Here `AK(E)` is the asymptotic structure of weakly compact subsets of `E`
with relations `K subset L + epsilon B_X`.

## Result Recorded

The source paper's own theorems imply the following partial affirmative answer.

1. If `X` is non-reflexive and `K(B_X) preceq AK(B_X)`, then
   `AK(X) ~ AK(B_X)`.
2. If `X` is non-reflexive and SWCG, then `AK(X) ~ AK(B_X) ~ omega`.
3. Consequently, in ZFC, Problem 8.1 has an affirmative answer for every
   separable non-reflexive Banach space containing no copy of `ell^1`.
4. Under analytic determinacy, Problem 8.1 has an affirmative answer for every
   separable non-reflexive Banach space.

This is not a full answer to Problem 8.1 for arbitrary non-reflexive Banach
spaces. It is also not claimed as a new theorem independent of the source
paper; it is a direct agent-identified consequence of the source's comparison
and classification results.

## Identification

For (1), Proposition 3.7(i) gives `AK(X) preceq K(X)`, Proposition 3.2(iii)
gives `K(X) ~ K(B_X)` for non-reflexive `X`, and the hypothesis gives
`K(B_X) preceq AK(B_X)`. Proposition 3.7(ii) gives the reverse reduction
`AK(B_X) preceq AK(X)`.

For (2), Lemma 4.2(ii) gives countably many weakly compact subsets of `X`
that strongly generate every weakly compact subset of `X`, so `AK(X) preceq
omega`. Theorem 4.3 gives `AK(B_X) ~ omega` for non-reflexive SWCG spaces,
and Proposition 3.7(ii) gives the reverse lower bound.

Theorem 6.1 states in ZFC that if `X` is separable and contains no `ell^1`,
then `AK(B_X) ~ K(B_X)`, so (1) applies. Theorem 8.1 classifies separable
spaces under analytic determinacy: in the non-reflexive `omega` case, (2)
applies; in the `omega^omega`, `K(Q)`, and `[mathfrak c]^{<omega}` cases,
Theorem 8.1 itself states `AK(B_X) ~ K(B_X)`, so (1) applies.

## Evidence

- `source_paper.pdf`: local copy of arXiv:1406.5526v3. The original question
  appears as the first problem in Section 10, "Open problems" in the TeX source
  and as Problem 8.1 in the theorem numbering.
- `solution_packet.pdf`: compact status note built from `main.tex`.

## Search Bounds

Cheap run indexes were searched for `1406.5526`, the title, `Tukey
classification`, `weakly compact sets`, `AK(B_X)`, and related keywords. No
prior packet or attempt for this exact target was found; the only local hit was
an adjacent weak-compactness literature-status packet for a different paper.

Web searches on 2026-06-16 for exact phrases around `AK(X)`, `AK(B_X)`, Tukey
classification, and weakly compact sets did not find a separate later full
answer. Semantic Scholar citation metadata for arXiv:1406.5526 was also
checked; the relevant 2016 Rodriguez open-problems survey records the related
`K(B_X)` consistency problem but not a full solution of Problem 8.1.

## Scope Limitations

The arbitrary non-reflexive case remains open in this packet. The natural
radius-normalization route from `AK(X)` to `AK(B_X) x omega` was also audited
and fails at the uniform Tukey tolerance: the parameter `delta` must be chosen
before the target radius bound is known, so the usual `K(X) ~ K(B_X) x omega`
proof does not transfer to `AK`.

## Human Review Notes

Recommended review focus:

- Check that Theorem 8.1 case (iia), `AK(B_X) ~ omega`, is correctly converted
  to the SWCG case through Theorem 4.3.
- Check the short reduction chain in item (1), especially use of Proposition
  3.7(i) with `E=X` and Proposition 3.2(iii).
- Confirm that this should remain a literature-implied partial-subcase record,
  not a claimed full solution of the source problem.
