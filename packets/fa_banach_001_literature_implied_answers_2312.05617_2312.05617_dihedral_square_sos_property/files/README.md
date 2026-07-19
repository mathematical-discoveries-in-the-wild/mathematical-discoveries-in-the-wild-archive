# Literature-Implied Answer: Dihedral Square SOS Property

Status: `literature_implied_answer (full source question)`

Source paper: Arthur Mehta, William Slofstra, and Yuming Zhao, *Positivity is undecidable in tensor products of free algebras*, arXiv:2312.05617v2 / JEMS online first, 2026.

Source question: In the introduction, immediately after Corollary 1.2, the authors state that they do not know whether
\[
\mathbb C\mathbb Z_2^{*2}\times \mathbb Z_2^{*2}
\]
has the SOS property. At the end of Example 6.8 they equivalently say that for \(G=\mathbb Z_2^{*2}\), they do not know whether \(\mathbb C G\times G\) is archimedean closed.

Answer recorded here: Yes. If \(G=\mathbb Z_2^{*2}\) is the infinite dihedral group, then \(\mathbb C[G\times G]\) has the SOS property.

Identification: \(G\cong \mathbb Z\rtimes C_2\), hence \(G\times G\cong \mathbb Z^2\rtimes (C_2\times C_2)\), so \(\mathbb C[G\times G]\cong \mathbb C[z^{\pm1},w^{\pm1}]\rtimes (C_2\times C_2)\), where the two involutions invert \(z\) and \(w\). Dritschel's two-variable matrix Fejer-Riesz theorem gives type-I SOS for all positive matrices over \(\mathbb C[z^{\pm1},w^{\pm1}]\). Savchuk-Schmudgen's crossed-product transfer theorem then gives type-I SOS for the finite crossed product.

Supporting literature:

- Yurii Savchuk and Konrad Schmudgen, *Positivstellensatze for Algebras of Matrices*, arXiv:1004.1529v2 / Linear Algebra Appl. 436 (2012), Section 5.3, Lemma 12 and Theorem 3: type-I Positivstellensatz for \(M_n(A)\) transfers to \(A\times_\alpha G\) for finite \(G\).
- Michael A. Dritschel, *Factoring non-negative operator valued trigonometric polynomials in two variables*, Math. Ann. 391 (2025), 515--537, theorem in the introduction: every positive finite-dimensional operator-valued trigonometric polynomial in two variables is a finite sum of hermitian squares of analytic polynomials.

Files:

- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_1004.1529.pdf`: crossed-product Positivstellensatz.
- `supporting_paper_dritschel_2024_two_variable_fejer_riesz.pdf`: two-variable matrix Fejer-Riesz theorem.
- `main.tex`, `solution_packet.pdf`: compact status/proof note.

Scope limitations: This answers only the explicitly excluded/tight endpoint \(n=m=2\) SOS/archimedean-closed question for \(\mathbb C\mathbb Z_2^{*2}\times \mathbb Z_2^{*2}\). It does not address the paper's \(\Pi^0_2\)-completeness conjectures or tracial-positivity bound questions.
