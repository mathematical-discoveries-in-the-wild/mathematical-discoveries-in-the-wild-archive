# Literature Status: Symplectic Codimension-One Question Answered

Status: `literature_already_answered`

Source/open-problem paper: arXiv:2204.01703, Jesus M. F. Castillo, Wilson
Cuellar, Manuel Gonzalez Ortiz, and Raul Pino, "Symplectic forms on Banach
spaces" / published as "On symplectic Banach spaces."

Supporting answer paper: arXiv:2404.08445, Hanchen Li and Chaofeng Zhu,
"Skew-adjoint linear relations between Banach spaces."

## Identification

The source paper states Proposition 8.11 on page 20: for a real
infinite-dimensional Hilbert space `H` with symplectic structure `omega`, there
are no bounded bilinear maps `Omega` and compact `kappa` on `R op H` such that
`Omega` extends `omega` and `Omega + kappa` is symplectic. Immediately after
the proof, the authors ask whether Proposition 8.11 holds for general Banach
spaces.

The later paper explicitly quotes this question in its Introduction, page 4,
identifying it as the question after Castillo--Cuellar--Gonzalez--Pino
Proposition 8.11. It says it solves the problem and generalizes it through
mod-2 kernel stability for skew-adjoint Fredholm relations on real Banach
spaces.

## Answer

The decisive formal statement is Corollary 1.5 of arXiv:2404.08445, page 5.
It says that if `(X, omega)` and `(X op R^n, tilde omega)` are real symplectic
Banach spaces and `L_{tilde omega|X} - L_omega` is compact, then in the strong
case `n` must be even. Taking `n = 1` rules out the codimension-one compact
perturbation scenario asked about after Proposition 8.11. Thus the source
question is answered affirmatively: Proposition 8.11 does hold for general
Banach spaces, in the strong symplectic setting of the question.

## Scope

This packet records a later explicit literature answer, not a new proof. It
clears the source paper's final "general Banach spaces" question. The
supporting result is stronger: it proves a mod-2 stability theorem for kernels
of skew-adjoint Fredholm relations and derives the finite-codimension parity
obstruction.

## Local Artifacts

- `source_paper.pdf`: arXiv:2204.01703.
- `supporting_paper_2404.08445.pdf`: arXiv:2404.08445.
- `solution_packet.pdf`: compact status note.

## Search Evidence

Cheap run indexes had no prior packet for `2204.01703` or this symplectic
codimension-one question. Web/arXiv search for the exact Proposition 8.11
sentence found arXiv:2404.08445, and the local target-pool scan independently
contains the same explicit answer passage.
