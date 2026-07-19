# Literature Status: Cogenerator Weak Stability

Status: `literature_already_answered`

Target: arXiv:0805.1039, Tanja Eisner, Balint Farkas, Rainer Nagel, and Andras Sereny, "Weakly and almost weakly stable C_0-semigroups".

Supporting answer: arXiv:2005.03821, Robert E. O'Brien, "Contractions, Cogenerators, and Weak Stability".

## Identification

The source paper closes with an open question following its cogenerator theorem for strong stability. The theorem says that for a C_0-semigroup of contractions with cogenerator G, strong stability of the semigroup is equivalent to strong stability of the powers of G. The authors then ask whether the analogue is true for weak stability, or more generally whether there is a connection between weak stability of a contractive semigroup and weak stability of its cogenerator.

O'Brien's 2020 paper explicitly treats this problem for C_0 contraction semigroups on Hilbert space. Its abstract and introduction say that the limit algebra gives a necessary and sufficient condition for the semigroup and cogenerator to be weakly stable equivalent. The remark following Theorem 5.3 states the criterion: weak stability of the semigroup is equivalent to weak stability of the cogenerator if and only if the unitary parts have a common limit algebra, equivalently are entangled. The same remark says this addresses Eisner's Open Question 2.23.

## Scope

This clears the cogenerator weak-stability question in the extracted source under the Hilbert-space contraction-semigroup setting stated there. It is not a new result from this run. It is also not an unconditional "always equivalent" theorem; the literature answer is a necessary-and-sufficient limit-algebra criterion.

The other open questions in arXiv:0805.1039, including the Hilbert-space resolvent-integrability converse and the sequence characterization problem, are not addressed by this packet.

## Evidence Checked

- Local cheap indexes for `0805.1039`, title keywords, `cogenerator`, and `weak stability` had no prior exact packet.
- Local parsed TeX source for arXiv:0805.1039 contains the source question in the closing "Comments and open questions" section after Theorem `thm:cogen`.
- Local parsed TeX source for arXiv:2005.03821 contains the abstract/introduction claim and the post-Theorem 5.3 remark explicitly addressing Eisner Open Question 2.23.
- Web/arXiv search for the two arXiv IDs confirmed the source and supporting paper metadata.

## Files

- `main.tex`: compact LaTeX status note.
- `solution_packet.pdf`: rendered status note.
- `source_0805.1039.tex`: local source TeX snapshot for the original question.
- `supporting_2005.03821.tex`: local source TeX snapshot for the supporting answer.
- `source_paper.pdf`: arXiv PDF for arXiv:0805.1039, when available.
- `supporting_paper_2005.03821.pdf`: arXiv PDF for arXiv:2005.03821, when available.

Ledger: `runs/fa_banach_001/ledger/results/0805.1039_cogenerator_weak_stability_answered_by_2005.03821.json`
