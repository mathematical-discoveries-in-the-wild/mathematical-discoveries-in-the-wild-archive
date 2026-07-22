# The central measure of the unit interval is Lebesgue measure

Status: `candidate_full_solution_likely_valid` for arXiv:1105.5706.

This packet answers the question on PDF page 7 of Piotr Niemiec's *Central
points and measures and dense subsets of compact metric spaces*:

```text
Is μ_[0,1] the Lebesgue measure?
```

The answer is yes.

## Proof mechanism

Identify probability measures on `[0,1]`, with the Kantorovich metric, with
their quantile functions in `L^1[0,1]`.

1. The first Chebyshev center consists exactly of the measures with mean
   `1/2`.
2. On their quantile functions define

   ```text
   (Dq)(t) = Lebesgue measure of {u : q(u) <= t}.
   ```

   The sublevel sets of monotone functions are initial intervals.  Fubini's
   theorem therefore shows that `D` is an involutive `L^1`-isometry.  It sends
   the mean of `q` to `1 - mean(q)`, so it preserves the first center.
3. The generalized Chebyshev center of a compact convex metric set is fixed
   by every isometry.  Hence the desired central quantile is fixed by `D`.
4. The only fixed point of `D` is `q(t)=t`.  This is the quantile function of
   Lebesgue measure.

The key new move is to use an isometry of the *first Chebyshev center* that
does not come merely from reflecting the underlying interval.

## Evidence

- `solution_packet.pdf`: complete proof.
- `source_paper.pdf`: arXiv:1105.5706.
- `figures/open_problem_crop.png`: source question and surrounding context.
- `code/quantile_inverse_probe.py`: finite-grid checks of the inverse-CDF
  isometry and mean-complement identities.

## Novelty status

Cheap run indexes and the source-probed corpus had no prior result for this
question.  Bounded exact-phrase and title/citation web searches on 2026-07-21
found the original arXiv/published paper and self-citations, but no later
answer.  Novelty confidence is moderate rather than definitive.

## Human review recommendation

Check the generalized-inverse conventions in Lemma 3 (all identities are
modulo null sets), and the shift from the central point of the whole quantile
space to the central point of its first Chebyshev center.  These are the two
places where a convention error would matter.

