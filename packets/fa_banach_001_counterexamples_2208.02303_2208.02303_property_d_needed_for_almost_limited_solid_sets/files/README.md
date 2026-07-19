# Counterexample: property `(d)` is needed in Proposition 3.2.1

Status: likely valid counterexample, needs human review.

Source paper: Safak Alpay, Eduard Emelyanov, and Svetlana Gorokhova,
"Regularly limited, Grothendieck, and Dunford--Pettis operators",
arXiv:2208.02303.

## Target

After Proposition 3.2.1, the source asks whether the proposition remains true
without assuming that the Banach lattice \(E\) has property `(d)`.

Proposition 3.2.1 states that, if \(E\in(d)\) and \(A\subset E\) is bounded
and solid, then the following are equivalent:

1. \(A\) is almost limited.
2. \(f_n(a_n)\to0\) for every disjoint weak-star null \((f_n)\subset E'\)
   and every disjoint \((a_n)\subset A\).
3. \(f_n(a_n)\to0\) for every disjoint positive weak-star null
   \((f_n)\subset E'_+\) and every disjoint \((a_n)\subset A\cap E_+\).

## Counterexample

Take \(E=C[0,1]\) and \(A=B_E\), the closed unit ball.

Condition (3) holds: if \((\mu_n)\subset M[0,1]_+\) is weak-star null, then
\(\|\mu_n\|=\mu_n([0,1])=\mu_n(\mathbf 1)\to0\). Hence
\(|\mu_n(a_n)|\le \|\mu_n\|\) for every \(a_n\in B_E\).

But \(A\) is not almost limited. Let
\[
  \nu_n=\delta_{1/(2n)}-\delta_{1/(2n+1)}.
\]
Then \((\nu_n)\) is disjoint and weak-star null in \(M[0,1]\), while
\[
  \sup_{\|f\|_\infty\le1}|\nu_n(f)|=2
\]
for every \(n\). Thus \((\nu_n)\) is not uniformly null on \(B_E\).

Therefore condition (3) does not imply condition (1) without property `(d)`.
The proposition does not remain true after removing that assumption.

## Files

- `main.tex`: human-readable proof note.
- `solution_packet.pdf`: rendered proof note.
- `source_paper.pdf`: rendered local copy of the arXiv source.
- `figures/open_problem_crop.png`: crop of the proposition and open question
  in the rendered source paper.
- `code/crop_open_problem.py`: reproducible crop generator.
- `code/verify_counterexample.py`: sanity check for the point sequence and
  separating functions.

No heavy computational verification is needed; the witness is explicit.
