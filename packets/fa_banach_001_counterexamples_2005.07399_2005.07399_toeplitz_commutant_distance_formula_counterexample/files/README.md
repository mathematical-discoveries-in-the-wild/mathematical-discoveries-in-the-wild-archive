# Counterexample: Toeplitz commutant obstruction to the C*-distance formula

Status: `counterexample_likely_valid`

Source paper: Priyanka Grover and Sushil Singla, *Birkhoff-James
orthogonality and applications : A survey*, arXiv:2005.07399.

## Target

On PDF pages 15--16, around source lines 358--366, the paper asks whether the
following formula is true. If `A` is a unital irreducible C*-algebra, `a in A`,
and `B` is a unital C*-subalgebra of `A`, must

```text
2 dist(a,B) = sup{ ||au - ua|| : u in A is unitary and bu = ub for all b in B } ?
```

The packet gives a counterexample.

## Counterexample

Let `H = ell_2(N)`, let `A = B(H)`, let `S` be the unilateral shift, and let
`B = C*(S)` be the Toeplitz algebra. Let `D` be the diagonal unitary
`D e_n = (-1)^n e_n`.

Then `A` is unital and irreducible, and `B` is a unital C*-subalgebra of `A`.
The only operators commuting with `B` are scalar multiples of the identity, so
every unitary commuting with `B` gives `DU-uD=0`. Hence the right hand side of
the proposed formula is `0`.

On the other hand `D` is not in `B`. Indeed every `X in C*(S)` has compact
commutator `[X,S]`, while `[D,S]e_n = -2(-1)^n e_{n+1}`, which is not compact.
Since `B` is norm closed, `dist(D,B)>0`. Therefore the left hand side is
positive and the proposed formula fails.

## Files

- `main.tex`: full counterexample packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of arXiv:2005.07399.
- `figures/open_problem_crop.png`: stitched source crop showing the open
  question and formula (4.3).
- `code/toeplitz_sanity_check.py`: finite-section sanity check for the
  commutator mechanism; the proof itself is analytic.

## Search Bounds

Before promotion, the cheap run indexes were searched for `2005.07399`,
`Birkhoff-James`, `orthogonality`, `distance formula`, `C*-subalgebra`,
`Toeplitz`, and related phrases. No prior packet for this target was found.

Web searches on 2026-06-19 for exact and close variants of `2 dist(a,B)`,
`au - ua`, `unitary`, `commutes`, `Birkhoff-James`, `conditional expectation`,
and `Toeplitz algebra` found the source arXiv paper but no separate later paper
explicitly resolving this exact question.

## Human Review Notes

Recommended review focus:

- Confirm that the paper's phrase "unital irreducible C*-algebra" permits the
  standard represented example `A=B(ell_2)`.
- Check the elementary commutant computation for `C*(S)`.
- Check the proof that `D` is outside `C*(S)` via compactness of commutators
  with `S`.
