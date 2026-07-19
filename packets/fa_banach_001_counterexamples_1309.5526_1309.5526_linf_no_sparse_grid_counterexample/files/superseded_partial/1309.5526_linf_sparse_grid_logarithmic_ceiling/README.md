# Superseded partial packet: logarithmic ceiling from the cube

status: superseded_by_counterexample

This packet is retained only as internal provenance for the current
counterexample packet
`runs/fa_banach_001/solutions/counterexamples/1309.5526_linf_no_sparse_grid_counterexample/`.
The theorem below remains useful history, but it is no longer a separate
top-level current result for Problem 4.

Source: Daniel J. Fresen, "Euclidean arrangements in Banach spaces",
arXiv:1309.5526.

Target: Problem 4 (`Euclidean grid`) asks whether every `n`-dimensional real
Banach space admits a basis on which all `omega_n`-sparse coefficient vectors
have uniformly Euclidean norm distortion, with `omega_n -> infinity`, and asks
whether one can take `omega_n = c log n`.

Result: The order `log n` is a necessary ceiling already for
`X = ell_infty^n`.  More precisely, if a basis of `ell_infty^n` satisfies

`||a||_2 <= ||sum a_j e_j||_infty <= C ||a||_2`

for every `k`-sparse coefficient vector `a`, then
`k <= 2 C^2 log(2n)`.  Thus no positive solution to the main problem can have
`omega_n / log n -> infinity`.  The remaining `omega_n = c log n` question is
therefore the sharp-order frontier.

Scope: This did not prove or disprove the main existence question, and it did
not rule out `omega_n = c log n` for sufficiently small `c`.  The enclosing
counterexample packet now rules out every unbounded sparsity sequence in
`ell_infty^n`, so this partial theorem is superseded.

Files:
- `main.tex`: partial-result note with proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: stitched crop of Problem 4 from PDF pages 3
  and 4 of the source paper.

Novelty check: checked run indexes for `1309.5526`, `Euclidean grid`,
`ell_infty`, and sparse/logarithmic keywords.  External exact-phrase searches
for the source problem did not surface this packet.  Novelty confidence is
low-to-moderate as a new observation because the result is close to standard
entropy folklore for Euclidean subspaces of `ell_infty^n`; the included proof
is self-contained.

Human review recommendation: verify the constant calculation in the
Rademacher/Hoeffding step and confirm that the intended reading of Problem 4
uses a single universal distortion constant `C`.  Under that reading, the
partial result correctly shows logarithmic optimality of any growth rate.
