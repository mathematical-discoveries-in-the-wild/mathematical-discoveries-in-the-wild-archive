# Partial result: lacunary martingale models have a Poisson \(L^1\) endpoint

Status: `partial_result_likely_valid`

Source target: Zhendong Xu and Hao Zhang, *From the Littlewood-Paley-Stein
Inequality to the Burkholder-Gundy Inequality*, arXiv:2111.05164.

Origin of the remaining question: the introduction of arXiv:2111.05164 says
that, after its proof of the optimal \(p \to \infty\) order for
\(\mathsf L_p^{\mathsf T}\), "it only remains to determine the optimal order"
of the reverse Poisson constant \(\mathsf L_p^{\mathsf P}\) as \(p \to 1\).
This is the scalar case of Xu's Problem 8.4 in arXiv:2105.12175.

## Claimed contribution

For the martingale-generated symmetric diffusion semigroups used in
arXiv:2111.05164, with a sufficiently lacunary generator spectrum, the
subordinated Poisson square function is pointwise equivalent to the martingale
square function. Consequently these model semigroups satisfy the endpoint
estimate
\[
  \|f-Ff\|_1 \le C \|G^{\mathsf P}f\|_1
\]
and the reverse Poisson constants stay bounded as \(p \downarrow 1\) in this
model class.

The proof is a direct Riesz-sequence estimate for the normalized Poisson
kernels \(2t\alpha_n e^{-t\alpha_n}\) in \(L^2((0,\infty),dt/t)\), followed by
Davis' endpoint martingale square-function inequality.

## Scope

This does not solve the full Xu problem for arbitrary symmetric submarkovian or
Markovian semigroups. It proves the positive endpoint behavior for a large
martingale-model subfamily: arbitrary filtrations are allowed, but the generator
eigenvalues on the martingale differences must satisfy a fixed lacunarity
condition.

## Files

- `main.tex` / `solution_packet.pdf`: human-readable proof packet.
- `code/gram_lacunary_check.py`: numerical sanity check for the Gram matrix
  bounds.
- `source_paper.pdf`: source paper arXiv:2111.05164, if available locally.

## Novelty check

Local index search found no prior packet for arXiv:2111.05164 or this Poisson
martingale endpoint subcase. Local source checks included arXiv:2105.12175,
arXiv:2105.12795, and arXiv:2111.05164. Web searches on 2026-07-18 for
`L_p^P p->1 Littlewood-Paley Poisson Xu`, `reverse Littlewood-Paley-Stein
Poisson p 1 Xu`, and semigroup-BMO endpoint variants found Xu's explicit
Problem 8.4 and classical/Euclidean positive endpoint results, but no theorem
settling this martingale-generated lacunary Poisson model as a recorded answer.

Human review recommendation: check the indexing between the Xu-Zhang
martingale semigroup and the generator eigenvalues, then verify the Gram
Riesz-sequence bound and the use of Davis' \(L^1\) martingale inequality.
