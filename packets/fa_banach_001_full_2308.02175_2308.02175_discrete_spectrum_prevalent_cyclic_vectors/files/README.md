# Discrete spectrum gives prevalent cyclic vectors

Status: `full_solution_likely_valid`

Run: `fa_banach_001`  
Lane: 16  
Agent: `agent_lane_16`  
Date: 2026-07-03

Source paper: Peter Koltai and Philipp Kunde, *A Koopman-Takens theorem: Linear least squares prediction of nonlinear time series*, arXiv:2308.02175v3.

## Claim Solved

The packet proves Conjecture 25 from the source paper: if an ergodic measure-preserving transformation has discrete spectrum, then its Koopman operator has a prevalent set of cyclic vectors in `L^2_mu`.

The proof gives the slightly sharper characterization that, after diagonalizing the Koopman operator in its pure point eigenbasis, a vector is cyclic exactly when its coefficient on every eigenline is nonzero. The cyclic vectors therefore contain a dense `G_delta` set and are prevalent.

## Packet Contents

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2308.02175v3.
- `figures/open_problem_crop.png`: crop of the source page containing Conjecture 25.

## Proof Idea

For an ergodic discrete-spectrum transformation, the Koopman eigenspaces are one-dimensional. In an eigenbasis the operator is a diagonal unitary with distinct diagonal entries. If a vector has a zero coordinate, its cyclic subspace stays in the corresponding coordinate hyperplane. If all coordinates are nonzero, its spectral measure is a purely atomic measure charging every eigenvalue; Kolmogorov's density theorem implies analytic polynomials are dense in the associated `L^2` space, so positive powers of the Koopman operator already generate every eigenline.

Prevalence follows from a one-dimensional probe vector with all coordinates nonzero: along any affine complex line in that probe direction, each coordinate can vanish for at most one scalar, so the exceptional set is countable.

## Novelty / Literature Check

Local cheap indexes were searched for `2308.02175`, `Koopman`, `Takens`, `cyclic vectors`, `discrete spectrum`, and `prevalent`; no exact prior packet for this conjecture was found. Web searches for exact phrases including `"discrete spectrum" "prevalent set of cyclic vectors"` and `"Koopman--Takens" "discr_spec_prevalence"` did not reveal a separate published resolution. The arXiv page confirms the current source version is v3 from 2024-03-31 and lists math.DS/math.FA.

The novelty confidence is moderate rather than high: the proof is short and uses standard ingredients already close to the source paper, especially Kolmogorov's density theorem and the representation/simple-spectrum facts for ergodic discrete-spectrum systems. Human review should treat this as a likely-valid standard-tool completion of the conjecture.

## Human Review Recommendation

Recommended for review as a full solution. The key points to check are:

- the one-dimensionality of Koopman eigenspaces under ergodicity;
- the use of Kolmogorov density for purely atomic spectral measures, ensuring positive powers suffice;
- the prevalence argument over the complex Hilbert space convention used by the source.
