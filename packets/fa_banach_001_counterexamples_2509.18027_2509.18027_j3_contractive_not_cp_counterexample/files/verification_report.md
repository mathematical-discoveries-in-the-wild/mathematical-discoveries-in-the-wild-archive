# Verification report

Status: `candidate_counterexample_likely_valid`

## Exact checks

- The source statement is Conjecture 6.10 on page 21 of arXiv:2509.18027.
- The source's non-dilatable matrix is Example 4.11 on page 13.
- Direct multiplication gives `B0 B0* + B0* B0 = diag(1,1,2/3)`.
- The packet independently proves that `B0` has no equality dilation in any
  dimension by inspecting the blocks of `CC*+C*C=I`.
- The generated matrix-convex set is levelwise compact by finite-dimensional
  conic Caratheodory.
- The separation statement was checked against Theorem 2.2 of Helton, Klep,
  and McCullough, arXiv:1407.8198. The separating monic pencil has size three.
- On a two-by-two generator the pencil is `[[I,Y],[Y*,I]]`, positive exactly
  when `||Y||<=1`.
- Failure at `B0` is failure of 3-positivity by Lemma 5.2 of the source paper.
- Contractivity follows from Theorem 5.1 of the source paper.

## Computational sanity check

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2509.18027_j3_contractive_not_cp_counterexample/code/check_finite_identities.py
```

The script checks only the finite identities. It does not construct the
separator `X`; its existence comes from the cited separation theorem.

Observed output:

```text
B0 Q-residual: 2.220e-16
maximum generator Q-residual: 3.140e-16
finite identity checks passed
```

The five-page PDF was rendered to PNG at 150 dpi and every page was visually
inspected. No clipped text, overlaps, broken symbols, or unreadable figures
were found.

## Remaining review risk

The counterexample is nonconstructive, so no numerical entries for `X` are
given. A reviewer should check the matrix-convex separation conventions and
the tensor-factor flip converting the real two-variable pencil to
`I+B tensor X+B* tensor X*`.
