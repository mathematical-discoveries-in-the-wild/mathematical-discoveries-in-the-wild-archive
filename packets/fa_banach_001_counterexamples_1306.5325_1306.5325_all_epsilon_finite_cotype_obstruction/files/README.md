# Counterexample packet: finite cotype is not enough for all small radii

status: candidate_counterexample_likely_valid

Source: Gilles Pisier, "On the metric entropy of the Banach-Mazur compactum",
arXiv:1306.5325.

Target: after observing that the condition

`log log N(S_n(X), d, 1 + epsilon) in o(n)`

for some `epsilon > 0` implies finite cotype, Pisier asks whether the converse
holds and formulates the problem of characterizing spaces satisfying the
condition "for some (or all) epsilon > 0".  The relevant source passage is on
PDF page 9 and TeX lines 570-585.

Result: the finite-cotype converse is false for the "all epsilon" version.
For every fixed `epsilon_0 > 0` there is an infinite-dimensional Banach space
`X_{epsilon_0}`, isomorphic to `ell_1` and hence of cotype 2, such that

`liminf_n (1/n) log log N(S_n(X_{epsilon_0}), d, 1 + epsilon_0) > 0`.

Thus no characterization for the all-radii version can be merely "finite
cotype", and the all-radii property is not invariant under equivalent
renorming: standard `ell_1` has the small entropy property at every fixed
radius by Bourgain-Lindenstrauss-Milman as cited in the source, while the
renormed `ell_1` built here fails at the prescribed radius.

Scope caveat: this packet does not solve the "some epsilon" version of
Pisier's problem.  In fact the constructed space is isomorphic to `ell_1`, so
the usual BLM argument transfers to give small entropy at sufficiently large
covering radii.  The packet is a counterexample to the all-epsilon finite
cotype converse, and a structural obstruction for any solution of the full
characterization problem.

Method: fix `s = 1 + epsilon_0`.  Pisier's local entropy theorem, applied with
center `ell_1^n` and any `R > s^2`, gives for all large `n` a family
`{E_{n,a}}` of at least `exp exp(c n)` many `n`-dimensional spaces, all
`R`-isomorphic to `ell_1^n`, and mutually separated by Banach-Mazur distance
greater than `s^2`.  Put all these spaces as coordinate summands in an
`ell_1`-direct sum.  The resulting space is `R`-isomorphic to `ell_1`, but
`S_n(X)` contains the entire separated family.  A ball of radius `s` cannot
contain two members of a family separated by more than `s^2`, so the covering
number at radius `s` is double exponential.

Files:
- `main.tex`: full proof note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1306.5325.
- `figures/open_problem_crop.png`: crop of the finite-cotype remark and open
  problem from PDF page 9.

Novelty check: cheap run indexes were searched for `1306.5325`, `S_n(X)`,
`SQ_n(X)`, `Banach-Mazur compactum`, `metric entropy`, and `finite cotype`;
no existing packet or attempt for this exact target appeared.  Exact-phrase
web searches for the problem and `S_n(X)`/`SQ_n(X)` did not surface a known
answer.  Novelty confidence is moderate pending human review, because the
argument is short and uses a theorem from the source paper itself.

Human review recommendation: verify the quantifier scope.  The proof appears
solid for the all-epsilon variant and the non-invariance observation, but it
should not be promoted as a solution of the some-epsilon characterization.
