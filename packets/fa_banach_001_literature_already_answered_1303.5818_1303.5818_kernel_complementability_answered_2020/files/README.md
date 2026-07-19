# Literature Answer: Complementability of the Two Kernels

Status: `literature_already_answered`

Source problem: Qingping Zeng and Huaijie Zhong, *Common properties of
bounded linear operators AC and BA: Spectral theory*, arXiv:1303.5818. On
PDF page 2, the introduction asks whether, for Banach spaces `X,Y` and bounded
operators

```text
A:X->Y,  B,C:Y->X,  ABA=ACA,
```

the kernels of `AC-I_Y` and `BA-I_X` are complemented simultaneously.

Supporting answer: Qingping Zeng, Kai Yan, and Shifang Zhang, *New results on
common properties of the products AC and BA, II*, **Mathematische
Nachrichten** 293 (2020), 1629--1635, DOI
[`10.1002/mana.201900038`](https://doi.org/10.1002/mana.201900038). Item (ii)
of the published abstract explicitly states that under `ABA=ACA`, `I-AC` and
`I-BA` share complementability of kernels and ranges. This contains the source
question verbatim up to the harmless sign change of each operator.

## Identification and sanity check

Write

```text
M = ker(BA-I_X),   N = ker(AC-I_Y),   D = BAC:Y->X.
```

The hypothesis gives bounded inverse restrictions

```text
A|_M : M -> N,             D|_N : N -> M,
D A|_M = I_M,              A D|_N = I_N.
```

Indeed, `A(M) subset N` and `D(N) subset M`; moreover
`BACA=BABA` and `ABAC=ACAC` on the relevant fixed-point spaces. Thus if
`P:X->M` is a bounded projection, then `A P D:Y->N` is a bounded projection.
Conversely, if `Q:Y->N` is a bounded projection, then `D Q A:X->M` is a
bounded projection. This independently checks the exact affirmative relation
identified in the 2020 paper; it is not claimed as a novel result of this run.

## Search bounds and files

The run indexes and local parsed corpus were searched for arXiv:1303.5818,
the exact question wording, `ABA=ACA`, and kernel complementability. A current
web search used the exact title and question, the operator identity, and the
phrases `share common complementability of kernels` and `I-AC I-BA`. The
decisive hit was the 2020 paper above; publisher, bibliographic, and later
citing pages agree on item (ii).

- `source_paper.pdf`: arXiv:1303.5818.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

The supporting PDF was not copied because the publisher PDF endpoint denied
automated access; the DOI landing metadata and published abstract are the
decisive evidence.

Ledger:
`runs/fa_banach_001/ledger/results/1303.5818_kernel_complementability_answered_2020.json`.
