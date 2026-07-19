# Full Candidate: arbitrary b-metric spaces admit completions

Status: candidate full solution, likely valid; human review strongly
recommended.

Source paper: S. Cobzas, "b-metric spaces, fixed points and Lipschitz
functions", arXiv:1802.02722.

## Target

Remark 1.18 of the source paper says that the existence of a completion of an
arbitrary b-metric space is still an important open problem. The paper recalls
the known positive answer for strong b-metrics, where the usual quotient of
Cauchy sequences works because the strong b-metric is continuous enough for
the limit distance to be well defined.

## Result

Every b-metric space admits a completion in the source paper's isometric
sense. More precisely, if \(d\) has relaxed triangle constant \(s\), then
there is a complete b-metric space \((\widehat X,D)\), with the same relaxed
triangle constant \(s\), and an isometric embedding \(j:X\to\widehat X\) whose
image is dense.

The completion is not claimed to be canonical or unique. The construction uses
a choice of one representative Cauchy sequence for each Cauchy-sequence class.

## Proof Idea

The usual strong-b-metric completion fails for arbitrary b-metrics because
\(\lim_n d(x_n,y_n)\) need not be well defined on equivalence classes. The
way around this is to stop asking for a canonical formula.

Take equivalence classes of Cauchy sequences as usual. For each class choose a
single representative sequence, choosing the constant representative for each
original point \(x\). Define
\[
  D(\xi,\eta)=\limsup_n d(x^\xi_n,x^\eta_n).
\]
Because the same index \(n\) is used in both representatives, the relaxed
triangle inequality passes directly to \(D\). Constant representatives make
the original embedding exactly isometric. Density is immediate from the
Cauchy property of each chosen representative. Completeness follows by a
diagonal argument applied to a \(D\)-Cauchy sequence of classes.

## Files

- `main.tex`: theorem, proof intuition, proof, novelty check, and review notes.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1802.02722.
- `figures/open_problem_crop.png`: crop of Remark 1.18.
- `code/make_open_problem_crop.py`: reproducible crop generator.

## Verification

Cheap-index search found no existing packet for arXiv:1802.02722. Local parsed
source search found the completion problem only in Remark 1.18 and nearby
context. Web search on 2026-06-18 for exact phrases including "completion of
an arbitrary b-metric space" and "Does every b-metric space admit a
completion" found the earlier strong-b-metric paper arXiv:1503.08126 but no
later full arbitrary-b-metric completion answer.
