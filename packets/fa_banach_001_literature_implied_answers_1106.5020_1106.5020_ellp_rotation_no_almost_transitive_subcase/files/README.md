# Literature-Implied Partial Subcase: Mazur/Banach-Mazur Rotation Problem

Status: `literature_implied_answer (partial subcase)`

Source problem paper: V. Ferenczi and C. Rosendal, *On isometry groups and
maximal symmetry*, arXiv:1106.5020.

Supporting paper: S. J. Dilworth and B. Randrianantoanina, *On an isomorphic
Banach-Mazur rotation problem and maximal norms in Banach spaces*,
arXiv:1310.7139.

## Target

The source paper records Mazur's rotation problem in the following form: if a
separable Banach space has an isometry group acting transitively on its unit
sphere, must the space be Hilbertian, i.e. isomorphic to separable Hilbert
space?

This packet records a later literature-implied negative-exclusion subcase:
`ell_p`, `1<p<infty`, `p != 2`, and all infinite-dimensional subspaces of
quotient spaces of `ell_p`, cannot provide non-Hilbertian counterexamples to
that isomorphic rotation problem.

## Result

No Banach space isomorphic to `ell_p`, `1<p<infty`, `p != 2`, nor to an
infinite-dimensional subspace of a quotient space of such an `ell_p`, admits an
equivalent transitive norm.

Indeed, the supporting paper proves the stronger statement that these classes
admit no equivalent almost transitive renorming. Since every transitive norm is
almost transitive, these spaces are excluded from the possible counterexample
classes for the source Mazur/Banach-Mazur rotation problem.

## Proof Summary

Ferenczi--Rosendal arXiv:1106.5020, page 2, states Mazur's rotation problem:
whether a separable Banach space whose isometry group acts transitively on the
sphere must be Hilbertian. The same paper later recalls the hierarchy
`transitive => almost transitive => convex transitive`.

Dilworth--Randrianantoanina arXiv:1310.7139 proves that `ell_p`,
`1<p<infty`, `p != 2`, and all infinite-dimensional subspaces of quotient
spaces of `ell_p`, admit no equivalent almost transitive renorming. This is
stated in the abstract and in Corollary 2.11; Theorem 2.4 gives the underlying
subspace-of-`ell_p` exclusion.

If a Banach space in one of these isomorphic classes had a transitive norm,
transporting that norm across the isomorphism would give an equivalent
transitive, hence equivalent almost transitive, renorming of the corresponding
`ell_p`-based model space. This contradicts arXiv:1310.7139. Therefore these
classes cannot witness a negative answer to the source problem.

## Evidence

- `source_paper.pdf`: local copy of arXiv:1106.5020. Page 2 records the
  Mazur rotation problem.
- `supporting_paper_1310.7139.pdf`: local copy of arXiv:1310.7139. Page 1
  states the main exclusion in the abstract; page 5 contains Theorem 2.4; page
  7 contains Corollary 2.11 for subspaces of quotient spaces of `ell_p`.
- `solution_packet.pdf`: compact human-readable status note built from
  `main.tex`.

## Search Bounds

Before packaging, the cheap run indexes were searched for `1106.5020`,
`1310.7139`, Dilworth, Randrianantoanina, Mazur rotation, Banach-Mazur
rotation, almost transitive renorming, `ell_p`, and subspaces of quotient
spaces. No prior packet or attempt for this exact 1106.5020/1310.7139 subcase
was found.

External arXiv/web search on 2026-06-14 found arXiv:1310.7139 as the relevant
later source. No full solution of Mazur's general rotation problem was
identified during this bounded check.

## Human Review Notes

Recommended review focus:

- Count this only as a literature-implied partial subcase, not a solution of
  the general Mazur rotation problem.
- Confirm that the conclusion is isomorphic-class exclusion: a transitive norm
  on a space isomorphic to the listed model class would be an equivalent
  transitive norm on that model.
- Confirm that the quotient-space statement is restricted to
  `1<p<infty`, `p != 2`, as in Corollary 2.11 of arXiv:1310.7139.
