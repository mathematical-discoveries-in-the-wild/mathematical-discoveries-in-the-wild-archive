# 2209.05986 odd discrete tori explicit ONB and X_p inequality

Status: `full_result_likely_valid`

Run: `fa_banach_001`
Agent: `agent_lane_04`
Lane: 1
Date: 2026-07-18

## Source

Antonio Ismael Cano-Marmol, Jose M. Conde-Alonso, and Javier Parcet,
"Trigonometric chaos and X_p inequalities I -- Balanced Fourier truncations
over discrete groups", arXiv:2209.05986.  The arXiv preprint later appeared in
Analysis & PDE 17(7), 2561-2584, 2024.

## Extracted Signal

Remark 2.4 asks whether the odd-cardinal cyclic case changes the preceding
even-cardinal discrete-torus picture, and says that an explicit orthonormal
basis for the cocycle Hilbert space of `Z_{2m+1}^n` is more tedious and left to
the interested reader.

## Result

The packet gives an explicit real Fourier-mode orthonormal basis for the
cocycle Hilbert space associated with the odd-cycle word length on
`Z_{2m+1}^n`.  The basis also shows that the coordinate subspaces are invariant
under the cocycle action, that the coordinate support derivatives
`partial_j lambda(g) = 1_{g_j != 0} lambda(g)` are distinguished, and therefore
that the same balanced Fourier-truncation `X_p` inequality as in the even
case follows from the source paper's Theorem B.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of the source arXiv PDF.
- `figures/open_problem_crop.png`: source crop of Remark 2.4.
- `code/verify_odd_cycle_onb.py`: numerical Gram and coefficient checker.

## Verification

The verifier checks odd cycles `N=3,5,7,9,11` and products with
`n=1,2,3`, confirming the ONB Gram matrix, the closed form for the negative
Fourier coefficients, and the derivative coefficient formulas up to floating
point tolerance.

Human review should focus on the normalization of the Fourier modes and on the
short passage from the explicit ONB to the source theorem's distinguished
derivative hypothesis.
