# Algebraic-coefficient uniform IDS approximation

Status: **candidate partial result; likely valid; human review requested**

Source: Felix Pogorzelski, *Convergence theorems for graph sequences*,
arXiv:1304.0945, Section 6.2, page 12.

## Result

Let `(G_n)` be any weakly convergent finite graph sequence of uniformly
bounded degree. Let `(H_n)` be a fixed-range, pattern-invariant,
selfadjoint operator sequence in the sense of the source paper. If every
value of every local kernel rule is a real algebraic number, then the
normalized spectral measures `nu_n` satisfy

```text
nu_n({lambda}) -> nu({lambda})  for every real lambda,
```

where `nu` is their weak limit. Consequently the spectral distribution
functions converge uniformly.

This replaces the integer-coefficient hypothesis in source Theorem 6.10 by
the strictly larger class of all real algebraic coefficients. It is only a
partial answer to the source question for arbitrary coefficients:
transcendental coefficient sets are not covered.

## Proof mechanism

After one global scaling, all kernel values lie in the ring of integers of a
finite Galois number field `K`. For each finite matrix, form the square of the
product of all nonzero pairwise eigenvalue differences. This generalized
discriminant is a nonzero algebraic integer in `K`. Its field norm is a
nonzero rational integer. All conjugate matrices have a uniform row-sum
bound, so the other Galois conjugates of the discriminant have at most
exponential-in-`|V(G_n)|^2` size. The norm therefore gives the lower bound
needed in the Abért--Thom--Virág anti-clustering argument.

The other arithmetic input also persists: an eigenvalue carrying normalized
multiplicity at least `1/k` has degree at most `k` over `K`; all of its
absolute conjugates are uniformly bounded. There are therefore only finitely
many such eigenvalues. Combining the two facts gives a uniform
punctured-neighborhood estimate at every real point, which prevents mass from
traveling into an atom under weak convergence.

## Novelty status

The exact all-weakly-convergent-graph-sequences formulation was not located in
a bounded search. Andreas Thom's arXiv:math/0701294 explicitly records the
algebraic-coefficient analogue for sofic group approximations, so the number
field mechanism itself is known. The 2026 preprint arXiv:2603.01610 proves a
rational-valued result for random operators over sofic groups and handles
arbitrary complex coefficients only through adapted approximants with varying
rational coefficients. Thus originality of the graph-sequence extension is
**provisional**, not established.

Searches inspected the local run indexes and used the phrases `algebraic
coefficients Lück approximation spectral measures graph sequences`, `number
field Lück approximation`, and `arbitrary coefficients graph sequences
spectral distribution`, together with arXiv:1304.0945,
arXiv:math/0701294, the Abért--Thom--Virág preprint cited by the source, and
arXiv:2603.01610.

## Verification report

Verdict: **likely valid**.

The proof was checked at the following points:

1. clearing denominators is global because the local rule has only finitely
   many values;
2. high normalized multiplicity bounds degree over the coefficient field;
3. the squared nonzero-pair discriminant lies in the coefficient field's ring
   of integers even when eigenvalues repeat;
4. the field norm and uniform bounds on every conjugate matrix give the
   claimed quantitative anti-clustering estimate;
5. Portmanteau inequalities convert that estimate into convergence of every
   atom.

No computational experiment is used as evidence. The recommended human review
focus is the generalized-discriminant argument in Lemma 2 of the packet,
especially the assertion that the squared product is in `O_K`.

## Files

- `solution_packet.pdf`: review packet
- `main.tex`: complete proof source
- `source_paper.pdf`: original source paper
- `figures/open_problem_crop.png`: source page 12

