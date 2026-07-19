# Literature-Implied Answer: vector-valued null UDS question

Status: `literature_implied_answer`.

Source paper: Michael Doré and Olga Maleva, *A universal differentiability set
in Banach spaces with separable dual*, arXiv:1103.5094.

Source question: in the introduction, after proving scalar-valued universal
differentiability sets in separable-dual Banach spaces, the paper notes that
for Lipschitz maps `R^n -> R^m` with `n >= m >= 2`, it was then unknown in
general whether there are Lebesgue null sets containing a differentiability
point of every such Lipschitz map. It says the answer was known only for
`m=2`, with `n=m=2` negative and `n>m=2` forthcoming, and that no similar
positive results were known for codomain dimension at least `3`.

Supporting answer: David Preiss and Gareth Speight, *Differentiability of
Lipschitz Functions in Lebesgue Null Sets*, arXiv:1304.6916. Its introduction
states that the converse to Rademacher's theorem holds iff `m >= n`, and its
Theorem 1 proves that for every `n>1` there is a Lebesgue null
`N subset R^n` containing a differentiability point of every Lipschitz
`f:R^n -> R^{n-1}`. It also records that a modification gives, for any
`n>m` and `tau>0`, such a set of Hausdorff dimension at most `m+tau`.

Scope: this answers the finite-dimensional vector-valued null-UDS question
raised in the source introduction. It does not add a new proof beyond the
later literature, and the source paper's main scalar separable-dual theorem is
same-paper solved.

Files:

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1103.5094.
- `supporting_paper_1304.6916.pdf`: arXiv:1304.6916.
