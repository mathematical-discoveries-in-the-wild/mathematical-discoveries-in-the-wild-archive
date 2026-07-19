# Counterexample packet: Crawford-number localization near convex generators

Status: likely valid counterexample.

Source paper: Geunsu Choi and Han Ju Lee, "On the Crawford number attaining operators", arXiv:2201.10031.

Targeted question: Question 3.2 asks whether, for `S subset B_X` with `B_X = closed co(S)`, the Crawford number `c(T)` can always be computed by restricting the infimum to states `(x,x*)` with `dist(x,S) < epsilon`.

Result: no.  Take `X = ell_infty^2` over the real field, let `S` be the four vertices of the unit square, and let `T(a,b) = (b,a)`.  Then `S` is finite and uniformly strongly exposed, and `B_X = co(S)`.  The state `((1,0), e_1*)` gives `c(T)=0`.  But for every `0 < epsilon < 1`, every state whose vector lies within `epsilon` of `S` satisfies `|x*(Tx)| >= 1 - epsilon`.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: rendered source paper.
- `figures/open_problem_crop.png`: crop of the original question.

Scope: this answers the localization formula in Question 3.2 as stated.  It does not settle the separate density questions for property `alpha` or property `beta` spaces.
