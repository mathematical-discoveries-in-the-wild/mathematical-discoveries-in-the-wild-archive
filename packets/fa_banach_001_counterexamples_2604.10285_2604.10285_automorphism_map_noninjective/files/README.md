# Counterexample: the automorphism-to-homeomorphism map is not injective

- Run: `fa_banach_001`
- Source paper: M.H.M. Rashid, *Operator Algebras of Bourgain Delbaen Spaces: Realization, Rigidity, and Ideal Structure*, arXiv:2604.10285.
- Source location: Remark 6.16, page 23 of the source PDF; TeX source around line 1205.
- Result type: counterexample to the literal injectivity question in Remark 6.16.
- Status: candidate counterexample, likely valid; recommended for human review.

## Source Question

Remark 6.16 asks about the natural map

```text
Aut(L(X_{C(K)})) -> Homeo(K),    Phi -> h,
```

arising from the induced Calkin-algebra action. It specifically asks whether
this map might be injective.

## Counterexample

For any infinite-dimensional Banach space `X`, and hence for the spaces
`X_{C(K)}` in the source paper, choose a nonzero rank-one projection `P`.
Then `U = I + P` is invertible and `Ad_U(T)=UTU^{-1}` is an automorphism of
`L(X)`.

Because `U-I=P` is finite-rank, hence compact, `U` has the same Calkin class
as `I`. Therefore `Ad_U` induces the identity automorphism on the Calkin
algebra. Under the source identification `Cal(X_{C(K)}) ~= C(K)`, it induces
the identity homeomorphism of `K`.

The automorphism `Ad_U` is nontrivial: if `P=f tensor x`, with `f(x)=1`, and
`y in ker f` is nonzero, then for `T=f tensor y` one has

```text
Ad_{I+P}(T) = T/2 != T.
```

Thus two distinct automorphisms, `id` and `Ad_{I+P}`, map to the same
homeomorphism. The proposed map is not injective.

## Verification

- `source_paper.pdf`: local copy of arXiv:2604.10285.
- `figures/open_problem_crop.png`: real crop of page 23 containing Remark 6.16.
- `main.tex` and `solution_packet.pdf`: formal proof packet.
- No computational verification is needed; the proof is a direct finite-rank
  operator calculation.
- Build command used:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

## Novelty / Duplicate Check

Local duplicate checks over `registry_index.tsv`, `solutions/index.tsv`,
`attempts/index.tsv`, `proof_gaps/index.tsv`, and active claims found nearby
Calkin-algebra packets for arXiv:1711.01340 and related Motakis papers, but no
packet or attempt for arXiv:2604.10285 or this automorphism-kernel question.

Bounded web searches on 2026-06-14 for exact and close phrases including
`"Aut(\\mathcal{L}(\\mathfrak{X}_{C(K)}))" "Homeo(K)"`,
`"automorphism group" "Bourgain-Delbaen" "Homeo(K)"`,
`"Operator Algebras of Bourgain" "Is it injective"`, and
`"I+P" finite-rank projection conjugation automorphism Calkin algebra identity`
found no prior answer to the exact Remark 6.16 injectivity question.

## Limitations

This packet answers the literal injectivity question negatively. It does not
construct a non-inner or outer automorphism in the kernel. If the intended
question is the induced map after quotienting `Aut(L(X_{C(K)}))` by inner
automorphisms, then this packet should be read as a correction to the stated
formulation, not as a solution of that stronger outer-automorphism problem.
