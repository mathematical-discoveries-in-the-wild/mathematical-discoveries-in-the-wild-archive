# Candidate full solution: real \(\mathcal{BL}_1L_2\) endpoint

Status: `candidate_full_solution_human_review_needed`

Source paper: Yves Raynaud, *New axiomatizable classes of Banach spaces via disjointness-preserving isometries*, arXiv:1603.07510.

## Claim

Raynaud's Question 6.17 asks whether the Banach-space reduct of
\(\mathcal{BL}_1L_q\) is axiomatizable for \(1<q\le 2\).  This packet claims a
positive answer at the real Hilbert endpoint:

```text
(\mathcal{BL}_1L_2)^B is axiomatizable as a class of real Banach spaces.
```

Equivalently, the class is closed under ultraroots.  Closure under
ultraproducts is supplied by the known Banach-lattice/mixed-norm theory.

## Proof Idea

The proof avoids reconstructing the lattice structure in Hilbert fibres,
which is impossible from the Banach norm alone.  Instead it defines a
canonical radial truncation operation \(\beta\) on \(L_1\)-direct integrals of
real Hilbert spaces.  The operation is described intrinsically using the
Boolean algebra of \(L\)-projections, is preserved by surjective linear
isometries, and commutes with ultraproducts.

A Keisler--Shelah common-ultrapower/equalizer argument then shows that
ultraroots inherit \(\beta\)-closed diagonal copies.  The remaining geometric
statement is that every closed \(\beta\)-invariant subspace of an
\(L_1\)-direct integral of Hilbert spaces is again an \(\ell_1\)-sum of
Hilbert-valued \(L_1\)-spaces.  This is proved by extracting a scalar
sub-\(\sigma\)-algebra and applying Raynaud's module representation lemma.

## Relation To Previous Packet

The previous active packet
`1603.07510_bl1lq_ge2_nonaxiomatizable_qle2` is no longer an active partial
solution.  It is stored under `history/absorbed_packets/` as a failed
stable-variable route: mutual finite representability gives ultrapower
embeddings, not the surjective ultrapower identification needed by that
argument.

This new packet does not claim the whole range \(1<q<2\).  It only claims the
real endpoint \(q=2\).

## Files

- `main.tex`: active proof packet.
- `solution_packet.pdf`: rendered active packet.
- `source_paper.pdf`: local copy of arXiv:1603.07510.
- `figures/question_6_17_crop.png`: source open-question crop.
- `evidence/supplied_endpoint_note_2026_06_18/`: supplied TeX/PDF proof draft.
- `history/absorbed_packets/1603.07510_bl1lq_ge2_nonaxiomatizable_qle2_failed_stable_variable_route/`: older failed partial route.

## Human Review Focus

Review as a serious candidate full proof, with special attention to:

1. the intrinsic characterization of \(L\)-projections and of the radial operation \(\beta\);
2. ultraproduct compatibility for \(\beta\);
3. the metric Keisler--Shelah common-ultrapower/equalizer transfer;
4. the proof that every closed \(\beta\)-invariant subspace is again an \(\ell_1\)-sum of Hilbert-valued \(L_1\)-spaces;
5. the use of Raynaud's module representation lemma with \(p=1\).
