# arXiv:2305.00859 -- norm attainment does not force boundary equicontinuity

Status: `counterexample_likely_valid_scoped`

Agent: `agent_super_00`

Updated: 2026-06-30T23:50:34Z

## Source Target

Source paper: Neeru Bala, Jaydeb Sarkar, Aryaman Sensarma, *A Bishop-Phelps-Bollobas theorem for disc algebra*, arXiv:2305.00859.

After Corollary 2.2, the paper says that the authors do not know how to remove the equicontinuity assumption from the preceding BPB theorem. It also says that equicontinuity is probably not necessary for norm attainment, but that the paper has no evidence for this claim.

## Result

The side question about norm attainment has a simple negative answer. The identity operator

```text
I : A(D) -> A(D)
```

is norm attaining, since `I(1)=1`, but the family `I(S_{A(D)})=S_{A(D)}` is not equicontinuous at any boundary point of the unit disc. For a boundary point `zeta`, the functions

```text
f_n(z) = conjugate(zeta)^n z^n
```

belong to the unit sphere of `A(D)`, satisfy `f_n(zeta)=1`, and fail equicontinuity at `zeta` by taking points `zeta exp(i pi/n)`.

Thus the equicontinuity hypothesis in the source theorem is not necessary for an operator into the disc algebra to attain its norm.

## Scope

This packet does **not** remove the equicontinuity hypothesis from the Bishop-Phelps-Bollobas theorem itself. It answers only the source paper's adjacent norm-attainment necessity comment.

## Files

- `main.tex` gives the formal statement and proof.
- `solution_packet.pdf` is the rendered review packet.
- `source_paper.pdf` is the source arXiv paper.
- `figures/open_problem_crop.png` shows the source sentence on PDF page 7.
- `code/render_open_problem_crop.py` regenerates the crop.

## Novelty Check

Cheap run-index search found no prior packet for arXiv:2305.00859. Adjacent BPB packets concern different BPB questions. Exact web searches for the paper title, `disc algebra`, `equicontinuity`, `norm attaining`, and `Bishop-Phelps-Bollobas` did not surface a later settlement or this exact observation; the claim is nevertheless elementary and should be reviewed mainly for scope, not technical difficulty.
