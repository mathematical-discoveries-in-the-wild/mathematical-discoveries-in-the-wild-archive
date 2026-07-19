# Literature-status packet: Borel isomorphism-class question and UB Borel clause

Status: `literature_already_answered` for the Bossard Borel-isomorphism-class question quoted in arXiv:1508.01961, with a scoped secondary answer to the `UB` Borel clause.

## Source question

Braga, *On the complexity of some inevitable classes of separable Banach spaces*, arXiv:1508.01961, Introduction:

> Let \(X\in \mathrm{SB}\) be a separable Banach space whose isomorphism class \(\langle X\rangle\) is Borel. Is \(X\) isomorphic to \(\ell_2\)?

The same source later asks, in the unconditional-basis subsection:

> Is \(\mathrm{UB}\) Borel? Is \(\mathrm{UB}\) complete analytic? What about \(S=\{X\in\mathrm{SB}: X\text{ has a Schauder basis}\}\)?

## Supporting identification

Kurka, *The isomorphism class of \(c_0\) is not Borel*, arXiv:1711.03328, Introduction, explicitly identifies Bossard's question and records that it had already been answered negatively by Godefroy, citing Godefroy's Theorem 6.2. The same paragraph also records that the isomorphism classes of \(\ell_p\), \(1<p<\infty\), are Borel. Taking any \(p\ne 2\) gives a non-Hilbert separable Banach space with Borel isomorphism class, so the source question has a negative answer in the literature.

Kurka's Theorem 3 also states that the class of spaces with an unconditional basis is analytic but not Borel. This answers the source's `Is UB Borel?' clause negatively. It does not settle whether `UB` is complete analytic, nor the corresponding Borel/complete-analytic questions for the class \(S\) of spaces with a Schauder basis.

## Files

- `source_paper.pdf`: arXiv:1508.01961.
- `supporting_paper_1711.03328.pdf`: Kurka arXiv:1711.03328.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

Ledger: `runs/fa_banach_001/ledger/results/1508.01961_bossard_borel_class_negative_godefroy_kurka.json`.

## Search and duplicate notes

Cheap indexes were searched for arXiv id `1508.01961`, title/core phrases, `UB`, `Schauder basis`, and Borel isomorphism-class keywords. No prior packet for this exact 1508.01961 status was found. A related local packet for arXiv:1711.03328 studies stronger partial consequences around \(c_0\oplus X\), but it does not record this source paper's Bossard question as answered.
