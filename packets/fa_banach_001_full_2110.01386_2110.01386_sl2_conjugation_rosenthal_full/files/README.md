# Full candidate solution: the conjugation action of SL2(R) is Rosenthal representable

status: full_solution_likely_valid

source_arxiv_id: 2110.01386

source_paper: Michael Megrelishvili, "Topological group actions by group automorphisms and Banach representations"

packet_path: runs/fa_banach_001/solutions/full/2110.01386_sl2_conjugation_rosenthal_full/

## Claim

Question 3.20 of the source paper has a positive answer:

\[
G=\mathrm{SL}_2(\mathbb R) \quad \Longrightarrow \quad G_c
\text{ is Rosenthal representable.}
\]

The proof is stronger: if a topological group \(G\) is a matrix group
\(G\leq \mathrm{GL}_m(\mathbb R)\) with the ambient matrix topology,
then its conjugation \(G\)-space \(G_c\) is Rosenthal representable.

## Mechanism

Embed \(G\) into the finite-dimensional vector space
\(M_m(\mathbb R)\).  Conjugation by elements of \(G\) is the restriction
of a linear action on \(M_m(\mathbb R)\).  The one-point
compactification of any finite-dimensional linear action is tame; this
is the partial-linear-map argument used in the source paper's proof of
Theorem 3.12.  The closure of \(G\) in the one-point compactification of
\(M_m(\mathbb R)\) is therefore a tame compact \(G\)-space and is a
proper \(G\)-compactification of \(G_c\).  Compact metric tame systems
are Rosenthal representable.

For \(G=\mathrm{SL}_2(\mathbb R)\), the group is closed in
\(M_2(\mathbb R)\), so the compactification is simply the Alexandrov
one-point compactification \(G\cup\{\infty\}\).

## Provenance

This packet supersedes the earlier partial packet
`2110.01386_sl2_unipotent_orbit_rosenthal`.  That partial result proved
tameness only for the unipotent conjugacy orbit.  The present proof
applies to the whole conjugation action and hence absorbs the partial
result.

This is not a literature-status packet: the source paper explicitly
states that the `SL_2(R)` case is unclear.  The packet adds the missing
ambient-linear compactification and heredity argument.

## Files

- `main.tex`: full proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: source crop of Question 3.20.
- `absorbed_packets/partial/2110.01386_sl2_unipotent_orbit_rosenthal/`: earlier partial packet now subsumed by this full proof.
