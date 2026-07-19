# Candidate Full Solution: Almost Nonexpansive Null Minimal Displacement for Q1

Status: human reviewed; proof appears correct, with author follow-up
recommended.

## Source

- arXiv:2307.12958
- Title: "Retraction methods and fixed point free maps with null minimal displacements on unit balls"
- Authors: Cleon S. Barroso and Valdir Ferreira
- Area: Banach spaces, metric fixed point theory
- Source PDF: `source_paper.pdf`
- ArXiv evidence crop: `figures/open_problem_crop.png`
- Journal/published-formulation crop supplied in the review thread:
  `figures/journal_question_crop.png`

No separate public journal PDF was located during the follow-up search. The
arXiv record currently lists only the arXiv DOI and has no journal reference.
The packet therefore keeps the original arXiv PDF as `source_paper.pdf` and
stores the user-supplied journal-formulation screenshot separately.

## Extracted Question

In the introduction, after citing Lin--Sternfeld's theorem that every noncompact
bounded closed convex set `K` in a Banach space admits a Lipschitz self-map with
positive minimal displacement, the authors ask:

`(Q1)` Is there a Lipschitz map `T: K -> K` with `d(T,K)=0` and no fixed point?

The journal/published formulation seen in the follow-up screenshot poses a
slightly different Q1: for every infinite-dimensional Banach space `X` and
every `epsilon>0`, do there exist `K in B(B_X)` and a `(1+epsilon)`-Lipschitz
map `T:K -> K` with `d(T,K)=0` and no fixed point?

The paper states that its own Theorem 4.1 only "particularly" solves `(Q1)` in
every Banach space by producing some suitable `K`.

Quantifier distinction:

- The source question as written asks: for every noncompact `K`, does there
  exist such a map on that same `K`?
- The source paper's Theorem 4.1 proves: for every Banach space `X`, there
  exists at least one suitable `K` in `B_X` with such maps; if `X` contains a
  complemented basic sequence, that `K` can be `B_X`.

The paper's Theorem 4.1 answers the journal formulation by producing a suitable
`K`. This packet proves a stronger statement that supersedes both the arXiv-body
formulation and the journal formulation: the same conclusion holds for every
preassigned noncompact bounded closed convex `K`, with `(1+epsilon)` Lipschitz
control.

## Claimed Result

Let `K` be any noncompact bounded closed convex subset of a real Banach space.
For every `epsilon>0`, there exists a `(1+epsilon)`-Lipschitz self-map
`G_epsilon:K -> K` with no fixed point and `d(G_epsilon,K)=0`.

The construction starts with the Lin--Sternfeld positive-displacement map
`F:K -> K`, then damps the displacement `F(x)-x` by a positive Lipschitz scalar
`lambda(x)` whose infimum on `K` is zero:

`G_epsilon(x) = x + c lambda(x)(F(x)-x)`.

The scalar `c>0` is chosen small enough to make the Lipschitz constant at most
`1+epsilon`. Because `c lambda(x)>0` everywhere, fixed points are not
introduced. Because `lambda` tends to zero along a separated sequence, the
minimal displacement of `G_epsilon` is zero.

## Verification Notes

- No numerical or finite search verification was used.
- The proof is a metric/Banach-space construction and uses only:
  - Lin--Sternfeld's theorem as cited in the source paper.
  - Noncompact complete bounded metric spaces are not totally bounded, hence
    contain a separated sequence.
  - The McShane Lipschitz extension formula.
  - Convexity and boundedness of `K`.

## Limitations

- This packet answers `(Q1)` only.
- It does not answer `(Q2)`, because the constructed map need not have uniformly
  Lipschitz iterates. Even `Lip(G_epsilon)<=1+epsilon` only gives the naive
  bound `Lip(G_epsilon^n)<=(1+epsilon)^n`.
- The strengthened theorem implies the journal Q1 with `K=B_X` for every
  infinite-dimensional `X`, since `B_X` is noncompact, bounded, closed, and
  convex.

## Human Review Recommendation

Human review completed. The proof appears correct. The idea is to start with a
Lipschitz fixed-point-free map `F` with positive minimal displacement and then
modify it by a positive Lipschitz damping scalar `lambda` whose infimum is zero.
This preserves the absence of fixed points while forcing
`d(G_epsilon,K)=0`, and the scaling parameter gives the
`(1+epsilon)`-Lipschitz bound.

The solution appears to be more general than what was asked: it gives the
conclusion for every preassigned noncompact bounded closed convex `K`, not just
for the existence of some suitable `K`. Author follow-up is recommended to
confirm the intended formulation and assess the value of the observation.

Additional files:

- `human_review.tex`: human verification note source.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: solution packet followed by the human verification
  note.
