# Full candidate: negative moments of Hilbert-kernel weights

Status: `full_solution_likely_valid` (awaiting human review).

For every `-1 < beta < 0`, this packet proves the conjecture stated on
page 31 of Mitra--Sire, arXiv:2106.03354:

```text
E[w_0(x)^beta]
  ~ kappa_beta(x) / (V_d rho(x) n log(n))^beta,
```

whenever the moment exists. It also proves the conjectured exact existence
criterion, for every fixed `n >= 1`:

```text
E[w_0(x)^beta] < infinity  iff  kappa_beta(x) < infinity.
```

The proof rewrites `beta=-a`, observes that
`Y=||x-X||^{-d}` has tail `P(Y>t) ~ V_d rho(x)/t`, and proves
fractional-moment convergence for its partial sums at scale `n log n`.
The weight identity
`w_0^{-a}=(1+||x-X_0||^d sum_{i=1}^n Y_i)^a` then gives both the
asymptotic and the iff criterion by independence and subadditivity.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained source.
- `source_paper.pdf`: original arXiv PDF.
- `figures/`: source pages containing Theorem 1 and the conjecture.
- `code/check_uniform_example.py`: finite Monte Carlo sanity check.
- `verification.md`: verifier-oriented audit.

Scope limitation: this proves the explicit negative-moment conjecture, but
does not prove existence of the separate heuristic scaling density `p` or
the source's suggested statement about `p(0)`.

Primary verifier focus: the fractional-moment lemma for i.i.d. variables with
tail `c/t`, in particular the uniform-integrability step.
