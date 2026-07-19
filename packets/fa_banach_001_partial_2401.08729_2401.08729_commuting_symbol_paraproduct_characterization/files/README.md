# Commuting-symbol characterization for semicommutative martingale paraproducts

Status: **partial result, likely valid; human review recommended**

Source: Zhenguo Wei and Hao Zhang, *Boundedness of operator-valued
commutators involving martingale paraproducts*, arXiv:2401.08729.  The open
question appears on PDF page 2: characterize boundedness of the
semicommutative paraproduct `pi_b` on `L_2(L_infty(R) tensor M)`.

## Result

Let `M` be a semifinite von Neumann algebra and suppose the essential range of
the symbol `b` is contained in one abelian von Neumann subalgebra `A` of `M`.
Then

`pi_b` is bounded on semicommutative `L_2` if and only if `b` has finite column
martingale BMO/Carleson norm, and the two norms are comparable with constants
depending only on the `d`-adic branching number.

In particular this gives a dimension-free necessary-and-sufficient condition
for simultaneously diagonalizable matrix-valued symbols, even when the
ambient algebra and the input functions remain noncommutative.

## Idea of the proof

Left multiplication represents `A` as a commuting family of normal operators
on `L_2(M)`.  The abelian spectral theorem diagonalizes that whole family.
After diagonalization, every finite truncation of `pi_b` is a direct integral
of ordinary scalar martingale paraproducts (tensored with multiplicity
identities).  Its norm is therefore the essential supremum of the scalar
fiber norms.  The column BMO norm is exactly the essential supremum of the
scalar fiber BMO norms.  The scalar Carleson embedding theorem identifies
those two quantities, and uniform truncation finishes the argument.

## Scope and novelty

The result does **not** characterize general noncommuting symbols; that is
where the logarithmic matrix obstruction in the source paper lives.  Local
run indexes and bounded arXiv searches on 2026-07-19 for combinations of
`operator-valued/semicommutative martingale paraproduct`, `commuting symbol`,
`abelian von Neumann algebra`, and `BMO characterization` found no explicit
statement of this subcase.  It may nevertheless be folklore implicit in the
abelian spectral theorem plus the scalar Carleson embedding theorem, so the
novelty confidence is moderate rather than high.

## Review focus

The key point to verify is the passage from finite martingale truncations to
the full paraproduct for general locally integrable symbols, including the
chosen indexing convention for column BMO.  The proof explicitly handles the
one-level indexing discrepancy with constants depending only on `d`.

Files:

- `main.tex` and `solution_packet.pdf`: formal statement and proof.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: the question on source PDF page 2.

