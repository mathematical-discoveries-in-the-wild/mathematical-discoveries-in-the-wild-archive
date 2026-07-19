# Consolidated resolution packet for Problem 3.19 and Theorem 3.21

Source: Jan Rozendaal and Mark Veraar, *Fourier multiplier theorems involving
type and cotype*, arXiv:1605.09340.

Status: `partial_result_likely_valid`, consolidated packet.

## What This Packet Contains

This is the single authoritative run packet for the arXiv:1605.09340 Problem
3.19 / Theorem 3.21 story. It consolidates:

- complete scalar classification of Problem 3.19;
- endpoint failures for every nonzero Banach pair `X,Y`;
- repair of Theorem 3.21 by replacing `p in [1,2]` with `1<p<=2`;
- explanation of the printed theorem endpoint conflict;
- latest literature-backed obstruction for the remaining interior range.

## Main Conclusions

For scalar `X=Y=C`, Problem 3.19 holds exactly for
`1<p<=2<=q<infinity`.

For every nonzero Banach pair `X,Y`, the endpoint faces fail:

- `p=1`, finite `q>=2`;
- `1<p<=2`, `q=infinity`.

Thus the only possible remaining range is
`1<p<=2<=q<infinity`.

The repaired Theorem 3.21 holds for `1<p<=2`, `2<=q<infinity` under the stated
lattice hypotheses. The printed `p=1` endpoint is impossible under the stated
weighted gamma-boundedness hypothesis.

## Remaining Open Core

The remaining interior classification appears to require, or bypass, endpoint
Bessel/Triebel-Lizorkin Sobolev-gamma embeddings:

```text
H_p^{d/p-d/2}(R^d;X) -> gamma(R^d;X),
gamma(R^d;Y) -> H_q^{d/q-d/2}(R^d;Y).
```

Known type/cotype theory gives the adjacent Besov embeddings, and later
vector-valued Pitt results give Bochner estimates, but neither closes the
gamma-radonifying endpoint.

## Superseded Artifacts

This packet supersedes the earlier separate packets/notes:

- `solutions/partial/1605.09340_scalar_endpoint_multiplier_failure/`
- `solutions/partial/1605.09340_theorem_3_21_endpoint_repair/`
- `solutions/partial/1605.09340_problem_3_19_endpoint_core_reduction/`
- `proof_gaps/1605.09340_theorem_3_21_scalar_endpoint_conflict/`
- `attempts/1605.09340_problem_3_19_interior_literature_full_push.md`

Those files were moved to the run archive so the lightweight indexes show this
single active packet.

## Files

- `main.tex`: consolidated packet source
- `solution_packet.pdf`: compiled packet
- `source_paper.pdf`: local copy of arXiv:1605.09340
- `figures/`: crops of Problem 3.19, Theorem 3.21, and the proof passage

## Human Review Recommendation

Review the Riesz-potential endpoint proof, the rank-one gamma-boundedness
estimate, and the Sobolev-gamma embedding input in the repaired theorem. If
these pass, this packet should be treated as the only active record for this
target.
