# Verification Report

Status: `candidate_counterexample_likely_valid`.

## Analytic audit

The following points were checked directly.

1. For `c=3 sqrt(3)/2`, the maximum of `x y^2` under
   `x^2+y^2=r^2` is `2r^3/(3 sqrt(3))`. Consequently
   `Re<-G(z),z> >= r^2-r^3>0` in the open unit ball, so `-G` is in
   the defining class `M`.
2. Direct multiplication gives `dPhi(z) G(z)=-Phi(z)`. Hence
   `f_t=e^t Phi` satisfies the Loewner PDE. Its normalized family is
   constant and every `f_t` is univalent, so it is a normal Loewner chain.
3. The degree-two coefficient equation and harmonic decoupling give the sharp
   bound `|b^1_{0,2}| <= c` on `S^0`. Since `Phi` attains the real bound,
   it is a support point.
4. On `A={zeta in boundary B^2: |zeta_2|<=1/4}`, the boundary limsup is
   at most `-1+c/16=-1+3sqrt(3)/32<-3/4`. The source hypothesis
   therefore holds for every time with `a=3/4`.
5. The conclusion fails because `f_0=Phi` belongs to `Supp(S^0)`.

## Deterministic check

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1603.01532_boundary_cap_dissipativity_support_point/code/verify_counterexample.py \
  --figure runs/fa_banach_001/solutions/counterexamples/1603.01532_boundary_cap_dissipativity_support_point/figures/boundary_dissipativity.png
```

The script samples the one-variable boundary optimization at 200,001 points,
checks the PDE identity at complex test points, numerically integrates the
degree-two coefficient kernel, and generates the boundary-cap figure. Its
output is:

```text
c=2.598076211353316
max_sampled_xy2=0.384900179451093
exact_max_xy2=0.384900179459751
c_times_exact_max=1.000000000000000
sampled_cap_sup=-0.842776470332046
conservative_cap_bound=-0.837620236790418
max_pde_residual=4.441e-16
coefficient_kernel_mass=1.000000000075
PASS
```

These checks are regression tests; the packet proof is analytic.

## Packet build and visual QA

`main.tex` was compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error`. The final `solution_packet.pdf` has four letter-sized pages.
The final log contains no LaTeX warnings, overfull or underfull boxes, or
undefined references. All four pages were rasterized at 150 DPI and inspected
at full resolution. The source-question crop, formulas, theorem, proof ending,
cap plot, review note, and bibliography are legible, with no clipping,
overlap, broken glyphs, or malformed page transitions.

## Novelty bounds

The run indexes were searched by arXiv id, exact title, Question 3.10 terms,
`exponentially squeezing`, `boundary`, and `support point`. A bounded web/arXiv
search used the exact question language, author names, and the extremal
constant `3 sqrt(3)/2`. It found the source and related Loewner-chain work but
no later paper explicitly resolving Question 3.10 or recording this boundary
cap counterexample. This is not an exhaustive novelty claim.

## Human review recommendation

The main review point is semantic: confirm that the printed phrase "for some
`A` contained in the boundary" has its literal meaning and carries no implicit
largeness condition. Under that reading, the cap has positive surface measure
and nonempty relative interior, so the counterexample is stronger than a
singleton or empty-set objection. A strengthened whole-boundary version is
outside the scope of this result.
