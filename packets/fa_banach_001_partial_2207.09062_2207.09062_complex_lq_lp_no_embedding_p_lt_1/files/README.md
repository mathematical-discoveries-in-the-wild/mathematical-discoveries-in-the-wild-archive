# Partial result: complete complex commutative finite-\(q\) no-embedding classification

Status: `partial_result_likely_valid`; complete for the finite-\(q\) complex commutative subproblem, but still partial relative to Xu's non-commutative Schatten question.

Source paper: arXiv:2207.09062, "On Isometric Embeddability of \(S_q^m\) into \(S_p^n\) as non-commutative Quasi-Banach space" by Chattopadhyay, Hong, Pradhan, and Ray.

Packet files:

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop of PDF page 2 showing Question 1.1 and Theorem 1.2.

## Result

New lemma proved in the packet: for \(0<p<1<q<\infty\) and \(2\le m\le n<\infty\), there is no complex-linear isometric embedding
\[
  \ell_q^m(\mathbb C) \longrightarrow \ell_p^n(\mathbb C).
\]

Combined conclusion: using source Theorem 1.2 for the complex cases \(q\notin2\mathbb N\), plus the new lemma for the omitted positive even integers \(q=2,4,6,\ldots\), one obtains the complete finite-\(q\) complex commutative no-embedding statement:
\[
  0<p<1,\quad 0<q<\infty,\quad p\ne q,\quad 2\le m\le n<\infty
  \implies
  \ell_q^m(\mathbb C)\not\hookrightarrow \ell_p^n(\mathbb C)
\]
linearly isometrically.

It does **not** solve the non-commutative question \(S_q^m\to S_p^n\). It also does not claim the commutative endpoint \(q=\infty\).

## Proof idea

If \(T:\ell_q^m(\mathbb C)\to\ell_p^n(\mathbb C)\) were a linear isometry, then
\[
  \sum_{r=1}^n |f_r(x)|^p=\|x\|_q^p
\]
for the coordinate functionals \(f_r\) of \(T\). Choose a nonzero coordinate functional \(f_j\), a nonzero vector \(x_0\in\ker f_j\), and a direction \(y\) with \(f_j(y)\ne0\). Along the real line \(x_0+ty\), the left side has a cusp term \(|t f_j(y)|^p\), hence is not differentiable at \(0\) because \(0<p<1\). The right side is differentiable at \(0\) because \(q>1\) and \(x_0\ne0\). Contradiction.

## Novelty and duplicate check

Cheap index search was run against `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and `proof_gaps/index.tsv` for `2207.09062`, `ell_q^m`, `ell_p^n`, and isometric-embedding keywords; no duplicate packet was found. A bounded web search for exact phrases around complex \(\ell_q^m\to\ell_p^n\), quasi-Banach \(p<1\), and arXiv:2207.09062 surfaced the source paper and unrelated hits, but no later paper explicitly closing this complex even-\(q\) commutative gap.

Human-review focus: verify that the source convention treats "isometric embedding" as a linear isometric embedding in the commutative theorem. The source proof on page 6 explicitly passes to a linear map \(T:\ell_q^2(\mathbb K)\to\ell_p^n(\mathbb K)\), matching the convention used here.
