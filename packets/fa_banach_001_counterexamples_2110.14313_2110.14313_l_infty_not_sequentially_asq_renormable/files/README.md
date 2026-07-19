# Counterexample Packet: `ell_infty` Is Not Sequentially ASQ Renormable

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `2110.14313`
- source paper: Antonio Aviles, Gonzalo Martinez-Cervantes, Abraham Rueda Zoca, *Banach spaces containing c_0 and elements in the fourth dual*
- target passage: introduction / source line 248, where the authors ask whether every Banach space containing `c0` can be renormed to be sequentially ASQ.

## Claim

The Banach space `ell_infty` contains an isomorphic copy of `c0`, but it admits no equivalent real norm that is sequentially ASQ. Thus the renorming question in arXiv:2110.14313 has a negative ZFC answer.

## Proof Intuition

A sequentially ASQ witness is much stronger than an ASQ renorming witness. If `(x_n)` is sequentially ASQ and `f_n` norms `x_n`, then the estimates for `x_n +/- t x` force `f_n(x) -> 0` for every fixed `x`. A diagonal subsequence of the pairs `(x_n,f_n)` is therefore almost biorthogonal, and the coordinate map `x -> (f_n(x))` lands in `c0`. After a small perturbation/invertibility argument this gives a bounded projection onto a copy of `c0`.

Consequently every sequentially ASQ Banach space contains a complemented copy of `c0`. Phillips' theorem, in the standard form that every operator `ell_infty -> c0` is weakly compact, rules out any complemented copy of `c0` in `ell_infty`. Hence `ell_infty` cannot be sequentially ASQ under any equivalent norm.

## Files

- `main.tex`: full proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:2110.14313
- `figures/open_problem_crop.png`: crop of the source passage
- `code/make_open_problem_crop.py`: reproducible crop script

## Novelty Check

Before promotion, the agent checked the run indexes for `2110.14313`, `sequentially ASQ`, `sequentially almost square`, `renormed to be sequentially ASQ`, `complemented c0`, and `ell_infty`. The existing ASQ/c0 packet records the known nonsequential ASQ renorming theorem, but no packet addressed the sequential renorming question. Web searches on 2026-06-20 for exact phrases around `sequentially ASQ`, `renormed`, `c_0`, `complemented copy of c_0`, and the paper title found the source paper but no later answer to this question.

Human review should focus on the diagonal projection lemma, especially the passage from pointwise-null norming functionals to an invertible almost-diagonal coefficient map on `c0`.
