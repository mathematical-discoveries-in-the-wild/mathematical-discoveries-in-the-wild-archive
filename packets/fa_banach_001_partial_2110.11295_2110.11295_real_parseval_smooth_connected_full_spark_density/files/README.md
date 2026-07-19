# Real Parseval Smooth Connected Full-Spark Density

Status: `partial_result_likely_valid`.

Source/open-problem paper: Tom Needham and Clayton Shonkwiler, *Toric Symplectic Geometry and Full Spark Frames*, arXiv:2110.11295.

## Result

This packet proves a real Parseval subcase of the paper's closing real/quaternionic analogue question.

Let
\[
\operatorname{PF}^{\mathbb R}_d(r)=\{F\in\mathbb R^{d\times N}: FF^T=I_d,\ \|f_i\|^2=r_i\}
\]
with \(r_i\in(0,1)\) and \(\sum_i r_i=d\). If \(\operatorname{PF}^{\mathbb R}_d(r)\) is a connected smooth real-analytic manifold, then its full-spark locus is nonempty, open, dense, and has full Hausdorff measure.

Combined with Mare's connectedness criteria for real Schur-Horn fibers and the standard smoothness criterion for fixed-operator frame varieties, this gives concrete nonconstant real prescribed-norm Parseval families where full-spark frames are generic.

## Scope

This is not the full real analogue of Needham--Shonkwiler Theorem 1.1. It treats the fixed-operator Parseval case \(\lambda=(1,\ldots,1)\), assumes smoothness and connectedness (verified for example in the generic paired families stated in the packet), and does not address quaternionic measures.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2110.11295.
- `supporting_paper_2309.11596.pdf`: Mare, *Connectivity properties of the Schur-Horn map for real Grassmannians*.
- `figures/open_problem_crop.png`: source discussion excerpt.
