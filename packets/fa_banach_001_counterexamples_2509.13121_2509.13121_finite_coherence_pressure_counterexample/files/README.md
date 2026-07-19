# Counterexample Packet: Finite Coherence Does Not Force Global Pressure

Status: candidate counterexample to a stated implication in arXiv:2509.13121.

This packet does not refute the main reflexive fixed point property conjecture in the paper. It refutes the specific Section 4.4 claim that finite low-coherence Hilbert certificates for `k <= m` force `P(C1,x_infty)>0`.

## Source

- arXiv:2509.13121
- Title: On the Fixed Point Property in Reflexive Banach Spaces
- Authors: Faruk Alpay, Hamdi Alakkad
- Source statement: Section 4.4, item 2, "Finite-dimensional certificates", across PDF pages 12-13.

## Packet Contents

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: full-width stitched screenshot of the source statement.
- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `code/verify_pressure.py`: exact finite calculation for `Phi_k`.

## Claim

Let `H = R^2`, `x_infty = 0`, and `C1 = {e1,e2}`. The two unit vectors have mutual coherence `mu=0<1/(2-1)`, and the advertised finite-level lower bound holds for `k<=2`. However `Phi_3(C1,0)=0`, since every 3-tuple chosen from a two-point set repeats one point and the repeated entries cancel with coefficients `1/2` and `-1/2`. Hence `P(C1,0)=inf_k Phi_k(C1,0)=0`.

Thus finite-level certificates up to the size of a finite low-coherence family do not force positive global pressure.

## Verification

Command:

```sh
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/counterexamples/2509.13121_finite_coherence_pressure_counterexample/code/verify_pressure.py
```

Expected output:

```text
Phi_1 = 0.707106781187
Phi_2 = 0.5
Phi_3 = 0
...
P = inf_k Phi_k = 0
```

## Human Review Notes

The proof is elementary. The key review point is categorical: this should be counted as a paper-statement counterexample, not as a solution of an author-labeled open problem and not as progress on the main reflexive FPP conjecture.
