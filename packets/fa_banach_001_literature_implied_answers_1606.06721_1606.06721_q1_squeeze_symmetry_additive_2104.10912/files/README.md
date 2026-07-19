# Literature-Implied Answer: Additive Lebesgue Bounds via Squeeze Symmetry

status: `literature_implied_answer (partial Q1 / broad additive-parameter formulation)`

Source target: Pablo M. Berna, Oscar Blasco, Gustavo Garrigos, *Lebesgue inequalities for the greedy algorithm in general bases*, arXiv:1606.06721.

Supporting paper: Fernando Albiac, Jose L. Ansorena, Pablo M. Berna, *New parameters and Lebesgue-type estimates in greedy approximation*, arXiv:2104.10912.

## Identification

Section 6 of the source paper asks Q1: find bounds for the Lebesgue constants `L_N` and `\widetilde L_N` that depend additively on the unconditionality constants and democracy/A-property constants; in particular, determine when one can have `L_N \lesssim k_N+\nu_N` or `L_N \lesssim k_N+\widetilde\mu_N`.

The supporting paper gives an agent-identified partial answer to this additive-bounds program, not to the literal `k_N+\nu_N` or `k_N+\widetilde\mu_N` variants. Its abstract says it answers Temlyakov's 2011 question by finding natural greedy-type parameters which combine linearly with the unconditionality parameters to determine the growth of the Lebesgue constants. Theorem 1.2 / Section 3 proves that, up to constants depending only on the quasi-Banach modulus, the Lebesgue constants are equivalent to `max{k_m, \lambda_m}`, where `\lambda_m` is the squeeze-symmetry parameter. Thus `L_m` is controlled additively by a natural replacement parameter: `L_m \lesssim k_m+\lambda_m`.

## Scope

This packet should not be read as a full answer to all final questions in arXiv:1606.06721. The source's Q2 about examples with arbitrary independent power growth `\nu_N \approx N^\alpha` and `k_N \approx N^\beta` remains outside this identification. The source's Q3 about `\gamma_N \approx 1` with `g_N` as large as possible is also outside this identification.

Search evidence on 2026-06-26: exact local index search found no prior packet for `1606.06721`; web/local searches for the exact Q2/Q3 phrases did not locate a direct resolution. Later papers `1811.04268`, `2205.06838`, and `2508.16893` were checked for nearby greedy-parameter questions; they address Chebyshev/weak greedy variants and later AAB parameter-power questions, not the full Q2/Q3 from the source.

Files:

- `source_paper.pdf`: arXiv:1606.06721.
- `supporting_paper_2104.10912.pdf`: arXiv:2104.10912.
- `solution_packet.pdf`: compact status note.

