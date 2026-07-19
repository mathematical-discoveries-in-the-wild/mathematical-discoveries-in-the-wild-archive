# Polynomial-Fiber Covering Counterexample on Hilbert Ball

Status: likely valid counterexample to the polynomial-fiber covering question in Ortega Castillo--Prieto, arXiv:1702.06471.

Source question: Section 3 asks whether the union of the polynomial fibers
\[
\bigcup_{x^{**}\in \overline{B}^{**}} M_{x^{**}}^{\mathcal P}(H(B))
\]
is all of \(M_{H(B)}\).

Result: For \(X=\ell_2\), \(B=B_X\), and \(H(B)=H^\infty(B)\), the union of the polynomial fibers is not all of \(M_{H^\infty(B)}\). A cluster point in \(M_{H^\infty(B)}\) of the evaluations at \(r e_n\), \(0<r<1\), restricts to a non-evaluation character on \(A_u(B)\), witnessed by the quadratic polynomial \(P(x)=\sum_n x_n^2\). Therefore it cannot belong to any polynomial fiber.

Scope: This does not solve the polynomial cluster value theorem itself, and it does not answer the more specialized \(C(K)\) program in Section 3. It gives a direct negative answer to the broad covering/range question for a standard algebra \(H^\infty(B_X)\).

Packet contents:

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:1702.06471.
- `figures/open_problem_crop.png`: crop of the source passage raising the question.

Novelty check: Exact phrase searches for the polynomial-fiber covering question and local index searches found no prior packet or exact literature answer. Related literature on large fibers of \(M(A_u(B_{\ell_p}))\) was identified, but the packet proof is self-contained and records this as related background rather than as a supporting theorem.
