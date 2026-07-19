# Radial-Twist Counterexample to the Coarse-Sum Coordinate Problem

Result type: `counterexample`

Status: human reviewed; appears correct.

Source paper:

- Bruno de Mendonca Braga, "Asymptotic structure and coarse Lipschitz
  geometry of Banach spaces", arXiv:1604.08661; Studia Mathematica 237
  (2017), 71-97.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Problem 5.7 asks whether every coarse Lipschitz embedding
`f=(f_1,f_2): X -> Y_1 \oplus Y_2` has an infinite-dimensional subspace
`X_0` such that one coordinate `f_i|_{X_0}` is again a coarse Lipschitz
embedding.

The packet gives a negative answer. Take `X=Y_1=Y_2=ell_2` and define

`F(x) = (cos(theta(||x||)) x, sin(theta(||x||)) x)`,

where `theta(r)` is a slowly varying triangular wave in `log(1+r)`.
The full map `F: ell_2 -> ell_2 \oplus_2 ell_2` is bi-Lipschitz, hence
a coarse Lipschitz embedding. But on infinitely many large spheres one
coordinate is identically zero, and on infinitely many other large
spheres the other coordinate is identically zero. Since every nonzero
linear subspace contains vectors of every radius, neither coordinate
coarsely embeds any infinite-dimensional subspace.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered proof packet.
- `human_review.tex`: human verification note.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: rendered packet followed by the human review.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of
  Problem 5.7 from page 20 of the source PDF.
- `code/check_radial_twist.py`: finite-dimensional numerical sanity
  check for the bi-Lipschitz estimates and coordinate collapses.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Rebuild

From this folder:

```bash
conda run -n sandbox python code/check_radial_twist.py
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

## Human Review Notes

The proof has been manually checked and appears correct. The main review
points are:

- the target sum is explicitly taken as the Hilbert two-sum; if the
  source paper's convention is the `ell_1` two-sum, the same example
  still works because the two norms are equivalent on `Y_1 x Y_2`;
- the coordinate failure is not a finite-dimensional artifact: the same
  antipodal collapse happens inside every nonzero linear subspace;
- the novelty check found the source paper and related coarse-Lipschitz
  papers, but no exact later answer to Problem 5.7.
