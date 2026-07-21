# Stable finite-type component and one-sided rank removal

**Status:** candidate partial result, likely valid, awaiting human review  
**Source:** Tim de Laat, Masato Mimura, and Mikael de la Salle, *On strong property (T) and fixed point properties for Lie groups*, arXiv:1508.05860v2; Ann. Inst. Fourier 66 (2016), 1859--1893.  
**Question location:** Section 2.4, immediately after Proposition 2.1, journal page 1867 (PDF page 10).  
**Packet:** `solution_packet.pdf`  
**Ledger:** `runs/fa_banach_001/ledger/results/1508.05860_rank_increase_reduction_finite_type_coefficients.json`

## Result

Proposition 2.1 assumes

\[
\dim V_k=\dim V_{k_0}
\]

and the authors ask whether this assumption is necessary.  The packet proves two precise advances.

1. Near \(k_0\), a canonical rank-\(\dim V_{k_0}\) projection \(Q_k\leq P_k\) exists, and the finite-type coefficient estimate controls
   \(Q_k f(\pi(k))-f(\pi(k_0))\) with no dimension hypothesis.
2. The full conclusion of Proposition 2.1 holds whenever
   \(\dim V_k\leq\dim V_{k_0}\).  Thus equality can be replaced by a one-sided inequality.

The proof uses the source paper's covariant map \(\psi\).  Since \(\psi(k)=\psi(k)P_k\) and \(\psi(k)\) is close to the rank-\(d_0\) projection \(P_{k_0}\), it has at least \(d_0\) large singular values.  Their spectral subspace is the stable projection \(Q_k\).  A uniformly bounded pseudoinverse transfers the source estimate for \(\psi(k)f(\pi(k))\) back to \(Q_k f(\pi(k))\).

## Scope

This is not a full answer.  It reduces the unresolved case exactly to newly appearing invariant directions: any counterexample to the rank-free proposition must involve points \(k_j\to k_0\) with

\[
\dim V_{k_j}>\dim V_{k_0}
\]

and simultaneous norm convergence of the scalar orbital convolution operators.  The packet does not control the extra component \((P_{k_j}-Q_{k_j})f(\pi(k_j))\).

## Verification

- `main.tex` contains the formal construction, theorem, proof, and obstruction corollary.
- `figures/open_problem_crop.png` is the complete source page containing Proposition 2.1 and the authors' question.
- `source_paper.pdf` is the published source article.
- The proof is finite-dimensional spectral calculus; no numerical computation is used.
- A bounded web/arXiv search on 2026-07-21 found no later settlement of the exact rank question.  Novelty remains provisional pending expert citation review.
- The rendered PDF was re-rendered to PNG and visually inspected page by page.

## Human-review focus

Check that the spectral projection \(Q_k\) lies in \(V_k\), and check the pseudoinverse identity used to pass from the source estimate for \(\psi(k)f(\pi(k))\) to the estimate for \(Q_kf(\pi(k))\).  Those are the only new ingredients; the scalar estimate is equation (2.4) in the source proof.

