# Full solution packet: the isotropic orthant constant has order n^{-1/2}

Status: `candidate_full_solution_likely_valid` (full resolution of the source's
order-of-magnitude question, pending human review)

Source: Matthieu Fradelizi, Mathieu Meyer, and Vlad Yaskin, *On the volume of
sections of a convex body by cones*, arXiv:1604.05351, Remark 3 on p. 11 of
the arXiv PDF.

## Result

For an isotropic convex body \(K\subset\mathbb R^n\) and an orthonormal basis
\(u_1,\ldots,u_n\), let

\[
p(K,u)=\frac{|K\cap\{x:\langle x,u_i\rangle\ge0,\ 1\le i\le n\}|}{|K|},
\qquad
\alpha_n=2\inf_{K,u}p(K,u)^{1/n}.
\]

The source established \(\alpha_n\ge n^{-1}\), conjectured order
\(n^{-1/2}\), and proved the matching upper order only when \(n\) is a power
of two.  This packet proves, for every \(n\ge1\),

\[
\frac{c}{\sqrt n}\le\alpha_n\le\frac{4e}{\sqrt n}
\]

with a universal explicit \(c>0\).  Thus \(\alpha_n\asymp n^{-1/2}\).

The exact numerical value of \(\alpha_n\) is not determined; the source's
asymptotic-order conjecture is fully resolved.

## Main ideas

- A nonnegative log-concave random variable has its second moment controlled
  by the square of its first moment.  Applying this to the negative half of
  every one-dimensional marginal, together with Grunbaum's halfspace bound,
  shows that an isotropic convex body contains a centered Euclidean ball whose
  radius is a universal multiple of its covariance scale.
- Gaussian maximum entropy bounds that covariance scale below by a universal
  multiple of \(|K|^{1/n}\).  The ball contributes exactly one \(2^{-n}\)
  sector to every orthant, producing the lower bound \(c/\sqrt n\).
- For the upper bound, write \(n\) as a sum of distinct powers of two.  In
  each coordinate block, a Sylvester-Hadamard basis cuts from the cube the
  simplex used by the source.  A block-product and binary-entropy estimate
  gives \(\alpha_n\le4e/\sqrt n\) in every dimension.

## Packet contents

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: full-width crop of Remark 3.
- `code/verify_hadamard_blocks.py`: Hadamard, determinant, binary-block, and
  constant checks.
- `code/make_open_problem_crop.py`: reproducible source crop.
- `verification_report.md`: verification scope and output.

## Novelty and review

Local registry/solution/attempt/proof-gap indexes were searched for the arXiv
id, `alpha_n`, isotropic orthant mass, orthant probability, and the core
geometric terms.  Three bounded web-search rounds on 2026-07-21 used the exact
source phrase, title, authors, `isotropic convex body`, `positive orthant`, and
the \(n^{-n/2}\) probability scale.  They found the source and unrelated
isotropic/log-concave literature, but no later answer or matching proof.  This
is not an exhaustive citation or priority search, so novelty confidence is
**moderate**.

Recommended review focus: the one-dimensional survival-function moment
lemma, its application to the supporting distance of \(K\), and the passage
from the source's power-of-two cube construction to arbitrary binary block
dimensions.
