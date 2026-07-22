# Full-result packet: the relative p-Wasserstein distance is a metric

Status: `candidate_full_solution_likely_valid`

Source: Peter Bubenik and Alex Elchesen, *Relative Optimal Transport*,
arXiv:2411.05678v3 (6 April 2026).

## Result

For every complete separable metric pair `(X,d,A)` with nonempty closed
reservoir `A`, every `1 <= p < infinity`, and all p-finite tight relative
measures `mu,nu`, the packet proves

`W_p(mu,nu) = hat W_p(mu,nu)`

and

`W_p(mu,nu) = 0  =>  mu = nu`.

The source had proved only `hat W_p <= W_p` in general, equality for `p=1`,
and that `W_p` is a pseudometric. It explicitly asks both remaining questions
for `p>1` on PDF pages 31 and 32. The result therefore resolves both questions
and upgrades the source pseudometric to a metric for every finite `p >= 1`.

## Proof mechanism

For equality, start from an arbitrary relative coupling. Collapse only points
within distance `delta` of `A` to a fixed reservoir point, then trivially
restore the two collapsed marginal tails. These are exactly the structured
couplings used to define `W_p`. Their costs converge to the original cost by
dominated convergence, with integrable dominator

`d_A(x)^p + d_A(y)^p`.

For definiteness, let `K` be compact and a positive distance from `A`. If a
coupling transports mass from `K` outside its closed `r`-neighborhood, that
mass pays relative cost greater than `r`. Arbitrarily small transport cost
gives `mu(K) <= nu(K_r)`. The neighborhood has finite mass because it remains
a positive distance from `A`; continuity from above gives
`mu(K) <= nu(K)`. Symmetry and tightness force equality of the two relative
measures.

## Packet contents

- `main.tex`: self-contained proof packet with definitions, proof intuition,
  theorem, proof, verification report, limitations, and bounded novelty check.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: current arXiv source PDF.
- `figures/open_problem_crop.png`: readable source crops containing both open
  questions.
- `tmp/`: LaTeX intermediates and rendered-page QA images.

No computation is used in the proof.

## Verification focus

1. Check the exact structured-coupling cost identity after retraction and
   trivial extension.
2. Check that dominated convergence is valid for possibly infinite-total-mass
   couplings; the displayed marginal-moment dominator is integrable.
3. Check representative-independence of marginal identities on sets disjoint
   from `A`.
4. Check the compact-neighborhood limiting argument. It uses finite mass, not
   compactness of the neighborhood, and does not assume the space is proper.

Current verdict: full solution likely valid. Human review is recommended,
especially on items 1 and 3.

## Novelty check

The cheap run indexes were searched for `2411.05678`, the title, relative
Wasserstein terminology, equality of the coupling formulas, and identity of
indiscernibles, with no overlap. A bounded web/arXiv search on 2026-07-21 used
the title, authors, exact open-question phrases, and close variants. It found
the source and adjacent work but no later settlement. The current v3 source
still states both questions as open. This supports, but does not prove,
novelty.
