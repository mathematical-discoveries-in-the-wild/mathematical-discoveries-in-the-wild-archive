# Inverse-series coefficient pattern: negative correction

Status: **literature_implied_answer (negative correction of Research Problem 1 as printed)**.

Original source: Frank Oertel, *Grothendieck's inequality and completely
correlation preserving functions -- a summary of recent results and an
indication of related research problems*, arXiv:2010.00746v2 (2020), Section
5.1, source PDF pages 13--15.

Supporting source: Frank Oertel, *Upper bounds for Grothendieck constants,
quantum correlation matrices and CCP functions*, arXiv:2305.04428v4 (2025
revision), Section 9.1, supporting PDF pages 116--120.

## Identification

Research Problem 1 asks for a proof of a proposed simplification of the
Lagrange-inversion formula in which every monomial in the `k`-th block has a
single common coefficient `m_k`. The proposal is false already for `n=5`.
The source's own displayed coefficient gives

```text
5 beta_5 alpha_1^9 =
  -5 alpha_1^3 alpha_5
  +30 alpha_1^2 alpha_2 alpha_4
  +15 alpha_1^2 alpha_3^2
  -105 alpha_1 alpha_2^2 alpha_3
  +70 alpha_2^4.
```

In the proposed form, both degree-six monomials in the `k=2` block must come
from `15 m_2 alpha_1^2 p_2`, so they would have the same coefficient. They
instead have coefficients 30 and 15. Equivalently,
`B^o_{4,2}(alpha_2,alpha_3,alpha_4) =
2 alpha_2 alpha_4 + alpha_3^2`; the multinomial weights cannot be replaced by
one common multiplier.

The later supporting paper silently removes the uniform-coefficient proposal
and gives the correct multinomial Bell-polynomial formula, together with a
determinantal representation. It does not explicitly announce a negative
answer to the 2020 problem, so this is an agent-identified literature
implication rather than an explicit literature answer.

## Scope

Only the proposed representation in item (1-RP1) is refuted. The standard
Lagrange--Bürmann/Bell-polynomial formula remains correct, and the broader
computational questions about inverse coefficients and Grothendieck bounds
are unaffected.

## Verification

Run:

```bash
python code/check_n5.py
```

The script checks the two partitions of 4 into two parts and confirms the
unequal multiplicities 2 and 1. This is a finite symbolic check, not a
numerical experiment.

## Search evidence

The run indexes were searched for arXiv:2010.00746, the paper title, Bell
polynomials, and inverse-series terms. A bounded web search on 21 July 2026
found papers about special Bell-polynomial values but no exact published
discussion of the failed uniform-`m_k` ansatz. The author's expanded sequel
arXiv:2305.04428 was then inspected locally; it provides the corrected exact
formula and is decisive for the literature-implied classification.

