# Literature Already Answered: A Subspace Without Bibasic Sequences

Status: literature_already_answered

Source paper: M. A. Taylor and V. G. Troitsky, "Bibasic sequences in Banach lattices", arXiv:1907.07589.

Supporting answer paper: T. Oikhberg, M. A. Taylor, P. Tradacete, and V. G. Troitsky, "Free Banach lattices", arXiv:2210.00614.

Additional corroborating survey: E. Garcia-Sanchez, D. de Hevia, and P. Tradacete, "Free objects in Banach space theory", arXiv:2302.10807.

## Source Question

In Remark 4.4, after proving that every closed infinite-dimensional subspace of the closed span of a bibasic sequence contains another bibasic sequence, arXiv:1907.07589 asks whether every closed infinite-dimensional subspace of a Banach lattice contains a bibasic sequence.

Equivalently for counterexample purposes: does there exist a subspace of a Banach lattice with no bibasic sequence?

## Supporting Answer

The later paper arXiv:2210.00614 explicitly says in its introduction that Section 7 constructs the first example of a subspace of a Banach lattice without a bibasic sequence and that this answers a question from Taylor-Troitsky.

The decisive formal statement is Theorem 7.5:

> The subspace phi(c_0) in FBL^(p)[c_0] does not contain any bibasic sequence as long as 1 <= p < infinity.

Taking p=1 gives the ordinary free Banach lattice FBL[c_0]. Since phi is the canonical linear isometric embedding of c_0 into FBL[c_0], phi(c_0) is a closed infinite-dimensional subspace of a Banach lattice. The theorem therefore gives a negative answer to Remark 4.4 of arXiv:1907.07589.

The survey arXiv:2302.10807 independently identifies the match: it says that arXiv:1907.07589 Remark 4.4 asked whether there exists a subspace of a Banach lattice with no bibasic sequence, and that arXiv:2210.00614 Theorem 7.5 shows the canonical copy of c_0 in FBL[c_0] has none.

## Scope

This is not a new theorem from the run. It is an exact later literature answer to one of the source paper's open questions.

The packet only settles the general closed-subspace bibasic question from Remark 4.4. It does not settle the later uo-bibasic variants or the order-continuous subspace questions in the final section of arXiv:1907.07589.

## Files

- `source_paper.pdf`: locally compiled PDF of arXiv:1907.07589.
- `supporting_paper_2210.00614.pdf`: arXiv:2210.00614, copied from an existing run packet.
- `source_tex/source_1907.07589.tex`: source TeX for arXiv:1907.07589.
- `source_tex/source_2210.00614.tex`: source TeX for arXiv:2210.00614.
- `source_tex/source_2302.10807.tex`: source TeX for the corroborating survey arXiv:2302.10807.
- `main.tex` / `solution_packet.pdf`: compact status note.

Ledger record: `runs/fa_banach_001/ledger/results/1907.07589_subspace_without_bibasic_answered_by_2210.00614.json`.
