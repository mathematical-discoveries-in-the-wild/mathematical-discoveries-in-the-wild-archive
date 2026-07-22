# Schatten Rhaly matrices for every positive exponent

Status: `full_solution_likely_valid`

Source: Carlo Bellavita, Eugenio Dellepiane, and Georgios Stylogiannis,
*Boundedness, compactness and Schatten class for Rhaly matrices*,
arXiv:2503.21930v3. The open question occurs in Section 7 on source PDF
page 36.

## Claimed contribution

For every `q>0`, define `N_alpha(epsilon)` as the length of the source
paper's greedy `(epsilon,L)` sequence and

`Phi_q(alpha) = q integral_0^infinity epsilon^(q-1) N_alpha(epsilon) d epsilon`.

For every bounded Rhaly matrix `R_alpha`, the packet proves

`sum_m a_m(R_alpha)^q` is comparable, with explicit constants, to
`||R_alpha||^q + Phi_q(alpha)`.

Consequently, `R_alpha` belongs to `S^q` exactly when it is bounded and
`Phi_q(alpha)<infinity`. Boundedness itself is the source's explicit dyadic
condition `sup_k sigma_k<infinity`. This gives a complete coefficient-side
characterization for all `q>0`, and in particular resolves the source's
missing range `0<q<=1`.

## Proof mechanism

The source's Lemma 4.3 shows that a greedy sequence of length at least `N`
forces `a_N >= epsilon/sqrt(2)`. Its Lemma 4.2 shows that finite length `N`
forces `a_(2N+2) <= epsilon/sqrt(2)`. Hence the singular-value counting
function and the greedy length sandwich each other after fixed rescalings.
The layer-cake identity converts this pointwise counting comparison into the
two-sided Schatten estimate for every positive exponent.

The endpoint divergence in the source's `q>1` argument appears only when it
further bounds the greedy count by a harmonic sum of dyadic coefficient
counts. Retaining the greedy count itself removes that loss.

## Verification and limitations

The proof is non-computational. `VERIFICATION.md` checks the count/index
conventions, extended-infinite cases, layer-cake constants, and the necessary
rank-one operator-norm term.

The result is an exact greedy-counting characterization. It does not prove
that the simpler dyadic Besov expression from the `q>1` theorem remains
sufficient when `q<=1`.

## Novelty search

The bounded search on 2026-07-22 covered the run's four cheap indexes; exact
title and arXiv-id searches; Rhaly/terraced matrices with Schatten endpoints,
approximation numbers, and `(epsilon,L)` sequences; the current source; and
the June 2026 factorable-matrix follow-up arXiv:2606.15875. The follow-up
still restricts its Schatten characterizations to `1<p<infinity`. No later
paper stating this counting criterion or resolving the endpoint question was
found. Novelty confidence is moderate.

## Files

- `solution_packet.pdf`, `main.tex`: complete theorem and proof.
- `source_paper.pdf`: arXiv:2503.21930v3.
- `figures/open_problem_crop.png`: source PDF page 36 evidence.
- `VERIFICATION.md`: adversarial proof audit.
- `code/crop_source_evidence.py`: reproducible screenshot crop.
