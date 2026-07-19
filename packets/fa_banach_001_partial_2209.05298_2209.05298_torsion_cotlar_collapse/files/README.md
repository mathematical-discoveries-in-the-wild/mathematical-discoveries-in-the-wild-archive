# Partial solution packet: torsion Cotlar collapse

## Source

- Paper: Adrian M. Gonzalez-Perez, Javier Parcet, and Runlian Xia,
  *Noncommutative Cotlar identities for groups acting on tree-like structures*
- arXiv: `2209.05298`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `partial`
- Target question: the source asks whether every function
  `m:G -> C` satisfying the noncommutative Cotlar identity for
  `G_0={e}` lifts to a UAC-space model of the kind in Models 1 or 2.
- Packet claim: if `G` is a torsion group, then the Cotlar closed formula
  forces `m` to be constant on `G \ {e}`. Hence torsion groups cannot supply
  nontrivial counterexamples to the reverse-UAC question. Moreover, every
  such constant-off-identity symbol has a trivial Model 1 lift on the regular
  star tree of `G`.

## Result

Let `G` be a torsion group and let `m:G -> C` satisfy

```text
(m(g^{-1}) - m(h)) (m(gh) - m(g)) = 0
```

for every `g != e` and every `h in G`. Then there is a scalar `alpha` such
that `m(g)=alpha` for every `g != e`.

Equivalently, in the torsion case the only possible freedom is the separate
value at the identity. The theorem is a solved subcase/obstruction, not a
full solution of the source reverse-construction problem.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/reverse_uac_question_page21_crop.png`: crop of the source question.
- `code/finite_cotlar_search.py`: finite sanity checker used during discovery.
- `tmp/`: LaTeX build output.

## Verification notes

The proof is purely algebraic after using the source paper's closed formula
for Cotlar multipliers. The finite checker only confirms the collapse on a
few small groups; it is not an input to the theorem.

Main reviewer focus:

- Check the finite-order inverse-symmetry induction.
- Check the two-value contradiction using `c=a^{-1}b`.
- Check that the regular-star construction is indeed a UAC/tree Model 1 lift
  for constant-off-identity symbols.
