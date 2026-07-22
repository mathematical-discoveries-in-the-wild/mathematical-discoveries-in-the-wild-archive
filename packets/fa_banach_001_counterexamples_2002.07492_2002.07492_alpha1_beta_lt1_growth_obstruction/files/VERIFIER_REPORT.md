# Verifier Report

Verdict: `likely valid`

Reviewer: `agent_lane_01` self-verification. This is not independent human
review.

## Formal audit

1. Reindexing the defining series gives
   `E_{1,beta}(z)=1/Gamma(beta)+z E_{1,beta+1}(z)` exactly.
2. Expanding `exp(zs)` under the beta integral on `[0,1]` gives the exact
   integral representation for `E_{1,beta+1}` term by term. The substitution
   `u=z(1-s)` uses one consistent principal branch on the ray from `0` to
   `z=i t`.
3. DLMF 8.11.2--8.11.3 gives the upper incomplete-gamma expansion with a
   remainder of order `z^(-2)` after two terms. Its sector contains
   `arg z=pi/2`, so the imaginary ray is not a Stokes-boundary exception.
4. Substitution cancels the two constant `1/Gamma(beta)` terms and leaves
   `(1-beta)/(Gamma(beta) z)+O(z^(-2))`. The sign was checked separately by
   direct algebra and by the numerical coefficient test.
5. The leading term at `z=i t` has modulus `t^(1-beta)`, whereas the remainder
   is `O(t^(-1))`. Since `0<beta<1`, the relative error tends to zero.
6. The example `phi=psi=1` on `[0,1]` is real, bounded, integrable, and has
   `inf|phi|=1`; it satisfies the class used by the source's preceding
   `alpha=1, beta>1` theorem.

## Computational smoke check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2002.07492_alpha1_beta_lt1_growth_obstruction/code/verify_asymptotic.py
```

Scope: nine points, beta in `{0.2,0.5,0.8}` and `t` in `{30,100,300}`. The
script evaluates the exact lower-incomplete-gamma representation at 70-digit
precision. All assertions pass. This is only a contradiction/sanity check,
not proof.

## Remaining human-review focus

- Confirm the intended scope of the source's phrase “van der Corput-type
  estimates.” The counterexample conclusively rules out decay in the broad
  nonvanishing measurable-phase class of the adjacent theorem; it does not
  rule out derivative-restricted estimates with beta-dependent rates.
- Check that the DLMF sector convention used for the upper incomplete gamma
  agrees with the principal powers used in the packet.
