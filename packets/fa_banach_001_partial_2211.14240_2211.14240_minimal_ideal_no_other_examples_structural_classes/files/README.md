# Isometric no-other-examples theorem in two structural classes

Status: `partial_solution_likely_valid`

Source: Nahuel Albarracin and Pablo Turco, *On the Lipschitz operator ideal
Lip_0 o A o Lip_0*, arXiv:2211.14240, page 11 after Proposition 2.16.

## Result

Let `A` be a minimal Banach operator ideal and set `B=A^max`. Assume that
`B` is either surjective, or both symmetric and injective (with the standard
isometric meanings). Then, isometrically,

```text
(Lip_0 o A o Lip_0)^min is of composition type
if and only if A has the approximable class OF.
```

This rules out both a new operator class and a nonstandard ideal norm in those
two broad structural classes. It does not answer the unrestricted question
for nonsurjective maximal hulls lacking symmetry or injectivity.

The quantitative refinement first proves

```text
||id_{F(E)}||_B = ||id_E||_A
```

for every finite-dimensional `E`. At `E=R` this gives the identity of
`F(R)=L_1(R)` with `B`-norm one. Norm-one quotient maps from `L_1(R)` onto
separable spaces, followed by maximality, upgrade source Proposition 2.17 to
the isometric equality `B^sur=L`. Surjectivity now gives `B=L` isometrically.
In the symmetric-injective case, adjoints of the canonical `l_1` quotient
maps yield the canonical isometric embeddings into `l_infinity`; injectivity
again gives `B=L` isometrically.

Files:

- `solution_packet.pdf`: theorem, proof, verification, and limitations.
- `source_paper.pdf`: the original paper.
- `figures/open_problem_crop.png`: exact source passage and Proposition 2.17.

Human review recommendation: verify the norm identity for the Dirac map and
the isometric passage from separable quotient spaces to the maximal
surjective hull.
