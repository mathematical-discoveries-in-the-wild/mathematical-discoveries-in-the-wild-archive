# One-sided complex endpoint inclusion for the conditioned Hardy/BMO problem

run: `fa_banach_001`  
agent: `agent_lane_00`  
status: candidate partial result, likely valid  
source: arXiv:2108.06341, Narcisse Randrianantoanina, "Interpolation between noncommutative martingale Hardy and BMO spaces: the case 0<p<1"

## Result

The source paper asks whether, for \(0<p<1\), the endpoint complex interpolation identity
\[
[\mathsf h_p^c(\mathcal M),\mathsf{bmo}^c(\mathcal M)]_\theta
  = \mathsf h_r^c(\mathcal M),
\qquad
1/r=(1-\theta)/p,
\]
remains valid.

This packet proves the one-sided inclusion in the Banach target range:
if \(0<p<1\), \(0<\theta<1\), and \(r=p/(1-\theta)>1\), then
\[
[\mathsf h_p^c(\mathcal M),\mathsf{bmo}^c(\mathcal M)]_\theta
  \hookrightarrow \mathsf h_r^c(\mathcal M)
\]
continuously.

## What Remains Open

This is not the full endpoint identity. The reverse inclusion
\[
\mathsf h_r^c(\mathcal M)
  \hookrightarrow [\mathsf h_p^c(\mathcal M),\mathsf{bmo}^c(\mathcal M)]_\theta
\]
is not proved here. The same route also does not cover the range \(r\leq 1\).

The missing reverse direction is exactly where one would want a full complex
reiteration/Wolff theorem for the quasi-Banach endpoint couple; the source
paper identifies the absence of such a theorem as the reason the finite-\(q\)
complex result does not settle the BMO endpoint.

## Proof Inputs

- arXiv:2108.06341, Theorem 3.16: finite-index complex interpolation
  \([\mathsf h_p^c,\mathsf h_q^c]_\theta=\mathsf h_r^c\).
- arXiv:2108.06341, Theorem 3.5: real endpoint interpolation with
  \((\mathsf h_p^c,\mathsf{bmo}^c)\).
- arXiv:0906.4437, Theorem 4.4: Banach-range endpoint complex interpolation
  \((\mathsf{bmo}^c,\mathsf h_1^c)_{1/p}=\mathsf h_p^c\) for \(1<p<\infty\).
- Wolff's complex interpolation inclusion lemma, in the quasi-Banach inclusion
  form used in arXiv:2108.06341, Corollary 3.19.

## Novelty and Literature Check

Local lightweight indexes were searched for `2108.06341`, `h_p^c`,
`bmo^c`, `complex interpolation`, `Hardy and BMO`, and related title terms; no
prior packet or attempt for this target was found.

External searches checked exact phrases from the open problem and close
variants including `h_p^c bmo^c complex interpolation 0<p<1`,
`When 0<p<1 h_p^c bmo^c open problem`, `2108.06341 interpolation`, and
`P. Jones interpolation theorem noncommutative martingale Hardy spaces`.
The search found the 2009 Banach-range endpoint theorem, the 2022
`h_\infty^c` real-method sequel, and the 2024 capital-\(\mathcal H\) real-method
sequel, but no later full solution of the conditioned BMO complex endpoint.

## Files

- `source_paper.pdf`: original arXiv:2108.06341 paper.
- `supporting_paper_0906.4437.pdf`: supporting Banach-range endpoint theorem.
- `figures/open_problem_crop.png`: rendered crop of the source open problem on page 27.
- `main.tex`: review packet source.
- `solution_packet.pdf`: rendered packet.

## Human Review Recommendation

Check the applicability and exact parameter formula of Wolff's inclusion lemma
for the quasi-Banach spaces used here. The proof deliberately claims only the
inclusion direction supplied by that lemma, not full Wolff equality.
