# Counterexample packet: divergent orthoprojections in a strictly convex space

status: candidate_counterexample_likely_valid

Source: Catalin Badea and Yuri I. Lyubich, "Geometric, spectral and
asymptotic properties of averaged products of projections in Banach spaces",
arXiv:1006.2052.

Target: In the discussion after the `ell_infty^2` divergent example on page 6,
the authors ask whether there is an example of divergence of iterates of a
product of orthoprojections in a strictly convex space.

Result: Yes, in a real strictly convex Banach space.  The packet constructs a
strictly convex renorming of an `ell_infty`-sum of two-dimensional blocks and
two norm-one projections `P,Q` such that `(PQ)^n` is not strongly convergent.

Method: For each `rho < 1`, build a two-dimensional strictly convex block with
two contractive rank-one projections whose product has eigenvalue `-rho^2`.
Let `rho_n -> 1` and take a weighted strictly convex norm on the `ell_infty`
sum of these blocks.  The block products individually converge, but their
eigenvalues approach `-1`; on the vector consisting of the block eigenvectors,
the even and odd powers of `PQ` stay separated in norm.

Files:
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: rendered copy of the source paper from the local arXiv
  source.
- `figures/open_question_crop.png`: crop of the source paragraph containing
  the open question.

Novelty check: local run indexes and prior archive notes were searched for
arXiv:1006.2052 and projection/orthoprojection/strictly-convex divergence
keywords.  A bounded web exact-phrase search for the source question and
strictly convex orthoprojections did not surface a known answer.  Novelty
confidence is moderate pending human review.

Human review recommendation: verify the finite-dimensional convex-body block
lemma and the strict convexity of the weighted `ell_infty`-sum norm.  If the
source question is interpreted as requiring complex-linear projections on a
complex Banach space, also check the balanced complex variant noted in the
packet.
