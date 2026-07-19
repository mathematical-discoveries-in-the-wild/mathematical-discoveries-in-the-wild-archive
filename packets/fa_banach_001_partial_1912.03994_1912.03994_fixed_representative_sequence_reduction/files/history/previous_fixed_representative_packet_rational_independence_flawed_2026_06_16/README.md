# Partial Result: Continuous Reduction on Fixed Representative-Sequence Strata

Status: `partial`

Run: `fa_banach_001`

Source paper: arXiv:1912.03994, Marek Cuth, Martin Dolezal, Michal Doucha,
and Ondrej Kurka, "Polish spaces of Banach spaces."

## Claim Recorded

Question 1 of arXiv:1912.03994 asks whether there is a continuous map
`\Phi : P_infty -> B` such that `X_mu` is linearly isometric to
`X_{Phi(mu)}` for every pseudonorm code `mu`.

This packet proves a partial positive result: if one fixes in advance an
infinite sequence of rational basis vectors whose images are linearly
independent and dense in each quotient `X_mu` under consideration, then the
desired reduction is continuous on that stratum.

Equivalently, the obstruction to the full Question 1 is not the quotient
renorming step once representatives are fixed; it is the global continuous
choice of an independent dense representative sequence.

## The Partial Theorem

Let `s = (s_j)` be a strictly increasing sequence of natural numbers. Let
`P_s` be the class of all `mu in P_infty` such that the quotient vectors
`[e_{s_j}]_mu` are linearly independent and have dense linear span in `X_mu`.
Then

```text
Phi_s(mu)(sum_j a_j e_j) = mu(sum_j a_j e_{s_j})
```

defines a continuous map `Phi_s : P_s -> B`, with `P_s` carrying the relative
topology from `P_infty`, and `X_{Phi_s(mu)}` is linearly isometric to `X_mu`
for every `mu in P_s`.

In particular, the same conclusion holds on every fixed coordinate-kernel
stratum where the non-null coordinate complement is fixed in advance.

## Evidence Locations

- arXiv:1912.03994, page 20, Question 1: asks for a continuous reduction from
  `P_infty` to `B`.
- arXiv:1912.03994, page 21, Question 2: asks for the corresponding
  `Sigma^0_2`-measurable reduction from `P_infty` to admissible `SB(X)`.
- arXiv:1912.03994, Proposition 2.7: gives a `Sigma^0_2`-measurable reduction
  by choosing independent coordinates in a non-continuous, lexicographic way.
- arXiv:1912.03994, Theorem 2.11: gives a `Sigma^0_2`-measurable reduction
  from `B` to admissible `SB_infty(X)`.

## Verification

The proof is direct: each output coordinate is a fixed input-coordinate
evaluation, hence continuous; independence of the fixed representatives makes
`Phi_s(mu)` a norm; density of those representatives makes the induced isometry
onto `X_mu`.

The packet PDF was compiled with `latexmk`. The open-question crops were
rendered from `source_paper.pdf` using the script in `code/`.

## Limitations

This does not solve Question 1 or Question 2 globally. It gives a relative
answer only after a representative sequence has been fixed uniformly on the
domain. It does not produce a continuous global selector of independent dense
representatives for arbitrary pseudonorms in `P_infty`.

## Search Notes

Cheap local index searches for `1912.03994`, `P_infty`, `B`, `Question 1`,
`continuous reduction`, and admissible topology terms found no prior packet for
this exact partial result. Web searches on 2026-06-16 found the source paper
and the sequel arXiv:2204.06834, but no exact answer to Question 1 or Question
2. Local inspection of arXiv:2204.06834 found extensive complexity results but
no direct resolution of these two reduction questions.

