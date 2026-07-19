# Partial result: `ell_q` characteristic domination at the natural exponent

Status: candidate partial result, likely valid.

Source paper: Ivan S. Yaroslavtsev, *Local characteristics and tangency of vector-valued martingales*, arXiv:1907.11588.

Target: Remark 12.10 asks whether the quasi-left-continuous characteristic-domination theorem extends to general local martingales. The previous Hilbert packet settles the Hilbert-valued case for all finite `p`. This packet pushes into a non-Hilbert UMD family.

Result: Let `1 < q < infinity` and let `X = ell_q`. If an `ell_q`-valued local martingale `N` is characteristically dominated by an `ell_q`-valued local martingale `M`, then

```text
E sup_t ||N_t||_q^q <= C_q E sup_t ||M_t||_q^q.
```

Equivalently, the general local martingale extension is true in `ell_q` at the natural exponent `p=q`. For `q != 2`, this is a genuinely non-Hilbert UMD subcase.

Proof mechanism: coordinate projections preserve characteristic domination. The scalar coordinate martingales are handled by the companion Hilbert all-`p` packet, and scalar BDG converts their maximal moments to quadratic-variation moments. Yaroslavtsev's UMD Banach-function-space BDG theorem for `ell_q = L^q(N)` then sums those scalar quadratic-variation estimates exactly:

```text
E sup_t ||N_t||_q^q ~= sum_k E [N^k]_infty^(q/2).
```

This avoids the failed `c0` occupancy obstruction because finite `ell_q` keeps the coordinate quadratic variations summable at exponent `q/2`.

Limitations:

- This does not prove the full non-Hilbert UMD problem for all `p`.
- This packet proves the countably atomic space `ell_q`. The same coordinate proof does not directly cover nonatomic `L^q(S)`, because point evaluations are not bounded or well-defined on equivalence classes.
- The result depends on the companion Hilbert all-finite-`p` packet for the scalar characteristic-domination comparison.

Novelty/literature check: Cheap indexes contained the `c0` counterexample and the Hilbert packets, but no `ell_q` non-Hilbert packet for arXiv:1907.11588. Web searches for `"characteristically dominated" "ell_q"`, `"characteristically dominated" "L^q"`, and `"aggregate domination" independent random variables "ell_q"` did not locate an exact existing result. The proof uses Yaroslavtsev's arXiv:1807.05573 UMD Banach-function-space BDG theorem; Dirksen--Yaroslavtsev arXiv:1707.00109 was checked as nearby `L^q` Burkholder-Rosenthal context.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `supporting_paper_1807.05573.pdf`: Yaroslavtsev's BDG paper used for the `ell_q` square-function theorem.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: continuation noting the symmetric discrete case.
- `code/ellq_occupancy_check.py`: finite sanity check for the old `c0` occupancy construction in fixed `ell_q`.
