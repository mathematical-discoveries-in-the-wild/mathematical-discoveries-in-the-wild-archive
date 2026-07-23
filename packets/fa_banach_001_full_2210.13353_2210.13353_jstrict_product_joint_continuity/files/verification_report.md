# Verification report

## Verdict

`likely valid` -- candidate full affirmative solution to Questions Q1 and Q2:
the multiplier Jordan product is separately J-strict continuous and jointly
J-strict continuous on norm-bounded sets.

## Source audit

1. The source defines the J-strict seminorms by
   `rho_a(z)=||z o a||`, for `a` in the underlying JB*-algebra.
2. The source proves that J-strict bounded sets coincide with norm-bounded
   sets.
3. The source records positive contractive approximate units with
   `||U_{1-e}(a)|| -> 0` for every `a` in the algebra.
4. The two questions appear verbatim on source page 25 and are captured in
   `figures/open_questions_crop.png`.

## Proof audit

- The local-tail expansion is sign-consistent:

```text
U_{1-e}(z) = z - 2(e o z) + 2(e o z) o e - e^2 o z.
```

Hence `L_e z=z-U_{1-e}z` belongs to the original algebra and

```text
||L_e z|| <= 4 rho_e(z) + rho_{e^2}(z).
```

- The tail-product identity follows by applying
  `U_{U_c z}=U_c U_z U_c` to the unit and polarizing in `z`; it does not
  assume associativity or specialness.
- For positive `a`, the standard JB inequality and the fundamental identity
  give

```text
||a o U_c(w)||^2 <= ||a|| ||w||^2 ||U_c(a)||.
```

- The bilinearized quadratic operator satisfies
  `||U_{x,y}(t)|| <= 3||x||||y||||t||`. Therefore, on a ball of radius `C`,

```text
rho_a(U_c x o U_c y)^2
    <= 9 C^4 ||a|| ||U_c(a)||.
```

- The epsilon order is correct: choose the approximate-unit element first to
  make the tail-tail term uniformly small, then choose the net indices to
  make the local terms small.
- Positive test elements suffice by positive/negative and real/imaginary
  decompositions. The identity `rho_a(z*)=rho_{a*}(z)` makes real and
  imaginary parts preserve J-strict null convergence.
- Translating from continuity at zero to arbitrary limits uses the exact
  bilinear expansion into a joint-null term and two separate-null terms.

## Exceptional-algebra check

`code/check_albert_identities.py` implements the real Albert algebra
`H_3(O)` with exact rational arithmetic. Forty seeded random trials checked:

```text
U_{U_c x}=U_c U_x U_c
U_c x o U_c y=U_c(U_{x,y}(c^2)).
```

All trials passed. This is not the proof, but it is a useful guard against
silently invoking an identity that holds only in special Jordan algebras.

## Reproduction

From the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/check_albert_identities.py
conda run --no-capture-output -n sandbox python code/make_open_questions_crop.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

## Remaining review risk

The proof is short but appears to introduce a new localization device for
this exact question. Human review should concentrate on Lemma 3
(polarization of the fundamental identity) and on the quantifier order in the
tail-tail estimate. The literature search was bounded, so novelty confidence
is moderate.
