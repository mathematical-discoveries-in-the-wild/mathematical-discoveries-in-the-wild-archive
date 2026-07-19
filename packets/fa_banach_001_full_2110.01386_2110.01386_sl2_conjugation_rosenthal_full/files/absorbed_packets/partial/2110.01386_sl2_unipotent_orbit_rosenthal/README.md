# Absorbed partial result: the SL2 unipotent orbit is Rosenthal representable

status: absorbed_into_full_solution

source_arxiv_id: 2110.01386

source_paper: Michael Megrelishvili, "Topological group actions by group automorphisms and Banach representations"

packet_path: runs/fa_banach_001/solutions/full/2110.01386_sl2_conjugation_rosenthal_full/absorbed_packets/partial/2110.01386_sl2_unipotent_orbit_rosenthal/

absorbed_by: runs/fa_banach_001/solutions/full/2110.01386_sl2_conjugation_rosenthal_full/

absorption_note: The full packet proves that the entire conjugation action of \(\mathrm{SL}_2(\mathbb R)\) is Rosenthal representable, so this unipotent-orbit partial result is retained only as proof history.

## Claim

Let \(G=\mathrm{SL}_2(\mathbb R)\), let
\[
u=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]
and let \(H=\operatorname{St}(u)\). The homogeneous \(G\)-space
\(G/H\), identified with the conjugacy orbit of \(u\) inside \(G_c\),
is Rosenthal representable.

Equivalently, the particular unipotent orbit used in the source paper
to prove non-reflexive representability is nevertheless Rosenthal
representable. Together with the source paper's Corollary 4.3, this
gives a natural \(G/H\) which is Rosenthal representable but not
reflexively representable.

## Scope

This does not answer Question 3.20 of the source paper: whether the
entire conjugation \(G\)-space \(G_c\) is Rosenthal representable for
\(G=\mathrm{SL}_2(\mathbb R)\). Tameness of this single orbit/factor is
not enough to imply tameness of the whole conjugation action.

The result partially addresses the homogeneous-space direction in
Question 4.4 and narrows the main frontier by showing that the standard
unipotent non-WAP obstruction is not a non-Rosenthal obstruction.

## Provenance

This is not a literature-status packet. The source paper proves that
the linear \(\mathrm{GL}_2(\mathbb R)\)-action on \(\mathbb R^2\) is
Rosenthal representable and notes that the unipotent conjugacy orbit is
a locally compact coset \(G/H\). The packet adds the explicit
\(\mathrm{SL}_2(\mathbb R)\)-equivariant factor map from the one-point
compactification of \(\mathbb R^2\) onto the one-point compactification
of that unipotent orbit.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/question_3_20_crop.png`: source crop of the main `SL_2(R)` question.
- `figures/coset_question_4_4_crop.png`: source crop of the stabilizer/coset passage and Question 4.4.
