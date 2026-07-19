# Literature-implied answer: two closing ideal-lattice questions for `C([0,omega_1])`

Status: `literature_implied_answer`

Source question paper: arXiv:1112.4800, Tomasz Kania and Niels Jakob
Laustsen, *Uniqueness of the maximal ideal of the Banach algebra of bounded
operators on C([0,omega_1])*.

Supporting paper: arXiv:1304.4951, Tomasz Kania and Niels Jakob Laustsen,
*Operators on two Banach spaces of continuous functions on locally compact
spaces of ordinals*.

## Identification

The closing remark of arXiv:1112.4800 asks whether

```text
overline(G_{C(K)})(C([0,omega_1])) subset M
```

is proper, and conjectures that it is. Here `K` is the one-point
compactification of the disjoint union of the spaces
`K_alpha=[0,omega^{omega^alpha}]`, `alpha<omega_1`, and `M` is the
Loy--Willis ideal.

This conjecture is false by later literature after identifying the factor
space. The source's `C(K)` is isomorphic to

```text
C scalar direct_sum (oplus_{alpha<omega_1} C(K_alpha))_{c0}.
```

For `A={omega^{omega^alpha}: alpha<omega_1}`, the non-scalar summand is
`E_A` in the notation of arXiv:1304.4951. Lemma 2.4 of that paper gives
`E_A isomorphic E_{omega_1} isometric C_0(L_0)`, and `E_{omega_1}` absorbs a
one-dimensional summand. Thus `C(K)` is isomorphic to `C_0(L_0)`.

The supporting paper records that the Loy--Willis ideal is exactly the ideal
of operators factoring through `C_0(L_0)`. Therefore the source inclusion is
an equality, not a proper inclusion.

The same closing remark asks whether

```text
overline(G_{C(K_alpha) direct_sum c0(omega_1)}) subset SZ_{alpha+1}
```

is proper for some or each countable ordinal `alpha`. The supporting paper
proves, for every countable `alpha >= 1`, the strict intermediate inclusion

```text
overline(G_{C(K_alpha) direct_sum c0(omega_1)})
  proper_subset
overline(G_{c0(omega_1, C(K_alpha))})
  subset
SZ_{alpha+1}.
```

Hence the source inclusion is proper for every nonzero countable ordinal
`alpha`. The `alpha=0` endpoint and the later stronger equality question
between the intermediate ideal and `SZ_{alpha+1}` are not claimed here.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1112.4800.
- `supporting_paper_1304.4951.pdf`: arXiv:1304.4951.

