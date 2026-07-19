# Literal two-point obstruction in Bima Question 33

Status: `counterexample` to the literal finite-cardinality formulation; likely
an edge-case correction rather than the intended main problem.

Source paper: Jan Bima, *Nagata Dimension and Lipschitz Extensions Into
Quasi-Banach Spaces*, arXiv:2402.03189v1.

## Claim

Question 33 asks whether
\[
\lim_{p\to 0}\mathfrak{ae}_p(n)=\infty
\]
for each \(n\ge 2\), and whether for any \(n,m\in\mathbb N\),
\[
\sup\{\lim_{p\to0}\mathfrak t_p(\mathcal N,\mathcal M):
\mathcal N\subset\mathcal M,\ |\mathcal N|\le n,\ |\mathcal M\setminus
\mathcal N|\le m\}=m+1.
\]

As written, both universal assertions fail already at \(n=2\).  Every
two-point metric space has \(\mathfrak{ae}_p(\mathcal N)=1\) for all
\(0<p\le1\), and one-point spaces do no worse.  Hence
\(\mathfrak{ae}_p(2)=1\), and for every \(m\ge1\) the second displayed
supremum with \(n=2\) is \(1\), not \(m+1\).

## Files

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: source paper.
- `figures/two_point_observation_page2.png`: source observation that two-point
  spaces have \(\mathfrak{ae}_p=1\).
- `figures/open_question_page20.png`: Question 33.

## Scope

This does not address the intended nontrivial finite problem for \(n\ge3\).
Indeed, the source paper's Theorem 30 gives a three-point example with
\(\mathfrak t_p\to2\) for one added point.  Human review should decide whether
to count this as a counterexample packet or simply as an erratum-style edge
case for the literal statement.

## Novelty check

Searches for exact phrases including `ae_p(2)`, `absolute p-extendability
two-point`, `two-point metric space absolute p-extendable`, and
`\mathfrak{ae}_p(n)` found no separate literature answer.  The decisive
two-point observation is already present in the source paper, but the final
question still quantifies over \(n\ge2\).
