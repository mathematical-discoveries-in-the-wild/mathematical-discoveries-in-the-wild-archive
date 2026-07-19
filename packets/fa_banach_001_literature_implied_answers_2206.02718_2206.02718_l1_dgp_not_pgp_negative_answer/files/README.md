# Literature-Implied Negative Answer: PGP cannot replace DPSP in Wnuk's disjoint test

Status: `literature_implied_answer`

Source problem paper: S. Alpay, E. Emelyanov, and S. Gorokhova, *Generalizations of L- and M-weakly compact operators*, arXiv:2206.02718.

Supporting source: M. L. Lourenco and V. C. C. Miranda, *A note on the Banach lattice `c_0(ell_2^n)`, its dual and its bidual*, arXiv:2011.09319.

## Target

In Section 1.2 of arXiv:2206.02718, immediately before Assertion `Wnuk2013`, the authors recall Wnuk's characterization:

> `E` has the dual positive Schur property iff every disjoint weak-star null sequence in `E'_+` is norm null.

They then write that they do not know whether, in this assertion, `(DPSP)` can be replaced by `(PGP)` and "norm null" by "weak null".

Equivalently, the proposed replacement would say:

> If every disjoint weak-star null sequence in `E'_+` is weakly null, then `E` has the positive Grothendieck property.

## Answer Recorded

The proposed replacement is false. The Banach lattice `E = ell_1` satisfies the disjoint positive weak-star test, but it does not have the positive Grothendieck property.

Indeed, every bounded disjoint sequence in `ell_infty = E'` is weakly null against `ba(N) = (ell_infty)'`, while the positive tail indicators

```text
u_n = 1_{ {k >= n} } in ell_infty
```

are weak-star null for the predual `ell_1` but are not weakly null: any free-ultrafilter functional sends every `u_n` to `1`.

## Literature Identification

The supporting paper arXiv:2011.09319 explicitly records the same separation in its introduction:

> "`ell_1` has the weak Grothendieck property, but it fails to have the positive Grothendieck ..."

Here the weak Grothendieck property is exactly the disjoint Grothendieck test, which is stronger than the positive-disjoint test asked about in arXiv:2206.02718. Thus the negative answer is an agent-identified implication of known literature, not a new counterexample claimed by this run.

## Evidence

- `source_paper.pdf`: local copy of arXiv:2206.02718. The question appears in Section 1.2, just before Assertion `Wnuk2013`; in the parsed TeX this is around lines 624--629.
- `supporting_paper_2011.09319.pdf`: local copy of arXiv:2011.09319. The introduction states the `ell_1` weak-versus-positive Grothendieck separation; in the parsed TeX this is around line 131.
- `solution_packet.pdf`: compact status note built from `main.tex`, including the direct proof with `E=ell_1`.

## Scope

This fully refutes the proposed PGP analogue of Wnuk's disjoint characterization. No part of this packet claims a new theorem beyond the direct identification and the elementary verification of the known `ell_1` example.

## Human Review Notes

Recommended review focus:

- Confirm that the source question is correctly formalized as the implication from the positive disjoint weak-star test to PGP.
- Check the finitely additive measure argument proving that bounded disjoint sequences in `ell_infty` are weakly null.
- Confirm that this should remain in `literature_implied_answers/` rather than `counterexamples/`, since arXiv:2011.09319 already states the key separation.

