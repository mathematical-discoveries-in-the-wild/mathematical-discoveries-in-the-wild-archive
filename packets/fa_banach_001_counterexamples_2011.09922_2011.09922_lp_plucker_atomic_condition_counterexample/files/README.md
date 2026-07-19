# A two-plane counterexample to the atomic condition for a Plucker ell-p integrand

Status: `candidate_counterexample_likely_valid`

Source: Antonio De Rosa and Riccardo Tione, *Regularity for graphs with bounded
anisotropic mean curvature*, arXiv:2011.09922v2, Remark 6.4 (page 26).

## Result

The source reports numerical evidence that every integrand on `G(4,2)` induced
by the ell-p norm of the six Plucker coordinates satisfies the scalar atomic
condition, hence the atomic condition.  This universal claim is false.

For any `a,b>0` with `a+b=1` and `a!=b`, put `t=sqrt(ab/2)` and consider the
unit simple bivectors

```text
x=(a,-t,t,t,t,-b),
y=(b,-t,t,t,t,-a).
```

For the equal two-atom measure on their two distinct planes, the averaged
first-variation matrix has eigenvalues

```text
d_p-sqrt(2)c_p, d_p-sqrt(2)c_p,
d_p+sqrt(2)c_p, d_p+sqrt(2)c_p,
```

up to a common positive normalization.  The smaller eigenvalue has a negative
limit as `p` decreases to `1` and is positive at `p=2`.  Hence it vanishes at
some `p_0 in (1,2)`.  At that exponent the averaged matrix has a
two-dimensional kernel although the measure is not Dirac, violating (AC2).

For `a=4/5`, `b=1/5`, numerical bisection gives
`p_0 approximately 1.1593840621`; the proof uses only continuity and
strict endpoint signs.

## Scope

This is a complete counterexample to the all-exponent atomic-condition claim
suggested in Remark 6.4.  It does not classify which individual exponents
satisfy (AC), and it does not affect Theorem 6.1, which proves only (AC1) for
all `p in (1,infinity)`.

## Packet contents

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained packet source.
- `verification.md`: independent algebra and scope audit.
- `code/verify_counterexample.py`: symbolic matrix and numerical root check.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Remark 6.4 from source page 26.

Human review should focus on the transcription of the source's coordinate
formula for `B_G` and on the two-eigenvalue calculation for the averaged
matrix.  Once those are confirmed, the intermediate-value argument is
elementary.
