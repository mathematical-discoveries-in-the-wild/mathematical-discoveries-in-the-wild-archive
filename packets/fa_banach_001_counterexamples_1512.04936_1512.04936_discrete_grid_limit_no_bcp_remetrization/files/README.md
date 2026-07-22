# Counterexample Packet: No Bi-Lipschitz BCP Remetrization

Run: `fa_banach_001`

Status: `counterexample_likely_valid`

## Source

- Enrico Le Donne and Séverine Rigot, *Besicovitch Covering Property on graded groups and applications to measure differentiation*, arXiv:1512.04936v1.
- Local PDF: `source_paper.pdf`.
- Target location: Section 8.3, printed page 55.

## Target

The source asks for an example of a finite-topological-dimensional metric
space `(X,d)` for which no distance bi-Lipschitz equivalent to `d` satisfies
the Besicovitch Covering Property (BCP).

## Result

Such an example exists even with `X` countable, bounded, complete, and
topologically discrete (hence of Lebesgue covering dimension zero).

For every `m,k >= 1`, take a labelled copy of the dyadic grid

```text
D_(m,k) = {0, 2^(-k), ..., 1}^m
```

with its sup metric. Put all distinct components at distance `3`. The resulting
metric space admits no bi-Lipschitz equivalent BCP metric.

## Proof Intuition

A hypothetical remetrization has one global bi-Lipschitz constant `L` and one
global BCP multiplicity `Q`. Restrict it to finer and finer grids of the fixed
cube dimension `m=Q+1`. Compactness produces an `L`-bi-Lipschitz limiting
metric on the full cube. WBCP with constant `Q` passes to the limit because
Besicovitch families are controlled by finitely many strict inequalities.
On a compact space, WBCP(`Q`) gives equal-radius open-cover refinements of
multiplicity at most `Q`; hence the limiting cube has covering dimension at
most `Q-1`. This contradicts `dim [0,1]^(Q+1)=Q+1`.

## Verification Notes

- The full space is discrete because every point lies in one finite component;
  shrinking mesh sizes in other labelled components do not create local
  accumulation.
- WBCP restricts to each component: any within-component Besicovitch family is
  still one in the ambient metric.
- The limit metric is obtained from uniformly Lipschitz extensions of the
  restricted distance functions on the dyadic grids.
- The WBCP limit step enlarges each radius by `epsilon`; strict exclusion gaps
  survive and the approximated common point stays in every ball.
- The dimension bound is proved directly by a maximal equal-radius family,
  compactness, and the Lebesgue-number lemma.

## Novelty/Literature Check

On 2026-07-21, the run's four cheap indexes were searched for arXiv:1512.04936
and the central BCP/bi-Lipschitz/topological-dimension terms. Bounded web and
arXiv searches used the exact source sentence and close variants. They found
the source and adjacent BCP literature but no later resolution or the discrete
grid-limit construction. This is a bounded search, not a guarantee of novelty.

## Limitations

The example is deliberately disconnected and non-doubling. The packet does
not settle stronger variants requiring connectedness, geodesicity, local
connectedness, or doubling.

## Files

- `main.tex`: complete proof.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question on printed page 55.
- `code/crop_open_problem.py`: reproducible crop helper.
- `verifier_report.md`: proof audit and verdict.
- `tmp/`: LaTeX and rendering intermediates.

## Human Review Recommendation

Check the compactness/grid-limit lemma first, especially the uniform extension
and `+epsilon` transfer of WBCP. Then verify the hereditary restriction to a
component. Those are the only nonstandard steps.
