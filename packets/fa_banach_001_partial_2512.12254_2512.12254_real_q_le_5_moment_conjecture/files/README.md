# Partial Solution Packet: Real exponents up to five in the non-negative Hunter moment conjecture

status: partial_result_likely_valid

run: fa_banach_001

target arXiv id: 2512.12254

source paper: Silouanos Brazitikos and Christos Pandis, "Sharp inequalities for symmetric polynomials, Hunter's conjecture, and moments of exponential random variables", arXiv:2512.12254.

## Claim

This packet proves Conjecture 4.8 of the source paper for every dimension and every real exponent

```text
0 < q <= 5.
```

The source conjectures that, for non-negative coefficients `a_i` with `sum a_i^2 = 1` and i.i.d. standard exponentials `X_i`,

```text
E(a_1 X_1 + ... + a_n X_n)^q >= min_{1 <= m <= n} rho(m,q).
```

The packet proves that in the range `0 < q <= 5` the right side is actually `rho(1,q)=Gamma(q+1)`, and every admissible positive linear combination has moment at least `Gamma(q+1)`.

## Main proof inputs

- The source paper's Theorem 4.5 for the integer endpoint `k=5`.
- The source paper's Borell log-concavity lemma for normalized moments of log-concave densities.
- The standard fact, via Prekopa-Leindler, that convolution preserves log-concavity.
- A scalar lemma showing `rho(m,q) >= rho(1,q)` for every integer `m >= 1` and `0 <= q <= 5`.

## Novelty and limitations

Bounded novelty check on 2026-07-18:

- Local run indexes had no prior packet for arXiv:2512.12254 or this Hunter/exponential-moment conjecture.
- Web/arXiv search found the later preprint arXiv:2602.03058, "Moments of sums of exponentials, beyond CHS", whose Schur-monotonicity theorem covers the related `0 <= q <= 4` non-negative-coefficient range.
- The search did not find a separate statement of the `0 < q <= 5` all-dimensional consequence packaged here.

This does not settle the full real-exponent conjecture. The range `q > 5` remains open in this packet. The verifier script also records that the simplest integer-endpoint interpolation strategy falls short just past `q=5`.

## Files

- `main.tex` - solution packet source.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:2512.12254.
- `supporting_context_2602.03058.pdf` - later adjacent paper used only for novelty/boundary context.
- `figures/open_problem_crop.png` - crop of the source conjecture from the source PDF.
- `code/check_q_le_5_endpoint.py` - scalar endpoint/interpolation verifier.

## Human review recommendation

Review as a likely valid partial solution. The key checks are:

1. The use of Theorem 4.5 of arXiv:2512.12254 at `k=5`.
2. The log-concavity of the density of `sum a_i X_i` after zero coefficients are removed.
3. The scalar lemma identifying `rho(1,q)` as the discrete minimum for `0 <= q <= 5`.
