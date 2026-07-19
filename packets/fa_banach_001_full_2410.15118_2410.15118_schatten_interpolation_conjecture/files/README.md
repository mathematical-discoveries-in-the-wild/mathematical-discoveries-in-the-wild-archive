# Full Solution: Schatten interpolation form of Conjecture 3.3

Run: `fa_banach_001`

Status: `full_solution_likely_valid`

Source target: Stanislaw J. Szarek and Pawel Wolff, *Radii of Euclidean
sections of ell_p-balls*, arXiv:2410.15118.

## Result

This packet proves Conjecture 3.3(b) from the source paper. For
`1 < p < 2`, put

```text
r = 2p/(2-p).
```

Then every finite real or complex matrix `B`, viewed as an operator
`ell_2 -> ell_p`, satisfies

```text
||B : ell_2 -> ell_p|| >= ||B||_{S_r}.
```

The source states that Conjecture 3.3(a), (b), and (c) are formally equivalent,
and that confirming any one of them yields the sharp `c = 1` version of the
radius lower bound

```text
lambda' >= d^(1/p - 1/2)
```

for `1 < p < 2`.

## Proof Mechanism

Dualize to the equivalent assertion that if `q = p' > 2` and
`1/r = 1/2 - 1/q`, then every matrix `C : ell_q -> ell_2` satisfies

```text
||C||_{S_r} <= ||C : ell_q -> ell_2||.
```

This is exactly the interpolation line between two endpoint facts:

- at `q = 2`, the assertion is `||C||_{S_infty} = ||C : ell_2 -> ell_2||`;
- at `q = infinity`, Rademacher averaging gives
  `||C||_{S_2} <= ||C : ell_infty -> ell_2||`.

Complex interpolation of the identity map between these operator ideals gives
the full range `2 < q < infinity`.

## Verification Notes

- Cheap run indexes were searched for `2410.15118`, the source title, the
  `pi_{r,2}(i_{p2})` conjecture, and the `ell_2 -> ell_p` Schatten
  formulation. No exact prior packet or attempt was found.
- Bounded web/literature searches for the exact phrases
  `pi_{r,2}(i_{p2})`, `Radii of Euclidean sections` with `Schatten`, and
  `ell_2 ell_p Schatten norm 2p/(2-p)` found no separate later answer.
- Random finite-dimensional numerical probes were run first; apparent ratios
  above one were traced to under-optimization of the nonconvex `ell_2 -> ell_p`
  norm. Exact two-row angular refinement gave no contradiction.
- The proof itself is independent of the numerical probe.

## Files

- `README.md` - this summary.
- `main.tex` - proof-packet source.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - rendered source paper.
- `figures/open_problem_crop.png` - crop of Conjecture 3.3 in the source.
- `code/finite_probe.py` - optional numerical sanity probe.

## Human Review Recommendation

Check the interpolation step:

```text
[ L(ell_2^n, ell_2^m), L(ell_infty^n, ell_2^m) ]_theta
  = L(ell_q^n, ell_2^m)
```

and

```text
[ S_infty, S_2 ]_theta = S_r,
```

with `1/q = (1-theta)/2` and `1/r = theta/2`. These are standard finite
dimensional interpolation identities; once accepted, the proof is a direct
contractive interpolation argument.
