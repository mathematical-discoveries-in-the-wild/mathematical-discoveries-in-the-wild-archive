# Counterexample: `S_lambda chi` Need Not Force The Depth-One Criterion

Status: counterexample likely valid.

Source: Nurulla Azamov, *Spectral flow and resonance index*,
arXiv:1604.07006v2, submitted 2016-04-24, revised 2016-07-28.

## Target

After Theorem 2.7, the source asks whether the three equivalent depth-one
criteria for a resonance vector `chi` are also equivalent to:

```text
(iv) S_lambda chi is a resonance vector.
```

Equivalently, since Theorem 2.7 proves that depth at least one is equivalent to
`A_lambda(r_lambda) S_lambda chi = -chi`, the question is whether (iv) implies
that identity.

## Answer

No. The packet gives a 5-dimensional real symmetric example with
`lambda=r_lambda=0`. For the exact Laurent coefficients of

```text
A_0(s) = (H_0+sV)^{-1}V
```

one has a nonzero resonance vector

```text
chi = (0, 1, 0, -2, 1)^T
```

such that `S_0 chi` is again a nonzero resonance vector, but

```text
(A_0 S_0 + I) chi = (0, 2/3, 1/3, -2/3, 1)^T != 0.
```

Thus `S_lambda chi` being a resonance vector does not imply item (iii) of
Theorem 2.7.

## Files

- `main.tex` - human-readable proof packet.
- `solution_packet.pdf` - compiled packet.
- `source_paper.pdf` - source arXiv paper.
- `figures/open_question_crop.png` - source crop containing Theorem 2.7 and the Question.
- `code/verify_counterexample.py` - exact SymPy verifier.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/counterexamples/1604.07006_depth_question_counterexample/code/verify_counterexample.py
```

The verifier recomputes the Laurent coefficients from the full inverse
`(H_0+sV)^{-1}V` and checks all displayed identities.
