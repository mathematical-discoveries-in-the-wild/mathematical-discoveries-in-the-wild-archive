# Counterexample: product groups do not have arbitrarily slow proper `L^p` cocycles

Status: `counterexample_likely_valid`

Source: Antonio Lopez Neumann and Juan Paucar, *On growth of cocycles of
isometric representations on `L^p`-spaces*, arXiv:2501.12808v2.

Target: Question 1 in Section 6 asks whether a compactly generated locally
compact group that is `a-FL^p`-menable for some `p>2`, is not a-T-menable, and
does not have property `(T)`, must have arbitrarily slow proper cocycles in
`L^p`.

Result: No. If `B` is a noncompact property `(T)` group that admits a proper
affine isometric action on an `L^p`-space, and `A` is a noncompact
`a-FL^p`-menable group without property `(T)`, then `G=A x B` satisfies the
hypotheses of Question 1 but fails the conclusion. In particular, for suitable
large `p`, the source paper's listed examples `SO(n,1) x Sp(m,1)` are
counterexamples.

Mechanism: choose a proper control function on `A x B` that grows
logarithmically in the `B`-direction. Any proper cocycle bounded by that
function would restrict to an unbounded `L^p`-cocycle of the property `(T)`
factor `B`, but the source paper's Theorem D gives an `n^{1/p}` lower bound
on convolution averages for every unbounded `L^p`-cocycle of such a group.
Compactly supported random walk averages are at most logarithmic under the
chosen control function, a contradiction.

Files:

- `main.tex` - proof packet source.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - locally rendered source PDF from the arXiv TeX source.
- `figures/open_problem_crop.png` - page crop containing Question 1.

Novelty check: cheap run indexes were searched for arXiv:2501.12808 and exact
phrases around "arbitrarily slow proper cocycles"; no prior packet was found.
Web searches on 2026-07-03 for the exact question and close variants found the
source paper but no later exact resolution.
