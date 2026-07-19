# A counterexample to the JNP factor converse for `C_p(X,E)`

Status: `counterexample_likely_valid`

Source: Christian Bargetz, Jerzy Kakol, and Damian Sobota, *On
complemented copies of the space c_0 in spaces C_p(X,E)*,
arXiv:2107.03211v3, Problem 4.8, page 7 (published in *Mathematische
Nachrichten* 297 (2024), 644-656).

## Result

Problem 4.8 has a negative answer. Take

- `X = beta N`, the Stone-Cech compactification of the discrete natural
  numbers;
- `E = c_00` with the norm inherited from `ell_1`.

Then neither `C_p(beta N)` nor `E` has the Josefson--Nissenzweig property,
but `C_p(beta N,E)` has the JNP. In fact, `C_p(beta N,E)` contains a
complemented copy of `(c_0)_p`.

The embedding sends `a=(a_n)` to the function that takes `n` to `a_n e_n`
on `N` and vanishes on the Stone-Cech remainder. A continuous left inverse
extracts the diagonal coordinates `pi_n(f(n))`. Compactness of every range
`f(beta N)` forces those diagonal coordinates to tend to zero.

The counterexample necessarily uses an incomplete normed range space. The
packet makes no claim about the converse under completeness, barrelledness,
or other regularity assumptions on `E`.

## Files

- `solution_packet.pdf`: human-readable counterexample and proof.
- `main.tex`: self-contained packet source.
- `source_paper.pdf`: arXiv:2107.03211v3.
- `supporting_paper_2003.06764.pdf`: Banakh--Gabriyelyan JNP background.
- `figures/open_problem_crop.png`: source Problem 4.8 and its context.
- `verification.md`: adversarial proof and novelty audit.
- `absorbed_packets/`: the earlier finite-slice partial packet, preserved as
  result history after final consolidation.

Ledger record:
`runs/fa_banach_001/ledger/results/2107.03211_jnp_betaomega_c00_counterexample.json`.
