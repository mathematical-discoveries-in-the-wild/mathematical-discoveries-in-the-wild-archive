# Full Result: Spreading Markushevich Bases in Banach Spaces are Schauder

## Source Question

- Source paper: J. L. Ansorena and A. Marcos, *Remarks about symmetry-type conditions of conditional bases of Banach spaces*, arXiv:2601.15784.
- Location: page 16, after Theorem 3.6 and the discussion of the summing basis of `c0`.
- Question: whether a spreading Markushevich basis that fails to be a Schauder basis exists.

## Answer

No. Every spreading Markushevich basis in a Banach space is a Schauder basis.

The proof uses Rosenthal's `ell_1` theorem and standard basic-subsequence selection. A spreading basis is seminormalized by the source paper. Rosenthal gives either an `ell_1` subsequence or a weak-Cauchy subsequence. The `ell_1` case is basic. A non-trivial weak-Cauchy subsequence has a basic subsequence. If the weak-Cauchy subsequence converges weakly in the ambient Banach space, totality of the Markushevich basis forces the weak limit to be zero, so Bessaga-Pelczynski gives a basic weakly-null subsequence. Finally, spreading equivalence transfers the bounded partial-sum projections from that basic subsequence back to the original complete minimal system.

## Files

- `main.tex`: full solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `supporting_paper_1607.03587.pdf`: conditional spreading basis context.
- `supporting_paper_1712.07638.pdf`: supporting weak-Cauchy selection reference.
- `figures/open_problem_crop.png`: crop of the source question on page 16.

## Review Focus

Review should check the use of the source definition of a spreading basis, specifically that the shift to a subsequence is an isomorphism onto the closed subsequence span. Review should also check the standard non-trivial weak-Cauchy selection step. With those conventions, the packet gives a full negative answer.
