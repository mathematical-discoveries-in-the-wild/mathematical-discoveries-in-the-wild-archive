# Counterexample: Resolvent Eventually Positive Does Not Force Semigroup Eventually Positive

Status: `candidate_counterexample_likely_valid`

Source paper: Daniel Daners, Jochen Glueck, and James B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294v2.

Target: Section 10, Open problems, item (d). The source asks whether, if the spectral bound `s(A)` is a dominant spectral value and the resolvent is individually eventually positive at `s(A)`, it follows, perhaps under additional regularity assumptions, that the semigroup is individually eventually positive.

## Result

The base implication is false, even in dimension four for a bounded real matrix. In particular, finite dimensionality, boundedness, uniform continuity, and analyticity of the semigroup do not suffice as the missing regularity assumptions.

Let

```text
K = 1/sqrt(3) * [[ 0, -1,  1],
                 [ 1,  0, -1],
                 [-1,  1,  0]]
```

on `R^3`, set `B = -I + 4K`, and set `A = 0 ⊕ B` on `R ⊕ R^3` with the standard coordinate cone.

Then `s(A)=0` is a dominant spectral value, and the resolvent is positive on `(0,1]`:

```text
R(lambda,A) >= 0    for all 0 < lambda <= 1.
```

So the resolvent is individually eventually positive at `s(A)`.

However,

```text
e^{tB} = e^{-t}(P + cos(4t)(I-P) + sin(4t)K),
```

where `P` is the projection onto the span of `(1,1,1)`. At times `t_n=(2n+1)pi/4`, the first coordinate of `e^{t_n B} e_1` is `-e^{-t_n}/3`. Hence the positive vector `(0,e_1)` is sent outside the positive cone for arbitrarily large times, so the semigroup is not individually eventually positive.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: crop of the source open problem.
- `code/verify_counterexample.py`: numerical sanity check for the displayed formulas.

## Verification

The proof is algebraic. The verifier script checks representative values of the resolvent and semigroup:

```bash
conda run --no-capture-output -n sandbox python code/verify_counterexample.py
```

It is not used as evidence in place of the proof; it is only a guard against transcription mistakes.

