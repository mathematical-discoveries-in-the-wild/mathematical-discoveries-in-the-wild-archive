# Literature-Implied Partial Answer: The Skein Free Space Is Not Dirac-Witnessed Plichko

Status: `literature_implied_answer (partial subcase)`.

## Source Question

- Source: Petr Hajek and Andres Quilis, *A complete metric space without non-trivial separable Lipschitz retracts*, arXiv:2206.10279.
- Location: Introduction, parsed source lines 110--115.
- Target statement: the authors say they do not know whether the Lipschitz-free space over their constructed skein metric space is Plichko, or even whether it has the Separable Complementation Property (SCP). They also mention `F(ell_infty)` as a possible candidate for failure of SCP/Plichko.

## Supporting Theorem

- Supporting paper: Antonio J. Guirao, Vicente Montesinos, and Andres Quilis, *On projectional skeletons and the Plichko property in Lipschitz-free Banach spaces*, arXiv:2305.08543.
- Supporting result: Theorem 2.1 characterizes when `F(M)` is `lambda`-Plichko witnessed by a subset of the Dirac measures `delta(M)`, in terms of separability of the relative balls `B(p, r d(p,0))` for all `r < 1/lambda`.

## Identification

Applying Theorem 2.1 to the skein space `M = Sk(omega_1)` from arXiv:2206.10279 shows that `F(M)` is not `lambda`-Plichko witnessed by Dirac measures for any finite `lambda >= 1`. Around the initial anchor point `B`, every sufficiently small ball contains an uncountable uniformly separated subset, obtained by taking one nearby non-endpoint from uncountably many distinct threads attached between the initial anchors `A` and `B`.

## Scope

This does **not** settle whether `F(M)` is Plichko in the unrestricted sense, and it does **not** settle SCP. The later paper explicitly notes that the converse from projectional structure to metric retractional structure is not automatic. This packet records only the Dirac-witnessed Plichko obstruction.

## Files

- `main.tex`: compact status note and proof of the local nonseparability implication.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2206.10279 source paper.
- `supporting_paper_2305.08543.pdf`: supporting theorem paper.
