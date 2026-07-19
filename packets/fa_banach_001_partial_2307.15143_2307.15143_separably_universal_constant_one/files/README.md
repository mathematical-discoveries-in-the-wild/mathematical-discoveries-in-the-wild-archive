# Separably Universal Spaces Have Constant-One Finite Determination

Status: `partial_result_likely_valid`

Source paper: Florin Catrina and Mikhail I. Ostrovskii, "Finite determination
for embeddings into Banach spaces: new proof, low distortion",
arXiv:2307.15143.

Source question: Problem 1 in Section 4 asks whether the `(3+epsilon)` in
Theorem 1.6 can be replaced by `(1+epsilon)`. The paper notes that this is the
same issue raised as Problem 5.1 in Ostrovska--Ostrovskii 2019.

## Result

Let `X` be separably isometrically universal, meaning every separable Banach
space admits a linear isometric embedding into `X`. Then `X` has sharp
constant-one finite determination for locally finite metric spaces:

If every finite subset of a locally finite metric space `M` embeds into `X`
with distortion at most `C`, then `M` itself embeds into `X` with distortion at
most `C`.

In particular, `D(C[0,1]) = 1` in the finite-determination sense of the source
question. The same applies to any Banach space containing an isometric copy of
a separably isometrically universal Banach space.

## Proof Idea

The standard finite-determination ultraproduct argument embeds `M` with the
same distortion into an ultrapower of `X`. Since `M` is locally finite, it is
countable, so the closed linear span of the ultrapower image is separable.
Separably isometric universality of `X` brings that separable Banach space back
into `X` by a linear isometry, without changing any metric distances.

## Novelty Check

Cheap indexes showed the existing packet
`1510.05974_lp01_finite_determination_constant_one`, which proves the analogous
constant-one result for `L_p[0,1]`, and an older no-promotion attempt on
finite subsets of `ell_p`. No prior packet covered `C[0,1]` or the general
separably universal mechanism. Web/arXiv searches for exact phrases involving
`D(C[0,1])`, `finite determination`, `C[0,1]`, `separably universal`, and
`locally finite metric spaces` found no explicit literature answer to this
subcase.

## Scope

This is a partial negative result for the source problem: separably universal
spaces cannot witness a strict finite-determination gap. The broad question
whether there exists any Banach space `X` with `D(X)>1^+` remains open.

## Packet Contents

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: local copy of arXiv:2307.15143.
- `figures/open_problem_crop.png`: crop of Problem 1 from page 15 of the
  source PDF.
