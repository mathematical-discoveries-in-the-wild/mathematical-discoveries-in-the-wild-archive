# Counterexample packet: nearly isometric need not imply almost Lipschitz

- Run: `fa_banach_001`
- Source arXiv id: `1503.06089`
- Source paper: Florent Baudier and Gilles Lancien, *Tight embeddability of proper and stable metric spaces*
- Source location: Section 5, Problem 4, PDF page 17
- Packet status: claimed counterexample, likely valid, needs human review
- Packet path: `runs/fa_banach_001/solutions/counterexamples/1503.06089_nearly_isometric_not_almost_lipschitz_bouquet/`

## Source Question

Problem 4 asks:

> Exhibit two metric spaces `X` and `Y` such that `X` nearly isometrically
> embeds into `Y`, but `X` does not almost Lipschitz embed into `Y`.

## Claimed Answer

Let `X = N_0` with its usual metric. Build `Y` as a wedge, at a common
basepoint, of one sublinearly distorted ray for every admissible compression
function `rho` from the source definition of nearly isometric embeddability.
For each `rho`, choose a concave nondecreasing unbounded function `g_rho`
with

```text
g_rho(0)=0,   g_rho(t)=t on [0,1],   rho(t) <= g_rho(t) <= t,
and g_rho(t)/t -> 0.
```

The `rho`-component is `N_0` with metric `g_rho(|m-n|)`. Distances between
different components are measured through the common basepoint.

Then `X` nearly isometrically embeds into `Y`: for a requested compression
`rho`, map `n` to the point `n` in the `rho`-component. However, `Y` contains
no bi-Lipschitz copy of the usual ray `N_0`, because a Lipschitz ray must
eventually stay in a single component, where all distances are sublinear.
Since an almost Lipschitz embedding of `N_0` would give a bi-Lipschitz
embedding by choosing a test function bounded below on `[1,infty)`, `X` does
not almost Lipschitz embed into `Y`.

## Novelty Check

Bounded search on 2026-06-15:

- Local cheap indexes for `1503.06089`, `nearly isometric`, and `almost Lipschitz`
  showed no direct packet or attempt for this source problem.
- Local parsed-source search for `"nearly isometrically embeds" "does not almost Lipschitz"`
  found only the source paper.
- Web searches for exact phrases including `"nearly isometrically embeds" "almost Lipschitz" metric spaces counterexample`,
  `"Exhibit two metric spaces" "nearly isometrically" "almost Lipschitz"`, and
  `site:arxiv.org "almost Lipschitz" "nearly isometric"` returned the source
  paper and no separate answer.

This is therefore recorded as an original run-level counterexample, not a
literature-status packet. Novelty confidence is bounded by those searches.

## Human Review Focus

The main points to verify are:

1. The concave majorant lemma really yields an unbounded sublinear metric
   transform dominating each admissible `rho`.
2. The wedge metric prevents a Lipschitz copy of the ray from switching
   components infinitely often once the image has linearly growing distance
   from the basepoint.
3. The reduction from almost Lipschitz embeddability of `N_0` to a
   bi-Lipschitz embedding uses the correct test function
   `phi(t)=t/2` for `t<=1` and `phi(t)=1/2` for `t>=1`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: rendered source page containing Problem 4.
