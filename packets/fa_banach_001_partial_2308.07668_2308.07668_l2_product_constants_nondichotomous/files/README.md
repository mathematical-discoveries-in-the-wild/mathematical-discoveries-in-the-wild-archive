# L2 Product Constants and Non-Dichotomy

Status: `partial` result for arXiv:2308.07668.

This packet resolves the Hilbertian subcase `p=2` of the source paper's question about the constants `c_n`, `c`, and dichotomy of the unit sphere of `L_p({0,1}^kappa)`.

## Claim

For every uncountable `kappa <= 2^omega`, with product measure `mu` on `{0,1}^kappa`, the constants from Proposition 55 of the source paper satisfy

```text
c_n = sqrt(2) for every n >= 1, and c = sqrt(2)
```

when `p=2`. Moreover `L_2(mu)` is isometric to the Hilbert space `ell_2(kappa)`, so by Proposition 54 of the source paper its unit sphere is almost dichotomous but not dichotomous:

```text
K^+(S_{L_2(mu)}) = [0, sqrt(2)),   Sigma(S_{L_2(mu)}) = (sqrt(2), 2].
```

## Evidence

- Source paper: `source_paper.pdf`.
- Open-question crop: `figures/open_problem_crop.png`, page 25 of the arXiv PDF.
- Packet PDF: `solution_packet.pdf`.
- Sanity checker: `code/check_l2_constant.py`.

## Scope

This does not solve the exact constants or dichotomy question for `p != 2`. The dichotomy statement for `p=2` is an identification with the source paper's earlier Hilbert-space result; the new packet proof is the direct computation of the `L_2` product constants `c_n`.

## Novelty Check

Checked the run indexes for `2308.07668`, the paper title, and `L_p/L_2` keywords; no duplicate packet was present. A bounded web phrase search for `"We do not know the exact value of c_n" "S_{L_p}" dichotomous` and for the paper title with `c_n L_p` returned no obvious later answer. Novelty confidence is modest because this is an elementary Hilbertian subcase and the source paper already contains the adjacent `ell_2(kappa)` non-dichotomy theorem.

## Human Review Recommendation

Check the conditional-expectation computation proving `c_n <= sqrt(2)` and the identification of `L_2({0,1}^kappa)` with a Hilbert space of density `kappa`. The result is intentionally scoped as a partial subcase.
