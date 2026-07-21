# Sharp constant for rank-one coordinate maps and frame rescaling

Status: `full_result_likely_valid`; `sharp_constant_4_over_pi`; `human_review_recommended`.

Source: Anton Tselishchev, *Rescaling of unconditional Schauder frames in
Hilbert spaces and completely bounded maps*, arXiv:2508.02802. Remark 2.6(1)
on PDF page 5 asks for the best constant in Theorems 2.2 and 2.3.

## Result

The optimal complex constant in both formulations is exactly

```text
K = 4/pi.
```

Thus every finite-dimensional map `Phi: ell_infinity^n -> B(H)` whose
coordinate images have rank at most one satisfies

```text
||Phi||_cb <= (4/pi) ||Phi||,
```

and no smaller universal constant is possible. Equivalently, the optimal
universal Bessel bound in the nonzero finite multiplier-rescaling theorem is
`(4/pi)C`. The optimal real rescaling constant is `pi/2`.

The upper bound evaluates the Gaussian refinement suggested in the source.
The lower bound is new to the checked literature: take many independent pairs
of Haar unit vectors in dimension `d`. Their scalar multiplier norm converges
uniformly to the square of the first absolute Haar-coordinate moment, while a
`d`-level amplification has norm at least `1/d`. The ratio tends to `4/pi`.
The same examples force the rescaling lower bound by a trace and
Cauchy-Schwarz argument.

## Novelty boundary

The source proves the theorem with `K=2`, explicitly says Gaussians give a
better constant, and leaves the best constant as an interesting problem.
Searches of the run indexes, local arXiv source corpus, exact web phrases,
forward references to arXiv:2508.02802, and the little-Grothendieck literature
found no prior statement of the sharp `4/pi` constant for these rank-one map
or frame-rescaling formulations. The construction uses a classical sharp
Gaussian/Haar mechanism, so the novelty assessment is strong for the stated
problem but still requires expert literature review.

## Files

- `main.tex`: self-contained sharp upper and lower bounds.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper containing the open problem.
- `figures/open_problem_crop.png`: source screenshot of Remark 2.6(1).
- `code/check_haar_constants.py`: exact-formula numerical sanity check.

