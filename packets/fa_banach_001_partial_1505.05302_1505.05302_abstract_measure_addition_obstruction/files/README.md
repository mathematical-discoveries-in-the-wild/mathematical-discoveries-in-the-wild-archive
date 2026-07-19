# Abstract-measure addition: exact obstruction reduction

Status: `partial_result_likely_valid`

## Source question

Peralta and Pfitzner, *Weak Banach-Saks property and Komlos' theorem for
preduals of JBW*-triples*, arXiv:1505.05302, page 6, ask whether addition is
sequentially jointly continuous (or jointly continuous) for the abstract
measure topology on every L-embedded Banach space. Their Theorem 3.2 proves
sequential joint continuity for JBW*-triple preduals.

## Result

The packet gives an exact two-branch obstruction to sequential joint
continuity. If addition fails on an L-embedded space, then after passing to a
subsequence there are two seminormalized asymptotically isometric `ell_1`
sequences `(x_n)` and `(y_n)` whose termwise sum `(z_n)` is seminormalized and
is of exactly one of the following types:

1. `(z_n)` is an `ell_1`-basic sequence with no almost/asymptotically
   isometric `ell_1` subsequence; every normalized weak-star cluster point
   loses norm in the singular summand.
2. `(z_n)` is weakly null. In this branch the limiting norms of `x_n` and
   `y_n` agree, and their singular weak-star limits cancel.

Conversely, either configuration forces failure of sequential joint
continuity. Thus the original problem is reduced exactly to excluding or
constructing these two geometric configurations.

The model `ell_1 direct-sum-infinity c_0` realizes the second configuration
with two isometric `ell_1` sequences. It is not L-embedded, because it is not
weakly sequentially complete, so this is a sharpness model rather than a
counterexample to the source problem.

## Scope

The packet does not decide whether either obstruction can occur in an
L-embedded space. The universal question remains open in this packet. It does
replace the topological formulation by two concrete sequence-geometric
targets and identifies the weak-null cancellation branch completely.

## Files

- `main.tex`: theorem, proof, sharpness model, and literature notes.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:1505.05302.
- `supporting_paper_math_0003154.pdf`: Pfitzner's abstract-measure-topology
  paper, arXiv:math/0003154.
- `figures/open_problem_crop.png`: source question on page 6.

## Verification

The proof is qualitative and uses no computer algebra. The main review points
are the subsequence extraction from the definition of `tau_mu`, the use of
Pfitzner's weak-star cluster criterion, and the Rosenthal/weak-sequential-
completeness dichotomy in the absence of an `ell_1` subsequence.

## Novelty check

Exact-phrase and close-variant searches were run through 19 July 2026 for
`abstract measure topology` with `addition`, `sequentially jointly
continuous`, `weakly null`, and termwise sums of asymptotically isometric
`ell_1` sequences. The searches found the source papers and applications of
the topology, but no later proof, counterexample, or this two-branch
reduction. This is bounded evidence only, not a claim of priority.

## Human review recommendation

Review as a likely valid substantial partial reduction. The most valuable
next step is to attack the weak-null cancellation branch, equivalently to ask
whether two asymptotically isometric `ell_1` embeddings into an L-embedded
space can have a seminormalized weakly null sum on the unit-vector basis.
