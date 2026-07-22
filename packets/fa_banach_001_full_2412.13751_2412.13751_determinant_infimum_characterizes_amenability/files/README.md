# The determinant infimum characterizes amenability

Status: `candidate_full_solution_likely_valid` for arXiv:2412.13751,
Problem 3.7 (PDF page 36).

Tim Austin asks whether a countable group `Gamma` must be amenable if

```text
Delta(phi_ac) = inf_F (det phi[F])^(1/|F|)
```

whenever `phi = tau(a^*(.)a)` for `a` in the complex group ring.  The answer
is yes.

## Proof mechanism

For a bounded positive invertible operator `B` and a finite-rank projection
`P`, the resolvent formula for `log` and a Schur complement give the
quantitative compression inequality

```text
Tr log(PBP) - Tr(P log(B) P)
    >= ||(1-P)BP||_HS^2 / (2 ||B||^2).
```

Given a finite symmetric set `S` in `Gamma`, take

```text
H = sum_(s in S) R_s,       a = 1 + t H,
```

with `t |S| < 1`, where `R_s` is right translation.  Then `a` is positive
and invertible.  For the coefficient in the problem, `phi[F]` is the
coordinate compression of `B=a^2`.  A Sylvester-block estimate transfers the
off-diagonal leakage of `a^2` to that of `H`.  The latter is exactly the
directed `S`-boundary:

```text
||(1-P_F) H P_F||_HS^2 = sum_(s in S) |F s \ F|.
```

Consequently the logarithmic determinant gap has the explicit lower bound

```text
log((det phi[F])^(1/|F|) / Delta(phi))
 >= 2 t^2 (1-t|S|)^2/(1+t|S|)^4
      * (1/|F|) sum_(s in S) |F s \ F|.
```

If the determinant infimum is equality for this `a`, the right side has
infimum zero.  Applying this to every finite symmetric `S` is precisely the
Folner criterion.

## Evidence

- `solution_packet.pdf`: full proof and quantitative strengthening.
- `source_paper.pdf`: arXiv:2412.13751v4.
- `figures/open_problem_crop.png`: Problem 3.7 and equation (3.8).
- `code/compression_gap_probe.py`: random finite-matrix and finite-translation
  checks of the two quantitative inequalities.

## Novelty status

The run indexes and local source corpus contained no resolution of this exact
problem.  Bounded exact-phrase, title/citation, and arXiv searches on
2026-07-21 found the current v4 source, in which the statement remains
Problem 3.7, but no later paper claiming an answer.  Novelty confidence is
moderate rather than definitive.

## Human review recommendation

The main points to audit are the normalization
`Delta(phi) = Delta(R_a)^2`, the identification of `phi[F]` with the
compression of `R_a^2`, and the resolvent/Schur-complement inequality.  These
are written independently in the packet so that no equality convention is
implicit.

