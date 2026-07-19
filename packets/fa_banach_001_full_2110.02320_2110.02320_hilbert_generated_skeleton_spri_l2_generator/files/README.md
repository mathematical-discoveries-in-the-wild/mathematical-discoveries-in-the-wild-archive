# Hilbert-generated spaces via invariant `ell_2` generators

Status: full candidate, likely valid.

Source paper: C. Correa, M. Cuth, and J. Somaglia, "Characterizations of weakly K-analytic and Vasak spaces using projectional skeletons and separable PRI", arXiv:2110.02320.

Open problem addressed: Problem 34 on page 28 asks to characterize Hilbert-generated spaces using projectional skeletons and SPRI.

Result: A nonseparable Banach space `X` is Hilbert generated if and only if it admits a projectional skeleton, equivalently a SPRI, that leaves invariant an `ell_2`-summable linearly dense generating set `A`: each projection sends every `a in A` to either `0` or `a`, and there is `C` such that

```text
sup { sum_{a in F} |x*(a)|^2 : F finite subset A } <= C^2 ||x*||^2
```

for every `x* in X*`.

Proof mechanism: a Hilbert generator `T:H->X` supplies `A={T e_i}` from an orthonormal basis of `H`; the adjoint estimate gives the displayed `ell_2` bound, hence `A` countably supports `X*`. The source paper's Corollary 21 and Theorem 25 then produce a projectional skeleton and SPRI invariant on `A`. Conversely, the displayed estimate makes the operator `ell_2(A)->X`, `e_a |-> a`, bounded with dense range.

Novelty check: cheap run indexes were searched for `2110.02320`, `Hilbert generated`, `projectional skeleton`, `SPRI`, `Markushevich`, and related terms. Relevant hits concerned older projectional-skeleton status packets and Hilbert-generated examples, but no exact packet for Problem 34 or this invariant `ell_2`-generator characterization. A bounded web search for the exact source problem and Hilbert-generated skeleton/SPRI phrases found no exact-match resolution. This is a minimal formal characterization rather than a claim that the broader program of finding a more intrinsic shrinkingness-style condition is exhausted.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2110.02320.
- `figures/open_problem_crop.png`: crop of Problem 34 in the source PDF.
