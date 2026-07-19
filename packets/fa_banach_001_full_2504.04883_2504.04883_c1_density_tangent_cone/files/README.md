# Full Solution Packet: `C^1` Density-Matrix Tangent Cone

Run: `fa_banach_001`

Status: `full_solution_likely_valid`

## Source

- Jihong Cai, Advith Govindarajan, Marius Junge, *How Far do Lindbladians Go?*,
  arXiv:2504.04883v2.
- Local PDF: `source_paper.pdf`.
- Relevant location: page 14, Section 3.1, immediately before Theorem 3.3.

## Target

The source defines the tangent cone of the density-matrix state space using
one-sided `C^2` paths and then says that a possible future direction is
weakening the analytic condition to `C^1`.

## Result

This packet proves that the weakening to `C^1` is valid and changes nothing.
For a finite-dimensional Hilbert space `H`, a density matrix `rho`, and
`s` the support projection of `rho`, define the one-sided `C^1` tangent cone

```text
T^1_rho D(H) = { gamma'(0) : gamma in C^1([0,eps), D(H)), gamma(0)=rho }.
```

Then

```text
T^1_rho D(H)
 = { x : x=x*, tr x=0, (1-s)x(1-s) >= 0 }.
```

This is the same cone stated in the source for `C^2` paths. Consequently the
source's Lindbladian tangent theorem remains true with `C^1` in place of
`C^2`.

## Idea Of The Proof

If `gamma(t)=rho+t x+o(t)` is a `C^1` state-space path, then compressing to the
kernel projection `q=1-s` gives

```text
q gamma(t) q = t qxq + o(t) >= 0.
```

Dividing by `t` and taking the closedness of the positive cone gives `qxq >= 0`.
Self-adjointness and trace zero are immediate.

Conversely, if `x` satisfies that condition, write matrices relative to
`supp rho` and its orthogonal complement:

```text
rho = [ R  0 ],        x = [ A  B ],
      [ 0  0 ]             [ B* C ],
```

where `R>0`, `C>=0`, and `tr A + tr C = 0`. Choose a positive matrix `D` on the
kernel large enough to dominate the Schur-complement term `B*R^{-1}B`, and set

```text
rho_t = [ R+tA-t^2 tr(D)R    tB       ].
        [ tB*                tC+t^2D  ]
```

For small `t>0`, the upper-left block stays positive, the Schur complement is
positive, and the trace remains one. Thus `rho_t` is a `C^2`, hence `C^1`, path
with derivative `x`.

## Verification Notes

- The proof is finite-dimensional and uses only block-matrix positivity via the
  Schur complement.
- The trace correction `-t^2 tr(D)R` is included so the constructed path stays
  in the affine hyperplane `tr rho_t = 1`.
- The open/closed boundary issue at `t=0` is handled by one-sided derivatives
  on `[0,epsilon)`, matching the source's convention.

## Novelty/Literature Check

Searches on 2026-07-18 for exact phrases around `How Far do Lindbladians Go`,
`C^1 tangent cone`, `density matrices tangent cone support projection`,
`positive semidefinite C1 tangent cone`, and `Lindbladian tangent cone` found
the source itself, generic convex-analysis references, and related later-looking
non-Markovianity review text, but no exact answer to the source's `C^1`
weakening direction. The result is standard in spirit from tangent-cone theory,
but this packet records the short direct argument in the notation of the source.

## Limitations

This does not solve the broader lifting/retract problem for selecting
Lindbladians continuously, smoothly, or analytically along arbitrary paths. It
only settles the regularity of the tangent-cone definition itself.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source future-work sentence.
- `tmp/`: render intermediates and source-page PNGs.

## Human Review Recommendation

Check the Schur-complement construction in the reverse inclusion, especially
the trace correction and the choice of `D`. This is the only substantive step.
