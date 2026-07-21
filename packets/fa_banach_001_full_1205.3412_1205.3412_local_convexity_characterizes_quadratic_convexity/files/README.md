# Local convexity characterizes quadratic convexity

Status: `candidate_full_likely_valid`

Source: Iryna Banakh, Taras Banakh, Anatolij Plichko and Anatoliy
Prykarpatsky, *On Local Convexity Of Nonlinear Mappings Between Banach
Spaces*, arXiv:1205.3412.

## Result

Problem 6.1 asks whether the following property forces a Banach space `X`
to have modulus of convexity of power type 2, or at least to be
(super)reflexive:

> Every Lipschitz-open, second-order Lipschitz self-map on an open subset of
> `X` is locally convex.

The packet gives a candidate full affirmative answer. Together with the
source paper's forward theorem, it proves the equivalence

```text
conv_2(X) > 0
  <=> every Lipschitz-open second-order Lipschitz f:U->X is locally convex.
```

Thus the stated property forces the given norm to have quadratic modulus of
convexity and consequently forces `X` to be superreflexive.

## Construction

If `conv_2(X)=0`, choose arbitrarily flat midpoint configurations
`z_n=(x_n+y_n)/2` and supporting functionals `sigma_n`. A dichotomy handles
the possibility that the supports rotate:

- either one fixed output direction is detected along arbitrarily flat
  configurations;
- or the next support can be chosen arbitrarily small on all previously
  selected output directions.

In both cases a summable symmetric bilinear map `B` is constructed with

```text
sigma_n(B(h_n,h_n)) >= beta_n ||h_n||^2,
h_n=(x_n-y_n)/2.
```

The quadratic perturbation

```text
f(x)=x+B(x,x)
```

on the unit ball is a small Lipschitz perturbation of the identity, hence is
injective and Lipschitz-open; it is also second-order Lipschitz. The positive
quadratic displacement above pushes the unique preimage of the midpoint of
`f(epsilon_n x_n)` and `f(epsilon_n y_n)` outside a slightly enlarged ball,
while both endpoints stay inside. Therefore images of arbitrarily small
centered balls are nonconvex.

## Files and review

- `main.tex`: full statement and proof.
- `solution_packet.pdf`: compiled proof packet.
- `verification.md`: adversarial audit and constant checks.
- `source_paper.pdf`: the source paper; Problem 6.1 is on its final body page.

Cheap run indexes and a bounded title/keyword search found no prior solution
of the converse. This is not an exhaustive novelty certification.

Human review recommendation: **send to a Banach-space geometer or nonlinear
analyst**. The main review point is the exhaustive supporting-functional
dichotomy; the perturbation and inverse estimates are elementary once that
selection is accepted.
