# Full Solution Packet: Dense span of continuous convex nc functions

status: full_solution_likely_valid

run: fa_banach_001

target arXiv id: 1905.08436

source paper: Kenneth R. Davidson and Matthew Kennedy, "Noncommutative Choquet theory", arXiv:1905.08436.

## Claim

The packet answers the source paper's question:

```text
For a compact nc convex set K, do convex nc functions in C(K) always span a dense subset of C(K)?
```

The answer is yes. The real linear span of the self-adjoint continuous convex nc functions is norm dense in `C(K)_sa`, and hence the complex linear span is norm dense in `C(K)`.

## Proof mechanism

The proof uses Proposition 7.2.8 of the source paper. That proposition says that two u.c.p. maps on `C(K)` that agree on all matrix-valued convex nc functions must be equal.

If a continuous self-adjoint functional annihilates the scalar convex functions, its Jordan decomposition gives two states that agree on all scalar convex functions. Compressing a matrix-valued convex function by a vector gives a scalar convex function, so the two states agree on all matrix-valued convex functions. Proposition 7.2.8 forces the two states to coincide, so the annihilating functional is zero. Hahn-Banach gives density.

## Novelty and limitations

Bounded novelty check on 2026-07-18:

- Local run indexes had no previous packet for arXiv:1905.08436.
- Local parsed sources and a web search for the exact dense-span formulation found the source paper and the later survey arXiv:2412.09455, but no explicit statement of this dense-span corollary.
- The proof is a short consequence of the source paper's own Proposition 7.2.8, so novelty should be reviewed as "overlooked corollary of the source paper" rather than an independent construction.

This answers the dense-span question. It does not prove the stronger pointwise statement that every element of `C(K)` is exactly a difference of two continuous convex nc functions.

## Files

- `main.tex` - solution packet source.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:1905.08436.
- `figures/open_problem_crop.png` - crop showing the source question and Proposition 7.2.8.

## Human review recommendation

Review as a likely valid full solution. The key checks are:

1. Vector compression of a matrix-valued convex nc function is a scalar-valued convex nc function.
2. The Jordan decomposition argument applies to real continuous functionals on the self-adjoint part of `C(K)`.
3. Proposition 7.2.8 of the source paper can be applied to the normalized positive parts.
