# Literature implied answer: spanning unimodular eigenvectors need not be perfectly spanning

status: literature_implied_answer

source: Sophie Grivaux, *A new class of frequently hypercyclic operators*,
arXiv:1001.2026.

supporting answer: Quentin Menet, *Linear chaos and frequent hypercyclicity*,
arXiv:1410.7173.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/1001.2026_spanning_unimodular_not_perfect_menet/`

ledger: `runs/fa_banach_001/ledger/results/1001.2026_spanning_unimodular_not_perfect_menet.json`

## Identification

In the final section of arXiv:1001.2026, Grivaux asks whether a hypercyclic
operator whose eigenvectors associated to eigenvalues of modulus one span a
dense subspace must have perfectly spanning unimodular eigenvectors.

Menet later constructs a chaotic operator on `ell_1` which is not
`U`-frequently hypercyclic, hence not frequently hypercyclic. Since a chaotic
operator has dense periodic points, and periodic points are spanned by
root-of-unity eigenvectors, Menet's operator has densely spanning unimodular
eigenvectors. If those eigenvectors were perfectly spanning, Grivaux's main
theorem in arXiv:1001.2026 would imply frequent hypercyclicity, contradicting
Menet's theorem.

Thus Grivaux's Question 2 has a negative answer by this literature
identification.

## Scope

This packet records the agent-identified implication from Menet's theorem to
Grivaux's Question 2. Menet explicitly answers the chaotic-implies-frequently
hypercyclic question; that broader duplicate is already recorded in
`runs/fa_banach_001/solutions/literature_already_answered/1005.1416_chaotic_not_fhc_answered_by_1410.7173/`.

This packet does not claim to answer Grivaux's related Question 3 about an
operator whose full unimodular point spectrum is countable. The implication
uses only the dense root-of-unity eigenspaces coming from periodic points, not
a verification of Menet's full unimodular point spectrum.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1001.2026 source paper.
- `supporting_paper_1410.7173.pdf`: Menet's supporting paper.
