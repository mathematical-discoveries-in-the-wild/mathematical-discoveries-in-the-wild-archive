# No-Smallness Similarity for Finite-Dimensional Admissible Modules

Source paper: Anatoly G. Baskakov, Ilya A. Krishtal, and Natalia B. Uskova,
"Method of similar operators in harmonious Banach spaces",
arXiv:2404.01227.

Status: candidate partial result, likely valid. The packet proves the source
conjecture in full for finite-dimensional `A`-admissible modules. It does not
settle the infinite-dimensional case.

## Result

Let `(M,0,Gamma)` be an admissible triple for a closed operator `A` on a
complex Banach space. Assume that `M` is finite-dimensional and
`Gamma(M) subset M`, as it is for the harmonious transforms in equation
(5.1) of the source. Then for every `B in M`, the operator `A-B` is similar
to `A`, with no norm restriction on `B`.

The intertwiner is explicit. If `M^q=0`, let

```text
L_B(X) = B Gamma X,
X_* = B + L_B(B) + ... + L_B^(q-1)(B),
U = I + Gamma X_*.
```

Then the sum is finite, `U` has a finite polynomial inverse, preserves
`D(A)` in both directions, and `(A-B)U=UA`.

## Proof Idea

Finite dimensionality turns the injective commutator solver `Gamma` into a
bijection. Admissibility then makes `M` an associative algebra and identifies
`Gamma^{-1}` with the nonsingular derivation `[A,cdot]`. A radical-quotient
argument forces every finite-dimensional algebra with such a derivation to
be nilpotent. Nilpotence terminates the paper's formal Friedrichs iteration,
so neither contraction estimates nor hypercausality are needed.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2404.01227.
- `figures/open_problem_crop.png`: Remark 5.16 on PDF page 23.
- `tmp/`: LaTeX build intermediates and rendered QA pages.

## Human Review Recommendation

Review as a strong solved subcase. The most important checks are:

1. `Gamma(M) subset M` is part of the harmonious setting (equation (5.1));
2. finite dimensionality makes `Gamma` onto after the commutator identity
   makes it one-to-one;
3. the Jacobson-radical argument really forces `M` to be nilpotent;
4. `Gamma` preserves every algebra power `M^k`, making `L_B` nilpotent;
5. both the intertwiner and its inverse preserve `D(A)`.

The unrestricted infinite-dimensional conjecture remains open.
