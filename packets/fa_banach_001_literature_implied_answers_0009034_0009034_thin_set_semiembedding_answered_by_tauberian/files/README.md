# Thin sets and semi-embeddings

Status: literature_implied_answer.

Source question: Olav Nygaard, "Boundedness and surjectivity in normed spaces",
arXiv:math/0009034, Question 6.2.

Supporting theorem: Jose Rodriguez, "On integration in Banach spaces and total
sets", arXiv:1806.10049, Remark 4.7, citing Neidinger--Rosenthal, Pacific
Journal of Mathematics 118 (1985), no. 1, 215--228.

## Identification

Nygaard asks whether, for every thin set `A subset B_X`, there are a Banach
space `Y` and a semi-embedding `T:Y -> X` such that `TY` contains `A` while
`T` is not onto.

The answer is yes by combining two statements:

1. Nygaard's Theorem 3.2 proof already constructs, for every thin `A`, a
   Tauberian injection `J:Y -> X` with `JY` containing `A` but `J` not onto.
2. Rodriguez's Remark 4.7 records the standard Neidinger--Rosenthal
   characterization: an operator is injective and Tauberian if and only if its
   restriction to every subspace is a semi-embedding. Taking the whole domain
   as the subspace shows that Nygaard's `J` is a semi-embedding.

Thus Question 6.2 has an affirmative literature-implied answer.

## Scope

This packet answers only Question 6.2. It does not address the surrounding
questions about bounded fundamental thin sets, norming thin sets, thickness of
inner functions/Blaschke products, or James boundaries in `H^\infty`.

This is an agent-identified implication. The supporting paper does not appear
to explicitly cite or resolve Nygaard's Question 6.2 by name.
