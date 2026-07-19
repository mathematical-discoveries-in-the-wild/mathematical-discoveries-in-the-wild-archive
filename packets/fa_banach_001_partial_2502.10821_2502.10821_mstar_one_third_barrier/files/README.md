# Partial solution packet: the \(M^*(r,r)\) one-third barrier

## Source

- Paper: Manwook Han and Sun Kwang Kim, *Geometry of the space of compact operators endowed with the numerical radius norm*
- arXiv: `2502.10821`
- Local source PDF: `source_paper.pdf`
- Source location: Proposition 3.7 and Question after Corollary 3.8 in the parsed source, lines 385-430.

## Classification

- Status: `partial`
- Target question: If `n(X)>0` and `K_v(X)` is an M-ideal in `L_v(X)`, must `X` be Asplund?
- Packet claim: the known implication `K_v(X) M-ideal => X has M^*(n(X),n(X))` has a sharp universal threshold at `1/3`. Every Banach space already has `M^*(r,r)` for `r<=1/3`, while `ell_1` obstructs `M^*(r,r)` for every `r>1/3`.
- Consequence for the target: if `n(X)>1/3` and `K_v(X)` is an M-ideal in `L_v(X)`, then `X` contains no isomorphic copy of `ell_1`. This improves the source paper's `ell_1`-exclusion threshold from `n(X)>1/2` to `n(X)>1/3`.

## Relation to the Source Question

This does not settle the Asplund question. It gives a sharp obstruction for the paper's main proof route: below `1/3`, the derived `M^*(n,n)` condition is automatic and therefore cannot force Asplundness. Between `1/3` and `1/2`, the new argument rules out `ell_1`, but it does not rule out non-Asplund spaces without `ell_1`, such as James-tree-type phenomena.

In the complex case, the standard lower bound `n(X) >= 1/e` makes the corollary applicable: a complex counterexample to the source question cannot contain `ell_1`.

## Novelty Check

Cheap run indexes had no exact prior packet for `2502.10821`, `K_v(X)`, or the numerical-radius M-ideal Asplund question. Local source search found only the source paper's citation chain for `M(r,s)` and no existing run packet with this `1/3` barrier. Web searches for exact phrases such as `"K_v(X)" "M-ideal" "Asplund"`, `"M^*(r,s)" "1/3" "ell_1"`, and `"M(r,s)" "1/3" "Banach space"` found the source paper but no later answer or matching constant-barrier result.

## Files

- `main.tex`: LaTeX source for the proof packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: source paper downloaded from arXiv.
- `figures/`: empty; PDF rendering tools were unavailable in this environment, so no screenshot crop was generated.
- `tmp/`: LaTeX build output.

## Verification Notes

The central estimate is elementary:

```text
limsup ||y*+z_beta*|| >= max{ ||y*||, limsup ||z_beta*|| - ||y*|| }
```

and this maximum is always at least one third of `||y*|| + limsup ||z_beta*||`. The `ell_1` witness uses the weak-star-null sequence `2e_n` in `ell_infty=(ell_1)^*` with fixed functionals `1` and `-1`, giving the ratio `1/3`.

Human review should focus on the standard lifting lemma from an almost-isometric `ell_1` subspace to weak-star-null functionals on `X^*`; it is the only nontrivial functional-analytic bookkeeping step.
