# Literature-Implied Partial Answer: Complex Selfadjoint `L_1`-Preduals

Status: `literature_implied_answer (partial subcase)`.

Source paper: Pavel Ludvik and Jiri Spurny, *Descriptive properties of elements of biduals of Banach spaces*, arXiv:1105.3413.

Source question: page 5 / introduction asks whether Theorem 1.4 remains valid for complex `L_1`-preduals. The paper proves the theorem for real `L_1`-preduals and says the complex case remains open because it is unclear whether Lusky's complementability theorem remains true in the complex setting.

Implied partial answer: the complex analogue of Theorem 1.4 holds for selfadjoint complex `L_1`-preduals, i.e. complex spaces isometric to `A(X)+iA(X)` for a Choquet simplex `X`. By Hirsberg-Lazar, this includes every complex Lindenstrauss space whose unit ball has an extreme point.

Reason: in the selfadjoint representation, restrict the bidual element to the canonical simplex `X`, apply the real simplex/real `L_1`-predual theorem from Ludvik-Spurny to the real and imaginary parts, then lift the resulting affine-class approximants back to the dual ball by integration against representing complex measures.

Scope limitation: this does not resolve the nonselfadjoint complex `L_1`-predual case. Wulbert constructed nonselfadjoint complex `L_1`-preduals, so the remaining case is not vacuous.

Files:
- `main.tex`: compact proof/status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source open-problem sentence.
