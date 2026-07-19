# Literature-Implied Partial Answer: BAP Point Separation for `FBL^{up p}[E]`

Source: H. Jardon-Sanchez, N. J. Laustsen, M. A. Taylor, P. Tradacete, and V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510.

Supporting paper: T. Oikhberg, *Geometry of unit balls of free Banach lattices, and its applications*, arXiv:2303.05209.

Status: `literature_implied_answer (partial BAP subcase)`, likely valid, pending human review.

## Source Question

Remark 6.2 of the source asks whether the free Banach lattice satisfying an upper `p`-estimate, and more generally `FBL^D[E]`, can be realized as a lattice of functions on the dual ball. Equivalently, it asks whether real-valued lattice homomorphisms separate points.

## Implied Answer

For `1 < p < infinity`, if the Banach space `E` has the bounded approximation property, then the canonical real-valued lattice homomorphisms

```text
hat{x*}: FBL^{up p}[E] -> R,  x* in E*
```

separate the points of `FBL^{up p}[E]`.

The proof combines two ingredients from Oikhberg's later paper:

- finite-dimensional `FBL^{up p}[F]` has a faithful functional representation;
- bounded approximation of `E` gives finite-dimensional lattice-homomorphic shadows of `FBL^{up p}[E]` converging point-norm to the identity.

If an element is invisible to all `hat{x*}`, every finite-dimensional shadow is zero; the shadows approximate the element, so the element is zero.

## Scope

This does not solve the full source question. It covers only the free upper `p`-estimate lattice and only when `E` has BAP. Arbitrary Banach spaces and arbitrary convexity conditions `D` remain open.

## Files

- `source_paper.pdf`: original arXiv PDF for 2101.03510.
- `supporting_paper_2303.05209.pdf`: supporting later paper.
- `figures/open_problem_crop.png`: crop of source Remark 6.2.
- `main.tex`: compact proof/status packet.
- `solution_packet.pdf`: rendered packet.
- `code/make_open_problem_crop.py`: regenerates the crop.
- `tmp/`: LaTeX build intermediates.

## Checks

Cheap indexes and local later sources were searched for the arXiv id, title, free Banach lattices, upper `p`-estimates, point separation, and lattice homomorphisms. No existing run packet for this exact BAP point-separation corollary was found.

## Human Review Focus

Check the finite-dimensional functional representation step and the passage from bounded approximation operators on `E` to point-norm convergence of the induced homomorphic shadows on `FBL^{up p}[E]`.
