# Verification report

Verdict: `likely valid full counterexample`

## Hypothesis audit

1. **Ambient space and domain.** `X=C`, `B={|z|<1}`, and `D=B`. Thus `D` is
   balanced and dense in `B`.
2. **Continuity and weak closedness.** The angle function `phi` is continuous,
   so `h(z)=(1-2 exp(i phi(|z|)))z` is continuous. In finite dimension weak
   and norm convergence agree; the graph is weakly closed.
3. **0-dissipativity.** For the unique support functional at `z`,
   `<h(z),z*>=(1-2 exp(i phi(|z|)))|z|^2`. Since
   `0<=phi<=pi/3`, its real part is nonpositive. The source inequality holds
   with `varsigma=0`.
4. **Known Abel average.** `T_1=I-h` satisfies
   `T_1(z)=2 exp(i phi(|z|))z`. Its output modulus is `2|z|`, so it is
   globally injective. For every `w in B`, the unique preimage has modulus
   `|w|/2<1/2<a`, where `phi=0`; hence `Phi_1(w)=w/2`.
5. **Holomorphy and self-map property.** `w -> w/2` is holomorphic and maps
   `B` into `B`.

## Failure audit at alpha=1/2

Let `a=sqrt(7)/5`, `b=3/5`, and choose `psi` by
`exp(i psi)=(2+i sqrt(3))/sqrt(7)`. Put
`z_1=a` and `z_2=b exp(-i psi)`. Then `phi(|z_1|)=0` and
`phi(|z_2|)=pi/3`. Since

`I-(1/2)h = (1/2 + exp(i phi(|z|))) I`,

exact calculation gives both images equal to `3sqrt(7)/10`. This target lies
in `B` because its squared modulus is `63/100<1`, while `z_1` and `z_2` are
distinct because their moduli differ. Hence the inverse at `alpha=1/2` is
not a function on `B`.

## Artifact audit

- The source crop contains the complete printed open question.
- The LaTeX packet was compiled without warnings, rendered page-by-page, and
  visually checked for clipping, overlap, malformed formulas, and unreadable
  text.
- `code/check_counterexample.py` numerically checks the exact collision and
  samples the dissipativity inequality. It is a sanity check only.

## Recommended independent focus

An independent reviewer should compare the definition of weak closedness and
the Abel-average inverse in the source with the packet's Steps 2 and 4. The
construction actually makes `I-h` globally injective, so it is valid under
the strongest natural reading of the inverse notation.

