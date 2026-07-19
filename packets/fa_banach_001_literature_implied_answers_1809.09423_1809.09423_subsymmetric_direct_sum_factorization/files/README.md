# Literature Implied Answer: Subsymmetric direct-sum factorization

Status: `literature_implied_answer (partial direct-sum variant)`

## Source Problem

- Source paper: Richard Lechner, Pavlos Motakis, Paul F. X. Mueller, and Thomas
  Schlumprecht, "Strategically reproducible bases and the factorization
  property", arXiv:1809.09423.
- Location: Section 8, Problem 8.1, page 32 of the downloaded PDF.
- Question: if `X` and `Y` have bases with the factorization property, does the
  union of the two bases, in the right order, have the factorization property in
  the complemented sum of `X` and `Y`?

## Supporting Literature

- Supporting paper: Richard Lechner, "Subsymmetric bases have the factorization
  property", arXiv:2011.09915.
- Supporting theorem: Theorem 2.3, page 4 of the downloaded PDF.
- Theorem 2.3 proves that, for a sequence of Banach spaces whose coordinate
  bases satisfy the paper's dual-pair hypotheses `(B1)--(B5)` uniformly and are
  uniformly subsymmetric and non-`ell^1`-splicing, the array basis
  `(e_{n,j})_{n,j}` has the factorization property in `ell^p((X_n))` for every
  `1 <= p <= infinity`.

## Scope

This packet does not claim a full answer to Problem 8.1.  It records a later
literature theorem giving a positive direct-sum analogue under stronger
structural hypotheses: uniformly subsymmetric, non-`ell^1`-splicing coordinate
bases in `ell^p` direct sums.

The following remain outside the packet:

- arbitrary bases with the factorization property;
- arbitrary complemented sums not identified with the `ell^p` direct-sum model;
- the other final-section questions in arXiv:1809.09423, including uniform
  factorization, strategic reproducibility of the `L^1(L^1)` bi-parameter Haar
  system, the Tsirelson-space basis question, and the `L^p(L^1)`/`L^1(L^p)`
  Haar questions.

## Evidence Files

- `source_paper.pdf`: arXiv:1809.09423.
- `supporting_paper_2011.09915.pdf`: arXiv:2011.09915.
- `figures/open_problem_crop.png`: Problem 8.1 from the source paper.
- `figures/supporting_theorem_crop.png`: Theorem 2.3 from the supporting paper.

## Bounded Search Notes

- Lightweight run indexes searched before packaging:
  `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and
  `proof_gaps/index.tsv`.
- Search phrases included: `1809.09423`, `Strategically reproducible`,
  `factorization property`, `reproducible bases`, `Tsirelson`, `subsymmetric`,
  and `unit vector basis in T`.
- No existing run packet or attempt covered this exact
  arXiv:1809.09423 / arXiv:2011.09915 direct-sum identification.

## Human Review Recommendation

Check whether the reviewer agrees that Lechner's `ell^p((X_n))` theorem should
be recorded as a partial direct-sum variant of Problem 8.1, rather than as a
full solution to the original complemented-sum question.
