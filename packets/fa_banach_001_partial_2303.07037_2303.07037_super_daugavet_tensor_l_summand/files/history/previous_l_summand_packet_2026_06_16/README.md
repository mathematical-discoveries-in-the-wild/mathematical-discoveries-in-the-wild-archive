# Partial Result: Super Daugavet Tensor Transfer Through L-Summands

Run: `fa_banach_001`

Source paper: Rainis Haller, Johann Langemets, Yoel Perreau, and Triinu
Veeorg, "Unconditional bases and Daugavet renormings", arXiv:2303.07037.

Target: the open tensor-transfer sentence in Section 3: the authors write that
they do not know whether super Daugavet points pass to projective tensor
products similarly to Daugavet points.

Status: candidate partial result. The packet proves a positive transfer
theorem when the second tensor factor is a one-dimensional L-summand. The
general projective tensor product problem remains open.

## Claim

Let `x` be a super Daugavet point in a Banach space `X`. Let `Y` contain a
unit vector `y` such that

```text
Y = span{y} \oplus_1 Z
```

isometrically. Then `x tensor y` is a super Daugavet point of
`X \widehat{\otimes}_pi Y`.

In particular this applies to `Y = ell_1(Gamma)` and `y=e_gamma`, and to
normalized atom vectors in `L_1(mu)`.

## Packet Files

- `source_paper.pdf`: local copy of the arXiv source paper.
- `figures/open_problem_crop.png`: crop of the tensor-transfer open sentence.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet, if LaTeX rendering succeeds.

## Human Review Recommendation

Check the isometric tensor decomposition
`X \widehat{\otimes}_pi (span{y} \oplus_1 Z)
 = X \oplus_1 (X \widehat{\otimes}_pi Z)` and the net proof of
super-Daugavet stability under `ell_1`-sums. Those are the only real moving
parts.
