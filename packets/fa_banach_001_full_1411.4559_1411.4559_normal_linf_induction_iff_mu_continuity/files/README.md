# Normal `L^infty` induction iff `mu`-continuity

Status: `full_solution_likely_valid`

Source: Deguang Han, David R. Larson, Bei Liu, and Rui Liu,
*Dilations of frames, operator valued measures and bounded linear maps*,
arXiv:1411.4559v2 (2014), Problem 2 on PDF page 19.

Source link: <https://arxiv.org/abs/1411.4559>

## Result

Let `(Omega,Sigma,mu)` be a probability space and let
`E:Sigma -> B(H)` be countably additive in the weak operator topology, exactly
as in the source definition. There is an ultraweakly continuous bounded linear
map

`phi:L^infty(mu) -> B(H)`, `phi(chi_B)=E(B)`,

if and only if `E` is absolutely continuous with respect to `mu`, meaning
`mu(B)=0 => E(B)=0`. The inducing map is unique. If `E(Omega)=I`, it is unital.

Thus the unrestricted answer is negative. On `[0,1]` with Lebesgue measure,
the Dirac OVM `E(B)=1_{0 in B} I` is a probability OVM, but it cannot be induced
from `L^infty(mu)` because `chi_{0}=0` there while `E({0})=I`.

## Proof mechanism

Weak-operator countable additivity and Orlicz-Pettis make each orbit `E(.)x`
a norm-countably-additive vector measure. Finite semivariation plus uniform
boundedness gives a uniform bound for all simple integrals. Trace-class
scalarizations therefore have uniformly bounded variation. Under
`E << mu`, their Radon-Nikodym densities define a bounded preadjoint
`S_1(H) -> L^1(mu)`; its adjoint is the required normal map.

## Novelty and scope

A bounded exact-phrase/close-variant search on 2026-07-22 used the source
title, Problem 2, `operator valued measure`, `ultraweakly continuous map`, and
`L^infty(mu)`. It found the source and related later work on normal dilations,
but no explicit answer to this induction question. This packet claims a full
proof of the literal question, not publication priority. The argument is a
short application of classical vector-measure theory and may be folklore.

## Packet files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source Problem 2, PDF page 19.
- `VERIFICATION.md`: independent proof-audit checklist and outcome.
- Ledger: `runs/fa_banach_001/ledger/results/1411.4559_normal_linf_induction_iff_mu_continuity.json`.

Human-review recommendation: verify the finite-semivariation step in Lemma 1
and the trace-class preadjoint assembly. These are the only substantive
functional-analytic steps; the null-set obstruction and counterexample are
immediate.

