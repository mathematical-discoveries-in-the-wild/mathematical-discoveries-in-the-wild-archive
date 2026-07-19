# Literature-Already-Answered: Main Metric X_p Conjectures

Status: `literature_already_answered`

Source target: Assaf Naor and Gideon Schechtman, *Metric X_p inequalities*, arXiv:1408.5819.

Supporting answer: Assaf Naor, *Discrete Riesz transforms and sharp metric X_p inequalities*, arXiv:1601.03332.

## Identification

The source paper arXiv:1408.5819 poses three central conjectures:

- Conjecture 1.5: the metric `X_p` inequality for `L_p` should hold with the sharp scaling parameter `m \gtrsim_p sqrt(n/k)`.
- Conjecture 1.8: for `2 < q < p`, the largest snowflake exponent for embedding `L_q` into `L_p` should be `q/p`.
- Conjecture 1.12: the distortion of the finite grids `[m]_q^n` in `L_p` should be controlled by the better of the Rosenthal and Schoenberg embeddings, equivalently by the phase-transition formula stated in the conjecture.

The later paper arXiv:1601.03332 explicitly says in its introduction that it resolves positively Conjectures 1.5, 1.8, and 1.12 of arXiv:1408.5819.

## Answer

The answer is already in the literature:

- Theorem 1 of arXiv:1601.03332 proves the sharp scaling metric `X_p` inequality for `L_p`: for `p >= 2`, the inequality holds when `m >= sqrt(n/k)`.
- Theorem 2 evaluates the critical snowflake exponent: for `2 < q < p`, the maximal `theta` for which `(L_q, ||x-y||_q^theta)` embeds bi-Lipschitzly into `L_p` is exactly `q/p`.
- Theorem 3 evaluates `c_p([m]_q^n)` up to constants depending only on `p,q`, giving the formula

```tex
c_p([m]_q^n) \asymp_{p,q}
\min\left\{
n^{(p-q)(q-2)/(q^2(p-2))},
m^{1-2/q}
\right\}.
```

## Scope Notes

This packet clears the source paper's main metric-embedding conjectures. It does not claim that every question in arXiv:1408.5819 is settled. In particular, arXiv:1601.03332 explicitly says that the convolution approach formulated as Question 6.1 of arXiv:1408.5819 remains open, and the source paper also has a separate Schatten-constant question.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1408.5819.
- `supporting_paper_1601.03332.pdf`: arXiv:1601.03332.

