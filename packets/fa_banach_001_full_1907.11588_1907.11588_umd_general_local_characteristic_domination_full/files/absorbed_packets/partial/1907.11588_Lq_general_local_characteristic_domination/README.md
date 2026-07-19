# Partial result: full `L^q` general local characteristic domination for `p,q>1`

Status: candidate partial result, likely valid.

Source paper: Ivan S. Yaroslavtsev, *Local characteristics and tangency of vector-valued martingales*, arXiv:1907.11588.

Target: Remark 12.10 asks whether characteristic domination gives maximal `L^p` comparison for general local martingales. The source proves the quasi-left-continuous case and identifies the discrete independent-increment comparison as the missing obstruction.

Result: Let `1<p,q<infinity`, let `S` be an arbitrary measure space, and put `X=L^q(S)`. If `N` and `M` are `X`-valued local martingales and `N` is characteristically dominated by `M` in the sense of Yaroslavtsev's Definition 12.9, then

```text
E sup_t ||N_t||_X^p <= C_{p,q} E sup_t ||M_t||_X^p.
```

This is a full positive answer for the concrete class `L^q(S)` and exponents `1<p,q<infinity`. It remains partial relative to the source's broad UMD-space problem and does not cover the endpoint `p=1`.

Proof mechanism: Dirksen-Yaroslavtsev's sharp `L^q` stochastic-integral estimates identify the jump part of an `L^q` martingale with the same Rosenthal sum/intersection norm used in the discrete packet. The new step is a collapse/monotonicity lemma: for the identity jump integrand `x`, that norm depends only on the total spatial jump compensator `nu(R_+ x .)`, not on how the compensator is split between accessible and quasi-left-continuous times. Time-dependent decompositions in the sum spaces can be conditionally averaged over the spatial jump value, and measure domination transports decompositions by Radon-Nikodym restriction. Continuous parts are handled by Yaroslavtsev's continuous characteristic-domination estimate.

Why this avoids the old pitfall: characteristic domination controls only the total spatial jump compensator, not the accessible and quasi-left-continuous pieces separately. The proof never compares those pieces componentwise; it first folds them into the total `L^q` Rosenthal jump norm.

Novelty/literature check: Cheap run indexes contained prior `c0`, Hilbert, `ell_q` at `p=q`, and discrete `L^q` packets, but no full `L^q` general-local packet. Literature checked during the push included arXiv:1907.11588, Dirksen-Yaroslavtsev arXiv:1707.00109, and Yaroslavtsev arXiv:1807.05573/related BDG context. I found the decisive ingredients but not an explicit statement of this total-compensator `L^q` characteristic-domination consequence.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `supporting_paper_1707.00109.pdf`: Dirksen-Yaroslavtsev sharp `L^q` Burkholder-Rosenthal/stochastic-integral estimates.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: continuation with the discrete independent-increment formulation.

Human review recommendation: high priority. The main point to audit is the collapse/monotonicity lemma for sum/intersection norms with random compensators; if accepted, the result closes the whole `L^q`, `p>1` subcase of Remark 12.10.
