# Regular-Family Replacement Classes: Full Isometry Groups

status: candidate_full_solution

source_arxiv_id: 1907.06815
source_title: Isometries of combinatorial Banach spaces
source_authors: C. Brech, V. Ferenczi, A. Tcaciuc

## Target

Brech--Ferenczi--Tcaciuc ask, after proving that isometries of combinatorial
Banach spaces are signed permutations:

- Question 16: Given a regular family `F`, what are the permutations of the
  basis which induce an isometry of `X_F`?
- Question 17: For which combinatorial spaces can we explicitly describe the
  group of its isometries?

## Result

For a spreading family `F`, define `i <=_F j` to mean that `j` can replace
`i` in every finite context without leaving `F`. This replacement relation is
a preorder, and for spreading families it is total. Its equivalence classes
are consecutive intervals of `N`.

The packet proves

```text
Aut(F) = product_C Sym(C),
```

where `C` ranges over the replacement classes. Therefore, for every regular
combinatorial Banach space,

```text
Isom(X_F) = Signs^N semidirect product product_C Sym(C),
```

with the same permutation part for `X_F^*`.

## Proof Idea

Spreading gives `i <=_F j` whenever `i < j`. If a permutation preserves the
family, it transports the replacement preorder and hence induces an order
automorphism of the well-ordered quotient by replacement classes. Such an
order automorphism is trivial, so the permutation must preserve every class.

Conversely, any permutation inside a replacement class is generated on each
finite set by transpositions of mutually replaceable coordinates, and each
such transposition preserves the family. Thus every blockwise permutation is
allowed. The signed-permutation theorem of Brech--Ferenczi--Tcaciuc then
transfers the family automorphism classification to the Banach-space isometry
group.

## History

The previous active packet proved only the threshold-family subcase
`F_g = {empty} union {A finite nonempty: |A| <= g(min A)}`. That packet has
been moved into `history/previous_threshold_family_partial_2026_06_14/`.
The new packet verifies that result as a special case and then proves the
general replacement-class theorem.

## Files

- `main.tex` - active full solution packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - source paper PDF.
- `figures/open_problem_crop.png` - crop of the source questions on page 11.
- `evidence/supplied_regular_family_isometries_2026_06_21/` - supplied TeX
  and PDF report used for this promotion.
- `history/previous_threshold_family_partial_2026_06_14/` - older partial
  packet, retained for provenance.

## Review Notes

The main proof points to check are:

- the transitivity argument for the replacement preorder;
- the claim that an automorphism of a spreading family fixes every replacement
  class because the quotient is a well-order;
- the converse construction reducing arbitrary blockwise permutations on a
  finite set to transpositions inside replacement classes;
- the transfer from family automorphisms to isometries via the
  Brech--Ferenczi--Tcaciuc signed-permutation theorem.

The packet includes a literature-status discussion. The result uses known
finite antecedents such as desirability/vicinal preorders, but it records the
countably infinite Banach-space conclusion as a candidate full solution rather
than as a mere literature-implied answer.
