# Type-I hypergraph norms satisfy the conjectured Hanner inequality

status: full_solution_likely_valid
model: GPT5.6
source_arxiv_id: 0903.3237
source_location: Conjecture 3.15, page 25
agent_id: agent_lane_04

## Claimed contribution

Conjecture 3.15 of Hatami's paper is true. If `H` is a semi-norming
hypergraph pair of Type I with parameter `s >= 2`, then every `L_H` space
satisfies the `|H|`-Hanner inequality. The proof does not need the source's
non-factorizability assumption.

For `q=|H|` and all `f,g in L_H`,

```text
||f+g||_H^q + ||f-g||_H^q
    <= (||f||_H+||g||_H)^q + | ||f||_H-||g||_H |^q.
```

## Proof mechanism

Write `m` for the support size of `H`, so `q=ms`. Expand the product
`product_omega (f_omega+g_omega)` into the sum `E` of its even-degree terms
and the sum `O` of its odd-degree terms. The products with minus signs are
then `E-O`.

1. Apply the classical `s`-Hanner inequality in the ordinary `L_s` space
   to `E,O`.
2. Apply Hatami's generalized Holder lemma to every mixed monomial. If the
   monomial contains `k` copies of `g`, its `L_s` norm is at most
   `||f||_H^(m-k) ||g||_H^k`.
3. Sum separately over even and odd `k`. These are the even and odd parts
   of the binomial expansion.
4. The function `(x,y) -> (x+y)^s+|x-y|^s` is increasing in both variables
   on the nonnegative quadrant. Substitution of the two binomial sums gives
   exactly the conjectured right-hand side.

## Verification

- Every exponent and use of the source Holder lemma is audited in
  `verification.md`.
- The argument works for real or complex functions because the classical
  Hanner inequality is valid for complex `L_s` spaces.
- A numerical adversarial search on the first non-even diagnostic,
  the Type-I `C4` norm with `s=3`, found no positive defect in 500,000 random
  matrix pairs; differential evolution converged to equality up to
  `3.1e-15`. This is only a consistency check.
- Exact phrase and theorem searches found the source and its thesis version,
  but no later proof of Conjecture 3.15. The novelty check is bounded rather
  than a complete bibliographic audit.

## Files

- `main.tex` and `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: Hatami's source paper.
- `figures/open_problem_crop.png`: source excerpt containing Conjecture 3.15.
- `verification.md`: adversarial proof review.
- `code/search_c4_hanner.py`: finite-dimensional numerical diagnostic.
- `code/crop_source.py`: reproducible source crop.

## Human review focus

The decisive step is the coordinatewise monotonicity of
`F_s(x,y)=(x+y)^s+|x-y|^s`, which permits replacing the norms of the even and
odd expansions by their separate binomial upper bounds. Without that
monotonicity, the ordinary triangle inequality would not be enough.
