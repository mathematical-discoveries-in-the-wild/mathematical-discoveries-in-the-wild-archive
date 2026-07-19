# Literature already answered: uniform boundedness in limit-operator Fredholm theory

Status: `literature_already_answered (Open Problem 8)`.

Source question: Simon N. Chandler-Wilde and Marko Lindner,
*Limit Operators, Collective Compactness, and the Spectral Theory of Infinite
Matrices*, arXiv:1005.0166.  In Chapter 9, Open Problem 8 asks whether the
uniform boundedness condition in Theorem `prop_rich_invinf`(iii) is redundant
for `p in (1,infty)`.  The source notes that the redundancy was known for
`p in {0,1,infty}` and for the Wiener algebra, but remained open for the
remaining `l^p` cases.

Supporting paper: Marko Lindner and Markus Seidel,
*An Affirmative Answer to a Core Issue on Limit Operators*, arXiv:1401.1300,
J. Funct. Anal. 267(3) (2014), 901--917.

Answer: Lindner--Seidel explicitly identify the same "big question" as whether
the operator spectrum of a rich operator is automatically uniformly invertible
when it is elementwise invertible.  Corollary 3.7 proves that for every rich
band-dominated operator all invertible limit operators have uniformly bounded
inverses.  Theorem 3.8 then states that a rich band-dominated operator on
`l^p(Z^N,X)`, for `p in {0} union [1,infty]`, is `P`-Fredholm if and only if
all its limit operators are invertible.  Thus the uniform boundedness condition
is redundant in particular for the source's open range `1<p<infty`.

Scope: this records an exact later literature answer to Open Problem 8, not a
new proof.  The supporting paper's Section 4 also explains that the rich and
band-dominated hypotheses are essential for its theorem.

Files:

- `source_paper.pdf`: arXiv:1005.0166.
- `supporting_paper_1401.1300.pdf`: arXiv:1401.1300.
- `solution_packet.pdf`: compact status note.
