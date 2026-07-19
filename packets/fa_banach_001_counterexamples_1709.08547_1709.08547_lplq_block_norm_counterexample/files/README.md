# Counterexample packet: block-norm obstruction for Open Problem 7.6

Status: candidate counterexample likely valid; needs human review of the cited
Guerre--Raynaud fibre representation for positive isometries.

Source paper: Stephan Fackler and Jochen Gluck, "A Toolkit for Constructing
Dilations on Banach Spaces", arXiv:1709.08547.

Targeted open problem: Open Problem 7.6 asks whether the weak operator closure
of the convex hull of all positive invertible isometries on
`L^p([0,1]; L^q([0,1]))` is the full set of positive contractions, or if not,
for a characterization.

Result: for `1 < p,q < infinity` with `p != q`, the closure is not the full
positive contraction cone. A concrete positive contraction is built on a
two-by-two rectangular step sublattice. Its finite compression has block norm
matrix `[[1,1],[0,0]]` when `q > p`, or `[[1,0],[1,0]]` when `p > q`; either
matrix has outer `ell_p` norm strictly larger than one. Every operator in the
WOT-closed convex hull of positive invertible isometries has all such compressed
block norm matrices dominated by an `ell_p` contraction, using the standard
outer/fibre form of positive isometries of `L^p(L^q)`.

Scope: this gives a negative answer to the equality question for `p != q`.
For `p = q`, Fubini reduces the space to scalar `L^p([0,1]^2)`, and the scalar
Greim/Fackler--Gluck argument gives equality. The packet does not give the
requested full characterization when `p != q`.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: rendered arXiv:1709.08547 source.
- `supporting_paper_2408.12755.pdf`: source quoting the relevant
  Guerre--Raynaud form for `L_p(L_q)` isometries.
- `figures/open_problem_crop.png`: crop of Open Problem 7.6.

Human-review focus: verify that the fibre-form representation used in the
separation lemma applies to positive invertible isometries for the full
`1<p,q<infinity`, `p != q`, range. If one wants to avoid that citation, the
same proof remains a rigorous counterexample in any exponent range where that
representation is accepted.
