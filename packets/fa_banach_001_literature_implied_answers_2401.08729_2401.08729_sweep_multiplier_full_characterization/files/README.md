# Full sweep–multiplier characterization of semicommutative paraproducts

Status: **literature-implied full structural answer, likely valid; human review recommended**

Source question: Zhenguo Wei and Hao Zhang, *Boundedness of operator-valued
commutators involving martingale paraproducts*, arXiv:2401.08729, PDF page 2.

## Result

For an arbitrary, possibly noncommuting, `d`-adic symbol `b`, let

`a_I = sum_alpha (b_I^alpha)^* b_I^alpha`

and form the positive finite sweeps

`S_F(b) = sum_{I in F} a_I 1_I/|I|`.

Then the semicommutative left paraproduct `pi_b` is bounded on `L_2` if and
only if both of the following quantities are finite:

1. the column martingale BMO norm of `b`;
2. the uniform `d`-adic Haar-multiplier norm of
   `Lambda_{S_F(b)} = pi_{S_F(b)} + pi_{S_F(b)}^*` over finite `F`.

Quantitatively, if `P(b) = sup_F ||pi_b^F||`,
`M(b) = sup_F ||Lambda_{S_F(b)}||`, and `C(b)=||b||_{BMO_c}`, then

`P(b)^2 <= M(b)+C(b)^2 <= 3 P(b)^2`.

Thus this is a necessary-and-sufficient condition for all noncommuting
symbols, not only the commuting subcase in the earlier lane-8 packet.

## Idea of the proof

For every finite coefficient set `F`, orthogonality of the Haar differences
gives an explicit positive square:

`(pi_b^F)^* pi_b^F f = sum_{I in F} (1_I/|I|) a_I m_I f`.

Relative to the Haar-tree decomposition, the strict lower and upper block
parts of this operator are exactly `pi_{S_F(b)}` and its adjoint.  Its block
diagonal part `D_F` is positive and is bounded by `C(b)^2`.  Hence

`(pi_b^F)^* pi_b^F = Lambda_{S_F(b)} + D_F`.

Conversely, indicator tests show `C(b) <= P(b)`.  These two observations give
the displayed two-sided estimate and uniform finite truncations construct the
full paraproduct.

## Provenance and scope

Blasco and Pott, arXiv:0805.0158, Lemma 2.3 and Theorem 2.4 (PDF pages 6–7),
prove the dyadic `B(H)`-valued identity and norm equivalence.  Representing
`M` by left multiplication on `L_2(M)` gives the semicommutative dyadic
answer immediately.  The packet supplies the direct `d`-adic Haar-block
proof, including the `(d-1)` Haar modes per interval and the infinite-symbol
truncation formulation.

This is a full **structural** characterization.  It is not a characterization
by column BMO alone, and it does not claim that the sweep-multiplier condition
can be replaced by a familiar scalar-like oscillation norm.  The sharp matrix
examples force the extra sweep term to grow at logarithmic-squared scale.

## Files

- `main.tex` and `solution_packet.pdf`: formal theorem, proof, and provenance.
- `source_paper.pdf`: arXiv:2401.08729.
- `supporting_0805.0158.pdf`: decisive Blasco–Pott paper.
- `figures/open_problem_crop.png`: source question on PDF page 2.
- `verification_report.md`: mathematical and packet checks.

