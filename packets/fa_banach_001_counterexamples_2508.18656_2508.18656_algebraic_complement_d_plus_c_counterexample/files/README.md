# Counterexample packet: algebraic complements refute the arbitrary-`D` extension question

Status: `counterexample_likely_valid`

Source paper: Geivison Ribeiro, *Isometric embeddings of separable Banach spaces into `(\ell^\infty \setminus c)\cup\{0\}`*, arXiv:2508.18656.

## Claim

The final open question of the source asks whether, for every arbitrary
possibly nonseparable subspace `D \subset ell_infty` with `D \cap c = {0}` and
every separable Banach space `E`, there is an isometry `T:E -> ell_infty` such
that

```text
T(E) \cap (D+c) = {0}.
```

The packet gives a negative answer as written.  Choose an algebraic complement
`D` of `c` in `ell_infty`, so `ell_infty = D \oplus c`.  Then `D \cap c = {0}`
but `D+c = ell_infty`, and no nonzero isometric copy can be disjoint from
`D+c`.

## Files

- `main.tex` - self-contained counterexample packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of the arXiv source PDF.
- `figures/open_problem_crop.png` - crop of the final open question on page 9.

## Scope

This answers only the final arbitrary-`D` question.  It does not address the
earlier question asking for a closed nonseparable extension `Z` when `D` is
finite-dimensional.

## Verification

The proof is purely algebraic.  The only set-theoretic input is the standard
Hamel-basis extension argument giving an algebraic complement to the proper
subspace `c` of `ell_infty`.

Bounded novelty check: local run indexes were searched for arXiv:2508.18656,
the title, `D+c`, and related embedding phrases.  Web searches on 2026-06-23
for exact phrases from the final open question and for the algebraic-complement
obstruction found no prior run packet or obvious published answer.

