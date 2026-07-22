# Verification notes

- The open question was checked in the abstract and Introduction of the source
  PDF. The full-width page-1 crop is in `figures/open_problem_crop.png`.
- The source dependencies were checked directly in the TeX/PDF:
  Theorem 3.4 (ordinary range dense in orbit-closed range), Corollary 4.6
  (orbit-closed convexity for selfadjoint `C`), Theorem 5.7 (support of a
  positive maximizer above the essential spectral top), and Proposition 5.12
  (successive spectral-block decomposition of a maximizer).
- Common-tail check: after matching a finite spectral truncation exactly, the
  trace-norm error is at most twice the discarded trace norm. All approximants
  share one fixed tail and their heads lie in one finite-dimensional
  selfadjoint orbit.
- Interior check: the finite-head values plus the fixed tail form a genuine
  subset of the original ordinary range, not merely of its closure. Westwick's
  finite-dimensional convexity theorem therefore fills the chosen triangle
  exactly.
- Boundary check: support gives `P^perp H subset ker X`. When
  `dim ker C=k<infinity`, `q=dim P^perp<=k`. All blocks strictly above the
  essential top contain positive eigenvalues, so the threshold compression
  has kernel dimension exactly `k-q`, independent of the maximizer.
- Infinite-block check: cumulative block dimensions tend to infinity, hence
  the prescribed blocks exhaust all nonzero eigenvalues of `C`. Positivity and
  trace equality force the complementary compression to vanish.
- Path check: the block conjugating unitary commutes with the supporting
  selfadjoint operator. A bounded selfadjoint Borel logarithm stays in the
  commutant, so its exponential path remains on the face; continuity of the
  imaginary trace coordinate gives every intermediate point.
- Degenerate-geometry check: if the closure has affine dimension at most one,
  the ordinary range is path-connected and hence is an interval in that line.
- No computation is used in the proof. The final PDF was compiled with build
  intermediates under `tmp/` and all rendered pages were visually inspected.

