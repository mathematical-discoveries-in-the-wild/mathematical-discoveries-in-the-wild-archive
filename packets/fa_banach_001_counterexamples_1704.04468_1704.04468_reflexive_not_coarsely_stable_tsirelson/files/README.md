# Counterexample packet: a reflexive space not coarsely embeddable into any stable metric space

status: counterexample

source_arxiv: 1704.04468

source_problem: Problem 1.5 / Kalton Problem 6.1, asking whether every separable reflexive Banach space embeds coarsely, respectively uniformly, into a stable space.

counterexample: Tsirelson's original space \(T^*\).

## Summary

This packet gives a negative answer to Problem 1.5 of Braga--Swift, arXiv:1704.04468. Tsirelson's original space \(T^*\) is separable and reflexive, but it cannot coarsely embed into any stable metric space. It also cannot uniformly embed into any stable metric space.

The main lemma is slightly stronger: if a Banach space finitely represents \(c_0\), then it cannot coarsely embed into a stable metric space. For a hypothetical coarse embedding \(f:X\to M\), finite representability gives uniformly distorted finite-dimensional copies of \(\ell_\infty^n\) in \(X\). Passing over a cofinal ultrafilter on finite subsets of the integer lattice of \(c_0\) yields a coarse embedding of that lattice into a stable metric ultrapower of \(M\). Since the integer lattice is a net in \(c_0\), this would make \(c_0\) coarsely embeddable into a stable metric space, contradicting Kalton's theorem.

Baudier--Lancien--Schlumprecht, arXiv:1705.06797, record that \(T^*\) is reflexive and all spreading models of \(T^*\) are isomorphic to \(c_0\). Hence \(c_0\) is finitely represented in \(T^*\), and the lemma applies.

## Evidence

- `source_paper.pdf`: Braga--Swift, "Coarse embeddings into superstable spaces", arXiv:1704.04468.
- `figures/open_problem_crop.png`: crop of source Problem 1.5.
- `supporting_paper_1705.06797.pdf`: Baudier--Lancien--Schlumprecht, "The coarse geometry of Tsirelson's space and applications", arXiv:1705.06797, used for the \(T^*\) facts.
- `solution_packet.pdf`: rendered proof packet.

## Novelty Check

Bounded search found no existing answer to this exact stable-metric version. Searched the run indexes for `1704.04468`, `ProblemReflexEmbStable`, `stable metric`, `separable reflexive`, `original Tsirelson`, and `c_0 spreading`. Web searches and arXiv API searches for exact/near phrases including `"Does every (separable) reflexive Banach space embed coarsely"`, `"stable metric space" "Tsirelson"`, and `"c_0" "stable metric" "coarse"` returned no prior answer hits. The later BLS paper is adjacent but is used here only for the standard properties of \(T^*\), not as an explicit answer to Problem 1.5.

## Human Review Recommendation

Review the cofinal-ultrapower construction in the main lemma, especially the passage from finite representability of \(c_0\) in \(X\) to a coarse embedding of the integer lattice of \(c_0\) into a stable metric ultrapower. Also verify the use of the standard fact that metric stability is preserved by metric ultrapowers.
