# Partial packet: L1 decoupling examples cannot answer the type 2 non-UMD question

Status: `candidate_partial_result_likely_valid`

Source target: arXiv:1006.5349, Sonja Cox and Mariusz Gorajski,
`Vector-valued stochastic delay equations - a semigroup approach`.

## Source Question

In Section 4.1, page 12 of the compiled source PDF, Cox and Gorajski write:

> The results in this article are also valid if E is a type 2 Banach space with the decoupling property but we do not know of any such spaces that are not in fact UMD spaces.

The source TeX location is `data/parsed/arxiv_sources/1006.5349/source.tex:541`.

## Result

This packet proves a partial no-go theorem for the standard known non-UMD
decoupling examples.

If `E` is either

- isomorphic to a closed subspace of a scalar `L^1(mu)` space, or
- one of the Cox-Veraar Bochner examples `L^1(S;Y)` with `S` sigma-finite
  and `Y` UMD,

then type 2 forces `E` back into the UMD class. In the scalar `L^1` subspace
case, type 2 plus inherited cotype 2 makes `E` Hilbertian by Kwapien's theorem.
In the Bochner `L^1(S;Y)` case, type 2 rules out arbitrarily many disjoint
positive-measure pieces, so `S` is finite atomic and `L^1(S;Y)` is a finite
`l_1`-sum of UMD spaces.

## Scope

This does not solve the full Cox-Gorajski question. It only eliminates the
main `L^1` routes currently visible in the local source corpus as sources of
non-UMD decoupling spaces. A type 2 decoupling non-UMD space, if it exists,
must come from a decoupling mechanism outside these `L^1` families.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: compiled local PDF of arXiv:1006.5349.
- `figures/open_problem_crop.png`: rendered page 12 showing the source aside.
- `tmp/`: LaTeX build intermediates and compiled source-paper intermediates.

## Verification Notes

- Cheap indexes searched: `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv`.
- Local source corpus checked for the exact arXiv id, title keywords, `type 2`,
  `decoupling property`, `UMD`, `L^1`, Cox-Veraar examples, and related
  Yaroslavtsev/Kalton-Lorist-Weis terminology.
- No duplicate packet for this source question was found.
- The proof uses only standard Banach-space facts: `L^1` has cotype 2, cotype
  passes to subspaces and isomorphs, Kwapien's type 2 plus cotype 2 theorem,
  and finite-sum stability of UMD.

Human-review recommendation: verify the measure-algebra reduction in the
Bochner `L^1(S;Y)` case and the intended scope of "standard known examples."
