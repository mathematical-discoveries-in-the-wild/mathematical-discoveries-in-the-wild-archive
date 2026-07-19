# Compact self-adjoint tracial joint spectral measures

status: full_solution_likely_valid

source_arxiv: 2310.03227

source_paper: Otte Heinavaara, *Tracial joint spectral measures*

## Result

The source lists as future work the existence and uniqueness of tracial joint
spectral measures `mu_{A,B}` for compact self-adjoint operators `A` and `B`.

This packet proves the compact self-adjoint case.  For every pair of compact
self-adjoint operators `A,B` on a separable Hilbert space there is a unique
positive Radon measure on the punctured plane `R^2 \ {0}`, supported in

```text
{(a,b): |a| + |b| <= ||A|| + ||B||},
```

such that for every `x,y` and every continuous test function `f` compactly
supported away from `0`,

```text
Tr H(f)(xA+yB) = int f(ax+by) d mu_{A,B}(a,b),
H(f)(s) = int_0^1 ((1-t)/t) f(ts) dt.
```

The identity extends to bounded Borel tests supported away from `0`.  If
`A,B` belong to `S_p`, the measure also satisfies the expected Schatten
`p`-moment identity.

## Why This Upgrades The Partial Packet

The previous packet required common finite-dimensional reducing blocks and a
summable Hilbert-Schmidt second moment.  The full proof avoids global moment
control.  Compactness is used only locally on annuli away from the origin:
finite-dimensional compression measures have uniformly bounded mass on each
compact subset of the punctured plane, because finitely many spectral values of
each compact linear combination can remain above a fixed threshold.

## Evidence

- `main.tex` contains the proof packet.
- `solution_packet.pdf` is the rendered proof.
- `source_paper.pdf` is arXiv:2310.03227.
- `figures/open_problem_crop.png` shows the future-work item from the source.
- `code/verify_diagonal_non_hs.py` illustrates a compact diagonal model beyond
  the Hilbert-Schmidt regime: annular mass is finite while the global second
  moment diverges.

## Human Review Recommendation

Review as a claimed full solution of the compact self-adjoint future-work item,
with the standard convention that the finite-dimensional measure is unique
away from the origin.  The main proof points to check are the uniform annular
mass estimate for finite-rank compressions, trace convergence for functions
vanishing near zero, and the ridge-density uniqueness lemma.
