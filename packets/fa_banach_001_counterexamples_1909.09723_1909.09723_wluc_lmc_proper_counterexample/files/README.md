# Counterexample: `WLUC(S)` Can Be Proper in `LMC(S)`

Status: counterexample likely valid.

Source: Andrzej Wisnicki, *Amenable semigroups and nonexpansive dynamical
systems*, arXiv:1909.09723v1, submitted 2019-09-20.

## Target

After Theorem 3.5, the source says:

```text
it seems to be an open problem whether WLUC(S) is a proper subspace of LMC(S).
```

Here `WLUC(S)` is the space of bounded continuous functions whose left
translation orbit is weakly continuous, while `LMC(S)` only asks for continuity
against multiplicative means on `C(S)`.

## Answer

Yes. The packet constructs a Hausdorff topological rectangular band
`S = A x N` and a bounded continuous function `f` such that:

- for every multiplicative mean `chi` on `C(S)`, the scalar map
  `s -> chi(L_s f)` is continuous, so `f in LMC(S)`;
- there is a bounded linear functional `Phi in C(S)^*` and a net
  `s_E -> s_infty` such that `Phi(L_{s_E} f) > 1/2` but
  `Phi(L_{s_infty} f) = 0`, so `f notin WLUC(S)`.

Thus `WLUC(S)` is a proper subspace of `LMC(S)`.

## Files

- `main.tex` - human-readable proof packet.
- `solution_packet.pdf` - compiled packet.
- `source_paper.pdf` - source arXiv paper.
- `figures/open_problem_crop.png` - source crop containing the open problem.

## Verification

No computational search is used. The verification is the formal proof in
`main.tex`: associativity and continuity of the rectangular band are explicit,
membership in `LMC(S)` is checked against an arbitrary multiplicative mean, and
failure of `WLUC(S)` is witnessed by a Hahn-Banach extension of integration
against an atomless regular probability measure on `beta N`.
