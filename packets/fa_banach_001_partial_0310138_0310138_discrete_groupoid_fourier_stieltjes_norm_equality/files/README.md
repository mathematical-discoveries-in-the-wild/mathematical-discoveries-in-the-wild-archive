# The two continuous Fourier--Stieltjes norms coincide for discrete groupoids

Status: **complete theorem for the discrete subclass; likely valid; send to
human review**.

Source: Alan L. T. Paterson, *The Fourier--Stieltjes and Fourier algebras for
locally compact groupoids*, arXiv:math/0310138, Section 5, pages 11--12.

## Source question

For the continuous Fourier--Stieltjes algebra \(B(G)\), Paterson defines
\(\|\phi\|_B\) by bounded Hilbert-bundle coefficient factorizations.  Pointwise
multiplication by \(\phi\) also gives a completely bounded map
\(T_\phi:C^*(G)\to C^*(G)\), hence a second norm
\(\|\phi\|_{\mathrm{cb}}\).  The source proves
\[
\|\phi\|_{\mathrm{cb}}\leq \|\phi\|_B
\]
and asks whether equality always holds.  It records equality for trivial pair
groupoids \(R_n\) and, by a separate argument, locally compact abelian groups.

## Result

The norms coincide for **every countable discrete groupoid** (with counting
Haar system):
\[
\boxed{\ \|\phi\|_B=\|T_\phi\|_{\mathrm{cb}}\quad(\phi\in B(G)).\ }
\]

This is a full theorem for a broad subclass of the source problem.  In
particular it settles every finite groupoid, including all matrix groupoids
\(I\times H\times I\) with nonabelian finite isotropy group \(H\), not only the
trivial case \(H=\{e\}\) covered by \(R_n\).

## Proof mechanism

Let \(A=C^*(G)\), \(H_0=\ell^2(G^0)\), and let
\(\sigma:A\to B(H_0)\) be the integrated trivial line-bundle representation:
\[
\sigma(\delta_g)=E_{r(g),s(g)}.
\]
For \(S=\sigma T_\phi\), Haagerup--Paulsen factorization gives
\[
S(a)=V^*\pi(a)W,\qquad
\|V\|\|W\|\leq \|S\|_{\mathrm{cb}}+\varepsilon.
\]
Cutting by the unit projections \(p_u=\delta_u\) produces fiber vectors
\[
\xi(u)=\pi(p_u)We_u,\qquad \eta(u)=\pi(p_u)Ve_u.
\]
The partial isometries \(\pi(\delta_g)\) form a genuine groupoid representation
between the fibers \(\pi(p_u)K\).  Its coefficient is
\(\overline{\phi(g)}\) under Paterson's conjugate-linear-first convention; the
conjugate Hilbert bundle therefore has coefficient \(\phi\).  Moreover
\[
\|\xi\|_\infty\|\eta\|_\infty
\leq \|V\|\|W\|
\leq \|T_\phi\|_{\mathrm{cb}}+\varepsilon.
\]
Taking the coefficient infimum and then \(\varepsilon\downarrow0\) proves the
missing reverse inequality.

## Verification and limitations

The proof is operator-theoretic rather than computational.  The packet checks
the delicate points explicitly:

- \(\sigma\) is a valid representation even when several arrows have the same
  source and range;
- \(\pi(\delta_g)\) is unitary from the source fiber onto the range fiber;
- the constructed sections are continuous because the unit space is discrete,
  and are uniformly bounded by \(\|W\|\) and \(\|V\|\);
- conjugating the Hilbert bundle removes the scalar conjugation caused by
  Paterson's inner-product convention; and
- composing with \(\sigma\) can only decrease the cb norm.

Discreteness is essential to this proof: the vectors \(e_u\in\ell^2(G^0)\)
and isolated arrow elements \(\delta_g\in C_c(G)\) are what permit pointwise
reconstruction.  The argument does not settle nondiscrete locally compact
groupoids.

## Bounded novelty check

Searches on 23 July 2026 covered the exact norm question and combinations of
`discrete groupoid`, `r-discrete groupoid`, `Fourier-Stieltjes`,
`coefficient norm`, and `completely bounded multiplier`.  The closest items
were Oty's Borel/r-discrete algebra (whose norm is defined from multipliers on
the Borel completion \(M^*(G)\)), Paterson's measured operator-space duality,
and modern restriction-map work.  No source located in this bounded search
states equality between Paterson's **continuous Hilbert-bundle coefficient
norm** and the multiplier norm on \(C^*(G)\) for all discrete groupoids.
Novelty confidence is moderate, not definitive.

## Human review recommendation

Check the use of Haagerup--Paulsen factorization and the conjugate-bundle
coefficient calculation.  If those pass, this is suitable as a concise
proposition/note and should be literature-searched by an expert in groupoid
operator algebras.

Files:

- `main.tex`: full proof and scope audit;
- `solution_packet.pdf`: compiled proof;
- `source_paper.pdf`: source paper.

Ledger:
`ledger/results/0310138_discrete_groupoid_fourier_stieltjes_norm_equality.json`.
