# Literature-Already-Answered Packet: geometry of (V(T))

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: the open question in arXiv:1706.08682 has a negative answer in the
authors' later paper arXiv:2001.09677. This packet records that literature
answer; it does not claim a new result from this run.

## Original question

- F. L. Hernández, E. M. Semenov, P. Tradacete, *Interpolation and
  extrapolation of strictly singular operators between (L_p) spaces*,
  arXiv:1706.08682; Adv. Math. 316 (2017), 667--690.
- Local source: `data/parsed/arxiv_sources/1706.08682/source.tex`, especially
  lines 526--590.
- PDF location: `source_paper.pdf`, page 14 (the displayed figure is numbered
  Figure 1 in this arXiv PDF).

For an operator (T:L_\infty\to L_1), the paper defines

\[
V(T)=\{(1/p,1/q):T:L_p\to L_q\text{ is strictly singular but not compact}\}.
\]

Its examples produced only horizontal, vertical, and diagonal-parallel pieces.
Immediately after the displayed example, the paper asks whether (V(T))
always has that shape.

## Decisive later answer

- F. L. Hernández, E. M. Semenov, P. Tradacete, *Strictly singular
  non-compact operators between (L_p) spaces*, arXiv:2001.09677; Rev. Mat.
  Iberoam. 39 (2023), no. 1, 181--200, DOI 10.4171/RMI/1360.
- Local source: `data/parsed/arxiv_sources/2001.09677/source.tex`, especially
  lines 66--112 and 363--398.
- PDF locations: `supporting_paper_2001.09677.pdf`, pages 2 and 8.

The later paper explicitly identifies the earlier question and says it will
answer it negatively. Its Theorem 9 proves the stronger exact statement that,
for every admissible line segment \(\ell\), there is an operator
\(T:L_\infty\to L_1\) for which

\[
L(T)=S(T)=L_\ell\cup\ell,\qquad K(T)=L_\ell,\qquad V(T)=\ell.
\]

The admissible family includes every line segment of positive slope lying
strictly below the diagonal. Choosing, for example, a segment of slope (2)
gives a (V(T)) which is neither horizontal, vertical, nor parallel to the
diagonal. Thus the answer to the 2017 question is **no**.

## Proof idea in the supporting paper

For slopes at least (1), the authors use a Riesz potential

\[
(T_\lambda f)(t)=\int_0^1 |t-u|^{-\lambda}f(u)\,du
\]

from Lebesgue measure on ((0,1)) to Hausdorff measure on an Ahlfors
\(\alpha\)-regular subset. They compute

\[
V(T_\lambda)=
\left\{\left(x,\frac{x-1+\lambda}{\alpha}\right):
1-\lambda<x<\min\left(1,\frac{1-\lambda}{1-\alpha}\right)\right\},
\]

whose slope is (1/\alpha). Duality supplies slopes in ((0,1)), while
Rademacher/disjoint-sequence factorizations handle horizontal and vertical
segments. The theorem determines (L(T)), (S(T)), and (K(T)), not merely
the inclusion of one unexpected segment.

## Verification and novelty classification

- Exact-source check: arXiv:1706.08682 poses the question after its constructed
  example and does not answer it there.
- Separate-paper check: arXiv:2001.09677 is a later, distinct paper and cites
  the 2017 paper as the source of the question.
- Exact-answer check: the introduction explicitly says the answer is negative,
  and Theorem 9 gives (V(T)=\ell).
- Scope check: both papers use the same definition of (V(T)) for operators
  (L_\infty\to L_1).
- Duplicate check: the existing full packet for arXiv:2001.09677 concerns that
  later paper's different endpoint-boundedness remark, not the 2017 geometry
  question.
- Novelty: none claimed. The correct classification is
  `literature_already_answered`.

## Files

- `README.md`: source chain and classification.
- `main.tex`: compact human-readable answer note.
- `solution_packet.pdf`: rendered answer note.
- `source_paper.pdf`: arXiv:1706.08682.
- `supporting_paper_2001.09677.pdf`: arXiv:2001.09677.

## Human review recommendation

Check page 14 of the source PDF, then pages 2 and 8 of the supporting PDF. The
logical match is direct: the later authors restate the earlier proposed shape,
announce a negative answer, and prove exact realization of positive-slope
segments.
