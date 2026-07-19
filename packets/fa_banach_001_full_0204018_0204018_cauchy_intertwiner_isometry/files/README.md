# Cauchy intertwiner isometry (arXiv:math/0204018)

**Status:** candidate full solution to Section 3.4, Open Problem (i), subject to
human review.

The source asks to choose norms for which its hyperbolic Cauchy formula
(W_\sigma), equation (3.3.23), is an isometry from
(F_2(\widetilde T)) onto (H_\sigma(\widetilde D)).  The source already
records the three inputs needed for a short completion: the principal-value
operator is bounded, it intertwines the two unitary realizations, and those
representations are irreducible.

For any bounded nonzero intertwiner (W) of irreducible unitary
representations, (W^*W) commutes with the source representation.  Its
spectral projections therefore define invariant subspaces, so irreducibility
forces (W^*W=cI) for a scalar (c>0).  Hence

\[
  \|Wf\|=\sqrt c\,\|f\|,
\]

the range is closed, and irreducibility of the target makes that nonzero
closed invariant range the whole target.  Giving the Hardy realization the
renormalized norm (c^{-1/2}\|\cdot\|) makes the original Cauchy formula an
onto isometry.  If the even-Clifford realization is displayed as several
irreducible sectors, the identical argument normalizes each sector by its own
positive scalar.

The proof uses the appendix's bounded principal-value extension, so it does
not incorrectly treat the singular vacuum vector as an (L^2) vector.

## Files

- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page 47 (PDF page 48), including
  the complete statement of Open Problem (i).
- `main.tex`: packet source; all build intermediates are in `tmp/`.

## Review focus

Verify that the chosen value of (\sigma) is in the irreducible unitary
range asserted in the source.  At a reducibility parameter, apply the stated
sectorwise version after decomposing the representation; one global scalar is
then not claimed.  The result answers only item (i); items (ii) and (iii) in
Section 3.4 remain open here.

## Novelty check

The run indexes and targeted web/arXiv searches through 2026-07-19 used the
exact title, exact problem language, `Cauchy formula isometry principal
series`, `H_sigma Hardy Kisil`, and the author's name.  They found the source,
the 1997 precursor on principal function theory, and later surveys, but no
paper explicitly resolving item (i).  The mechanism is the standard unitary
intertwiner/commutant argument, so novelty confidence is modest even though no
explicit answer was located.

Ledger: `runs/fa_banach_001/ledger/results/0204018_cauchy_intertwiner_isometry.json`.
