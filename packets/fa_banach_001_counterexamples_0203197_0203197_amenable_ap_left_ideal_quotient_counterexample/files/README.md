# Counterexample Packet: Amenable AP Algebra with a Non-AP Left-Ideal Quotient

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `0203197`
- source paper: Volker Runde, *Banach space properties forcing a reflexive, amenable Banach algebra to be trivial*
- target passage: PDF page 9 / source lines 382--392, where Runde asks whether an amenable Banach algebra with the approximation property has AP quotients by all closed left ideals.

## Claim

Runde's formal question has a negative answer.

There exists an amenable Banach algebra `A` whose underlying Banach space has the approximation property and a closed left ideal `L` such that `A/L` fails the approximation property.

## Construction

Fix `1 < p < infinity`, `p != 2`, and choose a quotient map

```text
q : ell_p -> Y
```

where `Y` fails the approximation property. Such quotients exist by the Lindenstrauss--Tzafriri results cited by Runde.

Let `B = A(ell_p) = K(ell_p)` be the Banach algebra of approximable operators on `ell_p`, and set `A = B^op`. The algebra `B`, hence also `A`, is amenable. As a Banach space, `B` has the metric approximation property, using the finite coordinate compressions of compact operators.

Let `F = ker q` and let

```text
J = { T in B : T(ell_p) subset F }.
```

Then `J` is a closed right ideal of `B`, hence a closed left ideal of `A`. The quotient `B/J = A/J` contains a complemented copy of `Y`: choose `x0 in ell_p` and `f in ell_p^*` with `f(x0)=1`, then

```text
i(qx) = [ z -> f(z)x ],        P([T]) = q(Tx0),
```

and `P i = id_Y`. Therefore, if `A/J` had AP, then `Y` would have AP, contradiction.

## Files

- `main.tex`: full counterexample packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:0203197
- `supporting_paper_0804.1725.pdf`: local copy of Blanco--Gronbaek, used for the approximable-operator amenability reference
- `figures/open_problem_crop.png`: crop of Runde's formal question
- `code/make_open_problem_crop.py`: script used to regenerate the crop
- `code/verify_counterexample_structure.py`: sanity check for the ideal/complemented-copy construction in finite matrix form

## Novelty Check

Before promotion, the run indexes were searched for `0203197`, the source title, `reflexive amenable Banach algebra`, `amenable Banach algebra approximation property left ideal quotient`, `A(ell_p)`, and `approximable operators left ideal quotient`. No prior packet for this question was present; only an earlier no-promotion attempt for the same paper was indexed.

External web searches for exact phrases around Runde's question and for later work on reflexive amenable Banach algebras did not reveal a direct settlement. A final targeted search for `"amenable Banach algebra" "closed left ideal" "fails the approximation property"`, `"A(ell_p)" "left ideal" "approximation property" quotient`, and close variants returned no hits. The counterexample uses a supporting paper already in the local corpus, Blanco--Gronbaek arXiv:0804.1725, for the amenability of algebras of approximable operators on classical `L_p` spaces.

Human review should focus on the orientation switch from a right ideal of `A(ell_p)` to a left ideal of the opposite algebra, and on the complemented embedding of the non-AP quotient `ell_p/F` into `A(ell_p)/J`.
