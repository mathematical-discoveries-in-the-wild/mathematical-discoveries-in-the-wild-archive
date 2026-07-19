# Literature Answer: Problem U in Totally Smooth Renormings

Status: `literature_already_answered`

Source/open-problem paper: Eve Oja, Tauri Viil, and Dirk Werner, *Totally smooth renormings*, arXiv:1807.07335, Archiv der Mathematik 112 (2019), 269--281.

Supporting answer paper: Ch. Cobollo, A. J. Guirao, and V. Montesinos, *A remark on totally smooth renormings*, arXiv:2305.11611.

## Question Identified

Oja--Viil--Werner ask Problem U in the introduction:

> If `X` has property `U` in its bidual `X**`, then does `X` admit an equivalent norm under which `X` is totally smooth in its bidual?

They immediately reformulate it as Problem U convex: can one renorm so that `X*` is strictly convex while `X` still has property `U` in its bidual? Their paper proves positive separable and WCG cases, describing the WCG theorem as a partial positive answer in general.

## Answer Located

Cobollo--Guirao--Montesinos explicitly cite the Oja--Viil--Werner WCG result and state that it holds in full generality, without any restriction on the space, in a stronger form via Raja's theorem on dual LUR norms. Their Theorem 1 proves the equivalence, for a Banach space `X`, of:

- `X` has an equivalent norm with Hahn--Banach smoothness/property U in the bidual.
- `X` has an equivalent norm whose dual norm is LUR.
- `X` has an equivalent norm with total smoothness.

Since the original norm in Problem U already has property U/HBS, Theorem 1 gives an equivalent norm whose dual norm is LUR, hence strictly convex, and under which `X` has total smoothness. This answers both Problem U and Problem U convex positively in full generality.

## Scope And Provenance

The supporting authors explicitly knew they were addressing the Oja--Viil--Werner result: the abstract names *Totally smooth renormings* and says the WCG result holds in full generality. This packet is therefore classified as `literature_already_answered`, not as a new proof from this run.

Local files:

- `source_paper.pdf`: arXiv:1807.07335.
- `supporting_paper_2305.11611.pdf`: arXiv:2305.11611.
- `main.tex` / `solution_packet.pdf`: compact status note.

Ledger: `runs/fa_banach_001/ledger/results/1807.07335_problem_u_answered_by_2305.11611.json`.
