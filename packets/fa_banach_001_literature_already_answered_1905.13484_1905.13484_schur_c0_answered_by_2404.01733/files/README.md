# Literature answer: the `schur-c0` problem is answered by the rapid Farah family

Status: `literature_already_answered`

Source problem: arXiv:1905.13484, Borodulin-Nadzieja--Farkas, *Analytic P-ideals and Banach spaces*, Problem labeled `schur-c0` in the section "Schur Property".

Supporting answer: arXiv:2404.01733, Borodulin-Nadzieja--Farkas--Jachimek--Pelczar-Barwacz, *The Zoo of combinatorial Banach spaces*, Subsection "The rapid Farah family", especially Theorem `elel`.

## Identification

The source asks whether there is a family `F` of finite subsets of `omega` such that the combinatorial Banach space `X_F` does not have the Schur property and contains no copy of `c0`.

The later ZOO paper explicitly studies the same implication chain

`Schur property => l1-saturation => no copies of c0`

for combinatorial Banach spaces, says that none of the implications reverse, and constructs the rapid Farah family `rFh`. It states that `(I_n)` witnesses that `X_rFh` does not have the Schur property, and Theorem `elel` proves that `X_rFh` is `l1`-saturated. Since every subspace of an `l1`-saturated space contains `l1`, such a space contains no copy of `c0`. Thus `F = rFh` answers the source problem affirmatively.

## Scope

This packet records a known later literature answer, not a new proof. It answers the existence problem `schur-c0`; it does not claim to settle the broader characterization problems for all families `F`.

## Files

- `source_paper.pdf`: arXiv:1905.13484.
- `supporting_paper_2404.01733.pdf`: arXiv:2404.01733.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
