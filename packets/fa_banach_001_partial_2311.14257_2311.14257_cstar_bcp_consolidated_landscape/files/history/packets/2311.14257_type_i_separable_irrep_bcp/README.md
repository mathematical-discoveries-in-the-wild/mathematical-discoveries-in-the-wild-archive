# Type I C*-Algebras with Separable Irreps Satisfy the Expected BCP Criterion

Status: likely valid partial result; superseded by
`2311.14257_type_i_complete_bcp_classification`.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

Let `A` be a Type I C*-algebra, and let `J_Fell(A)` be its largest Fell
ideal.  Then `J_Fell(A)` is essential.

Consequently, if every irreducible representation of `J_Fell(A)` acts on a
separable Hilbert space, then

```text
A has BCP  <=>  A has UBCP  <=>  Prim(A) has a countable pi-basis.
```

In particular, the expected criterion holds for every Type I C*-algebra all
of whose irreducible representations are separable.

This packet is now contained in the complete Type I classification packet,
which also proves the converse nonseparable Fell-fibre obstruction.

## Key Idea

The previous packet proved the criterion whenever there is an essential Fell
ideal with separable irreducible representations.  For Type I algebras, the
essentiality hypothesis is automatic.

Indeed, every nonzero Type I C*-algebra contains a nonzero continuous-trace
ideal.  If the largest Fell ideal of `A` were not essential, some nonzero
ideal `B` would be disjoint from it.  But `B` is Type I, so it contains a
nonzero continuous-trace ideal; this ideal is also an ideal of `A`, hence a
Fell ideal of `A`, contradiction.

## Scope

This removes the previous assumption that `A` itself is Fell.  The algebra may
be non-Fell and may have arbitrary Type I composition layers above the first
Fell layer.

This is still not the full arbitrary C*-classification.  It does not settle
non-Type-I open pieces, and it does not prove a negative theorem for Type I
algebras whose essential Fell ideal has nonseparable Hilbert fibres.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `supporting_paper_1207.2540.pdf`: Clark--an Huef--Raeburn Fell reference.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the use of the standard Type I composition-series theorem;
- the assertion that an ideal of an ideal is an ideal of the ambient
  C*-algebra;
- the passage from essentiality of the largest Fell ideal to the earlier
  essential-Fell BCP theorem.
