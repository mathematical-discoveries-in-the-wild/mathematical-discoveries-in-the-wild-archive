# No-Small-Alias Calderon Sum Subcase

Status: `partial_result_likely_valid`

Source paper: Ulrik Enstad and Jordy Timo van Velthoven, *On the Calderon sum formula for wavelet systems*, arXiv:2602.10766.

Packet path: `runs/fa_banach_001/solutions/partial/2602.10766_no_small_alias_calderon_sum/`

## Result

The source quotes the Bownik--Lemvig/Speegle conjecture that a Parseval affine wavelet system should satisfy the Calderon sum formula. The source proves this under an added regularity condition `\psi \in \mathcal B_\pi`.

This packet proves the conjectured Calderon formula without the `\mathcal B_\pi` assumption under the arithmetic no-small-alias condition

```tex
\delta(A,P):=\inf_{j\in\mathbb Z,\;m\in\mathbb Z^d\setminus\{0\}}
\|(A^jP)^{-t}m\|>0.
```

Equivalently, the reciprocal translation lattices appearing at the different wavelet scales have no nonzero vectors accumulating at the origin.

## Main Idea

Choose Fourier supports contained in cubes of diameter smaller than `\delta(A,P)`. For such test functions, no nonzero alias from any dual translation lattice can meet the support at any scale. The lattice Parseval identity for each fixed scale therefore collapses to its diagonal term. Summing over all scales and using the Parseval frame identity gives the Calderon sum formula locally on each small cube, hence a.e. on `\mathbb R^d`.

## Scope

This is a genuine subcase of the source conjecture, not a full solution. The condition is useful for lattice-automorphism/no-small-alias regimes, for instance when the dual lattices `(A^jP)^{-t}\mathbb Z^d` remain uniformly discrete. It does not cover expansive dilations, where reciprocal lattice vectors typically approach zero and alias-free localization is impossible.

## Files

- `main.tex` - proof packet source.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - local copy of arXiv:2602.10766.
- `figures/open_problem_crop.png` - crop of Conjecture 1.1 in the source paper.

## Verification

The packet was rendered with `latexmk -pdf`. The proof is analytic and does not use computational verification.
