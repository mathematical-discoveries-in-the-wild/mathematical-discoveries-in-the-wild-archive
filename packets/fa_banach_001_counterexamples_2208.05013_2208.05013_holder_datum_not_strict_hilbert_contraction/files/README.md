# Holder datum counterexample to strict Hilbert contraction

Status: likely valid narrow counterexample.

Source: arXiv:2208.05013, Max Fathi, Samuel Sra, and Melanie Weber, *Computing Brascamp-Lieb Constants through the lens of Thompson Geometry*.

## Result

The unqualified Section 6 question asking whether the normalized Picard map
`\tilde G=G/||G||` is strictly contractive in Hilbert's projective metric is
false on feasible Brascamp-Lieb data.

For the feasible Holder datum in dimension `d>=2`,

```text
A_1 = A_2 = I_d,   w_1 = w_2 = 1/2,
```

the source map satisfies `G(X)=X` for every positive definite `X`.  Since
Hilbert's projective metric is invariant under positive scalar normalization,
`\tilde G` preserves every Hilbert projective distance.  Taking
`X=diag(2,1)` and `Y=I_2` gives equality at distance `log 2 > 0`, so strict
contractivity fails.

## Scope

This is a literal/general feasible-datum counterexample.  It does not refute a
possible intended version restricted to simple Brascamp-Lieb data: the Holder
datum is feasible but not simple, because every nonzero proper subspace is
critical.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local build of the arXiv source paper.
- `figures/open_problem_crop.png`: crop of the Section 6 open-question passage.
- `code/verify_holder_identity.py`: exact numerical sanity check for the
  displayed `2 x 2` witness.

## Novelty Check

Local run indexes were searched for arXiv:2208.05013, the paper title,
`Brascamp-Lieb`, `Thompson Geometry`, `Hilbert projective`, and
`strictly contractive`; no exact prior packet or attempt was found.  A bounded
web search on 2026-07-03 for the exact open-question phrases, arXiv id, and
`Brascamp-Lieb Hilbert projective strictly contractive tilde G` found no
separate answer source.  Novelty confidence is moderate: the counterexample is
elementary and deliberately scoped to the unqualified statement.

## Human Review Recommendation

Check whether the intended reading of the source question silently assumes
simple data.  If yes, reclassify this as a literal-scope caveat rather than a
resolution of the simple-data problem.  If the question is read as stated for
general feasible data, the counterexample is complete.
