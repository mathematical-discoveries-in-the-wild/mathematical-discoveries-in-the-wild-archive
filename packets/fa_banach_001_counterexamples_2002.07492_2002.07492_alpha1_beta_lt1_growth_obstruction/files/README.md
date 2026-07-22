# Counterexample: the alpha=1, beta<1 kernel grows

Status: `counterexample_likely_valid`

Source: Michael Ruzhansky and Berikbol T. Torebek, *Van der Corput
lemmas for Mittag-Leffler functions. I*, arXiv:2002.07492. Open Question 1
on PDF page 28 asks whether van der Corput-type estimates are valid for
`I_{alpha,beta}(lambda)` when `alpha=1` and `beta<1`.

## Claimed contribution

For every `0<beta<1`, on the principal branch,

```text
E_{1,beta}(it)
  = (it)^(1-beta) exp(it)
    + (1-beta)/(Gamma(beta) it) + O(t^(-2)).
```

Consequently, take `[a,b]=[0,1]`, `phi(x)=1`, and `psi(x)=1`. These satisfy
the measurable nonvanishing-phase and `L1`-amplitude hypotheses of the
source paper's immediately preceding `alpha=1, beta>1` theorem, but

```text
I_{1,beta}(lambda) = E_{1,beta}(i lambda),
|I_{1,beta}(lambda)| / lambda^(1-beta) -> 1.
```

Thus there is no decay estimate in that class. More sharply, the `L1` operator
norm for the constant phase grows exactly on the scale
`lambda^(1-beta)`. The packet also proves that this is the sharp uniform scale
when `0<m<=|phi|<=M`, and gives the asymptotic reduction

```text
I_{1,beta}(lambda)
  = lambda^(1-beta) integral exp(i lambda phi(x))
      (i phi(x))^(1-beta) psi(x) dx
    + O(lambda^(-1) ||psi||_1).
```

This answers the source question negatively under the natural interpretation
suggested by its preceding theorem: an extension retaining van der
Corput-type decay for arbitrary nonvanishing measurable phases.

## Proof mechanism

The defining series gives

```text
E_{1,beta}(z) = 1/Gamma(beta) + z E_{1,beta+1}(z).
```

A beta-integral for the shifted function yields

```text
E_{1,beta+1}(z)
  = z^(-beta) exp(z) gamma(beta,z)/Gamma(beta).
```

Writing the lower incomplete gamma function as
`gamma(beta,z)=Gamma(beta)-Gamma(beta,z)` and using the standard large-`z`
upper incomplete-gamma expansion on the imaginary ray gives the displayed
kernel asymptotic. Its leading term has modulus `t^(1-beta)` and cannot be
cancelled by the `O(t^(-1))` remainder.

## Verification

The proof is analytic. The reusable numerical smoke check evaluates the exact
incomplete-gamma formula at beta `0.2`, `0.5`, and `0.8`, for `t=30,100,300`:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2002.07492_alpha1_beta_lt1_growth_obstruction/code/verify_asymptotic.py
```

All nine checks pass. They confirm the leading modulus ratio tends to one and
the first error coefficient tends to `(1-beta)/Gamma(beta)`; they are not part
of the proof. See `VERIFIER_REPORT.md` for the proof audit.

## Novelty and scope

The bounded novelty search on 21 July 2026 covered the run's registry,
solution, attempt, and proof-gap indexes; exact searches for arXiv:2002.07492,
its title, the verbatim open question, `E_{1,beta}` with `beta<1`, and the
authors plus possible later parts. It checked the full local sources of Part I
and arXiv:2005.04546, Part II. Part II treats `beta>1` and `beta=1`, not
`beta<1`. No explicit later answer was found. This supports but cannot certify
novelty.

The result does not say that every derivative-restricted oscillatory estimate
is impossible. The asymptotic reduction above shows that such estimates reduce
to classical oscillatory estimates with a prefactor `lambda^(1-beta)`. The
human reviewer should confirm that the intended reading of the source's broad
question is the nonvanishing-phase generality of the immediately preceding
theorem.

Human review recommendation: send to a special-functions or oscillatory-
integrals reviewer. The main mathematical audit points are the branch choice
in the incomplete-gamma identity and the scope interpretation of “van der
Corput-type estimates.”

Files:

- `source_paper.pdf`: arXiv:2002.07492.
- `figures/open_problem_crop.png`: source PDF page 28, Open Question 1.
- `main.tex`, `solution_packet.pdf`: full counterexample packet.
- `code/verify_asymptotic.py`: non-proof numerical smoke check.
- `VERIFIER_REPORT.md`: explicit self-verifier report.
