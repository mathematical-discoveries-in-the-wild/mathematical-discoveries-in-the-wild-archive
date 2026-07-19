# Positive local compactness and universal Hermite projections

Status: `strong_partial_likely_valid (positive-window classification plus universal Hermite projections)`

Source paper: Erling A. T. Svela and S. Ivan Trapasso, *A quantum harmonic analysis approach to nonlinear time-frequency concentration*, arXiv:2605.28786.

## Target

The source paper states that a full classification of smoothing and escape mechanisms for Cohen-class windows \(S\in \mathcal B(L^2(\mathbb R^d))\) remains open. It develops the essential concentration value, the compactness barrier, and a positive localized-average criterion. Near the end, the source notes that a sufficiently sparse subsequence of Hermite functions gives a noncompact positive diagonal example for a fixed bounded observation set \(\Omega\).

## Result

This packet proves an exact structural theorem on the positive cone and then applies it to tensor-Hermite projections.

For every positive operator \(S\in\mathcal B(L^2(\mathbb R^d))\), every measurable \(0<|\Omega|<\infty\), and every finite \(1\le p<\infty\),
\[
S\in \mathcal B_{\rm wc}(p,\Omega)
\quad\Longleftrightarrow\quad
H_{\Omega,S}:=\int_\Omega \alpha_z(S)\,dz \text{ is compact}.
\]
The forward direction is new relative to the source criterion: positivity turns weak-to-norm continuity into vanishing quadratic forms of \(H_{\Omega,S}\) on every weakly-null sequence, and for positive Hilbert-space operators this is equivalent to compactness.

As an explicit consequence, for each \(d\ge1\), there is a single noncompact positive orthogonal projection
\[
S_d=\sum_{k=1}^\infty u_k^{(d)}\otimes u_k^{(d)}
\quad\text{on }L^2(\mathbb R^d)
\]
onto a sparse tensor-Hermite sequence such that, for every measurable
\(\Omega\subset\mathbb R^{2d}\) with \(0<|\Omega|<\infty\), the localized
average \(H_{\Omega,S_d}\) is compact. Hence \(f\mapsto Q_{S_d}f\) is
weak-to-norm continuous into \(L^p(\Omega)\) for every finite \(p\), and the
concentration supremum is attained for every \(1\le p\le\infty\). The endpoint
\(p=\infty\) uses the source paper's numerical-radius formula and the fact that
orthogonal projections attain their numerical radius.

The Hermite construction uses
\[
u_n^{(d)}=\phi_n\otimes\phi_0\otimes\cdots\otimes\phi_0 .
\]
Their ambiguity functions factor. The first factor tends to zero off the
origin in \(\mathbb R^2\), while the exceptional set \(\{z_1=0\}\subset
\mathbb R^{2d}\) has measure zero. Dominated convergence therefore gives local
\(L^2\)-decay of \(A(u_n^{(d)})\) on every ball in \(\mathbb R^{2d}\), and the
diagonal plus finite-measure truncation argument gives compactness of
\(H_{\Omega,S_d}\).

## Scope

This closes the weak-continuity classification for positive bounded windows at
finite \(p\), but it does not classify arbitrary nonpositive Cohen-class
windows. The endpoint \(p=\infty\) is covered for attainment of these
projections, not by weak-to-norm continuity.

## Verification

- Cheap run indexes were searched for `2605.28786`, `positive localized
  average`, `compact localized average`, `Hermite projection`, `finite measure`,
  `all dimensions`, and related phrases; no duplicate packet was found.
- A bounded web search for the exact source title and strengthened Hermite
  finite-measure phrases found the source arXiv record and no later answer.
- The LaTeX packet rendered successfully to `solution_packet.pdf`.

## Human Review Focus

First check the positive-cone converse:
if \(S\ge0\) and \(S\in\mathcal B_{\rm wc}(p,\Omega)\), then
\[
\langle H_{\Omega,S} f_n,f_n\rangle=\int_\Omega Q_Sf_n
\]
vanishes on every normalized weakly-null sequence; a positive operator with
this property must be compact. Then check the tensor-Hermite local decay, the
bounded-window compactness of \(H_{E,S_d}\), and the finite-measure truncation
\[
H_{\Omega,S_d}=\lim_{R\to\infty}H_{\Omega\cap B_R,S_d}
\]
in operator norm.
