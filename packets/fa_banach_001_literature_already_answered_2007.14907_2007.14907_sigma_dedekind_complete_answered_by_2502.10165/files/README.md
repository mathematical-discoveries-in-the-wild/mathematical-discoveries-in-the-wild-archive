# Literature already answered: sigma-Dedekind complete lattice homomorphisms

status: `literature_already_answered`

source: Sheldon Dantas, Gonzalo Martinez-Cervantes, Jose David Rodriguez Abellan, and Abraham Rueda Zoca, *Norm-attaining lattice homomorphisms*, arXiv:2007.14907.

supporting answer: Eugene Bilokopytov, Enrique Garcia-Sanchez, David de Hevia, Gonzalo Martinez-Cervantes, and Pedro Tradacete, *Norm-attaining lattice homomorphisms and renormings of Banach lattices*, arXiv:2502.10165.

packet: `runs/fa_banach_001/solutions/literature_already_answered/2007.14907_sigma_dedekind_complete_answered_by_2502.10165/`

## Identification

In Section 4 of arXiv:2007.14907, after proving that every lattice homomorphism on an order-continuous Banach lattice attains its norm, the authors ask whether the theorem can be extended to sigma-Dedekind complete Banach lattices.

The later paper arXiv:2502.10165 explicitly says that its examples answer this question negatively. In particular, it renorms `ell_infty=C(beta N)` by

```text
|||x||| = ||x||_infty + sum_{n=1}^\infty 2^{-n}|x_n|
```

and observes that no evaluation `delta_t` for `t in beta N \ N` attains its norm.

## Scope

This packet records only the sigma-Dedekind-complete extension question from the source paper. It does not resolve the free Banach lattice Conjecture 5.5 of arXiv:2007.14907; arXiv:2502.10165 revisits that conjecture, notes a gap in the source's property `(P)` argument, and leaves the finite `p` free `p`-convex question open.

## Files

- `main.tex`: compact status note with the counterexample written out.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2007.14907 source paper.
- `supporting_paper_2502.10165.pdf`: later answering paper.
