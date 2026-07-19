# Adjoint-Strictly-Singular Subcase For The Dual Problem

Status: `partial_result_likely_valid`

Source: arXiv:1309.4516, Spiros A. Argyros, Kevin Beanland, Pavlos
Motakis, *Strictly singular operators in Tsirelson like spaces*.

## Problem Context

Problem 2(iii) of the source paper asks whether
`X_{0,1}^{n*}` has the same strictly singular product property as
`X_{0,1}^n`: if

```text
S_1,...,S_{n+1}: X_{0,1}^{n*} -> X_{0,1}^{n*}
```

are strictly singular, must `S_1...S_{n+1}` be compact?

## Result

The answer is yes for the adjoint-strictly-singular subcase:

If `S_i: X_{0,1}^{n*} -> X_{0,1}^{n*}` are bounded operators whose adjoints,
identified as operators on the reflexive predual `X_{0,1}^n`, are strictly
singular, then `S_1...S_{n+1}` is compact.

Equivalently, since `X_{0,1}^n` is reflexive and every operator on the dual has
a preadjoint, Problem 2(iii) would follow if every strictly singular operator
on `X_{0,1}^{n*}` had strictly singular preadjoint on `X_{0,1}^n`.

## Proof Sketch

Write `X = X_{0,1}^n`. If each `S_i^*: X -> X` is strictly singular, the
source paper's main theorem applied to `X` gives compactness of

```text
S_{n+1}^* ... S_1^* : X -> X.
```

But this operator is `(S_1...S_{n+1})^*`. By Schauder's theorem, an operator is
compact if and only if its adjoint is compact. Hence `S_1...S_{n+1}` is
compact.

## Limitations

This is not the full answer to Problem 2(iii). Strict singularity is not
self-dual in general, so the missing question is whether this particular
Tsirelson-like space has enough structure to force

```text
S strictly singular on X*  =>  S* strictly singular on X.
```

No proof of that implication was found.

## Files

- `main.tex`: formal packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1309.4516.
- `figures/open_problem_crop.png`: full-page crop of the source problem
  statement on PDF page 43.

## Duplicate And Literature Check

Cheap run indexes were searched for `1309.4516`, `Tsirelson like`, `dual
strictly singular`, and adjoint/strictly singular keywords. No duplicate packet
or attempt was found.

External searches on June 15, 2026 found the source paper, the related
distortion paper arXiv:1408.5065, and the related asymptotic-symmetry paper
arXiv:1902.10098, but no later full answer to Problem 2(iii). General
operator-theory references confirm that strict singularity is not self-dual in
general, which is why this packet is only a subcase/reduction.

