# Literature-Implied Answer: scalar `ell_p^2` BPBp reciprocal subcase

Status: `literature_implied_answer (partial subcase)`

Source/open-problem paper: Yun Sung Choi, Sheldon Dantas, Mingu Jung, Miguel Martin, "The Bishop-Phelps-Bollobas property and absolute sums", arXiv:1806.09366.

Supporting theorem: Kim--Lee, "Uniform convexity and the Bishop-Phelps-Bollobas property", Canad. J. Math. 66 (2014), Theorem 3.1; also cited in Dantas--Kadets--Kim--Lee--Martin, arXiv:1709.00032, Introduction, as saying that `(X,Y)` has the BPBp for every Banach space `Y` whenever `X` is uniformly convex.

## Identification

The source paper asks what happens for the reciprocal BPBp problem for `ell_p` sums, `1<p<infty`, after noting that the scalar-coordinate example `(R,Y)` does not extend to `R \oplus_1 R` or `R \oplus_\infty R` for suitable `Y` (source line 451 / Section 3). On the scalar two-summand reading, this asks whether `(R \oplus_p R,Y) = (ell_p^2,Y)` can fail despite both coordinate pairs being trivially BPBp.

## Answered Subcase

For every `1<p<infty` and every Banach space `Y`, the pair `(ell_p^2,Y)` has the BPBp. Indeed, `ell_p^2` is uniformly convex, and the Kim--Lee theorem gives the BPBp for `(X,Y)` for every range `Y` whenever `X` is uniformly convex. Thus the specific scalar-coordinate obstruction used for `p=1` and `p=infty` cannot occur for `1<p<infty`.

This is an agent-identified implication from known theorems, not an original proof and not a claim that the full arbitrary reciprocal problem for `(X_1 \oplus_p X_2,Y)` is solved.

## Scope Limits

- Answered: scalar two-coordinate subcase `X_1=X_2=R`, i.e. `ell_p^2`, for all `1<p<infty` and all Banach ranges `Y`.
- Not answered here: the general reciprocal problem asking whether `(X_1,Y)` and `(X_2,Y)` having BPBp imply `(X_1 \oplus_p X_2,Y)` having BPBp for arbitrary Banach spaces `X_1,X_2,Y`.
- Field: the source passage is written with `R`; the cited source `arXiv:1709.00032` states the BPBp definition over `K=R` or `C`, and the uniformly convex-domain theorem is quoted in that setting. The source question's displayed counterexample passage is real-scalar.

## Packet Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1806.09366.
- `supporting_paper_1709.00032.pdf`: arXiv support quoting the uniformly convex-domain theorem and the `ell_1^2` obstruction context.
- `source_paper.tex`, `supporting_source_1709.00032.tex`, `supporting_source_1605.00245.tex`: cached TeX provenance.

Ledger record: `runs/fa_banach_001/ledger/results/1806.09366_lpscalar_reciprocal_bpbp_uniform_convexity.json`.
