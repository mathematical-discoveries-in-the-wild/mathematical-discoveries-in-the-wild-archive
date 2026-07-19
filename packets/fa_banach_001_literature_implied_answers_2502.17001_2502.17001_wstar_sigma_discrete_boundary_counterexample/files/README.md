# Literature-Implied Answer: Weak-Star Sigma-Discrete Boundaries Do Not Force Isomorphic Polyhedrality

Status: `literature_implied_answer`

## Source Question

- Source paper: Jesus M. F. Castillo and Alberto Salguero Alarcon, "Polyhedrality for twisted sums with `C(omega^alpha)`", arXiv:2502.17001.
- Location: Section `Boundaries`, parsed source line 275.
- Source uncertainty: the authors state that the claim "every twisted sum of `c_0(kappa)` and a space with a weak-star sigma-discrete boundary is isomorphically polyhedral" is uncertain, because they do not know whether the existence of a weak-star sigma-discrete boundary implies isomorphic polyhedrality.

## Supporting Answer

- Supporting paper: Richard J. Smith, "Topology, isomorphic smoothness and polyhedrality in Banach spaces", arXiv:1804.02899.
- Location: Introduction / Section 2 transition, parsed source line 168.
- Supporting statement: Smith cites Bible's thesis, Remark 3.4.4, for a space
  `Z = ell_1 direct_sum ell_1(S_{ell_infty})` which is neither Asplund nor
  `c_0`-saturated, hence not isomorphically polyhedral by Smith's Theorem
  `thm_nec_conditions`, but which nevertheless admits an equivalent norm with a
  relatively weak-star-discrete boundary.

## Identification

A relatively weak-star-discrete boundary is, in particular, a weak-star
sigma-discrete boundary: it is a countable union with one relatively discrete
piece. Since isomorphic polyhedrality is invariant under equivalent renorming,
Bible's example as reported by Smith is a negative answer to the implication
question recorded in arXiv:2502.17001.

This is an agent-identified literature implication rather than a supporting paper
that explicitly cites arXiv:2502.17001.

## Scope

This packet answers only the boundary subquestion:

> Does the existence of a weak-star sigma-discrete boundary imply that the Banach
> space is isomorphically polyhedral?

Answer: no.

It does not settle the full 3-space problem for isomorphic polyhedrality, and it
does not by itself produce a twisted-sum counterexample to that 3-space problem.

## Files

- `source_2502.17001.tex`: parsed source TeX for the open-problem paper.
- `supporting_source_1804.02899.tex`: parsed source TeX for Smith's supporting literature implication.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

Local arXiv PDFs were not present in `data/raw/arxiv` for these IDs at packet
creation time; the packet uses the parsed source files available in the repository.

## Review Recommendation

Record the weak-star sigma-discrete boundary implication as negatively answered in
the literature via Bible's example as cited by Smith. Keep the broader 3-space
problem open for future queue work.
