# Hilbert Compression Gap Log Dichotomy

Status: likely valid source-convention answer to Question 5.22; the packet
flags the stricter proper-lower-function reading for human review.

Source target: arXiv:math/0612378, Question 5.22, asking whether every
finitely generated group has a Hilbert space compression gap of the form
`(f/log x, f)`.

## Result

For every infinite finitely generated group `G` that admits a uniform/coarse
embedding into Hilbert space, there is a proper increasing function `f` such
that, in the source paper's large-scale compression-gap convention, `G` has a
Hilbert space compression gap

```text
(f/log x, f).
```

If one reads Definition 3.3 as requiring the lower function `f/log x` itself
to be proper, then non-Hilbert-embeddable finitely generated groups are
immediate counterexamples to the literal "every finitely generated group"
statement, and the positive theorem gives a proper lower gap exactly when the
annular envelope produced below dominates `log x`.

## Proof Idea

For each dyadic annulus

```text
2^k <= d(x,y) < 2^{k+1},
```

let `H_k` be the best possible Hilbert separation that any 1-Lipschitz map can
force on that whole annulus.  If `G` coarsely embeds into Hilbert space, then
`H_k -> infinity`.

Set

```text
F_k = inf_{j >= k} H_j.
```

The tail infimum makes `F_k` increasing and still proper.  It is also an upper
bound, up to the source paper's comparison relation, for every Hilbert
compression function: a lower control at scale `2^j` cannot exceed the best
annular separation `H_j`.

For the lower bound, choose almost extremal 1-Lipschitz maps on each annulus
and take their Hilbert direct sum with coefficients `1/k`.  The square-sum of
`1/k` is finite, so the sum is Lipschitz.  On the `k`-th annulus, the `k`-th
coordinate alone gives separation at least `H_k/k >= F_k/k`, which is exactly
the desired single logarithmic loss.

## Scope and Caveat

The source paper already notes known finitely generated groups that do not
uniformly embed into Hilbert space.  Such groups cannot have any proper
Hilbert compression gap under the strict Definition 3.3 reading.  The new
content is the positive logarithmic-envelope theorem for every
Hilbert-coarsely-embeddable finitely generated group.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: arXiv:math/0612378 source paper.
- `figures/open_problem_crop.png`: crop of Question 5.22.
- `tmp/source.tex`: source TeX used for verification.

## Novelty Check

Searched the run indexes for `0612378`, `compression functions`, `uniform
embeddings`, `compression gap`, and nearby keywords; no duplicate packet was
found.  External searches for exact phrases such as `Hilbert space compression
gap f/log`, `compression gap coarsely embeds Hilbert log`, and citation
metadata for arXiv:math/0612378 did not reveal a later paper explicitly
answering Question 5.22.

## Review Focus

Please check:

- the annular definition of `H_k`;
- that `F_k=inf_{j>=k}H_j` is proper when `G` Hilbert-coarsely embeds;
- the upper-bound argument for arbitrary Hilbert lower controls;
- the Hilbert direct-sum construction with coefficients `1/k`;
- the interpretation of the literal question versus the uniformly embeddable
  version.
