# Full Packet: Nontrivial Type Is Not Needed at the Lattice Endpoint

- status: candidate full solution, likely valid
- run: `fa_banach_001`
- source arXiv id: `1508.02036`
- source paper: Jan Rozendaal, *Functional calculus for C_0-groups using (co)type*
- target passage: PDF page 22, after Theorem 6.3, where the author writes: "We do not know whether the assumption in Theorem 6.3 that X has nontrivial type is necessary."

## Claim

The nontrivial type assumption in Theorem 6.3 is not necessary in the natural missing endpoint case. The theorem extends to `p=1`: if `X` is isomorphic to a complemented subspace of a `q`-concave Banach lattice, `2 <= q < infinity`, then the same endpoint `R`-bounded operator-valued calculus holds with exponent `1 - 1/q`.

In particular, `X=L^1[0,1]` is an explicit no-nontrivial-type example where the conclusion holds.

## Idea of the Proof

Rozendaal's proof for `p>1` needs one uniform input: `Rad^n(X)` must sit complementedly in a suitable lattice with constants independent of `n`. The paper obtains this from Pisier's `K`-convexity characterization, hence from nontrivial type.

For Banach lattices of finite cotype, this uniform input can be obtained directly. If `Y` is `q`-concave, then `Rad^n(Y)` is uniformly isomorphic to the lattice `Y(ell_2^n)` with norm

```text
||(y_k)|| = ||(sum_k |y_k|^2)^{1/2}||_Y.
```

The lattice `Y(ell_2^n)` is again `q`-concave with constant independent of `n`, because pointwise `ell_q(ell_2) <= ell_2(ell_q)` for `q >= 2`. Complemented subspaces pass through `Rad^n` coordinatewise. This supplies exactly the missing uniformity and the rest of the original proof goes through.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:1508.02036
- `figures/open_problem_crop.png`: crop of the source passage
- `code/make_open_problem_crop.py`: reproducible crop script

## Novelty Check

The run indexes were searched for `1508.02036`, the source title, `second R-bounded calculus`, `nontrivial type`, `K-convex`, `Rademacher projection`, and functional-calculus/transference keywords. Only adjacent Fourier multiplier and transference packets appeared. Web searches on 2026-06-20 for exact phrases around the source sentence and theorem found the source paper and related multiplier papers, but no later answer to this endpoint question.

Human review should focus on the square-function model for `Rad^n(Y)` and the claim that its `q`-concavity constants are independent of `n`.
