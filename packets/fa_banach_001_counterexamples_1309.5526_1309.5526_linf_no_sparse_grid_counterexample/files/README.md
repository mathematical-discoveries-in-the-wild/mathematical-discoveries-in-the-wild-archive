# Counterexample packet: no sparse Euclidean grid in the cube

status: candidate_counterexample_likely_valid

Reviewer orientation: this is the single current packet for Fresen
arXiv:1309.5526, Problem 4, from this run.  An earlier lane-1 partial result
on the logarithmic ceiling has been nested under `superseded_partial/` and is
summarized in the PDF appendix, so reviewers can read one packet without
losing the development trail.

Source: Daniel J. Fresen, "Euclidean arrangements in Banach spaces",
arXiv:1309.5526.

Target: Problem 4 (`Euclidean grid`) asks whether there are a universal
constant `C > 0` and a sequence `omega_n -> infinity` such that every
`n`-dimensional real Banach space admits a basis `(e_j)` satisfying

`||a||_2 <= ||sum a_j e_j|| <= C ||a||_2`

for all `omega_n`-sparse coefficient vectors.

Result: The main problem has a negative answer already for
`X = ell_infty^n`.  More strongly, for each fixed distortion constant `C`,
there is no sequence of dimensions `n_m -> infinity`, sparsities
`k_m -> infinity`, and linear maps `T_m : R^{n_m} -> ell_infty^{n_m}` such
that

`||a||_2 <= ||T_m a||_infty <= C ||a||_2`

for every `k_m`-sparse vector `a`.  Hence no basis choice can make
`omega_n -> infinity` work in Fresen's Problem 4.

Method: The proof uses signed uniform vectors on an intermediate support size
`h = min(k/(64 C^2), sqrt(log n))`.  The upper estimate forces each row to
have only `O_C(h)` entries of size at least `1/sqrt(h)`.  The lower estimate
would force the signed high-coordinate patterns from the `n` rows to cover all
signed `h`-subsets.  A counting estimate shows this is impossible once
`h -> infinity`.

Files:
- `main.tex`: full counterexample note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: stitched crop of Problem 4 from PDF pages 3
  and 4 of the source paper.
- `superseded_partial/1309.5526_linf_sparse_grid_logarithmic_ceiling/`:
  archived copy of the previous partial packet, retained as internal
  provenance for the counterexample.

Relation to prior work: this strengthens and supersedes the previous partial
packet `1309.5526_linf_sparse_grid_logarithmic_ceiling`, which only ruled out
superlogarithmic sparsity.  The PDF appendix records that partial theorem and
explains how the present counting argument removes the remaining
`omega_n = O(log n)` window.  It also subsumes the need to attack the cube
row-polytope frontier separately.

Novelty check: checked run indexes and prior local packets for `1309.5526`,
`Euclidean grid`, `ell_infty`, sparse/logarithmic keywords, and row-polytope
phrases.  External exact-phrase searches for the source problem plus
`ell_infty`, `sparse Euclidean grid`, and `omega_n` did not surface a known
answer.  Novelty confidence is moderate pending human review, since the
argument is elementary but not found in the run memory.

Human review recommendation: verify the counting step and the quantifier
translation from bases of `ell_infty^n` to linear maps `T`.  If correct, this
is a full negative answer to the main Problem 4 as stated.
