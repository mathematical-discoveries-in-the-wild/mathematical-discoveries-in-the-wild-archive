# Full scoped result: large-target row embeddings of \(S_2^m\) into \(S_p^n\)

Status: `full_solution_likely_valid_scoped_large_target_existence`

Source paper: Arup Chattopadhyay, Guixiang Hong, Avijit Pal, Chandan Pradhan, and Samya Kumar Ray, "Isometric embeddability of \(S_q^m\) into \(S_p^n\)", arXiv:2008.13164v4, published in Journal of Functional Analysis 282 (2022), article 109281, DOI 10.1016/j.jfa.2021.109281.

Packet claim: for every \(m \ge 1\), every \(1 \le p \le \infty\), and every \(n \ge m^2\), there is a complex-linear isometric embedding
\[
S_2^m \longrightarrow S_p^n.
\]
Thus the large-target existence analogue of the source paper's even-\(p\) sentence holds for every \(p\), including non-even \(1<p<\infty\). On this reading, the first source uncertainty is answered positively. The same construction also gives the \(q=2\) large-target case of \(S_q^m \to S_1^n\).

## Source Signal

The relevant source passage is in the introduction, page 2 of the arXiv PDF. After Theorem 1.1, the authors write that they do not know whether \(S_2^m\) embeds isometrically into \(S_p^n\) for \(1<p<\infty\) when \(p\) is not an even integer. They then note that for even \(p\), Lyubich-Shatalova gives such embeddings for sufficiently large \(n\). They also say they do not know whether \(S_q^m\) embeds into \(S_1^n\) for \(q \in \{2,3\}\).

Local crop: `figures/open_problem_crop.png`.

## Result

Let \(\operatorname{vec}:S_2^m \to \ell_2^{m^2}\) be the usual vectorization of matrix entries. If \(n \ge m^2\), pad \(\operatorname{vec}(A)\) by zeros to a row vector \(r(A)\in\mathbb C^n\), and let \(\Phi(A)\in M_n\) be the matrix whose first row is \(r(A)\) and whose other rows are zero.

Then \(\Phi(A)\) has rank at most one and its only nonzero singular value is
\[
\|r(A)\|_2=\|A\|_{S_2^m}.
\]
All Schatten norms agree on a rank-one operator with a single singular value, so
\[
\|\Phi(A)\|_{S_p^n}=\|A\|_{S_2^m}
\]
for every \(1\le p\le\infty\). The map is complex-linear and injective.

## Proof Intuition

The open case is only hard if the target is required to retain matrix-algebraic structure or if \(n\) is small. Under the source paper's stated convention of plain linear isometry, a row subspace of \(S_p^n\) is Hilbertian for every \(p\): a one-row matrix has exactly one singular value, namely the Euclidean norm of that row. Since \(S_2^m\) is a Hilbert space of complex dimension \(m^2\), it fits into such a row once \(n\ge m^2\).

## Scope and Limitations

- This is a full solution only for the large-target existence reading of the source question.
- This packet does not classify the minimal \(n\) for which \(S_2^m\) embeds into \(S_p^n\).
- It does not solve the \(q=3\) case for embeddings into \(S_1^n\).
- It does not address complete isometry, algebraic embeddings, trace-preserving embeddings, or self-adjoint-range requirements.
- The proof is a standard row-Hilbert-space construction; novelty confidence is modest as a literature claim, but the run's cheap indexes and bounded web search did not find an existing local packet or exact later answer for this extracted source signal.

## Verification Notes

The argument is exact and does not depend on numerical computation. The optional script `code/verify_row_embedding.py` checks random finite examples by computing singular values and Schatten norms.

Human review should focus on the intended interpretation of the source question: if it asks for arbitrary sufficiently large target dimension and plain linear isometry, the row construction gives a complete positive answer. If the intended problem was instead a small-\(n\), optimal-\(n\), self-adjoint, algebraic, or complete-isometric version, this packet should be reclassified as a clarification rather than a solution to that stronger reading.

## References

- Chattopadhyay, Hong, Pal, Pradhan, and Ray, "Isometric embeddability of \(S_q^m\) into \(S_p^n\)", arXiv:2008.13164; J. Funct. Anal. 282 (2022), 109281.
- Chattopadhyay, Hong, Pradhan, and Ray, "On isometric embeddability of \(S_q^m\) into \(S_p^n\) as non-commutative quasi-Banach spaces", arXiv:2207.09062; Proc. Roy. Soc. Edinburgh Sect. A, published online 2023. This later paper extends the surrounding non-embedding program to \(p<1\), but does not remove the need for the simple \(q=2\), large-target row observation recorded here.
