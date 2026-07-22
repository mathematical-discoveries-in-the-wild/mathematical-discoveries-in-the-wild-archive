# Full negative answer: the induction map is not well defined on all Fourier multipliers

Status: `full_solution_likely_valid`

Source: Bat-Od Battseren, *On the growth of Fourier multipliers*,
arXiv:2011.00146, Remark 19 on source PDF page 10. The published version is
J. Noncommut. Geom. 18 (2024), 1209-1228, DOI 10.4171/JNCG/551; the same question
appears as Remark 4.2.

## Claimed contribution

Let `Gamma` be any uniform lattice in `G=SL(3,R)`, and let `Phi` be the
source paper's induction formula. Then there exists

```text
m in MA(Gamma) such that Phi(m) is not in MA(G).
```

Thus the proposed restriction `Phi: MA(Gamma) -> MA(G)` is not well defined.
This gives a full negative answer to Remark 19 / Remark 4.2.

## Proof mechanism

Two elementary continuity facts close the gap:

1. The source integral formula shows that the ambient map
   `Phi: ell-infinity(Gamma) -> C_b(G)` is a contraction.
2. For every locally compact group `H`, the Fourier multiplier norm dominates
   the sup norm: `||m||_infinity <= ||m||_MA(H)`.

If `Phi` mapped all of `MA(Gamma)` into `MA(G)`, take a sequence
`m_n -> m` in `MA(Gamma)` with `Phi(m_n) -> h` in `MA(G)`. Both convergences
are uniform, and ambient continuity also gives `Phi(m_n) -> Phi(m)` uniformly.
Hence `h=Phi(m)`, so the restricted map has closed graph. Since both multiplier
spaces are Banach, the closed graph theorem makes the restriction bounded. This
contradicts the source's Theorem A (published Theorem B), which proves that no
bounded restriction exists.

## Verification

The proof is qualitative and has no finite computational dependency. The
verification report checks each functional-analytic interface explicitly:

- the normalized integral formula gives the ambient sup-norm contraction;
- the coefficient-function argument gives the multiplier-to-sup embedding;
- uniqueness of uniform limits closes the graph;
- the source theorem has the same lattice and induction-map quantifiers.

Verifier focus: confirm that the source theorem is read as excluding an
everywhere-defined bounded restriction for each uniform lattice under
consideration. The 2024 published proof explicitly begins by assuming that the
map is both well defined and bounded.

## Novelty and scope

The bounded novelty check on 2026-07-22 covered the four cheap run indexes;
the exact arXiv id, title, author, induction formula, and well-definedness
phrase; arXiv searches combining `MA(Gamma)`, `MA(G)`, `induction map`,
`well defined`, and `closed graph`; the open-access 2024 journal version; and
the author's later arXiv:2408.09638 on `M_d` multipliers and lattices. No later
paper or separate statement of this closed-graph resolution was found.

Novelty confidence is moderate: the argument is short and elementary, so it
may be folklore or implicit in the wording of the published Theorem B. The
paper nevertheless explicitly retains the well-definedness question in Remark
4.2. The result is scoped to the source induction formula and the uniform
lattices in `SL(3,R)` covered by its unboundedness theorem. It does not classify
other lattice/group pairs for which induction preserves `MA`.

Human review recommendation: check the quantifiers in published Theorem B and
the standard fact that `MA(H)` is Banach with multiplier norm. If those are read
as in the source, the proof is complete.

Files:

- `source_paper.pdf`: arXiv:2011.00146.
- `published_version.pdf`: open-access JNCG 18 (2024) version.
- `figures/open_problem_crop.png`: source Remark 19, PDF page 10.
- `figures/induction_and_unboundedness_crop.png`: source Lemma 18 and Theorem A,
  PDF page 9.
- `main.tex`, `solution_packet.pdf`: full proof packet.
- `VERIFICATION.md`: adversarial verification report.
- `code/crop_source_evidence.py`: reproducible source-page crops.
