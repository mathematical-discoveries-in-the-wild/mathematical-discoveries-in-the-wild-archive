# Partial packet: distortion <2 obstruction for coarse-Lipschitz c0 into duals

Status: candidate partial result, likely valid.

Source: Bruno de Mendonca Braga, Gilles Lancien, Colin Petitjean, and
Antonin Prochazka, "On Kalton's interlaced graphs and nonlinear embeddings
into dual Banach spaces", arXiv:1909.12132.

Target: the paper asks whether `c_0` coarsely Lipschitz embeds into a
separable dual space. The source proves a quantitative obstruction at
coarse-Lipschitz distortion strictly smaller than `3/2`; it also proves an
abstract graph obstruction at distortion strictly smaller than `2`, while
noting that it is not clear whether that graph is isometric to a subset of
`c_0`.

Result: the `3/2` obstruction on the actual grid of `c_0` improves to `2`.
If `Grid(c_0) cap 2B_{c_0}` Lipschitz embeds into `X^*` with distortion
strictly less than `2`, then `X` contains an isomorphic copy of `ell_1`.
Consequently, if `c_0` coarse-Lipschitz embeds into `X^*` with
coarse-Lipschitz distortion strictly less than `2`, then `X` contains
`ell_1`. In particular, `c_0` does not admit such an embedding into a
separable dual.

Proof idea: repeat Proposition 6.1 of the source, but replace the indicator
vectors by signed truncations
`s_A^m = 1_{A cap [1,m]} - 1_{[1,m] setminus A}` and compare `2e_k` with
`-2e_k`. If `k in A`, then both `||s_A^m-2e_k||` and
`||s_{N setminus A}^m+2e_k||` are `1`, while `||2e_k-(-2e_k)||=4`.
Thus the alternating weak-Cauchy obstruction has gap `4-epsilon-2D`, giving
the threshold `D<2`.

Novelty check: local run indexes were searched for arXiv:1909.12132 and exact
keywords around Kalton interlaced graphs, `c_0`, separable duals, and
coarse-Lipschitz distortion. No prior packet for this arXiv id was found.
Web/arXiv searches on 2026-06-28 for phrases including `"c_0" "coarse
Lipschitz" "separable dual"`, `"c_0" "coarse Lipschitz distortion" "2"`, and
`"Grid(c_0)" "distortion" "2"` surfaced the source paper but no exact
duplicate of this signed-grid improvement.

Human review recommendation: check the signed truncation substitution in the
proof of Proposition 6.1 and the scaling step from coarse-Lipschitz distortion
to a genuine Lipschitz embedding on the bounded grid.
