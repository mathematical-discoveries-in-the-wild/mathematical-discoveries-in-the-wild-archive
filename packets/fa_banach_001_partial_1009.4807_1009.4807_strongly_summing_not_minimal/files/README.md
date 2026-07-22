# Partial solution: the strongly summing desired family is not minimal

- Source: Daniel Pellegrino and Joedson Santos, *Absolutely summing
  multilinear operators: a panorama*, arXiv:1009.4807, Quaestiones
  Mathematicae 34 (2011), 447--478.
- Extracted target: Problem 7.2 on PDF page 25 asks whether
  `(L_ss,p)_{p>=1}` is a maximal or minimal desired ideal.
- Status: `partial_result_likely_valid`.
- Scope: a complete negative answer to the **minimality** half of Problem 7.2;
  the maximality half remains open.

## Result

The packet constructs a proper desired subfamily of the strongly summing
family. For each `p>=1`, let `G_p` be the Banach atomic multi-ideal generated
by factorizations

```text
E_1 x ... x E_n --(B_1,...,B_n)--> (ell_1)^n --A--> ell_2 --u--> F,
```

with atomic cost

```text
||u|| pi_p(A_tilde) product_j ||B_j||,
```

where `A_tilde` is the linearization. Grothendieck's theorem makes every such
central kernel admissible. Define

```text
M_p = L_d,p + G_p
```

with the quotient sum norm. Then `(M_p)_{p>=1}` is a desired family and the
inclusion `M_p -> L_ss,p` has norm at most one.

Strictness is witnessed simultaneously for every `p` by

```text
Delta(x,y,z) = sum_i x_i y_i z_i  on (ell_2)^3.
```

Every scalar form is strongly `p`-summing. But every member of `M_p` has
`T(e_i,e_i,e_i)->0`: Pitt's theorem gives this for the atomic hull, while an
exact weak-`p` norm calculation gives it for dominated trilinear forms.
Since `Delta(e_i,e_i,e_i)=1`, `Delta` is outside every `M_p`.

## Evidence and verification

- `source_paper.pdf` is the arXiv source PDF.
- `figures/open_problem_crop.png` is a real rendering of PDF page 25 showing
  Problem 7.2 and its context.
- `code/make_open_problem_crop.py` regenerates the crop.
- `main.tex` contains the complete atomic-quotient, ideal-stability,
  inclusion, Grothendieck, and separation arguments.
- `solution_packet.pdf` is the rendered packet and was visually inspected
  page by page.
- No numerical experiment is used as proof.

## Novelty check

The run's cheap registry/solution indexes were searched for arXiv:1009.4807
and the terms around strongly summing, strongly multiple summing, desired
families, and minimality; no duplicate result was found.

A bounded web/literature search on 2026-07-22 used the exact title and phrases
`"strongly p-summing" "minimal"`, `"desired family"`, `Problem 7.2`, and
the notation variants `L_ss,p` and `L_sm,p`. It also inspected later work on
strongly multiple inclusion theorems, factorable strongly summing operators,
and multilinear summability associated to tensor norms. Those sources provide
related structures and partial inclusion results, but the search did not find
an explicit answer to this minimality question or the atomic construction in
this packet. This is a bounded novelty check, not a claim of publication
priority.

## Human review focus

The most useful expert checks are:

1. the Banach atomic-hull realization as an `ell_1` quotient and its csm/cud
   stability;
2. the norm-one inclusions needed by the source's definition of minimality;
3. the diagonal-null argument after atomic completion; and
4. the exact weak-`p` norm calculation for finite canonical basis blocks in
   `ell_2`.
