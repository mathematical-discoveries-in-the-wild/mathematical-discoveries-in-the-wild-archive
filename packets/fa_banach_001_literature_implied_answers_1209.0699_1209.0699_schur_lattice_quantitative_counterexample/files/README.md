# Literature-implied answer: Schur Banach lattice outside finite-dimensional ell_1 sums

Status: `literature_implied_answer (negative answer / explicit counterexample)`.

Source paper: Timur Oikhberg and Eugeniu Spinu, *Domination of operators in the non-commutative setting*, arXiv:1209.0699.

Supporting papers:

- Miroslav Kacena, Ondrej F. K. Kalenda, and Jiri Spurny, *Quantitative Dunford-Pettis property*, arXiv:1110.1243.
- Ondrej F. K. Kalenda, *Quantitative Schur property and measures of weak non-compactness*, arXiv:2505.12893.

## Identification

Oikhberg--Spinu, Remark `rem:not l_1` in the Positive Schur Property subsection, observe that an order-continuous atomic Banach lattice with the Schur property need not be isomorphic to `ell_1`: any `ell_1`-sum of finite-dimensional lattices has the Schur property, and choosing the blocks `ell_2^n` avoids `ell_1`. They then say they do not know any Banach lattice with the Schur property that is not isomorphic, even as a Banach space, to an `ell_1`-sum of finite-dimensional spaces.

The later literature supplies such an example after identification. Kacena--Kalenda--Spurny, Example 10.1, construct
`X^* = (oplus_n X_{1/n}^*)_{ell_1}`, where each `X_alpha^*` is the vector lattice `ell_1` with norm
`||x||_alpha^* = alpha ||x||_1 + ||x||_infty`. Hence `X^*` is a Banach lattice, indeed an atomic/order-continuous one, and Example 10.1 states that `X^*` has the Schur property.

Kalenda's later quantitative-Schur paper states that this same `X^*` fails the quantitative Schur property. The same paper proves that arbitrary `ell_1`-sums preserve the `c`-Schur property. Since every finite-dimensional Banach space has the `1`-Schur property and quantitative Schur is invariant under Banach-space isomorphism up to changing the constant, any space isomorphic to an `ell_1`-sum of finite-dimensional spaces must have quantitative Schur. Therefore the Kacena--Kalenda--Spurny `X^*` is not isomorphic to such a sum.

## Scope

This packet records a literature-implied answer to the source remark: there does exist a Banach lattice with the Schur property that is not isomorphic to an `ell_1`-sum of finite-dimensional spaces. The supporting authors do not explicitly identify Oikhberg--Spinu's remark; the relation is an agent-identified implication. The packet does not address the main non-commutative domination problem in arXiv:1209.0699.

## Files

- `source_paper.pdf`: arXiv:1209.0699.
- `supporting_paper_1110.1243.pdf`: arXiv:1110.1243.
- `supporting_paper_2505.12893.pdf`: arXiv:2505.12893.
- `evidence_sources/`: local TeX sources used for line-level checking.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status packet.
