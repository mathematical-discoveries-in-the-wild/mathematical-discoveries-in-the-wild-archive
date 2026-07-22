# Full Solution Packet: Non-Self-Adjoint Semiclassical Sobolev Regularity

Run: `fa_banach_001`

Status: `full_solution_likely_valid`

## Source

- Laurent Lafleche, *Optimal Semiclassical Regularity of Projection Operators
  and Strong Weyl Law*, arXiv:2302.04816v3.
- Local PDF: `source_paper.pdf`.
- Relevant location: page 7, Figure 2 and its caption; the underlying statement
  is Theorem 1 on page 5.

## Target

For non-self-adjoint idempotents, Theorem 1 proves the forbidden Sobolev
regularity only in part of the `(s,1/p)` diagram unless an extra uniform
`L^{2+epsilon}` bound is assumed. Figure 2 conjectures that the same
trace-only obstruction holds in the remaining top-right region.

## Result

The conjecture is true. If `P_h^2=P_h`, `h^d Tr(P_h)=1`, `p>1`, and
`0<s<=1` with `s>=1/p`, then

```text
||P_h||_{dot W^{s,p}} -> infinity as h -> 0,
```

without self-adjointness and without any uniform `L^{2+epsilon}` hypothesis.
For `0<s<1`, the same range-projection reduction also removes the extra
hypothesis from the source's Besov nonregularity result.

## Proof Intuition

Let `Q_h` be the orthogonal projection onto `Ran(P_h)`. It has exactly the
same rank and normalized trace as `P_h`. The key geometric fact is that, for
any two idempotents `P_0,P_1` and the orthogonal projections `Q_0,Q_1` onto
their ranges,

```text
||Q_1-Q_0||_{S_p} <= 2^{1/p} ||P_1-P_0||_{S_p}.
```

Indeed, `P_1x` is one particular approximation to `x` from `Ran(P_1)`, while
`Q_1x` is the best approximation. Applying this to every Weyl translation
shows that the fractional Sobolev seminorm of `Q_h` is controlled by that of
`P_h`. The source's already-proved self-adjoint theorem for `Q_h` therefore
forces divergence for `P_h`. At order one, the same comparison is made on the
off-diagonal block of each commutator.

## Verification Notes

- The range-projection lemma is proved by positive-operator order and the
  exact two-projection identity for Schatten norms.
- Trace-class idempotents are finite-rank, and their trace equals their rank,
  so `Q_h` satisfies the source theorem's normalization.
- The order-one argument uses the lower-left block of `[A,P_h]` relative to
  `Ran(P_h)`, avoiding any condition-number estimate for the oblique
  projection.
- `code/check_projection_inequality.py` tested both key inequalities on 3,500
  random complex cases, including strongly oblique idempotents and Schatten
  exponents `1, 1.5, 2, 3, infinity`.

## Novelty/Literature Check

On 2026-07-21, the run registry, solution, attempt, and proof-gap indexes were
searched for arXiv:2302.04816, the exact title, and the core
non-self-adjoint/Sobolev terminology. Web searches for the exact paper title,
the Figure 2 caption, the conjecture sentence, and combinations of Lafleche,
non-self-adjoint idempotents, trace condition, and quantum Sobolev regularity
found the source and adjacent quantum Sobolev work, but no later paper claiming
this extension. This is a bounded search, not a guarantee of novelty.

## Limitations

The packet settles the Sobolev conjecture stated in Figure 2. It also proves
the Besov conclusion for `0<s<1`, which includes every critical case
`s=1/p` with `p>1`. It does not claim the separate second-difference Besov
endpoint `s=1, p=1`, nor a new proof of the source's self-adjoint theorem.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page 7, Figure 2 and full caption.
- `code/crop_open_problem.py`: reproducible crop helper.
- `code/check_projection_inequality.py`: numerical regression check.
- `verifier_report.md`: explicit proof audit and verifier verdict.
- `tmp/`: LaTeX and rendering intermediates.

## Human Review Recommendation

Check the singular-value comparison in Lemma 1 and the domain/compression step
for the unbounded position and momentum generators at `s=1`. These are the
only substantive transfer steps; all remaining nonregularity is exactly the
self-adjoint result already proved in the source.
