# Partial packet: p-Lorentz core reverse inclusion for the endpoint complex BMO problem

status: partial result, likely valid  
source: arXiv:2108.06341, Narcisse Randrianantoanina, "Interpolation between noncommutative martingale Hardy and BMO spaces: the case 0<p<1"  
supporting sources: arXiv:2212.08714 and arXiv:0906.4437  
run: fa_banach_001  
agent: agent_lane_00  
date: 2026-06-16

## Claim

Let \(0<p<1\), \(0<\theta<1\), and \(1/r=(1-\theta)/p\), with \(r>1\). Then
\[
\mathsf h_{r,p}^c(\mathcal M)
\hookrightarrow
[\mathsf h_p^c(\mathcal M),\mathsf h_\infty^c(\mathcal M)]_\theta
\hookrightarrow
[\mathsf h_p^c(\mathcal M),\mathsf{bmo}^c(\mathcal M)]_\theta
\hookrightarrow
\mathsf h_r^c(\mathcal M).
\]
Here \(\mathsf h_{r,p}^c\) is the column conditioned Hardy space associated with
the Lorentz space \(L_{r,p}\).

This gives an unconditional Lorentz-core part of the missing reverse inclusion.
It does not prove the full reverse inclusion from \(\mathsf h_r^c\).

## Proof idea

The 2022 Cuculescu/K-closedness theorem proves the real interpolation identity
\[
(\mathsf h_p^c,\mathsf h_\infty^c)_{\theta,p}
=\mathsf h_{r,p}^c .
\]
The couple \((\mathsf h_p^c,\mathsf h_\infty^c)\) is \(p\)-Banach, and for a
\(p\)-Banach couple the real interpolation space with summability index \(p\)
embeds into the complex interpolation space. Applying this gives the first
inclusion.
The endpoint embedding \(\mathsf h_\infty^c\hookrightarrow \mathsf{bmo}^c\)
gives the second by functoriality. The last inclusion is the previously
packaged one-sided \(r>1\) Wolff/Banach-endpoint argument.

## Limitations

The result captures \(L_{r,p}\)-Lorentz square functions, not all
\(L_r\)-square functions. Since \(L_{r,p}\subsetneq L_r\) in general, this is a
proper core theorem rather than a full endpoint solution. This corrects an
over-optimistic intermediate \(L_{r,1}\) formulation: in the quasi-Banach range,
the safe analytic-series embedding uses the \(p\)-summability exponent.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered PDF.
- `source_paper.pdf`: arXiv:2108.06341.
- `supporting_paper_2212.08714.pdf`: real endpoint \(h_p^c/h_\infty^c\) theorem.
- `supporting_paper_0906.4437.pdf`: Banach \(h_1^c/bmo^c\) endpoint theorem.
- `figures/open_problem_crop.png`: source open-problem excerpt.

## Human review recommendation

Review as an unconditional partial theorem. The key checks are the
\(p\)-Banach real-to-complex embedding
\((A_0,A_1)_{\theta,p}\hookrightarrow[A_0,A_1]_\theta\) and the use of the
2022 real interpolation identity with Lorentz parameter \(p\).
