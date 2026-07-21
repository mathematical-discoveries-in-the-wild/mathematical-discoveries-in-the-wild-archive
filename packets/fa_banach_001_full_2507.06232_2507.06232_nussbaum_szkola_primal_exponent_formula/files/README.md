# Lifted primal formula for the Petz--Augustin random-coding exponent

Source paper: Hao-Chung Cheng and Po-Chieh Liu, *Error Exponents for
Quantum Packing Problems via An Operator Layer Cake Theorem*,
arXiv:2507.06232v4.

Status: candidate full solution, likely valid, scoped to the finite-alphabet
finite-dimensional setting of the source remark.

## Source Question

Remark 4.4 on PDF page 23 asks whether the Petz--Augustin
constant-composition exponent

```text
sup_{alpha in [1/2,1]} (1-alpha)/alpha
    [I_alpha^Aug(p;N) - R]
```

has a primal-domain expression analogous to the classical
Csiszár--Körner formula. The paper explains that the literal quantum-state
analogue of the classical formula instead dualizes to the log-Euclidean
Rényi divergence and therefore gives the wrong exponent.

## Result

The answer is affirmative after a canonical spectral lift and a time-sharing
convexification.

For each channel state `rho_x` and auxiliary state `sigma`, form their
Nussbaum--Szkoła probability distributions `P_{x,sigma}` and
`Q_{x,sigma}`. For an auxiliary tilted distribution `T_x`, define

```text
A = sum_x p(x) D(T_x || P_{x,sigma}),
B = sum_x p(x) D(T_x || Q_{x,sigma}).
```

Let `K` be the closed convex hull of all such `(A,B)` pairs. Then the exact
Petz--Augustin exponent is

```text
inf_{(A,B) in K} { A + (B-R)_+ }.
```

Every point needed for the infimum is approximable by time-sharing among at
most three primitive data sets. In the commuting case the spectral lift is
classical, `B` splits into mutual information plus an output-divergence term,
and the formula reduces exactly to the Csiszár--Körner expression.

## Proof Mechanism

For `s in [0,1]` and `alpha=1/(1+s)`, the Gibbs variational identity gives

```text
s D_alpha(P||Q)
  = inf_T {D(T||P) + s D(T||Q)}.
```

Nussbaum--Szkoła distributions preserve the Petz Rényi divergence exactly.
After minimizing over the Augustin state `sigma`, the dual exponent becomes

```text
sup_{s in [0,1]} inf_{(A,B) in K} {A+s(B-R)}.
```

Sion minimax interchanges the supremum and infimum; maximizing over `s`
produces `(B-R)_+`. This supplies the missing primal-domain formula.

## Scope and Limitation

The result is exact for finite input alphabets and finite-dimensional output
systems, which is the default setting surrounding Remark 4.4. It is a
classical spectral lift of a genuinely noncommutative exponent. It does not
produce the more restrictive and potentially more desirable formula whose
optimization variables are only alternative quantum channel states, and it
does not claim an infinite-dimensional extension.

## Novelty Check

The bounded search covered all four cheap run indexes and arXiv searches for
the exact phrase `primal-domain expression`, Petz--Augustin/Csiszár--Körner
variants, Nussbaum--Szkoła variational formulas, and constant-composition
Petz exponents. It also inspected the source paper, arXiv:2308.02929 on
Nussbaum--Szkoła `f`-divergences, and arXiv:2601.06492 on algorithms for
Petz--Augustin capacity. No exact lifted primal exponent formula or answer to
Remark 4.4 was found. Novelty remains provisional pending expert search.

## Verification

- The proof is analytic and self-contained modulo standard finite-dimensional
  minimax and convex-hull theorems.
- `code/check_variational_identity.py` checked 400 random noncommuting matrix
  instances of the Petz/Gibbs identity and 100 random classical chain-rule
  instances.
- The code is a sanity check, not a proof.
- The source crop and every page of `solution_packet.pdf` were visually
  inspected.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:2507.06232v4.
- `figures/open_problem_crop.png`: Theorem 4.3 and Remark 4.4 on source page 23.
- `code/check_variational_identity.py`: reusable numerical identity check.

Ledger:
`runs/fa_banach_001/ledger/results/2507.06232_nussbaum_szkola_primal_exponent_formula.json`.

## Human Review Recommendation

Review as a scoped candidate full solution. The key review points are whether
the lifted/time-shared formula meets the intended meaning of `primal-domain`,
the closure endpoint at `s=0`, and the Sion minimax step. Preserve the stated
limitation that a simpler quantum-state-only formula remains open.
