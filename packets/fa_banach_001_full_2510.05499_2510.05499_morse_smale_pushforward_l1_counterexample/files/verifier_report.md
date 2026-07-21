# Verifier report

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2510.05499_morse_smale_pushforward_L1_counterexample/code/verify_adjoint_tower.py
```

Output on 2026-07-21:

```text
PASS: det(diag(1/2,4)) = 2 and the stable adjoint multiplier is 1.
PASS: N=  2, ||psi_N||=1, adjoint error=1/2.
PASS: N=  3, ||psi_N||=1, adjoint error=1/3.
PASS: N=  5, ||psi_N||=1, adjoint error=1/5.
PASS: N= 10, ||psi_N||=1, adjoint error=1/10.
PASS: N= 50, ||psi_N||=1, adjoint error=1/50.
PASS: N=100, ||psi_N||=1, adjoint error=1/100.
PASS: the exact tower error tends to zero while the dual norm stays one.
```

All calculations use `fractions.Fraction`. The check confirms the exact
Jacobian cancellation and the adjacent-coefficient norm bound for triangular
towers. It does not replace the geometric realization or the functional-
analytic surjectivity argument proved in `main.tex`.
