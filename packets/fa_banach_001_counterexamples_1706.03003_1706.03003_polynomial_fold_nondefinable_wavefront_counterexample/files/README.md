# Counterexample packet: a polynomial fold with nondefinable wave-front set

status: counterexample_likely_valid

source_arxiv: 1706.03003

source_question: Example 3.4.6, PDF page 35, asks whether wave-front sets of special distributions are definable, specifically mentioning pushforwards of smooth distributions under polynomial mappings.

## Result

The answer is negative for the broad reading natural in the paper's
\(\mathcal C^{\exp}\)-class framework.

For every non-archimedean local field \(F\) of odd residue characteristic, let
\(q_F\) be the residue-field cardinality, put
\[
X_F=(\mathcal O_F\setminus\{0\})^2,
\qquad
h_F(x,y)=q_F^{\operatorname{ord}x}-\operatorname{ord}y,
\]
and let \(u_F\) be the smooth distribution on \(X_F\times\mathcal O_F\)
represented by the locally constant density \(h_F(x,y)\).  Push it forward by
the restriction of the polynomial map
\[
f_F(x,y,t)=(x,y,t^2).
\]
Then
\[
\operatorname{WF}_{F^\times}(f_{F,*}u_F)
=
\left\{
  ((x,y,0),(0,0,\eta)):
  h_F(x,y)\ne0,\ \eta\in F^\times
\right\}.
\]
This wave-front set is not definable in the Denef--Pas framework.  Indeed,
the zero locus of \(h_F\) has valuation image
\[
\{(m,n)\in\mathbb N^2:n=q_F^m\},
\]
which is not Presburger-definable.

The input is a smooth distribution of \(\mathcal C^{\exp}\)-class, the map is
polynomial, and it is proper on the support of the input distribution.  Thus
all hypotheses needed to form the pushforward and apply the source paper's
wave-front pushforward theorem are satisfied.

## Proof mechanism

Write \(\nu_F=(t\mapsto t^2)_*(1_{\mathcal O_F}|dt|)\).  Its mass on the ball
\(B_r(0)\), for \(r\ge0\), is
\[
\nu_F(B_r(0))=q_F^{-\lceil r/2\rceil}.
\]
A smooth density near zero would instead give \(c q_F^{-r}\) for all large
\(r\), so \(\nu_F\) is singular exactly at zero.  Since
\(f_{F,*}u_F=(h_F|d(x,y)|)\otimes\nu_F\), its singular support is precisely
\(\{h_F\ne0\}\times\{0\}\).  The source pushforward theorem gives the upper
bound by the normal cone of the fold, which contains only the vertical
covectors \((0,0,\eta)\).  Projection of wave-front set onto singular support,
together with \(F^\times\)-conicity, gives the displayed equality.

## Evidence

- `source_paper.pdf`: Cluckers--Halupczok--Loeser--Raibaut,
  *Distributions and wave front sets in the uniform non-archimedean setting*,
  arXiv:1706.03003.
- `figures/open_problem_crop.png`: the complete live question on PDF page 35.
- `main.tex`: full theorem and proof.
- `solution_packet.pdf`: rendered proof packet.
- `verification_report.md`: independent checklist of hypotheses and proof
  dependencies.

## Interpretation limitation

The counterexample uses a smooth constructible/\(\mathcal C^{\exp}\)-density
whose nonzero locus is deliberately nondefinable.  It therefore rules out a
blanket definability theorem for the class named in the source question.  It
does **not** rule out a narrower theorem assuming that the smooth density
itself has a definable zero/nonzero locus (for example, a fixed algebraic
measure or a Denef--Pas-definable locally constant density).  That narrower
problem remains open in this packet.

## Novelty check

A bounded check on 2026-07-22 searched the run registry, solution, attempt,
and proof-gap indexes; the local arXiv corpus; the 2019 follow-up
arXiv:1909.09048; and arXiv web searches for combinations of “non-archimedean
wave front set,” “definable,” “polynomial push-forward,” “smooth
distribution,” and the exact source wording.  The searches found the source
paper, Raibaut's *Motivic wave front sets* (arXiv:1810.10567), and the later
WF-holonomicity paper, but no statement or example matching this polynomial
fold counterexample.  The novelty verdict is therefore only bounded-search
confidence, not a claim of exhaustive priority.

## Human review recommendation

Review as a likely valid counterexample.  The two points deserving the most
attention are (i) the intended breadth of “smooth distributions” in the
source sentence, and (ii) the standard model-theoretic step that the graph
\(n=q_F^m\) is not Presburger-definable.  The microlocal calculation itself is
forced by the source paper's pushforward bound and singular-support projection
theorem.

