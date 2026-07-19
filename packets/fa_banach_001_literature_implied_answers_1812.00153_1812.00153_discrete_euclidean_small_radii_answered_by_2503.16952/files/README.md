# Partial Literature Answer: Discrete Euclidean Ball Small-Radii Range

Status: `literature_implied_answer (partial small-radii subrange)`

Source target: arXiv:1812.00153, J. Bourgain, M. Mirek, E. M. Stein, and
B. Wrobel, *On the Hardy--Littlewood maximal functions in high dimensions:
Continuous and discrete perspective*.

Source problem/direction: Section 3, "Discrete perspective", reduces the
dimension-free full discrete \(B^2\) maximal problem to the range
\(1\le N\le Cd\) after proving the large-scale bound. It explicitly says new
methods are needed for the full maximal function and asks for improved
multiplier estimates beyond the dyadic result.

Identification: Niksinski--Wrobel, arXiv:2503.16952, gives a later partial
answer for Euclidean balls: Theorem 1.1 proves dimension-free estimates for
the full discrete Euclidean ball maximal function on \(\ell^p(\mathbb Z^d)\),
\(p\in[2,\infty]\), over radii \(0\le t\le d^{1/2-\varepsilon}\). Its Remark 1
combines this with the large-scale theorem from the source survey to identify
the remaining Euclidean ball range as \(t\in(d^{1/2-\varepsilon},Cd)\).

Scope: this is not a full solution of the source's discrete Euclidean-ball
problem. It does not cover the middle range \(d^{1/2-\varepsilon}<t<Cd\), does
not remove the epsilon, and does not provide the full \(p\in(3/2,\infty]\) or
\(p\in(1,\infty]\) answer discussed in arXiv:1812.00153.

Files:
- `main.tex` / `solution_packet.pdf`: compact status note.
- `source_paper.pdf`: arXiv:1812.00153.
- `supporting_paper_2503.16952.pdf`: arXiv:2503.16952.

