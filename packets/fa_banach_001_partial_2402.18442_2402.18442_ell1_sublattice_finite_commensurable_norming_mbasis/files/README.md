# Closed sublattices of `ell_1(Gamma)` in the norming-M-basis heredity problem

Status: `partial_result`

Source: Petr Hajek and Tommaso Russo, *Norming Markushevich bases: recent
results and open problems*, arXiv:2402.18442.

Open problem: Problem 6.1 asks whether every closed subspace of a Banach
space with a norming Markushevich basis again admits a norming Markushevich
basis.

## Result

Every closed sublattice of `ell_1(Gamma)` has a `1`-norming Markushevich
basis. More precisely, any closed sublattice of `ell_1(Gamma)` is lattice
isometric to an atomic `L_1` space, hence to a weighted `ell_1(A)`, and its
atoms give the desired norming M-basis.

Combining this with the finite-codimensional invariance packet already
promoted in this run gives the following extension: if a closed subspace
`Z` of `ell_1(Gamma)` is finitely commensurable with a closed sublattice `L`
in the sense that `Z + L` has finite-dimensional quotient over both `Z` and
`L`, then `Z` has a norming M-basis.

## Scope

This strengthens a named subcase in the source discussion. Hajek and Russo
record that closed sublattices of `ell_1(Gamma)` are known to be `1`-Plichko;
the packet observes that the lattice structure yields the stronger
norming-M-basis conclusion.

This does not solve the arbitrary subspace problem for `ell_1(Gamma)`.
The proof uses positivity and lattice closure in an essential way.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2402.18442.
- `figures/open_problem_crop.png`: source crop for Problem 6.1.

## Verification Notes

The literature check used the source v3 arXiv page, local parsed source,
and web searches for:

```text
"norming Markushevich bases" heredity subspaces
"norming M-basis" subspace heredity
"subspaces of l1(Gamma)" Plichko Kalenda Question 4.44
"closed sublattice" "ell_1" "norming M-basis"
"closed sublattice of l1 Gamma is isometric to l1"
```

No later resolution of Problem 6.1 or exact closed-sublattice
norming-M-basis statement was found. The closed-sublattice step itself is a
standard Banach-lattice consequence of Kakutani representation and atomicity;
the novelty here is the application to the source problem and the finite
commensurability corollary.

## Human Review Recommendation

Review as a narrow but durable positive subcase of Problem 6.1, especially
the atomicity lemma for closed sublattices of `ell_1(Gamma)` and the
finite-commensurability corollary's use of the earlier finite-codimensional
invariance packet.
