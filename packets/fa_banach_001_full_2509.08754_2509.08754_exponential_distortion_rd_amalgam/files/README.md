# Rapid decay survives exponential distortion

Status: `candidate_full_likely_valid`

Source: Srivatsav Kunnawalkam Elayavalli, Gregory Patchell and Lizzy
Teryoshin, *Some remarks on decay in countable groups and amalgamated free
products*, arXiv:2509.08754.

## Result

The source asks for specific or systematic amalgamated free products in which
RD or SD survives despite high distortion. This packet gives an explicit
nondegenerate example with RD and exponential distortion.

Let `A` be the direct sum of countably many copies of `C_2`, with basis
`e_0,e_1,...`. Define weighted lengths

```text
ell_0(sum_{n in S} e_n) = sum_{n in S} 2^n,
ell_1(sum_{n in S} e_n) = sum_{n in S} 2^(2^n).
```

Take

```text
G = A x C_2,  L_G(a,u) = ell_1(a) + delta_2(u),
H = A x C_3,  L_H(a,v) = ell_0(a) + delta_3(v),
```

and amalgamate the central copies of `A`. Both embeddings are proper, and

```text
Gamma = G *_A H = A x (C_2 * C_3).
```

The universal length from the source has the exact formula

```text
L^U(a,q) = ell_0(a) + |q|.
```

Binary expansion gives `|B_ell_0(R)|=R+1`. Thus `(A,ell_0)` has RD, while
`C_2*C_3` has RD because it is a free product of finite groups. The source's
direct-product permanence lemma therefore proves that `(Gamma,L^U)` has RD.

For every integer `r>=1`, the element `a_r` whose support is the binary
expansion of `r` satisfies

```text
L^U(a_r)=r,                 L_G(a_r)>2^(r/2).
```

Conversely `L_G(a)<=2^(r+1)` whenever `L^U(a)<=r`. Hence the distortion
function of `(L^U|_G,L_G)` is genuinely exponential, and in particular the
polynomial-distortion hypothesis of the source's RD theorem fails.

## Scope

- This answers the final high-distortion amalgam question in the source's
  setting of countable groups equipped with arbitrary length functions.
- It does not address the harder neighboring questions about finitely
  generated or finitely presented groups with their word lengths.
- The example is deliberately transparent and length-engineered, but it is
  nondegenerate: `A` is proper in both vertex groups.

See `main.tex` and `solution_packet.pdf` for the proof and `verification.md`
for the adversarial audit.

Cheap run indexes and a bounded primary arXiv search found no later resolution
or occurrence of this weighted Boolean construction. This is not an exhaustive
novelty certification.

Human review recommendation: **send to a geometric group theorist familiar
with RD**. The main review question is whether the authors intended to exclude
engineered non-word length functions in their final, broadly phrased question.
