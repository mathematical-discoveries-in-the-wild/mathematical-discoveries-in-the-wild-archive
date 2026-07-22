# Counterexample packet: restricted surface-spline Lagrange functions need not be exponentially local

Run: fa_banach_001

Status: candidate_counterexample_likely_valid for Conjecture 1 of arXiv:1005.2424 as literally stated.

## Source problem

T. Hangelbroek, F. J. Narcowich, X. Sun, and J. D. Ward, *Kernel Approximation on Manifolds II: The L-infinity norm of the L2-projector*, arXiv:1005.2424, Conjecture 1 on PDF page 20 (Section 6).

For restricted surface splines on S^d, Conjecture 1 asserts that the Lagrange functions for every quasiuniform family form a local basis in the exponential sense of Assumption 3.4 and satisfy the Holder estimate of Assumption 3.5.

## Counterexample

Take d=m=1, so the manifold is the circle and the source kernel is

    k(theta) = sqrt(1-cos(theta)) = sqrt(2) |sin(theta/2)|,
    Pi_1 = span{1, cos(theta), sin(theta)}.

For odd N >= 5, take the uniform grid Xi_N={2*pi*j/N} and let chi_N be the Lagrange function centered at 0. Its antipodal value is exactly

    chi_N(pi) = (1/N) * ((2*cos(pi/N)-1)/cos(pi/(2*N)) - 1),

and therefore

    N^3 chi_N(pi) -> -7*pi^2/8.

The grids have separation radius q_N=pi/N, fill distance h_N=pi/N, and mesh ratio 1. Assumption 3.4 would instead imply

    |chi_N(pi)| <= C exp(-nu*pi/q_N) = C exp(-nu*N),

which is incompatible with the exact cubic tail.

## Mechanism

The polynomial part of chi_N is forced by the side conditions and cardinal data to be

    p_N(theta) = (1+2*cos(theta))/N.

Between adjacent grid nodes, chi_N-p_N is a linear combination of translates of k and hence solves u''+u/4=0. On the cell centered at the antipode, both endpoint values of chi_N vanish. Solving this two-point ODE gives the displayed exact formula without needing the unknown kernel coefficients.

## Scope

- This falsifies the universal exponential-locality assertion in Conjecture 1 under its literal inclusion of S^1 (d=1, m=1).
- It does not challenge the Holder part of Conjecture 1, bounded Lebesgue constants, stability, or approximation conclusions [A]-[E].
- It does not address Conjectures 2 or 3, nor the even-dimensional spherical case.
- If the authors intended an unstated restriction d >= 2, this is an endpoint obstruction rather than a counterexample to that narrower intention. No such restriction was found in the source statement.

## Literature and novelty check

The cheap run indexes had no record for arXiv:1005.2424 or this circle construction. Bounded web searches on 2026-07-22 used the arXiv id, the exact conjecture title, restricted surface splines, S^1, odd-dimensional spheres, Lagrange functions, and exponential decay. They found no prior counterexample or this exact antipodal formula.

The closest later source is Hangelbroek--Narcowich--Ward, arXiv:1012.4852. It cites the source paper, proves exact exponential localization for even-dimensional spheres (Theorem 5.3), proves a near-exponential estimate with a polynomial floor in the general case (Theorem 5.5), and explicitly says exponential decay on odd-dimensional spheres was believed to hold. That later statement makes the S^1 obstruction directly relevant; it does not contain the counterexample above.

## Files

- README.md: this summary.
- main.tex: full proof and verification discussion.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: arXiv:1005.2424.
- supporting_paper_1012.4852.pdf: decisive later status source.
- figures/open_problem_crop.png: rendered source PDF page 20 containing Conjecture 1.
- code/verify_antipodal_formula.py: numerical augmented-system check of the exact formula; evidence only, not part of the proof.

## Human review recommendation

Check first that the source quantifiers permit the standard circle S^1; the displayed conjecture gives no lower bound on d. Then verify the discrete moment calculation forcing p_N=(1+2 cos(theta))/N and the two-point ODE calculation on the antipodal grid cell. Those are the only substantive steps.
