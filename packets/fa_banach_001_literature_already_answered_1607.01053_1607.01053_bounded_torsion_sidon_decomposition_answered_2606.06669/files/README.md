# Bounded-torsion Sidon decomposition answered by Lewko (2026)

Status: **literature_already_answered (partial subcase)**.

Original source: Gilles Pisier, *Subgaussian sequences in probability and
Fourier analysis*, arXiv:1607.01053v3 (2016), Section 7, especially Remark
7.3 on PDF page 23.

Supporting paper: Mark Lewko, *The Sidon Decomposition Problem in Abelian
Groups of Bounded Torsion*, arXiv:2606.06669 (2026), Theorem 1.2 on PDF page
2.

## Identification

Pisier asks whether every subgaussian (equivalently Sidon) set of characters
is a finite union of quasi-independent sets. After recording the prime and
squarefree-exponent results, Remark 7.3 explicitly says that the equivalence
was still open even for exponent `p=4`.

Lewko proves the remaining bounded-torsion case: if the discrete dual group
has bounded torsion, every Sidon set is a finite union of quasi-independent
sets. This includes `(Z/4Z)^I` and therefore answers Pisier's highlighted
`p=4` subproblem, as well as every other fixed bounded-torsion case.

The supporting paper explicitly cites Pisier's 2016 survey and identifies the
prime-power obstruction as the outstanding bounded-torsion problem.

## Scope

This is not a full answer to Pisier's general conjecture. Lewko explicitly
states that the analogous problem for the dual group `Z` remains open. Thus
the packet records a complete literature answer only for the bounded-torsion
subcase.

## Files

- `main.tex` and `solution_packet.pdf`: compact status note.
- `source_paper.pdf`: arXiv:1607.01053v3.
- `supporting_paper_2606.06669.pdf`: arXiv:2606.06669.
- Ledger: `runs/fa_banach_001/ledger/results/1607.01053_bounded_torsion_sidon_decomposition_answered_2606.06669.json`.

## Search evidence

The run's registry, solution, attempt, and proof-gap indexes were searched for
the two arXiv ids and for subgaussian/Sidon/quasi-independent decomposition
terms. No prior packet was present. A targeted arXiv search found Lewko's June
2026 paper. Its introduction cites Pisier's survey, describes the remaining
prime-power obstruction, and states that its main theorem answers the
bounded-torsion question.
