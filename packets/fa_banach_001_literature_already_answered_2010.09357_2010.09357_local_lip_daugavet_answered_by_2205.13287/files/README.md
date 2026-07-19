# Literature Status: Local Lipschitz Functions Are Daugavet Points

Status: `literature_already_answered`

## Source Question

- Source paper: Mingu Jung and Abraham Rueda Zoca, "Daugavet points and Delta-points in Lipschitz-free spaces", arXiv:2010.09357.
- Location: Section 3, after Proposition 3.4 (`prop:daugaLipikw` in the source), where the authors ask whether a local norm-one function in `Lip_0(M)` must be a Daugavet point.
- Source result before the question: spreadingly local functions are Daugavet points; local functions are proved to be `w*`-Daugavet points.

## Supporting Answer

- Supporting paper: Rainis Haller, Andre Ostrak, and Mart Poldvere, "Diameter two properties for spaces of Lipschitz functions", arXiv:2205.13287.
- Location: Introduction, Theorem 1.5; Section 5, "Local norm-one Lipschitz function is a Daugavet point", especially Theorem 5.4 and Proposition 5.3 in the parsed source.
- Answer: yes. If `M` is a pointed metric space and `f in S_{Lip_0(M)}` is local, then `f` is a Daugavet point.

## Evidence

The supporting paper explicitly identifies the Jung--Rueda Zoca question and states that it fully answers it. The proof upgrades the original weak-star argument by representing arbitrary elements of `Lip_0(M)^*` via bounded finitely additive measures on the de Leeuw transform of `M`. Given a local norming pair sequence with distances tending to zero, the proof modifies a test Lipschitz function on a small set whose two coordinate cylinders have arbitrarily small measure. This keeps the arbitrary weak slice condition while forcing distance almost two from the local function.

## Scope

This packet records a known later answer, not a new proof from this run. It closes the exact extracted question from arXiv:2010.09357 about local norm-one Lipschitz functions in `Lip_0(M)` being Daugavet points. It does not record new progress on the separate Delta-point questions in the same source paper.

## Files

- `source_paper_2010.09357.pdf`: original source paper.
- `supporting_paper_2205.13287.pdf`: supporting answer paper.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

## Review Recommendation

Treat this target as answered in the literature by arXiv:2205.13287. Future agents should not re-attack the local Lipschitz implies Daugavet point question from arXiv:2010.09357 unless the task is to extract or simplify the Haller--Ostrak--Poldvere proof.
