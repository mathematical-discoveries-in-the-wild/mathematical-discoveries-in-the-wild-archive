# Literature Answer: Sharp CHS-to-Operator Lower Constant

Status: `literature_already_answered`

Source problem: Ludovick Bouthat, Angel Chavez, and Stephan Ramon Garcia,
*Hunter's positivity theorem and random vector norms*, arXiv:2403.10314.
Problem 5 on PDF page 59 asks for a sharp lower bound in Theorem 10.5. For
Hermitian `A`, that theorem compares

```text
||A||_d = h_d(lambda(A))^(1/d)
```

with the operator norm, but gives only Hunter's non-sharp lower constant.

Supporting answer: Silouanos Brazitikos and Christos Pandis, *Sharp
inequalities for symmetric polynomials, Hunter's conjecture, and moments of
exponential random variables*, arXiv:2512.12254. Section 6, especially
Theorem 6.1, Lemmas 6.2--6.3, and Corollary 6.4 (beginning on PDF page 37),
determines the exact minimum of `h_{2k}` on the real `ell_infinity`-sphere and
states the resulting optimal comparison with the operator norm. The
introduction on PDF page 5 explicitly says that Section 6 answers the sharp
matrix-norm lower-constant question.

## Identification

Let `d=2k`, `n>=2`, and let `tau_{n,k}` be the unique root in `(-1,0)` of

```text
h_{2k-1}(tau,...,tau,1) = 0,
```

where `tau` occurs `n` times in this stationarity equation. The supporting
paper proves

```text
min_{||x||_infinity=1} h_{2k}(x)
  = binom(n+2k-1,2k) |tau_{n,k}|^(2k).
```

Consequently the exact constant in the source problem is

```text
C_{n,2k} = binom(n+2k-1,2k)^(1/(2k)) |tau_{n,k}|,
```

and equality is realized, up to scaling, global sign, and permutation, by a
Hermitian matrix with eigenvalue vector `(tau,...,tau,1)`, with `tau` occurring
`n-1` times. This is exactly the optimization behind Problem 5 because
`||A||_op=max_i |lambda_i(A)|` and `||A||_d^d=h_d(lambda(A))`.

There is a minor indexing inconsistency in the displayed statement of
Theorem 6.1: it writes `n-1` copies of `t` in the odd-degree root equation.
Lemma 6.2, Lemma 6.3, Corollary 6.4, and the derivative/stationarity calculation
use the correct equation with `n` copies. For example, when `n=2` and `k=1`,
the correct root is `2t+1=0`. The extremizing vector itself has `n-1` copies.

## Scope and provenance

This is a full literature resolution of Problem 5 only; it does not answer the
other open problems in Section 11 of arXiv:2403.10314. It is not a new proof
produced by this run. The relation was verified from the two arXiv sources and
by bounded searches for the exact problem wording, paper title, arXiv ids,
`complete homogeneous symmetric polynomial operator norm sharp lower bound`,
and `random vector norms Problem 5`.

Files:

- `source_paper.pdf`: arXiv:2403.10314.
- `supporting_paper_2512.12254.pdf`: decisive later answer.
- `main.tex`, `solution_packet.pdf`: compact status note.

Ledger: `runs/fa_banach_001/ledger/results/2403.10314_problem5_sharp_chs_operator_lower_bound.json`.

