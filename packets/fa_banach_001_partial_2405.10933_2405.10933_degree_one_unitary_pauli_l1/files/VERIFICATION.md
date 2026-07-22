# Verifier report

Verdict: `pass_likely_valid_candidate_partial`

Verifier: `agent_lane_12` (self-audit before human review)

Date: 2026-07-21

## Formal proof audit

- The degree-one expansion separates uniquely into the identity coefficient
  and traceless single-qubit summands.
- For each pair of active qubits, the support-exactly-two part of `U* U = I`
  is `B_j^* tensor B_k + B_j tensor B_k^* = 0`; no other term contributes on
  that support.
- The simple-tensor dependence lemma is valid over complex vector spaces and
  forces each local piece with an active partner to be phase-Hermitian.
- The resulting pairwise phase condition is incompatible with three active
  qubits.
- The one-active-qubit case is handled separately by four-term Parseval, so
  the proof does not incorrectly assume phase-Hermiticity there.
- In the two-active-qubit case, the one-qubit components force the identity
  coefficient to vanish; the scalar component gives `r_1^2+r_2^2=1`.
- Two applications of Cauchy--Schwarz give the upper bound `sqrt(6)`, and all
  equality conditions are realized by the displayed example.
- Tensor products multiply Pauli coefficient `ell_1` norms and add degrees;
  since the base extremizer has no identity coefficient, its `d`th tensor
  power has degree exactly `d`.
- The one-ancilla block dilation is Hermitian and squares to the identity;
  its `X` and `Y` Pauli sectors are disjoint, so its coefficient `ell_1`
  dominates that of the original unitary.
- Under the stated collision-free hypothesis, each commuting Pauli pair is
  the unique contributor to its product label in `F^2`; hence all distinct
  support elements anticommute.
- Partitioning a pairwise anticommuting family by support size and applying
  the classical sunflower lemma with `r=3^k+1` gives the displayed explicit
  support bound.  The possible multiplicity on a fixed support is at most
  `3^k`.

No missing hypothesis or immediate algebraic contradiction was found.

## Computational consistency check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2405.10933_degree_one_unitary_pauli_l1/code/verify_extremizer.py
```

Output:

```text
verified: U_star is unitary, degree one, and has Pauli ell_1 = sqrt(6)
verified: tensor-power ell_1 norms equal 6^(d/2) for d=1,2,3,4
```

This check is supplementary and does not replace the algebraic proof.

## Packet QA

- `main.tex` compiles without warnings or overfull boxes.
- The six rendered pages were visually inspected; no clipping, broken
  glyphs, or layout defects were found.
- The source crop is full width and contains the Pauli-degree definition and
  all of Question 4.

## Human-review focus

Check the extraction of the support-two equation, the phase normalization,
and the exact injectivity hypothesis in the collision-free theorem.  The
result is partial: it settles `d=1` sharply and gives a lower bound for all
`d`, while the higher-degree upper bound is conditional on the absence of
commuting-product collisions.
