# Counterexample: quantum Wasserstein channel complexity is not convex

Status: `candidate_counterexample_likely_valid`;
`full_negative_answer_to_channel_complexity_convexity_question`.

Source: Gergely Bunth, Jozsef Pitrik, Tamas Titkos, and Daniel Virosztek,
*On the metric property of quantum Wasserstein divergences*,
arXiv:2402.13150v4, Section 5.1, equation (37) and printed page 18.

The authors ask whether

```text
C_W(Phi) = max_rho d_A(rho, Phi(rho))
```

is convex as a function of the quantum channel `Phi`. The answer is no, even
for one qubit and their own symmetric Pauli cost
`A={sigma_x,sigma_y,sigma_z}`.

Let `X(rho)=sigma_x rho sigma_x` and
`Lambda_t=(1-t)Id+tX`. For the pure input `rho_0=|0><0|`, the source paper's
pure-state formula gives exactly

```text
d_s(rho_0,Lambda_t(rho_0))^2 = 4t + 4 sqrt(t(1-t)).
```

Hence

```text
C_W(Lambda_1/4) >= sqrt(1+sqrt(3)).
```

The Pauli cost operator is

```text
C_s = 8(I-|Omega><Omega|),
```

so every qubit channel has `C_W<=2sqrt(2)`, while `C_W(Id)=0`. Convexity would
therefore imply

```text
C_W(Lambda_1/4) <= (1/4)C_W(X) <= sqrt(2)/2,
```

contradicting the preceding exact lower bound. Near zero the mechanism is even
clearer: the lower bound grows like `2 t^(1/4)`, whereas convexity would force
linear growth.

The paper's main De Palma--Trevisan triangle-inequality conjecture was later
settled by Melchior Wirth, arXiv:2511.20450. This packet instead gives a new
full negative answer to the distinct open question in Section 5.1.

Files:

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: exact page-18 open-question passage.
- `code/verify_counterexample.py`: exact symbolic matrix check.
- `verification.md`: commands, outputs, and adversarial checks.

A bounded local-index and web search on 22 July 2026 found no prior answer to
this exact question. Hits concerning order-one/Hamming-Wasserstein channel
complexities use different definitions. Novelty is plausible, not certified.

Human review should first check the pure-input formula normalization and the
two-line cost-operator bound. Expected review effort is low.

Model: GPT5.6.
