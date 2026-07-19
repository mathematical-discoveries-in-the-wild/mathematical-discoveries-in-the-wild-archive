# 1209.4619 unconditional translate-frame gap answered by 2312.01757

Status: `literature_already_answered`

Source/open-problem paper:

- D. Freeman, E. Odell, Th. Schlumprecht, and A. Zsak, *Unconditional structures of translates for L_p(R^d)*, arXiv:1209.4619.
- Section 3, Theorem 3.2 proves the positive half: for every `2<p<infty`, every dimension `d`, and every unbounded sequence of translation parameters in `R^d`, there is an unconditional Schauder frame for `L_p(R^d)` whose vectors are translates of one function.
- This leaves the complementary arbitrary-translate frame question for `1<p<=2`, beyond the source's integer-translate obstruction and distinct from the final Schauder-basis/basic-sequence problems in Section 6.

Supporting answer:

- Nir Lev and Anton Tselishchev, *There are no unconditional Schauder frames of translates in L^p(R), 1<=p<=2*, arXiv:2312.01757.
- The introduction explicitly says that the existence of an unconditional Schauder frame of translates in `L^p(R)`, `1<p<=2`, remained open after the Freeman--Odell--Schlumprecht--Zsak positive result for `p>2`.
- Theorem 1.1 proves the negative answer: for `1<=p<=2`, `L^p(R)` admits no unconditional Schauder frame of the form `(T_{lambda_n} g, g_n^*)`.

Identification:

Together, arXiv:1209.4619 and arXiv:2312.01757 give the sharp dichotomy for unconditional Schauder frames whose vectors are translates of a single function on the line:

- `p>2`: such frames exist, even along arbitrary unbounded translate sequences, by arXiv:1209.4619.
- `1<=p<=2`: such frames do not exist, by arXiv:2312.01757.

Scope limitations:

This packet records the frame gap only. It does not solve the still-open Schauder-basis problem for translates in `L_p(R)`, nor the Section 6 basic-sequence and unconditional-FDD questions from arXiv:1209.4619.

Files:

- `source_paper.pdf`: arXiv:1209.4619.
- `supporting_paper_2312.01757.pdf`: arXiv:2312.01757.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- Ledger record: `runs/fa_banach_001/ledger/results/1209.4619_unconditional_frame_p_le_2_answered_by_2312.01757.json`.
