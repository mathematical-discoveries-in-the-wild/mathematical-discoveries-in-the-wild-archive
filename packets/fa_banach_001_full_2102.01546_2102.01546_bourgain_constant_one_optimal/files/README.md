# Full Result: Optimal Bourgain Constant One

Status: human reviewed; proof appears correct.

Source: Jose Rodriguez, "`epsilon`-weakly precompact sets in Banach spaces", arXiv:2102.01546.

Open question: Question 2.21 asks whether the constant `2` is optimal in Theorem 2.11, the quantitative Bourgain-Maurey-Pisier theorem for uniformly integrable Bochner `L_1` selectors.

## Claim

The constant `2` is not optimal. The theorem holds with the optimal constant `1`:

- if `F(omega)` is `epsilon`-weakly precompact a.e., no uniformly integrable selector sequence can be an `ell_1` sequence with constant `C > epsilon/2`;
- every uniformly integrable subset of `S_1(F)` is `epsilon`-weakly precompact in `L_1(mu,X)`.

The constant `1` is sharp, already on a one-point probability space with the scaled unit vector basis in `ell_1`.

## Main idea

Rodriguez's Lemma 2.17 centers the scalar sequence
`<z_n, phi(t)>` at its `liminf`, losing the full scalar oscillation `epsilon`.
Centering instead at

```text
(limsup <z_n, phi(t)> + liminf <z_n, phi(t)>)/2
```

and applying Rodriguez's own reverse Fatou Lemma 2.13 gives an `epsilon/2`
bound. The rest of the proof of Theorem 2.11 then runs unchanged, with the
Behrends/Kalenda-Pfitzner-Spurny endpoint handled by applying the improved
`ell_1` exclusion to every `epsilon' > epsilon`.

## Files

- `main.tex`: self-contained solution packet source.
- `solution_packet.pdf`: rendered packet.
- `human_review.tex`: human verification note source.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: solution packet followed by the human verification
  note.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: rendered crop containing Question 2.21.

## Novelty check

Bounded web searches on 2026-06-13 for exact phrases around arXiv:2102.01546,
Question 2.21, Theorem 2.11, the Bourgain constant, Bourgain-Maurey-Pisier,
and weakly conditionally compact sets in `L^1_X` found Rodriguez's source paper
and related background, but no later explicit resolution of Question 2.21.

## Human review

Human review completed. The proof appears correct. The critical line is the
midpoint-Fatou replacement for Lemma 2.14 inside Lemma 2.17: the original proof
centers at an endpoint of the scalar cluster interval, while the corrected
proof centers at its midpoint and therefore controls the error by the average,
or half, oscillation. Once this is done, the rest of the argument is essentially
the proof from the original paper, with the final sharpness example supplied by
the scaled unit vector basis of `ell_1`.
