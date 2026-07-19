# Literature-Implied Answer: Higher Property (T) Converse Is False

Status: `literature_implied_answer (negative)`.

Source target: arXiv:1401.5362, U. Bader and P. W. Nowak,
*Cohomology of deformations*.

Source question: Section 5.1, "Higher property (T) and reduced cohomology",
defines Bader--Nowak property `(T_n)` for a group of type `F_{n+1}` as the
condition that `H^{n+1}(Gamma, pi)` is reduced for every unitary representation
`pi`. Immediately after Definition 5.1, the authors ask whether this reducedness
condition implies vanishing of `H^{n+1}(Gamma, pi)` for every unitary `pi`.

Identification: Bader--Sauer, arXiv:2308.06517v3, *Higher Kazhdan property and
unitary cohomology of arithmetic groups*, states in the introduction that the
higher analogues of the Delorme--Guichardet criteria are not equivalent. More
decisively, Remark 3.10 says that for `n > 1`, reducedness of `H^k(Gamma,U)` for
all `k <= n` and all unitary `U` does not imply their vanishing property
`(T_n)`, because `SL_{n+1}(Q_p)` and its lattices have reduced cohomology in all
degrees. Combined with Garland's vanishing through degree `n-1`, recorded in the
same paper, the failure occurs in degree `n`.

Scope: this gives a negative answer to the source converse in every genuinely
higher degree. The degree-zero case remains the classical Delorme--Guichardet
theorem: property `(T_0)` is equivalent to vanishing of first cohomology for all
unitary representations.

Provenance: the supporting paper does not present itself as answering the exact
question in arXiv:1401.5362. The relation is an agent-identified implication
after matching the original Bader--Nowak Hausdorff/reduced definition with the
later separation examples.

Files:
- `main.tex` / `solution_packet.pdf`: compact status note.
- `source_paper.pdf`: arXiv:1401.5362, when downloaded.
- `supporting_paper_2308.06517.pdf`: arXiv:2308.06517v3, when downloaded.

