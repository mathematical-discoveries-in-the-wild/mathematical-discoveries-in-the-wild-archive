# Nilpotent right perturbations give hypercyclic generalized derivations

status: likely valid full positive answer to Section 6 Question 1

source: arXiv:1605.07409, Clifford Gilmore, "Dynamics of Generalised Derivations and Elementary Operators"

packet path: `runs/fa_banach_001/solutions/partial/1605.07409_nilpotent_right_perturbation_derivations/`

## Result

This packet gives a positive answer to Question 1 in Section 6 of the source paper, which asks whether reasonable sufficient conditions exist on `(A,B)` inducing hypercyclic `tau_{A,B}` on separable Banach ideals. Let `A in L(X)` have a right inverse `F` with `AF=I`, spectral radius `r(F)<1`, and a dense subspace `X_0` such that every vector of `X_0` is eventually killed by the powers of `A`. Then, for every separable admissible Banach ideal `J subset L(X)` and every nonzero nilpotent `N in L(X)`, the generalized derivation

```text
tau_{A,N}(S) = A S - S N
```

satisfies the Hypercyclicity Criterion on `J`, hence is hypercyclic.

In particular, on `X = ell_2`, let `W_lambda` be `lambda` times the backward shift for any `lambda > 1`, and let `N` be any nonzero nilpotent operator on `X`. Then, for every separable admissible Banach ideal `J subset L(X)`,

```text
tau_{W_lambda,N}(S) = W_lambda S - S N
```

satisfies the Hypercyclicity Criterion on `J`, hence is hypercyclic.

This gives examples where both members of the pair `(A,B)` are nontrivial and not the identity/scalar cases emphasized in the source paper.

## Scope

The source question is existential rather than classificatory, so this theorem is recorded as a full positive answer to that question. It is not a characterization of all hypercyclic generalized derivations, and it does not settle the paper's second final question about contrasting behavior on different ideals.

## Verification

The proof is self-contained. The key points are:

- `A` has a right inverse `F` whose powers decay exponentially up to constants because `r(F)<1`.
- `R_N` is nilpotent and commutes with `L_A` and `L_F`.
- The finite nilpotent polynomial in `(L_A-R_N)^n L_F^n` has an inverse with only polynomial growth in `n`, while `L_F^n` decays exponentially.
- On the dense finite-rank subspace with ranges in `X_0`, the powers of the derivation are eventually zero.

## Novelty check

Before promotion to `full/`, the run indexes and local parsed source corpus were searched for `1605.07409`, generalized/generalised derivations, elementary operators, nilpotent right perturbations, `L_A - R_N`, and Hypercyclicity Criterion variants. Targeted web/arXiv searches on 2026-06-21 for `"nilpotent right perturbation" "generalized derivation" hypercyclic`, `"generalised derivation" "nilpotent" "Hypercyclicity Criterion"`, `"L_A - R_N" hypercyclic nilpotent`, and the exact source-question phrase found the source paper but no later matching criterion.

## Files

- `main.tex`: full packet source
- `solution_packet.pdf`: rendered proof packet
- `source_paper.pdf`: local copy of the arXiv source paper
- `figures/open_problem_crop.png`: crop of the source open question
- `history/packets/partial_packet_ell2_nilpotent_right_perturbation_2026_06_21/`: nested historical partial packet absorbed into this full result
