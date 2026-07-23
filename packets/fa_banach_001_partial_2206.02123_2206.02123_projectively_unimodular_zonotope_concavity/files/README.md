# Projectively unimodular zonotopes satisfy the segment-sum concavity conjecture

Status: **partial result; likely valid; send to human review**.

Source: Matthieu Fradelizi, Mokshay Madiman, Mathieu Meyer, and Artem
Zvavitch, *On the volume of the Minkowski sum of zonoids*, arXiv:2206.02123,
Section 5, page 20; Journal of Functional Analysis 286 (2024), article
110247.

## Source conjecture

For a zonoid \(Z\subset\mathbb R^n\), vectors \(u_1,\ldots,u_m\), and
\(m\leq n\), set
\[
P(t)=\operatorname{Vol}_n\left(Z+t\sum_{j=1}^m[0,u_j]\right).
\]
The source conjectures that \(P(t)^{1/m}\) is concave for \(t\geq0\).
The exact source passage is reproduced in
`figures/open_problem_crop.png`.

## Result

The conjectured conclusion holds when the combined generators of the finite
zonotope \(Z\) and the \(m\) distinguished segments are projectively
equivalent to the columns of a totally unimodular matrix.  In fact, \(P\)
then has only negative real zeros.

This includes graphical zonotopes in arbitrary dimension.  For example, a
partition of the edges of \(K_5\) gives a non-parallelotope example in
dimension four with \(m=3\):
\[
P(t)=4t^3+33t^2+72t+16=(t+4)^2(4t+1).
\]

The mechanism is elementary.  The zonotope determinant formula and total
unimodularity turn the volume polynomial into
\[
\lvert\det T\rvert
\det\!\left(A\operatorname{diag}(c_ex_e)A^{\mathsf T}\right).
\]
After the \(Z\)-variables are set to \(1\) and the distinguished variables to
\(t\), this is a positive-semidefinite determinantal pencil \(B+tC\) with
\(B>0\), hence a real-rooted polynomial.  Cauchy--Schwarz applied to its
linear-factor representation proves the requested \(1/m\)-concavity.

## Verification

The proof in `main.tex` is self-contained apart from the standard zonotope
volume formula and Cauchy--Binet, both used explicitly.  The exact script
`code/verify_graphical_example.py`:

- checks every minor of the reduced \(K_5\) incidence matrix;
- verifies the Cauchy--Binet and basis-sum formulas agree;
- factors \(P\) exactly; and
- verifies \(3PP''-2(P')^2=-450(t+4)^2\).

Run it with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2206.02123_projectively_unimodular_zonotope_concavity/code/verify_graphical_example.py
```

## Limitations and novelty check

The general conjecture remains open.  The proof needs projective total
unimodularity of the **combined** \(Z\)- and \(L\)-directions; an arbitrary
zonoid does not have this structure.

A bounded search on 2026-07-23 covered the exact conjecture text, the arXiv id
2206.02123, and combinations of `zonoid`, `totally unimodular`, `graphical
zonotope`, `volume polynomial`, `real stable`, and `concavity` in arXiv and
general web indexes.  It recovered the source paper and standard neighboring
work on Lorentzian/volume polynomials, but no paper stating this exact
projectively-unimodular subcase.  Novelty confidence is therefore moderate,
not definitive.

## Human review recommendation

Check the determinant identity under projective rescaling and the direct
upper-half-plane argument for \(\det(B+tC)\).  If those pass, the result is
ready as a concise proposition or note; the main remaining editorial choice
is whether the projectively-unimodular condition should be reformulated in
regular-matroid language.

Ledger:
`ledger/results/2206.02123_projectively_unimodular_zonotope_concavity.json`.
