# Counterexample packet: two-point spaces have no metric frame

Status: candidate counterexample, likely valid.

Source: K. Mahesh Krishna, "Metric, Schauder and Operator-Valued Frames",
arXiv:2202.13697. The relevant source passage is on PDF page 68, in Section
2.1, immediately after the definition of metric frame: the source says that
after defining metric frames, "the first question which comes is the
existence" and notes that the Banach-space analogue is known while the metric
case is not.

Result: not every separable metric space admits a metric frame in the sense of
Definition 2.1.10. In fact, any metric space admitting such a frame must be
Lipschitz path connected. Therefore the two-point metric space
`{0,1}` with distance `1` has no metric frame.

Scope note: this does not contradict the weaker Theorem 2.1.17 in the source,
which supplies a BK-space, Lipschitz coordinates, and a set-theoretic
reconstruction map without requiring the reconstruction map to be Lipschitz.
The obstruction applies exactly when the source definition of metric frame is
used, because that definition requires a Lipschitz reconstruction operator
defined on the whole BK-space.

Novelty check: before promotion, the lightweight run indexes were searched for
`2202.13697`, `metric frame`, `Lipschitz retract`, `path connected`, and
related phrases; no prior packet or attempt for this target was found. Web and
arXiv searches on 2026-06-28 for the exact source title and phrases including
`metric frame separable metric`, `metric frame Lipschitz retract`, and `metric
frame path connected` found the source paper, the related arXiv:2011.01870
paper, and adjacent Lipschitz-frame work, but no duplicate of this elementary
path-connectedness obstruction.

Human review recommendation: verify that Definition 2.1.10 indeed requires the
reconstruction map `S: M_d -> M` to be Lipschitz on the entire BK-space. If so,
the connectedness argument is immediate and the two-point example is a genuine
counterexample to the broad metric-frame existence question.

