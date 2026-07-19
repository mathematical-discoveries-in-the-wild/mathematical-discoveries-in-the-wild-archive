# Threshold Families: Explicit Isometry Groups

status: candidate partial result

source_arxiv_id: 1907.06815
source_title: Isometries of combinatorial Banach spaces
source_authors: C. Brech, V. Ferenczi, A. Tcaciuc

## Target

Brech--Ferenczi--Tcaciuc ask in Section 5:

- Question 16: Given a regular family `F`, what are the permutations of the basis which induce an isometry of `X_F`?
- Question 17: For which combinatorial spaces can we explicitly describe the group of its isometries?

The packet gives a complete answer for threshold regular families

```text
F_g = {empty} union {F finite nonempty: |F| <= g(min F)}
```

where `g:N -> N` is nondecreasing and `g(n) >= 1`.

## Result

For `F_g`, the permutations inducing isometries are exactly the permutations preserving every level set of `g`. Thus

```text
Isom(X_{F_g}) = Signs^N semidirect product prod_m Sym({n : g(n)=m}),
```

with the analogous description for `X_{F_g}^*`.

This strictly packages a solved subcase of the source questions. It extends the source paper's final example from consecutive unit-increment plateaus to arbitrary nondecreasing threshold functions.

## Files

- `main.tex` - self-contained proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - source paper PDF.
- `figures/open_problem_crop.png` - crop of the source questions on page 11.

## Verification

No computational verification is needed. The proof is a direct invariant argument:
the largest size of a set in `F_g` containing `n` is exactly `g(n)`, so every family automorphism preserves `g`; conversely, preserving `g` preserves membership in `F_g`.

Local novelty check: cheap indexes and source text were searched for arXiv `1907.06815`, combinatorial-Banach/isometry keywords, and threshold-family language. No existing run packet or attempt covers this result.

## Human Review Recommendation

Review as a likely-valid partial result. The main point to check is the compactness proof for `F_g` and the converse implication that every `g`-level-preserving permutation preserves the threshold family.
