# 1210.7324 -- numerical-index-one MUP under the SCD/lushness route

Status: literature_implied_answer (partial subcase).

## Source question

Original paper: Dongni Tan, Xujian Huang, and Rui Liu, *Generalized-Lush
Spaces and the Mazur-Ulam Property*, arXiv:1210.7324.

At the end of the paper, after proving that local-GL spaces and hence lush
spaces have the Mazur-Ulam property, the authors ask:

> Does every Banach space with numerical index 1 have the MUP?

The paper also notes that there are Banach spaces with numerical index one
which are not lush, so this final question is strictly wider than the paper's
main theorem.

## Supporting literature

Supporting paper: Vladimir Kadets, Miguel Martin, Javier Meri, and Antonio
Perez, *Spear operators between Banach spaces*, arXiv:1701.02977, Lecture
Notes in Mathematics 2205, Springer, 2018.

That paper records the standard identity-case implications:

- \(X\) has numerical index one exactly when \(\operatorname{Id}_X\) is a
  spear operator.
- Numerical index one implies the alternative Daugavet property (aDP).
- By the cited SCD theorem, if \(X\) has the aDP and \(B_Y\) is SCD for every
  separable subspace \(Y\subset X\), then \(X\) is lush. In particular, this
  applies when \(X\) has the convex point of continuity property, the
  Radon-Nikodym property, or does not contain a copy of \(\ell_1\).

## Identification

Let \(X\) be a Banach space with numerical index one and suppose that
\(B_Y\) is SCD for every separable subspace \(Y\subset X\). Numerical index
one makes \(\operatorname{Id}_X\) a spear operator, hence \(X\) has the aDP.
The SCD theorem from Kadets--Martin--Meri--Perez then makes \(X\) lush.
Tan--Huang--Liu prove that every lush space has the Mazur-Ulam property.
Therefore every numerical-index-one Banach space satisfying the SCD
separable-subspace condition has the MUP.

Concrete included subcases: finite-dimensional numerical-index-one spaces,
and more generally numerical-index-one spaces with the convex point of
continuity property, the Radon-Nikodym property, or no isomorphic copy of
\(\ell_1\).

## Scope limitation

This is not a full solution of the final question in arXiv:1210.7324. The
supporting route still passes through lushness, while the source paper and
the later spear-operator survey both record numerical-index-one spaces that
are not lush. Thus the unrestricted question remains open outside the
SCD/lushness mechanism.

The relation is agent-identified rather than explicitly presented by the
supporting authors as an answer to the final question of arXiv:1210.7324.
The supporting paper cites the Tan--Huang--Liu paper when discussing the
connection between lushness and Tingley's/Mazur-Ulam problem, but it does not
state this corollary as a named answer to that question.

## Search evidence

Cheap run indexes were searched for `1210.7324`, `Mazur-Ulam`, `MUP`,
`Tingley`, `numerical index`, `lush`, `local-GL`, `almost-CL`, and `spear`.
No duplicate packet for arXiv:1210.7324 was present. Nearby packets cover the
two-dimensional MUP literature answer, C*-algebra/Schatten and uniform-algebra
Tingley subcases, and finite-rank aDP/lushness for spear operators.

External web searches on 2026-06-29 for combinations of `numerical index one`,
`Mazur-Ulam property`, `MUP`, `Tingley's problem`, `lush`, and `SCD` found no
exact full answer to the unrestricted numerical-index-one question. They did
confirm the relevant arXiv records for arXiv:1210.7324, arXiv:1701.02977, and
Banakh's two-dimensional MUP result arXiv:2103.09268.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source/open-question paper, arXiv:1210.7324.
- `supporting_paper_1701.02977.pdf`: supporting theorem source.
- `source_1210.7324.tex.gz`, `supporting_source_1701.02977.tex.gz`: local
  arXiv source archives.
- `source_metadata_1210.7324.json`, `supporting_metadata_1701.02977.json`:
  local arXiv source download metadata.
- Ledger: `runs/fa_banach_001/ledger/results/1210.7324_scd_numerical_index_one_mup.json`.
