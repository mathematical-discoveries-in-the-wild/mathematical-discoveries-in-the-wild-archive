# Verification Notes

Status: candidate full solution, likely valid pending expert review.

## Mathematical checks

- Rowwise translation to first entry zero preserves every spectral
  multiplicity and ordering.
- Under the source’s discrete unbounded model, every row has only finitely
  many entries below a fixed spectral target.
- Every equality among visible tuple sums is an integer-coefficient homogeneous
  linear equation.
- Every strict ordering and every row gap is an open sign condition for an
  integer-coefficient linear form.
- The equality locus is a rational subspace, hence has dense rational points.
- Clearing denominators preserves all zero and sign conditions.
- Integer tails start strictly above the preserved target, so no new tuple can
  enter the first `k` spectral positions after normalization.
- The proof is pointwise and does not assume that the real supremum is
  attained.

## Computational status

No computation is part of the mathematical proof.

## Render status

`solution_packet.pdf` compiled to five pages with no LaTeX warnings,
undefined references, overfull boxes, or underfull boxes. All five pages were
rendered to PNG and visually inspected at final resolution. A stray escaped
spacing command found in the first render was corrected and the affected page
was re-rendered; the final packet has no clipping, overlap, broken glyphs, or
illegible material. The source crop was checked against Conjecture 1.4 on page
4 of the source PDF.
