# Counterexample Packet: Dyadic Averages Separate `I` from `closure(J)`

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `1512.07483`
- source paper: Jochen Glueck, *Growth rates and the peripheral spectrum of
  positive operators*
- target passage: PDF page 10, Remarks 4.5(c), asking whether the ideal `I`
  from Lemma 4.4 always coincides with `closure(J)` when `(S_n)` is not norm
  bounded.

## Claim

The equality `I = closure(J)` can fail. In fact, on `E=L^1[0,1]` there is an
unbounded sequence of positive operators `(S_n)` for which

```text
J = {f in L^1 : ||S_n |f|||_1 -> 0} = {0},
```

but the constant function `1` belongs to

```text
I = {f : exists f_n -> f in L^1 with ||S_n |f_n|||_1 -> 0}.
```

Thus `closure(J) = {0}` is a proper subset of `I`.

## Construction

Enumerate the dyadic intervals

```text
D_{k,j} = [(j-1)2^{-k}, j2^{-k}), 1 <= j <= 2^k,
```

level by level. For `D=D_{k,j}`, define the positive rank-one operator

```text
S_D f = 2^k (integral_D f) * 1_[0,1].
```

Then `||S_D |f|||_1` is exactly the average of `|f|` over `D`.

For `f=1`, choose `f_D = 1_[0,1]\D`. Then `||f_D-1||_1 = |D| -> 0` and
`S_D |f_D| = 0`, so `1 in I`. On the other hand, if `g in J`, the averages of
`|g|` over all sufficiently fine dyadic intervals tend uniformly to zero.
The dyadic differentiation theorem forces `g=0` almost everywhere.

## Files

- `main.tex`: full counterexample packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:1512.07483
- `figures/open_problem_crop.png`: crop of Remarks 4.5(c)
- `code/verify_dyadic_counterexample.py`: finite-level sanity check for the
  construction

## Novelty Check

Before promotion, the agent searched the run indexes for `1512.07483`,
`Growth rates and the peripheral spectrum`, `Lemma 4.4`, `I coincides with
closure J`, `positive operators S_n`, and related Banach-lattice ideal phrases.
No prior packet or attempt addressed this target.

External web searches for the exact question phrases, including `"The author
does not know whether" "I coincides with" "overline{J}"`, `"Growth rates and
the peripheral spectrum" "I coincides" "J"`, and `"S_n|x_n|" "S_n|x|"
"closed ideal" Banach lattice`, found no explicit later answer in this bounded
pass.

Human review should focus on the passage from `J` to uniform vanishing of
dyadic averages by level, and on the application of the dyadic differentiation
theorem to conclude `J={0}`.
