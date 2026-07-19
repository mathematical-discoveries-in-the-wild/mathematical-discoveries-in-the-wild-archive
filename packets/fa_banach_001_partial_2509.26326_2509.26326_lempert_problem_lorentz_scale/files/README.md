# Partial Result: Lempert's Problem on the Lorentz Scale

Status: `partial_result_likely_valid`

Source: Andreas Defant, Daniel Galicer, Martin Mansilla, Mieczyslaw Mastylo, and Santiago Muro, *Local constants and Bohr's phenomenon for Banach spaces of analytic polynomials*, arXiv:2509.26326.

## Source Question

After Theorem 2.21, the source paper recalls Lempert's problem: can the projection constants in Theorem 2.21 be replaced by the unconditional basis constants of the monomial basis? Equivalently, for a Banach sequence lattice `X`, is

```text
X = ell_1  iff  sup_{m,n} chi_mon(P_m(X_n))^{1/m} < infinity?
```

## Result

The answer is affirmative on the classical Lorentz scale. Let `X = ell_{p,q}` with `1 <= p < infinity` and `1 <= q <= infinity`. If

```text
sup_{m,n} chi_mon(P_m(X_n))^{1/m} < infinity,
```

then `p=q=1`, so `X = ell_1`.

Equivalently, every non-`ell_1` Lorentz sequence lattice `ell_{p,q}` violates the bounded-root monomial unconditionality condition in Lempert's problem.

## Proof Mechanism

The source paper quotes Bayart's partial result: under the bounded-root monomial unconditionality hypothesis, for every `epsilon > 0` there is `D(epsilon)` such that

```text
||id : X_n -> ell_1^n|| <= D(epsilon) (log log n)^epsilon
```

for all `n`.

For Lorentz spaces, this identity norm is much larger unless `X=ell_1`:

- if `p>1`, testing on the all-ones vector gives growth at least `c n^{1/p'}`;
- if `p=1` and `1<q<infinity`, testing on `(1,1/2,...,1/n)` gives growth at least `c (log n)^{1/q'}`;
- if `p=1` and `q=infinity`, the same test gives growth at least `c log n`.

Each growth rate eventually dominates `(log log n)^epsilon` for a suitable positive `epsilon`, contradicting Bayart's necessary condition.

## Scope

- This does not solve Lempert's problem for all Banach sequence lattices.
- It records a complete positive answer for the Lorentz family `ell_{p,q}`, `1 <= p < infinity`, `1 <= q <= infinity`.
- The main external input is Bayart's theorem as quoted in the source paper; the Lorentz identity-norm obstruction is elementary.

## Search/Novelty Notes

Cheap run indexes were searched for `2509.26326`, `Lempert`, `monomial basis`, `unconditional basis constant`, `Bayart`, and Lorentz variants. No prior durable packet for this target or subcase was found.

External searches on 2026-06-21 for `"Lempert's problem" "monomial basis"`, `"Lempert's problem" "log log" "Bayart"`, and `"Lempert" "Lorentz" "monomial"` found no later full resolution or duplicate Lorentz-scale statement. This packet should be reviewed as a new recorded corollary/partial result, not as a claimed full solution of Lempert's problem.

## Packet Contents

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2509.26326.
- `figures/open_problem_crop.png`: crop of page 28 containing the Lempert problem and Bayart bound.
- `code/make_open_problem_crop.py`: reproducible crop script.
