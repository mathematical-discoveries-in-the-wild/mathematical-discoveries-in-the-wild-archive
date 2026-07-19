# Balanced simplex joins interpolate the endpoint examples

status: partial_result_likely_valid
model: GPT5.6
source_arxiv_id: 2509.13898
source_location: Remark 2, page 2; Lemma 12, equations (24)--(26), page 10
agent_id: agent_lane_04

## Claimed contribution

For every `n >= 1` and `1 <= r <= n`, there is an `n`-dimensional convex
polytope with exactly `n+r` vertices and isoperimetric quotient comparable,
up to universal constants, to

```text
n / sqrt(r).
```

The construction is the `ell_1`-sum (join) of `r` regular simplices in
balanced dimensions `b_i`, scaled to inradius `1/sqrt(b_i)`.  It interpolates
exactly between a regular `n`-simplex (`r=1`, quotient of order `n`) and the
`n`-dimensional cross-polytope (`r=n`, quotient of order `sqrt(n)`).

Equivalently, if `I_n(beta)` denotes the infimum of the isoperimetric quotient
over `n`-polytopes with `beta` vertices, then

```text
I_n(n+r) <= C n/sqrt(r),   1 <= r <= n.
```

Together with classical isoperimetry this gives
`c sqrt(n) <= I_n(n+r) <= C n/sqrt(r)`.  The matching interpolating lower
bound remains open.

## Why this is only partial

Remark 2 asks how the universal lower bound should interpolate for every
polytope with `n+1 < beta < 2n` vertices.  This packet supplies an explicit
upper construction for the extremal infimum and hence a candidate scale; it
does not prove that every such polytope has quotient at least
`c n/sqrt(beta-n)`.

## Proof mechanism

For balanced positive integers `b_1+...+b_r=n`, let `Delta_i` be a regular
`b_i`-simplex centered at the origin and scaled to inradius
`h_i=1/sqrt(b_i)`.  Lemma 12 of the source gives the vertex count, volume, and
surface area of their join.  The regular-simplex volume formula reduces these
quantities to

```text
V(K) = (1/n!) product_i (b_i+1)^((b_i+1)/2),
S(K) = n sqrt(n) V(K).
```

Consequently

```text
iq(K) = n sqrt(n)
        [product_i (b_i+1)^((b_i+1)/2) / n!]^(1/n).
```

Balancing the `b_i` makes the product factor comparable to `sqrt(n/r)`, and
Stirling's formula completes the estimate.

## Verification and novelty status

- Endpoint substitution recovers the source's exact simplex and
  cross-polytope formulas.
- `code/verify_formula.py` checked all `125250` pairs with
  `1 <= r <= n <= 500`, including vertex counts and the normalized quotient.
  This is a consistency check, not evidence replacing the proof.
- Exact arXiv/title/formula searches and the run's four lightweight indexes
  found no statement of this `n/sqrt(r)` join construction as of 2026-07-19.
  The search was bounded and did not include a complete MathSciNet or
  zbMATH citation audit, so novelty confidence is moderate rather than final.
- The construction is a new application of the source paper's own Lemma 12;
  the source applies that lemma later to symmetric cube blocks with at least
  `2n` vertices, not to the open `n+r` interpolation range.

## Files

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: original paper.
- `figures/open_problem_crop.png`: full-width source crop of Remark 2.
- `verification.md`: adversarial verification report.
- `code/verify_formula.py`: exact-log numerical consistency audit.
- `code/crop_source.py`: reproducible source-crop script.

## Human review focus

The decisive checks are that the non-symmetric part of source Lemma 12 really
applies to regular simplices (only its later affine-minimality clause requires
origin symmetry), and that the balanced-product estimate is uniform when
`r` is close to either endpoint.
