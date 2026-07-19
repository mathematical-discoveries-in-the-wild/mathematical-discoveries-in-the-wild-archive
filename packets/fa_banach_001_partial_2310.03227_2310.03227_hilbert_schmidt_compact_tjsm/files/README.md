# Hilbert-Schmidt block compact tracial joint spectral measures

status: superseded_by_full_solution

Superseded note: this partial packet has been superseded by the full compact
self-adjoint packet at
`runs/fa_banach_001/solutions/full/2310.03227_compact_self_adjoint_tjsm/`.
The old proof is retained as historical support for the easier block-diagonal
subcase.

source_arxiv: 2310.03227

source_paper: Otte Heinavaara, *Tracial joint spectral measures*

## Result

The source lists as future work the existence and uniqueness of the measures
`mu_{A,B}` for compact self-adjoint operators `A` and `B`.

This packet proves a compact-operator subcase.  If compact self-adjoint
operators `A` and `B` decompose over a common orthogonal direct sum of
finite-dimensional reducing subspaces,

```text
H = direct_sum_j H_j,       A = direct_sum_j A_j,       B = direct_sum_j B_j,
```

and

```text
sum_j (Tr A_j^2 + Tr B_j^2) < infinity,
```

then the finite-dimensional tracial joint spectral measures `mu_{A_j,B_j}`
sum to a unique positive Radon measure on `R^2 \ {0}` with finite second
moment.  The measure satisfies the source trace identity for bounded Borel
test functions supported away from zero, and also the `|t|^p` identities for
all `p >= 2`.

In particular, every commuting compact self-adjoint Hilbert-Schmidt pair has
such a canonical tracial joint spectral measure.

## Scope

This does not solve the full compact self-adjoint problem.  The attempted
general Hilbert-Schmidt compression route has a real technical issue: one must
rule out loss of the weighted second moment at the origin when passing finite
matrix measures to a limit.  The common reducing-block hypothesis avoids that
problem by making the measure an explicit countable sum.

## Evidence

- `main.tex` contains the proof packet.
- `solution_packet.pdf` is the rendered proof.
- `source_paper.pdf` is arXiv:2310.03227.
- `figures/open_problem_crop.png` shows the future-work item from the source.
- `code/verify_commuting_model.py` checks the normalization for the commuting
  diagonal Hilbert-Schmidt model.

## Human Review Recommendation

Review as a scoped partial result for the compact-operator future-work item.
The key points to check are the local finiteness estimate away from the origin,
the summability of the trace identity over blocks, and the moment-determinacy
uniqueness argument.
