# Verification record

Verdict: `counterexample_likely_valid`.

## Claim under review

The characteristic-`p` extension of Lemma 7.2 in arXiv:2504.10209 is false:
there is a complete nontrivially valued nonarchimedean field `K` and an
infinite algebraic extension field `L/K` such that `L`, with a multiplicative
norm, is a Banach `K`-algebra.

## Adversarial audit

1. **Does `K=L^p` contain the coefficients required for algebraicity?**
   Yes.  For every `x∈L`, the element `x^p` belongs to `K` by definition, and
   `x` is a root of `X^p-x^p∈K[X]`.

2. **Could `K` fail to be complete?**
   No.  For `L=k((t))`, Frobenius gives
   `L^p=k^p((t^p))`.  This is a Laurent-series field in the uniformizer
   `s=t^p`, hence is complete for the inherited absolute value `|s|=|t|^p`.
   Equivalently, a Cauchy sequence of `p`th powers has Cauchy roots because
   `|a-b|^p=|a^p-b^p|`.

3. **Could the field extension nevertheless be finite?**
   No.  For every `N`, the monomials
   `u_1^{e_1}...u_N^{e_N}`, `0≤e_i<p`, are linearly independent over
   `K=k^p((t^p))`.  Expanding a hypothetical finite relation in powers of
   `t^p` reduces coefficientwise to their standard independence over `k^p`.
   That independence follows by restricting the finitely many coefficients to
   a finite rational-function field, where the residue-class monomials form a
   basis over the subfield of `p`th powers.  Thus `[L:K]≥p^N` for all `N`.

4. **Is the norm compatible with the source assumptions?**
   Yes.  The `t`-adic absolute value on `L` is nontrivial, ultrametric, and
   multiplicative.  Its restriction is the given absolute value on `K`, and
   `|ax|=|a||x|` for `a∈K`, `x∈L`.  Completeness of `L` makes it a Banach
   `K`-algebra in a stronger sense than required by the source lemma.

5. **Does the example refute every conclusion of Lemma 7.2?**
   It refutes the finiteness conclusion and therefore the lemma as a
   conjunction.  It intentionally does not refute the nonarchimedeanity
   conclusion: the example is itself nonarchimedean.  No stronger claim is
   made.

6. **Does this solve the paper's full positive-characteristic automatic-
   continuity problem?** No.  The packet answers only Remark 7.3.  A general
   replacement for Theorems 1.2 or 1.3 remains outside its scope.

## Novelty check

On 2026-07-22, the run's registry, solution, attempt, and proof-gap indexes
were searched for arXiv:2504.10209 and the core terms `purely inseparable`,
`p-degree`, `Frobenius`, and `algebraic Banach field extension`.  No prior
packet or answer was found.  A bounded external search used the exact paper
title, the exact opening phrase of Remark 7.3, the lemma label
`NormsOnFiniteExtensions`, the author name, and positive-characteristic
variants.  It found the source paper and summaries of it, but no distinct
paper claiming to resolve Remark 7.3.  This is evidence, not a proof of
novelty; human literature review remains recommended.

## Artifact verification

- The original source PDF is stored as `source_paper.pdf` (16 pages).
- `figures/open_problem_crop.png` was rendered from source PDF page 11 and
  visually checked for legibility and correct context.
- `solution_packet.pdf` was compiled from `main.tex`; every rendered page was
  visually inspected after compilation.
