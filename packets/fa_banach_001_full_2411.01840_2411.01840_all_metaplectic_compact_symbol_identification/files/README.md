# All-metaplectic compact-symbol identification

Status: `full_solution_likely_valid`

This packet removes the simultaneous-diagonalizability hypothesis from Theorem 5.11 of Henry McNulty, *Metaplectic Quantum Time--Frequency Analysis, Operator Reconstruction and Identification*, arXiv:2411.01840.  For every symplectic matrix and every compact support set, a sufficiently fine real lattice identifies the corresponding compactly supported metaplectic-symbol class with the standard Gaussian window.

The key new lemma is elementary: for every invertible complex matrix (C) and compact (K\subset\mathbb R^m), the functions

\[
  \{e^{t^TC\lambda}:\lambda\in\varepsilon\mathbb Z^m\}
\]

are uniformly dense in (C(K)) when (\varepsilon>0) is small enough.  A local logarithm recovers all coordinate functions from the lattice exponentials, after which Stone--Weierstrass applies.

Files:

- `solution_packet.pdf`: rendered expert-facing proof packet.
- `main.tex`: complete proof source.
- `source_paper.pdf`: original arXiv paper.
- `figures/source_theorem_crop.png`: source Theorem 5.11.
- `figures/open_problem_crop.png`: source Remark 5.14 proposing removal of diagonalizability.
- `verification.md`: proof audit and novelty-search bounds.
- `code/sanity_check.py`: non-proof numerical checks of the two matrix/logarithm steps.

Reproduce the numerical sanity check with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2411.01840_all_metaplectic_compact_symbol_identification/code/sanity_check.py
```

Human-review recommendation: verify the standard metaplectic-Gaussian orbit formula and the short proof that (ZP+iR) is invertible.  Those are the only convention-sensitive steps; the uniform-density lemma is self-contained.
