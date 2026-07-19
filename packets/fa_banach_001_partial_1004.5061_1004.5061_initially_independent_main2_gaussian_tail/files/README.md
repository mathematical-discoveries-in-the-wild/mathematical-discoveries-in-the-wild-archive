# Partial Result: Gaussian tail for initially independent Theorem 4.2 integrands

Status: candidate partial result, likely valid; human review recommended.

Source paper: Mark Veraar and Lutz Weis, "A note on maximal estimates for
stochastic convolutions", arXiv:1004.5061.

## Target

After Theorem 4.2, the source paper says that it is unknown whether there are
exponential tail estimates in the general setting of Theorem 4.2. The same
paragraph explains that a bound \(C_{p,Y}^{\gamma}\lesssim_X \sqrt p\) would
give the desired quadratic exponential tail, while the then-recent
Cox--Veraar result only gave \(C_{p,Y}^{\gamma}\lesssim_X p\).

## Result

The quadratic tail is true in the deterministic and initially independent
subcase of Theorem 4.2. If the integrand \(G\) is measurable with respect to an
initial sigma-field independent of the driving Brownian motion and
\[
  \|G(\omega)\|_{\gamma(\mathbb R_+;H,X)}\le \sqrt M
  \quad\text{a.s.},
\]
then, with \(K_2\) the \(p=2\) maximal-estimate constant from Theorem 4.2,
\[
  \mathbb P\!\left(\sup_{t\ge0}\|S\diamond G(t)\|
       \ge K_2\sqrt M + u\right)
  \le \exp\!\left(-{u^2\over 2K_2^2M}\right)
  \quad(u\ge0).
\]
In particular, for \(\lambda\ge 2K_2\sqrt M\),
\[
  \mathbb P\!\left(\sup_{t\ge0}\|S\diamond G(t)\|\ge\lambda\right)
  \le \exp\!\left(-{\lambda^2\over 8K_2^2M}\right).
\]

## Proof Idea

Condition on the initial sigma-field. The integrand becomes deterministic, so
the stochastic convolution is a centered Gaussian process indexed by time. The
source paper's Theorem 4.2 at \(p=2\) gives
\[
  \left(\mathbb E\sup_t\|S\diamond g(t)\|^2\right)^{1/2}
  \le K_2\|g\|_\gamma .
\]
This bounds both the mean of the supremum and the weak variance parameter of
the Gaussian process. Borell's Gaussian concentration inequality then gives
the quadratic tail conditionally, and integration over the initial randomness
gives the stated estimate.

## Scope

This does not solve the full adapted problem. In the adapted case the process
is no longer conditionally Gaussian after freezing only the past, and the
source paper's own route still requires the open \(\sqrt p\) growth problem for
UMD stochastic-integral/decoupling constants. Cox--Veraar, arXiv:1107.2218,
explicitly note that this \(\sqrt p\)-growth is open already for
\(X=L^q\), \(q\ne2\).

## Files

- `main.tex`: theorem, proof intuition, proof, limitations, and references.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1004.5061.
- `supporting_paper_1107.2218.pdf`: local copy of the Cox--Veraar
  decoupling paper used for the open-constant boundary.
- `figures/open_problem_crop.png`: crop of the source paragraph after
  Theorem 4.2.
- `code/make_open_problem_crop.py`: reproducible crop generator.

## Verification

Cheap-index search found no existing packet for arXiv:1004.5061. Local source
inspection separated the same-paper answered Theorem 2.4 exponential-tail
signal from the real open paragraph after Theorem 4.2. Literature checks on
the exact paragraph, \(C_{p,Y}^{\gamma}\), Cox--Veraar arXiv:1107.2218, and
Yaroslavtsev arXiv:1807.05573 found qualitative and linear-growth support but
no full adapted quadratic-tail result.
