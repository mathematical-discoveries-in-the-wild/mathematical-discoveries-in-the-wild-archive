# Integer Spectra via Rational Chambers

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Bernard Helffer, Thomas Hoffmann-Ostenhof, and Philipp Marquetand, “On
  maximal multiplicities for Hamiltonians with separable variables,”
  arXiv:1908.02752 (2019).
- Target: Conjecture 1.4 on page 4.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The packet proves that for every real admissible matrix `A`, every number of
rows `N`, and every spectral position `k`, there is an integer matrix `B` with

```text
m(k,B) = m(k,A).
```

This is stronger than equality of the two suprema in Conjecture 1.4.

After normalizing the first entry of every row to zero, only finitely many
entries can contribute at or below the `k`-th spectral level. Equalities and
strict order relations among their tuple sums form a relatively open chamber
in a rational linear subspace. A rational point in the same chamber preserves
the entire finite multiplicity pattern; clearing denominators makes the
prefixes integral, and sufficiently large increasing integer tails complete
the construction.

## Files

- `main.tex`: complete proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source image containing Conjecture 1.4.
- `verification.md`: mathematical and render verification notes.
- `tmp/`: LaTeX intermediates and page renders used for QA.

## Novelty check

Bounded local-index and web searches on July 22, 2026 used arXiv:1908.02752,
the exact source title and conjecture wording, the authors, and combinations
of “integer entries,” “maximal multiplicities,” “separable variables,” and
“rational chamber.” They found no direct answer or later resolution. Novelty
confidence is moderate pending specialist review.

## Human review focus

Please check:

- the interpretation of the source’s standing discreteness/unboundedness
  convention;
- preservation of the complete multiplicity-counted finite spectral order;
- the integer-tail extension and exclusion of new low spectral sums.
