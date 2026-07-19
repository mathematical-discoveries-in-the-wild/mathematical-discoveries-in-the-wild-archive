# Dedekind Finiteness Is Not Open In The Free-Monoid Quotient Coding

Status: partial result likely valid.

Source paper: Tomasz Kania, *Polish spaces for countable and separable
structures through quotient encodings*, arXiv:2604.15843.

Open-problem source: Section 12, "Extensions and open questions", asks under
"Dedekind finiteness for Banach algebras" whether the closed set of Dedekind
finite quotients is non-open in the Wijsman topology.

Result: for the standard unital Banach-algebra quotient generator
`A = ell_1(S)`, where `S` is the free monoid on countably many generators, the
Dedekind-finite class is not open.  The scalar quotient is Dedekind finite but
is the Wijsman limit of Dedekind-infinite quotients.

Packet contents:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local render of the source arXiv TeX.
- `tmp/`: LaTeX build outputs.

Human review notes:

The construction sends the generator pair `(s_{2n-1},s_{2n})` to the backward
and forward unilateral shifts `L,R`, with `LR=I` and `RL!=I`, and sends every
other generator to zero.  The resulting kernels are Dedekind-infinite
quotients.  Since each fixed element of `ell_1(S)` is approximated by
finite-support elements involving only finitely many generators, these kernels
converge in the Wijsman topology to the augmentation kernel of the scalar
quotient.

Scope limitation: this answers the non-openness question for the standard
free-monoid generator used in the paper, not for every possible quotient
generator or every other admissible topology.
