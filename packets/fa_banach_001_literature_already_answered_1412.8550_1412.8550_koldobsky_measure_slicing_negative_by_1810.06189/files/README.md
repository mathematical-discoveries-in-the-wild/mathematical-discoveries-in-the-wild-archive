# Koldobsky Measure-Slicing Problem: Negative Answer by Klartag--Livshyts

Status: `literature_already_answered (negative; fails already for k=1)`.

This packet records a later-literature answer, not a new proof from this run.

Source/open-problem paper:

- arXiv:1412.8550, Alexander Koldobsky, "Slicing inequalities for measures of convex bodies".
- Exact source location:
  - Problem `prob` in the Introduction, source lines 116-122.
  - The same question is stated in the abstract at source lines 55-63.

Supporting answer:

- arXiv:1810.06189, Boaz Klartag and Galyna V. Livshyts, "The lower bound for Koldobsky's slicing inequality via random rounding".
- Exact answer locations:
  - Abstract, source lines 70-72, states the sharp lower-bound construction.
  - Introduction, source lines 86-93, defines the hyperplane section measure and the quantity \(S_{\mu,K}\).
  - Introduction, source lines 96-110, identifies Koldobsky's question, recalls the upper bound \(S_n\leq \sqrt n\), and states Theorem 1.
  - Proof construction, source lines 540-543, defines the symmetric Gaussian-convolution measure.
  - Proof conclusion, source lines 623-630, gives \(\mu(L)\geq 1/2\), while the preceding section bound gives all hyperplane sections \(O(n^{-1/2})\).
  - Bibliography, source line 798, cites Koldobsky's 2015 paper.

## Identification

Koldobsky asks whether there is an absolute constant \(C\) such that, for
every \(n\), every \(1\leq k<n\), every origin-symmetric convex body \(L\subset
\mathbb R^n\), and every non-negative even continuous density measure \(\mu\),
\[
  \mu(L) \leq C^k \max_{H\in Gr_{n-k}}\mu(L\cap H)|L|^{k/n}.
\]

For \(k=1\), this asks for a uniform bound on
\[
  S_{\mu,L}
  =
  \inf_{\xi\in S^{n-1}}
  \frac{\mu(L)}
       {|L|^{1/n}\mu^+(L\cap \xi^\perp)}.
\]

Klartag--Livshyts prove that for every \(n\) there are a measure \(\mu\) and a
symmetric convex body \(L\subset\mathbb R^n\) such that all affine hyperplane
sections, in particular all central sections, satisfy
\[
  \mu^+(L\cap(\xi^\perp+t\xi))
  \leq
  \frac{C}{\sqrt n}\,\mu(L)|L|^{-1/n}.
\]
At \(t=0\), this gives \(S_{\mu,L}\geq c\sqrt n\). Therefore no absolute
constant can satisfy Koldobsky's Problem `prob`, since the proposed statement
would already require \(S_{\mu,L}\leq C\) when \(k=1\).

The density hypothesis is compatible with the source problem: the supporting
proof constructs \(\mu\) as the convolution of the standard Gaussian measure
with a symmetrized discrete measure. Hence the resulting density is
continuous, non-negative, and even.

## Scope

This is a negative literature answer to the full arbitrary-measure
absolute-constant problem in arXiv:1412.8550, because a counterexample in one
allowed codimension disproves the universal "for every \(k\)" assertion.

The packet does not contradict the positive subclasses proved in the source
paper: unconditional bodies, duals of bounded volume ratio, and proportional
codimension \(k\geq \lambda n\). It also does not address Bourgain's original
Lebesgue-volume slicing problem.

For \(k=1\), the later paper also records the sharp order of the worst
arbitrary-measure hyperplane constant: Koldobsky's earlier upper bound gives
\(S_n\leq \sqrt n\), while Klartag--Livshyts give \(S_n\geq c\sqrt n\).

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source paper arXiv:1412.8550.
- `supporting_paper_1810.06189.pdf`: supporting answer paper.
- `tmp/`: LaTeX build intermediates.

