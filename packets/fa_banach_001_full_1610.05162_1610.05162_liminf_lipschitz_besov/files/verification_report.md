# Verification report

Packet: `1610.05162_liminf_lipschitz_besov`

Date: 2026-07-21

Verdict: `candidate_full_solution_likely_valid`, suitable for human review.

## Analytic proof audit

The proof has four components.

1. **Translation triangle inequality.** For
   `omega(h)=||f(.+h)-f||_infinity`, translation invariance gives
   `omega(a) <= omega(h)+omega(a-h)` for every pair of displacements.
2. **All-smaller-scale propagation.** If `omega(a_0)/|a_0| >= M`, dividing
   `a_0` into `n` equal increments shows that the supremal translation
   quotient is at least `M/2` at every smaller radius.
3. **Cumulative mass and integration by parts.** Averaging the triangle
   inequality over a ball gives
   `F(t) >= c M^q t^(N+q)` for the cumulative mass of `omega^q`.
   Stieltjes integration by parts against `t^(-N-rq)` then yields the sharp
   factor `1/(1-r)`. The boundary term at zero is controlled directly by the
   assumed finiteness of the Besov integral.
4. **Lipschitz upper bound and representative.** The estimates
   `omega(h)<=L|h|` and `omega(h)<=2||f||_infinity` give the upper bound by
   polar integration. Mollification plus Arzela-Ascoli turns a finite
   translation seminorm into a genuine Lipschitz representative.

No computational assertion closes an analytic gap.

## Reproducible numerical checks

Command run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/verify_constants.py
```

The script checks the explicit lower constant is positive and below the upper
constant for several dimensions and exponents. For the model modulus
`omega(h)=min(|h|,1)`, it evaluates the radial Besov integral exactly and
checks that `(1-r)A_r` converges to `|S^(N-1)|/q` for the tested parameter
grid. This supports the normalization and polar-coordinate bookkeeping; it
is not a proof of the theorem.

## Novelty bounds

The local registry, solution, attempt, and proof-gap indexes were searched for
arXiv:1610.05162, the paper title, BBM/Besov limiting embeddings, `liminf`, and
Lipschitz criteria. Two bounded web searches used:

- the exact sentence beginning `Due to the lack of continuity of the
  translations in L infinity`;
- the paper title, author, arXiv id, and `Remark 2.13`;
- `translation modulus`, `Abel mean`, `liminf Besov norm`, and `Lipschitz
  characterization`;
- close variants about replacing a normalized limsup with liminf.

Five cached arXiv sources citing Brasseur's paper were also searched in full
text. No later answer or matching proof was found. Novelty confidence is
moderate because this was not an exhaustive MathSciNet/zbMATH or citation-
graph priority search.

## Human-review focus

- Verify the averaging constant in the cumulative-spreading lemma.
- Verify the Stieltjes integration-by-parts formula and disappearance of the
  lower boundary term.
- Verify that the source's inhomogeneous Besov norm differs only by a term
  annihilated by `(1-r)^(1/q)`.
- Confirm that the mollification argument produces a representative with the
  claimed Lipschitz constant for an `L^infinity` equivalence class.
- Confirm the scope: this fully answers Remark 2.13, but does not claim an
  exact limit or optimal constants.
