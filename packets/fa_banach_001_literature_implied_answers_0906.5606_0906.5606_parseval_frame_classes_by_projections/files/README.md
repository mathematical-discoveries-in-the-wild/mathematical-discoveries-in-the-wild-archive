# Literature-Implied Answer: Parseval Frame Equivalence Classes

Status: literature_implied_answer.

Source:
- P. G. Casazza, G. Kutyniok, S. Li, and C. J. Rozell, "Fusion frames: existence and construction", arXiv:0906.5606.
- Local PDF: `source_paper.pdf`.

Source subproblem:
- In Section 4, subsection "Extensions and Related Problems", under "Equivalence Classes", the source says that it is still unsolved to "Construct one Parseval frame in each equivalence class choosing unitary equivalence as the relation."

Supporting literature:
- R. B. Holmes and V. I. Paulsen, "Optimal frames for erasures", Linear Algebra Appl. 377 (2004), 31--51, DOI: 10.1016/j.laa.2003.07.012.
- The supporting paper identifies normalized tight frames with rank projections via their Gramian/analysis projection and states a one-to-one correspondence between `n x n` rank `k` projections and type-I/unitary equivalence classes of `(n,k)`-frames.
- The downloaded ScienceDirect access page is saved as `supporting_source_holmes_paulsen_sciencedirect.html`; the direct endpoint did not produce a PDF file in this environment.

Identification:
- Parseval frames in the source's problem are normalized tight frames in Holmes-Paulsen's terminology.
- The source's unitary equivalence is Holmes-Paulsen's type-I equivalence.
- Therefore each rank-`k` orthogonal projection `P` on `F^n` gives a canonical representative of one equivalence class: the Parseval frame `{P e_i}_{i=1}^n` in `ran P`.

Scope:
- This answers the finite ordered Parseval-frame problem under unitary equivalence.
- It does not answer the broader fusion-frame equivalence-class program, the weighted fusion-frame design problem, the chordal-distance design problem, or the sparsity maximality conjecture in the same source subsection.

Ledger:
- `runs/fa_banach_001/ledger/results/0906.5606_parseval_frame_classes_by_projections.json`
