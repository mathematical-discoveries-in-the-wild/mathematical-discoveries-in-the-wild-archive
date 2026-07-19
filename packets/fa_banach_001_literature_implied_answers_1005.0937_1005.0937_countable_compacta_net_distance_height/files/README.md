# Literature-Implied Partial Answer: Countable Compacta Height Obstruction

## Source Question

- Source paper: Rafal Gorak, *Coarse version of the Banach-Stone theorem*, arXiv:1005.0937.
- Location: Final remarks, Problem labeled `problem Banach-Stone ogolny`, and the immediately following countable-compacta problem.
- Question: whether `d_N(C(X), C(Y)) < 2` forces compact spaces `X` and `Y` to be homeomorphic; in particular, what can be said for countable compacta and for `X` a convergent sequence.

## Status

`literature_implied_answer (partial countable-compacta height subcase)`.

The supporting paper Antonin Prochazka and Luis Sanchez-Gonzalez, *Low distortion embeddings between C(K) spaces*, arXiv:1408.0211, proves Corollary `c:AnswerGorak`:
if `gamma != alpha < omega_1` and `m,n` are positive integers, then
`d_N(C([0, omega^gamma * n]), C([0, omega^alpha * m])) >= 2`.

Together with the Mazurkiewicz-Sierpinski classification of countable compacta, this shows that among countable compacta a net distance strictly below `2` forces the same ordinal height/exponent. Thus the different-height countable-compacta subcase of Gorak's threshold-2 question has a negative obstruction.

## Scope

- This is not an original proof; it records a later literature theorem and the standard countable-compacta identification.
- The supporting paper explicitly says that Corollary `c:AnswerGorak` partially answers Gorak's Problem 2.
- It does not settle the same-height finite multiplicity cases `[0, omega^alpha * m]` versus `[0, omega^alpha * n]`.
- For the source paper's convergent-sequence test case `X = [0, omega]`, this packet only records that any countable `Y` with `d_N(C(X), C(Y)) < 2` must have the same height/exponent. It does not prove that `Y` is homeomorphic to `X`.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1005.0937 source paper.
- `supporting_paper_1408.0211.pdf`: supporting arXiv paper.
