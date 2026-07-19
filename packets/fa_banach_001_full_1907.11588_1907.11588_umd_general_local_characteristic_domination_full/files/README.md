# Full result: UMD general local characteristic domination

Status: `full_solution_likely_valid`.

Source problem: Ivan S. Yaroslavtsev, *Local characteristics and tangency of
vector-valued martingales*, arXiv:1907.11588, Remark 12.10.

Result: the general local-martingale characteristic-domination theorem holds
for every UMD Banach space. More precisely, if `X` is UMD, `1<=p<infinity`,
and `N` is characteristically dominated by `M` in Yaroslavtsev's sense, then

```text
E sup_t ||N_t||^p <= C_{p,X} E sup_t ||M_t||^p.
```

The new ingredient is stronger than needed for UMD: the finite
independent-increment aggregate-domination comparison holds in every Banach
space of finite cotype. This is the form used by Yaroslavtsev's
accessible-jump approximation, which truncates to finitely many predictable
jumps and then passes to the limit. Since every UMD space has finite cotype,
this removes the accessible-jump obstruction isolated in the source remark.

Relation to the `c0` counterexample: the counterexample answers the broad
arbitrary-Banach-space discrete aggregate-domination question negatively. This
full packet answers the UMD/finite-cotype side positively. They are
complementary, not conflicting: `c0` is not UMD and has no finite cotype.

Proof idea: the previous conditional packet reduced the symmetric discrete
problem to de-Poissonization. This packet proves de-Poissonization in finite
cotype. The Maurey--Pisier contraction principle, quoted in the explicit form
from Ivanisvili--van Handel--Volberg arXiv:2003.06345, says that in a cotype
`q` space iid symmetric scalar coefficients are controlled by Rademacher
coefficients with a tail integral. For Bernoulli selectors of density `a`,
this gives a thinning factor `a^(1/max(q,p))`. A compound-Poisson sum is
decomposed into layers `{Pois(p_i)>=k}`; the `k`-th layer is a thinning of the
original family with density at most `1/k!`. The thinning factors are summable.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `supporting_paper_2003.06345.pdf`: Maurey--Pisier contraction principle as
  quoted/proved in Ivanisvili--van Handel--Volberg.
- `figures/open_problem_crop.png`: crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: crop of the discrete
  aggregate-domination formulation.
- `verification_audit.md`: line-by-line audit summary.
- `absorbed_packets/`: earlier Hilbert, `ell_q`, `L^q`, endpoint, and
  conditional packets that are now superseded by this full proof.

Verification note: the proof has now been checked against the exact
Maurey--Pisier contraction principle in arXiv:2003.06345 and against the
finite predictable-jump approximation passages surrounding Yaroslavtsev's
Remark 12.10. The main remaining human audit points are the finite-cotype
thinning lemma and the final use of the accessible-jump approximation.

Proof-history note: the old positive partial and conditional packets have been
moved under `absorbed_packets/` so that the durable solution layer now presents
one parent full result. The `c0` counterexample remains outside this folder as
the non-UMD boundary case.
