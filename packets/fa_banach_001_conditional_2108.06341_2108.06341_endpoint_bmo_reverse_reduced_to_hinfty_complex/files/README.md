# Conditional packet: endpoint BMO reverse inclusion via the h-infinity and conditioned endpoints

status: conditional reduction, likely valid  
source: arXiv:2108.06341, Narcisse Randrianantoanina, "Interpolation between noncommutative martingale Hardy and BMO spaces: the case 0<p<1"  
supporting sources: arXiv:0906.4437, arXiv:2212.08714, plus route checks against Pisier and Kalton endpoint interpolation machinery  
run: fa_banach_001  
agent: agent_lane_00  
date: 2026-06-16

## Claim

Let \(0<p<1\), \(0<\theta<1\), and \(1/r=(1-\theta)/p\), with \(r>1\). The previous lane-0 packet proves
\[
[\mathsf h_p^c(\mathcal M),\mathsf{bmo}^c(\mathcal M)]_\theta
\hookrightarrow \mathsf h_r^c(\mathcal M).
\]
This packet proves the reverse inclusion conditionally. The first reduction is:
if
\[
\mathsf h_r^c(\mathcal M)
\hookrightarrow [\mathsf h_p^c(\mathcal M),\mathsf h_\infty^c(\mathcal M)]_\theta,
\]
then
\[
\mathsf h_r^c(\mathcal M)
\hookrightarrow [\mathsf h_p^c(\mathcal M),\mathsf{bmo}^c(\mathcal M)]_\theta.
\]
Consequently, under this \(h_\infty^c\)-endpoint complex interpolation dependency,
\[
[\mathsf h_p^c(\mathcal M),\mathsf{bmo}^c(\mathcal M)]_\theta
=\mathsf h_r^c(\mathcal M)
\]
with equivalent quasi-norms.

This revision pushes the dependency one step further. It records a sufficient
condition for the \(h_\infty^c\) endpoint reverse inclusion in terms of the
conditioned sequence spaces:
\[
L_r^{\rm cond}(\mathcal M;\ell_2^c)
\hookrightarrow
[L_p^{\rm cond}(\mathcal M;\ell_2^c),
  L_\infty^{\rm cond}(\mathcal M;\ell_2^c)]_\theta,
\]
together with the natural endpoint extension of the Kadison--Schwarz
martingale-difference projection. Under that conditioned endpoint dependency,
the full \(r>1\) \(bmo^c\)-endpoint complex identity follows.

## Conditional dependency

The main unproved dependency is exactly the reverse inclusion for the complex endpoint couple
\[
(\mathsf h_p^c(\mathcal M),\mathsf h_\infty^c(\mathcal M)).
\]
Randrianantoanina's later paper arXiv:2212.08714 proves the corresponding real/K-method theorem and explicitly records that the complex interpolation version remains open. This packet does not prove that open \(h_\infty^c\) endpoint result.

The new lower-level dependency is the corresponding endpoint complex
interpolation/retraction statement for Junge's conditioned spaces. This is
strictly more concrete: the finite-index conditioned spaces interpolate by
arXiv:2108.06341, and arXiv:2212.08714 supplies the \(L_\infty^{\rm cond}\)
framework. The obvious ambient-retraction proof would require a uniform
\(L_\infty\) column Stein projection estimate; that estimate is exactly the
endpoint obstruction and is not available in general.

## Proof idea

The proof is short but useful for coordination. The space \(\mathsf h_\infty^c(\mathcal M)\) embeds continuously into \(\mathsf{bmo}^c(\mathcal M)\), because bounded full conditioned square function controls all conditioned BMO tails. Complex interpolation is monotone under continuous endpoint embeddings. Therefore the assumed \(h_\infty^c\) reverse inclusion immediately gives the desired \(bmo^c\) reverse inclusion. The already packaged one-sided Wolff argument supplies the opposite inclusion for \(r>1\).

## Literature and obstruction notes

- arXiv:2212.08714 proves K-closedness and real interpolation for \((\mathsf h_p^c,\mathsf h_\infty^c)\), but states that the complex version is still open.
- arXiv:2412.12769 proves a Wolff-reiteration theorem for \(A\)-convex quasi-Banach function spaces with one nonseparable endpoint. Its theorem is not directly applicable here because the martingale Hardy/BMO spaces are not quasi-Banach function lattices, and the paper explicitly leaves the corresponding general \(A\)-convex quasi-Banach-space Wolff theorem open.
- Pisier's arXiv:math/9201229 proves the \(H^1/H^\infty\) complex endpoint for classical, triangular Schatten, and operator-valued analytic Hardy spaces. The mechanism uses Hardy algebra factorization and triangular/outer factorization, so it does not directly apply to conditioned martingale Hardy spaces.
- Kalton's arXiv:math/9402206 characterizes complex interpolation stability for Hardy-type subspaces of Köthe function spaces by BMO-regularity. This again gives the right conceptual language but not a direct theorem for noncommutative conditioned martingale subspaces.
- The conditional result does not address the range \(r\leq 1\), because the current one-sided \(bmo^c\to h_r^c\) inclusion also remains unavailable there.

## Files

- `main.tex`: conditional proof packet.
- `solution_packet.pdf`: rendered PDF.
- `source_paper.pdf`: arXiv:2108.06341.
- `supporting_paper_0906.4437.pdf`: Banach endpoint \(h_1^c/bmo^c\) theorem.
- `supporting_paper_2212.08714.pdf`: \(h_\infty^c\) K-closedness and explicit complex-open note.
- `figures/open_problem_crop.png`: source open-problem excerpt copied from the previous packet.

## Human review recommendation

Review as a conditional reduction, not as a full solution. The main mathematical value is that the missing \(r>1\) reverse inclusion is now reduced first to the recognized \(h_\infty^c\) complex endpoint problem and then to a concrete conditioned endpoint interpolation/retraction problem. A full solution would still need either that conditioned endpoint theorem, a direct \(h_\infty^c\) analytic construction, or a direct analytic construction into the \(bmo^c\) endpoint.
