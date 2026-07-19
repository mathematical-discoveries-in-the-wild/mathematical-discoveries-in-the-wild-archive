# Partial Result: Locally Split-Range Pre-Hilbert-Schmidt Operators

Status: `strengthened_partial_result_likely_valid`

Source: arXiv:1406.7546, Said Amana Abdillah, Jean Esterle, and Bernhard H. Haak, "Sur quelques extensions au cadre Banachique de la notion d'operateur de Hilbert-Schmidt".

## Target

At the end of Section 5, the source conjectures that every pre-Hilbert-Schmidt operator `u:E -> F` factors through a Hilbert-Schmidt space.

## Result

The conjecture holds when the range factorization is locally split on both sides.

Precisely, suppose `u:E -> F` is pre-Hilbert-Schmidt and

```text
u = j q,     q:E -> Y,     j:Y -> F,
```

where `q` is onto and `j` is an isomorphic embedding. If finite-dimensional subspaces of `Y` lift through `q` with a uniform constant, and finite-dimensional subspaces of `j(Y)` are uniformly locally complemented in `F`, then `Y` is a Hilbert-Schmidt space, so `u` factors through a Hilbert-Schmidt space.

In particular, if `u(E)` is closed and complemented in `F`, and the quotient map `E -> u(E)` has a bounded linear right inverse, then `u(E)` is Hilbert-Schmidt. The range of any pre-Hilbert-Schmidt projection is therefore a Hilbert-Schmidt space.

## Proof Mechanism

The source proves that a Banach space `Y` is Hilbert-Schmidt iff every operator `Y -> H` into a Hilbert space is 2-summing. The proof first shows that a pre-Hilbert-Schmidt operator has a uniform Hilbert-test constant: `pi_2(Wu) <= C_u ||W||` for all Hilbert-valued `W`. Then, for a finite family in `Y`, local complementability extends `B` only on its span, and local lifting pulls that finite family back through `q`. Since `2`-summing is tested on finite families, the uniform local constants are enough.

The false route with merely complemented range is recorded in `runs/fa_banach_001/attempts/1406.7546_phs_complemented_range_false_start/`; quotient maps do not automatically provide the uniform weak `ell_2` lifting needed for that stronger claim.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: downloaded arXiv source PDF.
- `source_1406.7546.tex`: local TeX source snapshot.

Ledger: `runs/fa_banach_001/ledger/results/1406.7546_split_range_phs_factorization.json`
