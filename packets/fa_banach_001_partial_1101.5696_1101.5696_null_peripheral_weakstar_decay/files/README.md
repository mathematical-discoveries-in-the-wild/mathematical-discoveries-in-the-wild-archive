# Partial result: null peripheral spectrum forces the decay in Question 5

Status: `partial_result_likely_valid`

Source paper: Matthew Daws, Richard Haydon, Thomas Schlumprecht, and Stuart White, "Shift invariant preduals of ell_1(Z)", arXiv:1101.5696.

Packet path: `runs/fa_banach_001/solutions/partial/1101.5696_null_peripheral_weakstar_decay/`

## Extracted Question

Question 5 on PDF page 29 asks which elements `a in ell_1(Z)` occur as weak-star limit points of the point masses `{delta_n : n in Z}` for a shift-invariant predual, and in particular whether
`lim_n ||a^n||_infty = 0`
is necessary as well as sufficient.

## Result

Let `a in ell_1(Z)` occur as such a weak-star limit point, and let
`f(z)=sum_k a(k) z^k` be its Fourier transform. If the peripheral set
`{z in T : |f(z)|=1}` has Haar measure zero, then
`||a^n||_infty -> 0`.

Consequently the necessity part of Question 5 is affirmative for every finitely supported non-point-mass weak-star limit candidate.

## Scope

This is not a full solution of Question 5. The remaining case is an infinite-support power-bounded element of the Wiener algebra whose Fourier transform has unit modulus on a positive-measure set. The previous attempt had isolated power-boundedness; this packet records the clean null-peripheral completion and the finite-support corollary.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of Question 5.

## Novelty/duplicate Check

Cheap indexes were searched for `1101.5696`, `Shift invariant preduals`, `ell_1(Z)`, `weak star`, and nearby predual keywords. The only existing hit was the earlier unfinished attempt `runs/fa_banach_001/attempts/1101.5696_weakstar_limit_power_decay.md`; no solution packet was present. A bounded web search for power-bounded Wiener-algebra and convolution-power concentration keywords did not reveal an exact full answer during this pass.

## Human Review Recommendation

Check the finite-support corollary's Laurent-polynomial inner-function step and confirm that the source Proposition 4.6 exclusion of unimodular point masses covers translates by shift-invariance. The core Plancherel argument is short and should be easy to verify.
