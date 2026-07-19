# Counterexample Packet: Banach-Algebra Centers Need Not Tensor Correctly

- status: candidate counterexample, finite-dimensional and directly checked
- run: `fa_banach_001`
- source arXiv id: `1809.01131`
- source paper: Ved Prakash Gupta and Ranjana Jain, *On Banach space projective tensor product of C*-algebras*
- target passage: final question after the paper proves
  `Z(A \otimes_\gamma B)=Z(A)\otimes_\gamma Z(B)` for C*-algebras

## Claim

The unrestricted Banach-algebra analogue of the C*-algebra center theorem is
false.

There are finite-dimensional Banach algebras `A` and `B` such that the natural
map

```text
Z(A) \otimes_gamma Z(B) -> Z(A \otimes_gamma B)
```

is injective but not surjective.

## Construction

Let `A=M_2(C)`. Let `B=span{e,n}` with multiplication

```text
e^2=e,       en=ne=n^2=0.
```

With the norm `||alpha e + beta n||=|alpha|+|beta|`, `B` is a
finite-dimensional Banach algebra. It is commutative, so `Z(B)=B`, while
`Z(A)=C I`.

As a vector space,

```text
A \otimes_gamma B = (A \otimes e) direct_sum (A \otimes n).
```

All products involving the `n` coordinate vanish. Therefore

```text
Z(A \otimes_gamma B) = C I \otimes e  +  A \otimes n,
```

whereas

```text
Z(A) \otimes_gamma Z(B) = C I \otimes e  +  C I \otimes n.
```

Thus `E_12 \otimes n` is central in `A \otimes_gamma B` but does not belong to
`Z(A)\otimes_gamma Z(B)`.

## Interpretation

This gives a clean negative answer to the naive unrestricted Banach-algebra
extension of the source paper's C*-algebra center theorem. The obstruction is
annihilator mass: a nonzero two-sided annihilator in one factor makes whole
noncentral slabs from the other factor central in the tensor product.

The packet does **not** settle stronger variants with both Banach algebras
unital, or with bounded approximate identities. Those restrictions remove the
annihilator mechanism and are the genuinely subtler follow-up questions.

## Files

- `main.tex`: full proof packet
- `solution_packet.pdf`: rendered proof packet
- `source_paper.pdf`: local copy of arXiv:1809.01131

## Novelty Check

The run indexes were searched for `1809.01131`, the paper title, and tensor
product center keywords. No prior packet for this center question was found.

External searches for combinations of `center`, `centre`, `projective tensor
product`, `Banach algebra`, `Z(A)`, `Z(B)`, and `two-sided annihilator` found
the source paper and adjacent C*-algebra/Arens-regularity material, but no
direct recorded answer to the final Banach-algebra question in this elementary
annihilator form.

## Human Review Recommendation

Reviewers should check that the source question is read as the unrestricted
Banach-algebra analogue of the C*-algebra equality. If the intended question is
secretly restricted to unital Banach algebras or to algebras with bounded
approximate identities, this packet should be classified as a counterexample
only to the unrestricted formulation.
