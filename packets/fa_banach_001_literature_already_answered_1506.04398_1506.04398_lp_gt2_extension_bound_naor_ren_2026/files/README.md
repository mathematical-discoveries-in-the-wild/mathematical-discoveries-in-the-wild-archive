# Literature-Already-Answered Packet: `e_n(ell_p, ell_q)` for `p,q>2`

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is an exact later-literature answer/status improvement to a
question recorded by Naor--Rabani, not a new proof from this run.

## Source Problem

- Assaf Naor, Yuval Rabani, *On Lipschitz extension from finite subsets*,
  arXiv:1506.04398; Israel J. Math. 219(1):115--161, 2017.
- Local PDF: `source_paper.pdf`.
- Evidence image:
  - `figures/open_problem_crop.png` (page 8, Section 1.4).

The source paper surveys basic open questions on Lipschitz extension between
`ell_p` spaces. In the case `p,q in (2,infty)`, it records that no upper bound
on `e_n(ell_p,ell_q)` asymptotically smaller than the general `LN05` bound
`O((log n)/log log n)` was known.

## Supporting Literature

- Assaf Naor, Kevin Ren, *Euclidean embedding, randomized clustering, and
  Lipschitz extension for finite and doubling subsets of `L_p` when `p>2`*,
  arXiv:2502.10543.
- Local PDF: `supporting_paper_2502.10543.pdf`.
- Evidence images:
  - `figures/supporting_answer_crop.png` (page 7, Theorem 1.5 and explicit
    statement that it answers a question stated in Naor--Rabani 2017).
  - `figures/supporting_reference_crop.png` (page 59, bibliography entry
    `[82]` identifying Naor--Rabani 2017).

## Literature Status

The improved upper bound is now known. Naor--Ren prove that for every
`2<p<infty`,

```text
e_n(L_p) <= C p^2 sqrt(log n),
```

where `e_n(L_p)` is the supremum over all subsets of `L_p` of cardinality at
most `n` and all Banach targets. They explicitly state that this answers the
natural question left open by `LN05` and stated in Naor--Rabani 2017.

Since `ell_p` embeds isometrically into an `L_p` space, the theorem restricts
to `ell_p`. Taking the Banach target to be `ell_q` gives

```text
e_n(ell_p, ell_q) <= C p^2 sqrt(log n) = o((log n)/log log n)
```

for every fixed `p,q in (2,infty)`.

## Proof Idea

The source passage asks whether the `p,q>2` extension problem has any upper
bound better than the universal finite-metric extension bound. Naor--Ren prove
a stronger theorem for the whole domain `L_p`: every `n`-point subset of
`L_p` admits Banach-valued Lipschitz extensions with loss `O_p(sqrt(log n))`.
Because `ell_p` sits isometrically in `L_p`, an extension from `L_p` can be
restricted back to `ell_p`; choosing the target Banach space to be `ell_q`
therefore yields the desired special case.

## Limitations

- This is a literature-status packet, not an original result.
- It addresses the source paper's `p,q>2` upper-bound gap for Lipschitz
  extension between `ell_p` spaces.
- It does not settle the separate Kalton Holder-extension questions or the
  finite-dimensional Ball extension question in the same source paper.
- It does not give sharp asymptotics; the exact growth rate remains a further
  problem beyond this status identification.

## Files

- `README.md`: this packet summary.
- `main.tex`: literature-status packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original source paper.
- `supporting_paper_2502.10543.pdf`: later paper answering the question.
- `figures/open_problem_crop.png`: source open-status crop.
- `figures/supporting_answer_crop.png`: supporting theorem and answer crop.
- `figures/supporting_reference_crop.png`: supporting bibliography crop.
- `tmp/`: LaTeX build intermediates.

## Verification And Search Notes

Before packaging, the run lightweight indexes were searched for `1506.04398`,
the title phrase, `Lipschitz extension`, `finite subsets`, `ell_p`, `ell_q`,
and nearby core terms. No existing exact packet or attempt was found. Broad
hits to other Lipschitz/free-space packets were not duplicates, and human-only
archive contents were not opened.

The source and supporting arXiv PDFs and source bundles were checked directly.
The supporting paper explicitly cites Naor--Rabani 2017 as a place where the
answered question was stated.

## Human Review Recommendation

Treat the `p,q>2` upper-bound gap recorded in arXiv:1506.04398 Section 1.4 as
already answered by arXiv:2502.10543. Keep the named Kalton and Ball questions
from arXiv:1506.04398 separate; this packet does not claim they are solved.
