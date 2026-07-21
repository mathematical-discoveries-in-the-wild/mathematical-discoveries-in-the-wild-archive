# Lorentz endpoint estimate for elliptic canceling operators: answered positively

Status: `literature_already_answered`

Original source: Daniel Spector, *New Directions in Harmonic Analysis on
L^1*, arXiv:1903.09292, Open Problem 7.3 on page 19.

Supporting source: Dmitriy Stolyarov, *Hardy--Littlewood--Sobolev inequality
for p=1*, arXiv:2010.05297v3, abstract, Example 1.4, Theorem 1.1, and
Corollary 1.7 on pages 1--4.

## Identification

Spector asks whether every first-order homogeneous constant-coefficient
operator `A(D)` that is elliptic and canceling satisfies

```text
||u||_{L^{d/(d-1),1}} <= C ||A(D)u||_1
```

for all compactly supported smooth `V`-valued `u` in dimension `d >= 3`.
The source identifies this with Van Schaftingen's Open Problem 8.3.

Stolyarov proves the stronger endpoint Hardy--Littlewood--Sobolev theorem for
all translation- and dilation-invariant Fourier-restriction spaces satisfying
the cancellation condition. For an elliptic operator of order `m`, his
abstract states the particular consequence

```text
||nabla^{m-1} u||_{L^{d/(d-1),1}} <= C ||A(D)u||_1.
```

Taking `m=1` gives Spector's requested estimate exactly. Stolyarov also says
immediately after Corollary 1.7 that the result solves Van Schaftingen's Open
Problem 8.3, the same problem number cited by Spector.

## Scope

This packet records a complete positive literature answer to Open Problem 7.3.
It does not claim that the methodological Open Problem 7.2 (finding a proof
without coarea) or the measure trace Open Problem 7.5 is settled.

Stolyarov's Corollary 1.7 also gives a short route to Spector's potential
Open Problem 7.4: apply it to `g=A(D)I_1 f`, then recover `I_alpha f` from
`I_alpha g` with the smooth degree-zero left inverse of
`|xi|^{-1}A(xi)`. This is a derived implication rather than the exact
author-identified match used for the packet status.

## Evidence

The exact source question is on page 19 of `source_paper.pdf`. The supporting
abstract is on page 1; Example 1.4, Theorem 1.1, Corollary 1.7, and the explicit
Open Problem 8.3 resolution statement are on pages 2--4 of
`supporting_paper_2010.05297.pdf`.

Human review recommendation: `quick theorem-match verification only`.
