# Frame structure for the wedge Stolarsky energy

**Status:** candidate partial solution, likely valid, subject to human review.

Bilyk and Lacey ask whether minimizers of their wedge Stolarsky energy admit a
geometric or functional-analytic characterization. Writing the normalized
geodesic distance as `arccos(<x,y>)/pi` turns the potential into

\[
  \left(\frac12-d(x,y)\right)^2
  =\frac1{\pi^2}\arcsin^2\!\left(\langle x,y\rangle\right).
\]

The function `Phi(s)=arcsin(sqrt(s))^2` is strictly increasing and strictly
convex. Combining Jensen's inequality with the Welch frame-potential bound
gives a sharp energy bound. Equality holds exactly for real equiangular tight
frames whenever `N>d+1`.

Consequences:

- For `N<=d+1`, the minimizers are exactly orthonormal systems.
- For `N=d+2`, the minimizers are exactly regular simplices, up to an
  orthogonal transformation and independent sign changes.
- For every `(N,d+1)` admitting a real equiangular tight frame, the ETFs are
  exactly the global minimizers.
- At the first non-ETF pair, five vectors in `R^3`, no global minimizer is a
  unit-norm tight frame. Naimark complementation and universal optimality of
  the regular pentagon give the exact minimum among tight frames, and an
  explicit cyclic deformation has strictly lower energy.
- Within the cyclic five-vector family, the unique optimizer is
  `q*=0.314800327343...`, with energy `1.620843159568...`; it is non-tight.

The original general problem remains open when `N>d+2` and no real ETF exists.
In particular, the packet does not prove that the cyclic five-vector optimizer
is the unrestricted global optimizer; it proves globally that every optimizer
for that parameter pair must be non-tight.

## Files

- `solution_packet.pdf`: complete partial-result proof packet.
- `source_paper.pdf`: arXiv:1511.08452v4.
- `figures/open_problem_crop.png`: Theorem 1.23 and the full future-work
  question from source PDF page 9.
- `code/verify_wedge_energy.py`: numerical sanity checks for orthonormal and
  simplex configurations, 60,000 random configurations, and the cyclic
  descent theorem.
- `code/explore_no_etf.py`: 250 seeded unconstrained optimizations for the
  first non-ETF case; all converged to the cyclic numerical candidate.
- `main.tex`: packet source; build and rendered-page intermediates are in
  `tmp/`.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python code/verify_wedge_energy.py
```

The numerical checks are not part of the proof. The main verifier checks the
exact formulas for ambient dimensions 2, 3, and 4, finds no random violation
of the ETF bound, and reproduces the cyclic derivative and scalar optimum.

## Novelty and review focus

Run indexes and targeted arXiv/web searches through 2026-07-19 used the paper
title, arXiv id, `arcsin squared frame potential`, `wedge energy`,
`equiangular tight frame`, `five points real projective plane`, and
`pentagonal frame energy`. They found the source, general ETF/frame-potential
literature, and Cohn--Kumar universal optimality, but no explicit application
to the wedge energy or the non-tightness obstruction. Novelty confidence is
modest because the proofs combine standard frame and energy bounds.

Human review should check strict convexity at the endpoints, the equality
conditions in the frame-potential and Jensen steps, the Naimark-complement
normalization, applicability of regular-pentagon universal optimality to the
doubled-angle potential, and the analytic sign of the descent derivative.

Ledger: `runs/fa_banach_001/ledger/results/1511.08452_wedge_energy_etf_minimizers.json`.
