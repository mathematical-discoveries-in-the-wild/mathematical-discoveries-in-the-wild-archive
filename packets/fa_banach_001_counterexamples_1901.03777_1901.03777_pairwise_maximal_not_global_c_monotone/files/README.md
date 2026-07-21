# Counterexample packet: pairwise maximal monotonicity does not force maximal c-monotonicity

status: candidate_counterexample_likely_valid

source_arxiv: 1901.03777

source_paper: Sedi Bartz, Heinz H. Bauschke, Hung M. Phan, and Xianfu Wang, *Multi-marginal maximal monotonicity and convex analysis* (arXiv:1901.03777v2; Mathematical Programming 185 (2021), 385--408).

source_question: After Proposition 5.9, PDF page 22, the authors ask whether maximal monotonicity of all two-marginal projections \(\Gamma_{i,j}\) implies maximal \(c\)-monotonicity of \(\Gamma\).

result: No. There is a counterexample already for \(N=3\) and \(H=\mathbb R^3\).

## Claimed Counterexample

Let
\[
  \rho(t)=\operatorname{sgn}(t)(|t|-1)_+,
  \qquad
  \alpha(t)=\frac13\rho(t),
  \qquad
  \beta(t)=t-\frac23\rho(t).
\]
For \(s=(s_{12},s_{13},s_{23})\in H=\mathbb R^3\), set
\[
\begin{aligned}
T_1(s)&=(\alpha(s_{12}),\alpha(s_{13}),\beta(s_{23})),\\
T_2(s)&=(\alpha(s_{12}),\beta(s_{13}),\alpha(s_{23})),\\
T_3(s)&=(\beta(s_{12}),\alpha(s_{13}),\alpha(s_{23})).
\end{aligned}
\]
Then \(T_1+T_2+T_3=\operatorname{Id}\). Define
\[
  \widetilde\Gamma
   =\{(T_1(s),T_2(s),T_3(s)):s\in H\},
  \qquad
  \Gamma=\widetilde\Gamma\setminus\{(0,0,0)\}.
\]
Here each displayed zero in the deleted triple is the zero vector of \(H\).

The scalar maps \(\alpha\) and \(\beta\) are nondecreasing. Consequently, for every \(i\ne j\) and \(s,t\in H\),
\[
  \langle T_i(s)-T_i(t),T_j(s)-T_j(t)\rangle\ge 0.
\]
Thus all pair projections are monotone and \(\widetilde\Gamma\), hence \(\Gamma\), is \(c\)-monotone.

Put \(\phi=2\alpha=2\rho/3\) and \(\psi=\alpha+\beta=\operatorname{Id}-\rho/3\). Both scalar maps are onto \(\mathbb R\). The three pair-sum maps are
\[
\begin{aligned}
T_1+T_2&=(\phi(s_{12}),\psi(s_{13}),\psi(s_{23})),\\
T_1+T_3&=(\psi(s_{12}),\phi(s_{13}),\psi(s_{23})),\\
T_2+T_3&=(\psi(s_{12}),\psi(s_{13}),\phi(s_{23})),
\end{aligned}
\]
so each is onto \(H\). Minty's theorem therefore makes every pair projection \(\widetilde\Gamma_{i,j}\) maximally monotone.

Deleting the origin changes none of these pair projections. For example, the deleted \((1,2)\)-pair \((0,0)\) is also produced by \(s=(1/2,0,0)\ne0\), because \(\rho\) vanishes on \([-1,1]\). The witnesses \((0,1/2,0)\) and \((0,0,1/2)\) do the same for the other two pairs. Hence
\[
  \Gamma_{i,j}=\widetilde\Gamma_{i,j}
  \quad(1\le i<j\le3),
\]
and every \(\Gamma_{i,j}\) is maximally monotone. Nevertheless, \(\Gamma\) has the proper \(c\)-monotone extension \(\widetilde\Gamma\), so \(\Gamma\) is not maximally \(c\)-monotone.

## Proof Intuition

The pair projections cannot detect a global hole when each deleted pair has a different replacement point. Soft thresholding supplies exactly the needed flat fiber. One coordinate is dedicated to each pair: on the \(ij\)-coordinate, both \(T_i\) and \(T_j\) vanish throughout \([-1,1]\), while the remaining map carries that coordinate so that the three maps still sum to the identity. Away from the flat interval, the pair sum remains onto. Thus each pair relation passes Minty's maximality test even after the single global triple at the origin is removed.

## Verification

- `verification.md` gives an adversarial step-by-step verifier report.
- `code/verify_counterexample.py` checks the piecewise identities, monotonicity inequalities, explicit pair-sum inverses, and deletion witnesses on deterministic breakpoints and 50,000 seeded random samples.
- Run with:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/counterexamples/1901.03777_pairwise_maximal_not_global_c_monotone/code/verify_counterexample.py
```

The computation is a regression check, not the proof; the proof is the piecewise argument in `main.tex`.

## Evidence

- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop from PDF page 22 containing Proposition 5.9 and the exact open question.
- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.

## Novelty Check

A bounded search on 2026-07-21 used the exact quoted question, combinations of “two-marginal projections”, “maximal monotonicity”, and “maximal c-monotonicity”, the arXiv id 1901.03777, the source title, and citation-facing searches. The local run indexes and full-text corpus were also searched. Results found the source paper, bibliographic mirrors, a later paper on a different multi-conjugacy/maximality question, and general surveys, but no paper explicitly resolving this pair-projection question and no matching counterexample. This supports only a novelty claim of “no answer found in the bounded search”, not a definitive literature-wide priority claim.

## Limitation and Human Review Recommendation

The counterexample exploits a nonclosed global set: it removes one point from a continuous maximally \(c\)-monotone parametrized set while leaving all pair projections unchanged. The source question imposes no closedness assumption, so this answers it as written. A strengthened question assuming that \(\Gamma\) is closed (or is exactly the join determined by its pair projections) is not addressed.

Human review should focus on three short points: (1) the pairwise inner-product inequality from coordinatewise monotonicity, (2) the Minty range calculation for each pair projection, and (3) the three nonzero witnesses showing that deleting the origin does not alter any pair projection.

## Reference

S. Bartz, H. H. Bauschke, H. M. Phan, and X. Wang, *Multi-marginal maximal monotonicity and convex analysis*, Mathematical Programming 185 (2021), 385--408; arXiv:1901.03777v2.
