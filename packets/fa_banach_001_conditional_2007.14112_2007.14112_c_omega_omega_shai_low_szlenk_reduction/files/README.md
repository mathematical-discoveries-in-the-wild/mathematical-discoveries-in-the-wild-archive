# Conditional packet: the `C[0, omega^omega]` SHAI subcase from a low-Szlenk ideal equality

## Source

- Paper: Bence Horvath and Tomasz Kania, *Surjective homomorphisms from algebras of operators on long sequence spaces are automatically injective*
- arXiv: `2007.14112`
- Source question: Question 3.26 asks whether `C(K)` has SHAI for `K=[0,1]`, `K=[0, omega^omega]`, `K=beta N \ N`, and `K=beta Gamma` for uncountable discrete `Gamma`.
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `conditional`
- Scope: conditional solution of the `K=[0, omega^omega]` subcase only.
- Packet claim: if, for `X=C[0, omega^omega]`, the closed ideal of operators approximately factoring through `c0` coincides with the ideal of operators of Szlenk index at most `omega`, then `X` has SHAI.

## Conditional Dependency

The packet does not prove the operator-ideal equality

```text
overline{G}_{c0}(C[0, omega^omega]) = SZ_1(C[0, omega^omega]).
```

Equivalently, it assumes that every operator on `C[0, omega^omega]` with Szlenk index at most `omega` is a norm limit of operators factoring through `c0`.

## Proof Intuition

The source already proves that any non-injective SHAI quotient of `B(C(K))` kills `overline{G}_{c0}(C(K))`. Under the low-Szlenk equality, this ideal is maximal for `C[0, omega^omega]`: outside it, Bourgain's Szlenk theorem and Pelczynski's complementation theorem force the identity on `C[0, omega^omega]` to factor through the operator. Then a non-injective quotient would make `B(Y)` a simple quotient; this contradicts finite-rank ideals when `Y` is infinite-dimensional, while the square property of `C[0, omega^omega]` rules out finite-dimensional quotients.

## Files

- `main.tex`: LaTeX source for the conditional packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original open-problem source.
- `supporting_paper_1811.06865.pdf`: Horvath SHAI criterion and square/no finite-dimensional quotient context.
- `supporting_paper_1304.4951.pdf`: Kania-Laustsen formulation of Bourgain and Pelczynski theorems.
- `supporting_paper_1003.5710.pdf`: Brooker Szlenk-operator ideal reference.
- `figures/open_problem_page20_question326.png`: crop of the source open question.
- `code/crop_evidence.py`: reproduces the source-question crop.
- `tmp/`: LaTeX build outputs.

## Verification Notes

Local indexes were checked for `2007.14112`, the paper title, `SHAI`, `C(K)`, `C[0,1]`, `C[0, omega^omega]`, `beta N \ N`, and related phrases. Web/literature searches found the source, Horvath's 2018 SHAI paper, Johnson--Phillips--Schechtman's later `L^p` SHAI paper, Kania--Laustsen's ordinal-operator paper, Brooker's Szlenk-ideal paper, and Alspach's `C(omega^alpha)` preservation paper, but no explicit answer to Question 3.26.

The main reviewer focus is the conditional dependency: prove or disprove the low-Szlenk equality for `C[0, omega^omega]`. A counterexample would likely be an operator of Szlenk index at most `omega` on `C[0, omega^omega]` that is not approximately factorable through `c0`.
