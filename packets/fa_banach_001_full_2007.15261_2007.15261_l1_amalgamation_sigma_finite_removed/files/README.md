# Removing the Sigma-Finite Hypothesis in L1 Amalgamation

Status: `full_solution_likely_valid` for the specific question after Lemma 4.2
of arXiv:2007.15261.

Source paper: Antonio Aviles and Pedro Tradacete, "Amalgamation and injectivity
in Banach lattices", arXiv:2007.15261.

## Source Question

After Lemma 4.2, the authors write that they do not know whether the technical
assumption that the common measure `nu_0` is sigma-finite can be removed.

Lemma 4.2 states that if `nu_0` is sigma-finite and

```text
u_i : L_1(nu_0) -> L_1(nu_i),  i=1,2,
```

are lattice isometric embeddings, then the two embeddings can be amalgamated
inside another `L_1` space.

## Result

The sigma-finiteness assumption on `nu_0` can be removed.

The proof decomposes `L_1(nu_0)` by Maharam's theorem into an `ell_1`-sum of
sigma-finite `L_1` bands. On each sigma-finite component, apply the source
Lemma 4.2. The images of distinct components generate disjoint principal bands
in the two codomain `L_1` spaces, so the componentwise amalgams can be summed
with the residual codomain bands. The resulting `ell_1`-sum is again an `L_1`
space and gives the desired global amalgam.

## Files

- `source_paper.pdf`: local copy of arXiv:2007.15261.
- `figures/maharam_decomposition_page11.png`: source page with the Maharam
  decomposition used in the proof.
- `figures/l1_amalgamation_lemma_page13.png`: source page with Lemma 4.2.
- `figures/sigma_finite_question_page14.png`: source page containing the
  sigma-finiteness question.
- `code/make_crops.py`: reproducible crop-generation script.
- `main.tex`: source for the solution packet.
- `solution_packet.pdf`: rendered packet.

## Human Review Recommendation

Review as a full solution to the narrow sigma-finiteness-removal question after
Lemma 4.2. It does not address the separate later question about whether every
separably `BL`-injective Banach lattice is isomorphic to a 1-separably
`BL`-injective one.
