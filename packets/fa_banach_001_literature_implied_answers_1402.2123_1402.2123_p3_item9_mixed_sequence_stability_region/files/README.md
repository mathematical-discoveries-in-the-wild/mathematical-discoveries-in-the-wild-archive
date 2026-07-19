# Literature-implied partial answer: stability of mixed sequence self-pairs

Status: `literature_implied_answer (partial subcase)`.

Source question: Duanxu Dai, *On Qian's problem for
\(\mathcal L_\infty\)-spaces*, arXiv:1402.2123v4, Problem 4.7(9), PDF page
11.  In the notation

\[
E_{p,q}=\left(\bigoplus_{n=1}^{\infty}\ell_p\right)_{\ell_q}
       =\ell_q(\ell_p),
\]

the source asks whether the self-pair \((E_{p,q},E_{p,q})\) is stable.

## Identified answer

Over the real scalars, the pair \((E_{p,q},E_{p,q})\) is
\((1,2)\)-stable whenever

\[
1<p,q<\infty,\qquad p\ne q,\qquad p,q\ne2,
\qquad\text{and}\qquad \neg(1<q<p<2).
\]

Equivalently, every standard \(\varepsilon\)-isometry
\(f:E_{p,q}\to E_{p,q}\) admits a linear operator
\(T:E_{p,q}\to E_{p,q}\) with

\[
\|T\|=1,
\qquad
\|Tf(x)-x\|\le 2\varepsilon\quad(x\in E_{p,q}).
\]

## Identification

The conclusion follows by combining three results that predate the source
question.

1. Koldobsky's Theorem 3 (Indiana Univ. Math. J. 40 (1991), journal pages
   697--699) classifies real linear self-isometries of
   \(L_r(X;L_s(Y))\) when \(r\ne s\), \(s\ne2\), and
   \(s\notin(r,2)\) if \(r<2\).  Applied to finite weighted atomic models
   of \(\ell_q(\ell_p)\), it gives the weighted-rearrangement/fibre form of
   every isometric embedding of \(E_{p,q}\) into itself.
2. For the image of the canonical double basis, that form gives disjoint
   outer supports between distinct outer blocks and, within one block,
   equal fibre norms and disjoint inner supports.  Theorem 5.1 of Lemmens,
   Randrianantoanina, and van Gaans (arXiv:math/0511044, PDF page 19) says
   exactly that a real subspace with such a basis is the range of a
   contractive projection.
3. Remarks 2.5(2) of Semrl and Vaisala (arXiv:math/0112294, PDF page 9)
   show that a standard \(\varepsilon\)-nearisometry into a uniformly
   convex and uniformly smooth space has a norm-one linear left inverse
   with error at most \(2\varepsilon\), provided its asymptotic isometric
   copy is the range of a norm-one projection.  Mixed sequence spaces in
   the displayed reflexive range are uniformly convex and uniformly
   smooth, so the preceding step supplies that projection.

The compact proof and the parameter translation \((r,s)=(q,p)\) are given
in `main.tex` and `solution_packet.pdf`.

## Provenance and scope

This is an agent-identified implication, not an original theorem of this
run.  None of the three supporting papers presents its result as an answer
to Dai's later Problem 4.7(9), but their combination already yields the
stated subcase.  For that reason the packet is placed under
`literature_implied_answers` rather than `partial`.

This packet does **not** settle the endpoints \(p=1\), \(q=1\), or infinity;
the cases \(p=2\) or \(q=2\); the remaining real triangle
\(1<q<p<2\); item (10) with \(L_p\) fibres; or any other item of Problem
4.7.

The bounded search checked the exact Problem 4.7 wording, the arXiv id,
mixed-norm/Qian-stability phrases, and citation trails for the three decisive
theorems.  No later paper explicitly advertising this subcase as an answer
was found.  Since all decisive ingredients predate arXiv:1402.2123, the
mathematical relation is nevertheless classified as literature-implied.

## Files

- `source_paper.pdf`: arXiv:1402.2123v4.
- `supporting_paper_koldobsky_1991.pdf`: Koldobsky's 1991 journal paper.
- `supporting_paper_0511044.pdf`: contractive-complementation theorem.
- `supporting_paper_0112294.pdf`: sharp near-isometry theorem.
- `main.tex`: compact identification and proof.
- `solution_packet.pdf`: rendered status note.
- Ledger: `runs/fa_banach_001/ledger/results/1402.2123_p3_item9_mixed_sequence_stability_region.json`.

