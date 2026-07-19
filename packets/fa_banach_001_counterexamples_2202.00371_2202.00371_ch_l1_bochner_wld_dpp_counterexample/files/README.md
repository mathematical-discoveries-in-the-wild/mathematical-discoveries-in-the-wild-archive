# Counterexample Packet: CH `L1(mu)` WLD-DPP Factor

Run: `fa_banach_001`

Status: counterexample under CH, likely valid.

Source paper: A. Aviles, G. Martinez-Cervantes, J. Rodriguez,
A. Rueda Zoca, *Topological properties in tensor products of Banach spaces*,
arXiv:2202.00371.

## Target

Question 8(b) asks whether `X \hat\otimes_\pi Y` is WLD whenever `X` and `Y`
are WLD and one of them has the Dunford-Pettis property.

## Result

Assuming CH, the answer to Question 8(b) is negative.

More precisely, under CH there are WLD Banach spaces `X,Y` such that `X` has
the Dunford-Pettis property but

```text
X \hat\otimes_\pi Y
```

is not WLD.  One can take `X = L1(mu)` for a finite measure `mu`.

## Key Point

The source paper cites that, under CH, there is a WLD Banach space `Y` whose
dual ball `(B_{Y*}, w*)` fails property `(M)`.  Its Lebesgue-Bochner
corollary says that for WLD `Y`, property `(M)` of `(B_{Y*}, w*)` is equivalent
to `L1(mu,Y)` being WLD for every finite measure `mu`.  Hence failure of
property `(M)` gives a finite measure `mu` with `L1(mu,Y)` not WLD.

Since `L1(mu,Y)` is isometric to `L1(mu) \hat\otimes_\pi Y`, and finite-measure
`L1(mu)` spaces are WCG, WLD, and have the Dunford-Pettis property, this is a
CH counterexample to the source question.

Equivalently, via the source paper's Theorem 4.1, the same `mu` yields a
bounded operator `L1(mu) -> Y*` with nonseparable range.

## Relation to Previous Packet

This complements the ZFC positive partial packet
`solutions/partial/2202.00371_c0_projective_tensor_wld_subcase/`, which proves
the `c0(Gamma)` factor subcase.  The present packet shows that the arbitrary
WLD+DPP question cannot have an unconditional positive answer under CH.

## Contents

- `source_paper.pdf`: local copy of arXiv:2202.00371.
- `figures/open_question_page28.png`: rendered source page containing the open
  questions.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `code/README.md`: note on verification method.

## Limitations

This is not a ZFC counterexample.  It proves a negative answer under the
standard extra set-theoretic assumption CH.  The ZFC status of Question 8(b)
remains separate.

## Human Review Recommendation

Review as a likely valid counterexample under CH.  The main points to check
are the source corollary's quantifier "for every finite measure `mu`" and the
standard facts that finite-measure `L1(mu)` is WCG/WLD and has the
Dunford-Pettis property.
