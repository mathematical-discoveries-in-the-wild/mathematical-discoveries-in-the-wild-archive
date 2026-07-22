# Counterexample: Sublinear Near-Additivity Does Not Force Asymptotic Additivity

Status: `candidate_counterexample_likely_valid`

Source: Raimundo Briceño and Godofredo Iommi, *Ergodic theorems for set maps
under weak forms of additivity*, arXiv:2501.14581v1. Question 5.2 on PDF
page 27 asks whether the summability assumption in Proposition 5.1 can be
weakened to monotonicity of `(C_n)` and `C_n/n -> 0`.

## Claimed contribution

The answer is no, already on the one-point dynamical system. Let

```text
B = exp(4),
h(x) = sin(log(log(x+B))),
f_0 = 0,            f_n(*) = n h(n)  (n >= 1),
C_0 = 0,            C_n = 15 n/log(n+B)  (n >= 1).
```

Then `(C_n)` is positive for `n >= 1`, nondecreasing, subadditive, and
`C_n/n -> 0`. For all nonnegative integers `m,n`,

```text
|f_(n+m) - f_n - f_m o T^n| <= C_n + C_m.
```

Nevertheless `f_n/n = sin(log(log(n+B)))` has limsup `1` and liminf `-1`.
On a one-point system every additive realization is `S_n g = n g`, so

```text
inf_g limsup_n |f_n-S_n g|/n = 1,
```

and the sequence is not asymptotically additive.

## Proof mechanism

The phase `log log(x+B)` oscillates forever but has derivative

```text
1/((x+B) log(x+B)).
```

For `1 <= m <= n`, split the additive defect as

```text
n |h(n+m)-h(n)| + m |h(n+m)-h(m)|.
```

The first term is at most `n/log(n+B)`. For the second, the cases
`m <= sqrt(n)` and `m > sqrt(n)` give bounds `14 n/log(n+B)` and
`2 n/log(n+B)`, respectively. Thus the total is at most `C_n`.

## Verification and novelty

Run the finite-range checker with

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2501.14581_sublinear_near_additivity_counterexample/code/verify_counterexample.py
```

It exhaustively checks every pair `1 <= m <= n <= 800`, checks selected
logarithmic-scale pairs up to `n=10^12`, and checks monotonicity and
subadditivity over finite ranges. These computations are sanity checks only;
the packet contains the uniform proof.

The bounded novelty check on 2026-07-22 covered the four lightweight run
indexes, arXiv:2501.14581, the exact wording of Question 5.2, and searches for
`C_n + C_m`, `asymptotically additive`, `sublinear nearly additive`, and close
variants. No separate paper explicitly resolving Question 5.2 was found. The
source itself mentions Füredi's negative result only for the analogous
one-sided nearly-subadditive scalar problem. Novelty is not certified beyond
this bounded search.

Human review recommendation: send to an ergodic-theory or regular-variation
reviewer. The main audit point is the two-regime estimate for the additive
defect; all other reductions are immediate on the one-point system.

Files:

- `source_paper.pdf`: arXiv:2501.14581v1.
- `figures/open_problem_crop.png`: Question 5.2 on source PDF page 27.
- `main.tex`, `solution_packet.pdf`: complete counterexample packet.
- `verification_report.md`: proof audit.
- `code/verify_counterexample.py`: finite-range numerical checks.
