# Full scoped result: BDP is stable for Bochner \(L^p\), \(1<p<\infty\)

Status: `full_solution_likely_valid_scoped_bdp_p_gt_1`

Source paper: Sudeshna Basu and Susmita Seal, *Small Combination of Slices, Dentability and Stability Results Of Small Diameter Properties In Banach Spaces*, arXiv:2108.02908.

Related endpoint packet: `runs/fa_banach_001/solutions/counterexamples/2011.14591_l1_scalar_bdp_converse_counterexample/`.

## Claim

The source proves that if \(L^p(\mu,X)\) has BDP, then \(X\) has BDP, for \(1\le p<\infty\), and asks whether the converse is true.

This packet proves the converse for every nonzero finite measure space and every \(1<p<\infty\):
\[
  X\text{ has BDP}\quad\Longrightarrow\quad L^p(\mu,X)\text{ has BDP}.
\]
Together with the source implication, this gives
\[
  L^p(\mu,X)\text{ has BDP}\quad\Longleftrightarrow\quad X\text{ has BDP}
\]
for \(1<p<\infty\).

The existing endpoint packet records that the converse fails at \(p=1\) over Lebesgue measure with \(X=\mathbb R\). Thus the BDP converse has the expected exponent split: false at \(p=1\), true for \(1<p<\infty\).

## Proof Idea

Choose a small slice \(S(B_X,x^*,\eta)\) of \(B_X\). In \(L^p(\mu,X)\), use the slice determined by
\[
  F(f)=\int x^*(f(t))\,d\mu(t).
\]
For \(1<p<\infty\), the scalar functional \(h\mapsto\int h\) strongly exposes the constant \(1\) in the unit ball of scalar \(L^p\). Hence if \(F(f)\) is close to \(1\), then \(\|f(t)\|\) is close to \(1\) in \(L^p\), and the defect
\[
  \|f(t)\|-x^*(f(t))
\]
is small in \(L^1\). Outside a set of small \(L^p\)-mass, the normalized values \(f(t)/\|f(t)\|\) lie in the original small slice of \(B_X\). Two functions in the lifted slice therefore differ by at most the original slice diameter, plus a small scalar exposure error.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2108.02908.
- `figures/open_problem_crop.png`: crop of the source Bochner converse remark.

## Scope

This is a full positive solution for the BDP converse when \(1<p<\infty\), and completes the BDP exponent classification when combined with the existing \(p=1\) counterexample packet.

It does not settle the analogous BHP converse for \(1<p<\infty\), nor the later Kothe-Bochner BSCSP question recorded in arXiv:2307.03631.

## Novelty Check

Cheap run indexes were searched for `2108.02908`, `2011.14591`, `BDP`, `BHP`, `Lebesgue-Bochner`, `Ball Dentable Property`, and the Bochner converse language. The existing p=1 endpoint packet was found and used as related provenance; it explicitly left the \(1<p<\infty\) positive direction unsettled.

Web searches for exact phrases around `Ball Dentable Property Lp Bochner`, `BDP Lebesgue-Bochner p>1`, and the source title returned the source paper but no separate explicit \(1<p<\infty\) BDP converse answer.

## Human Review Focus

Check the sequential lifting lemma, especially the passage from near equality in scalar Holder to \(L^p\)-small exceptional sets. The proof only uses standard uniform convexity of scalar \(L^p\) for \(1<p<\infty\).

