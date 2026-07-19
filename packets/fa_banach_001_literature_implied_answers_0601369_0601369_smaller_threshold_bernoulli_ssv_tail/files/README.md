# Smaller-threshold Bernoulli smallest-singular-value tail

Status: `literature_implied_answer (partial subcase)`

Run: `fa_banach_001`  
Source: arXiv:math/0601369, Artstein-Avidan--Friedland--Milman--Sodin,
"Polynomial bounds for large Bernoulli sections of ell_1^N"  
Supporting theorem: arXiv:2408.14389, Dabagia--Fernandez, "The smallest
singular value of inhomogenous random rectangular matrices"  
Processed: 2026-07-03 by `agent_lane_04` in lane 1

## Scope

The 2006 paper asks whether the probability

`P{lambda_min(n^{-1}XX^T) <= delta^2/8}`

for a `(1-delta)n x n` Bernoulli sign matrix is as small as
`exp(-n delta^C/C)`.

A later rectangular smallest-singular-value theorem implies the same
exponential-in-codimension tail for the smaller-threshold event

`P{lambda_min(n^{-1}XX^T) <= c0 delta^2}`.

Here `c0>0` is a universal constant coming from the supporting theorem. This
does **not** settle the exact `delta^2/8` threshold asked in the source.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: original 2006 arXiv paper.
- `supporting_paper_2408.14389.pdf`: supporting 2024/2026 arXiv paper.

## Identification

Apply the supporting theorem to `A=X^T`, an `n x p` Bernoulli matrix with
`p=(1-delta)n`. It gives

`P{s_p(A) <= eps (sqrt(n+1)-sqrt(p))} <= (C eps)^{n-p+1}+e^{-cn}`.

Choosing fixed `eps` with `C eps < 1` and using
`sqrt(n)-sqrt((1-delta)n) >= delta sqrt(n)/2`, this becomes

`P{lambda_min(n^{-1}XX^T) <= c0 delta^2} <= exp(-c1 delta n)+e^{-cn}`.

This is an agent-identified implication, not a supporting-paper claim that it
answers arXiv:math/0601369.

