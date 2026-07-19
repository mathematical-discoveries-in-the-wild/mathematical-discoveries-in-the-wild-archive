# Partial Result: Weak-star complemented subcase of the Rosenthal projection conjecture

Status: `partial`

Run: `fa_banach_001`

Source paper: arXiv:0912.3133, Pascal Lefevre, Daniel Li, Herve Queffelec,
and Luis Rodriguez-Piazza, "Some translation-invariant Banach function spaces
which contain c0."

## Claim Recorded

The source paper conjectures that `C_Lambda` is complemented in
`L^\infty_Lambda` only in the trivial/Rosenthal case
`C_Lambda = L^\infty_Lambda`.

This packet proves the conjecture for weak-star continuous projections:

If there is a bounded projection

```text
P : L^\infty_Lambda -> C_Lambda
```

which is continuous for the weak-star topology inherited from
`L^\infty(G) = L^1(G)^*`, then `Lambda` is a Rosenthal set.

## Proof Summary

The trigonometric polynomials with spectrum in `Lambda` are weak-star dense in
`L^\infty_Lambda`. Since a weak-star continuous projection onto `C_Lambda`
fixes those polynomials, it fixes their whole weak-star closure. Hence the
projection is the identity on `L^\infty_Lambda`, and its range condition forces
`L^\infty_Lambda = C_Lambda`.

## Limitations

This does not solve the source conjecture for arbitrary bounded projections.
The missing case is precisely non-weak-star-continuous projections.

## Files

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: local copy of arXiv:0912.3133.
- `figures/conjecture_intro_page2.png`: source page where the conjecture is stated in the introduction.
- `figures/section5_question_page16.png`: source page with the complemented-subspace discussion and final question.
