# Partial packet: nondense-square algebras answer Question 3.4 positively

Status: `partial_solution`

This packet records a positive subcase of Question 3.4 in Gardella--Thiel,
*Extending representations of Banach algebras to their biduals*, arXiv:1703.00882.

## Source Question

Question 3.4 asks whether, for a Banach algebra `A` without a left unit, there
must exist a representation `phi:A -> B(X)` on some Banach space `X` such that
the essential space of `phi` is not complemented.

The source gives examples for `A=c_0` and for many nonunital C*-algebras via
multiplier algebras. This packet gives a different positive subcase.

## Result

If `closure(A^2) != A`, then Question 3.4 has a positive answer.

Choose a nonzero functional `chi in A*` annihilating `A^2`. Let

```text
0 -> H -> Z_2 -> H -> 0
```

be the Kalton-Peck nonsplit twisted Hilbert exact sequence, and put
`T = i q` where `i:H -> Z_2` is the inclusion and `q:Z_2 -> H` is the quotient
map. Then `T^2=0` and `Range(T)=i(H)` is closed but not complemented.

Define `phi(a)=chi(a)T`. Since `chi(A^2)=0` and `T^2=0`, `phi` is a bounded
representation of `A`. Its essential space is exactly `Range(T)`, hence is not
complemented.

## Scope

This does not solve Question 3.4 for Banach algebras with dense square and no
left unit. In particular it does not settle the fixed-algebra problem for all
nonunital C*-algebras complemented in their multiplier algebras.

## Files

- `solution_packet.pdf`: human-readable packet.
- `main.tex`: LaTeX source.
