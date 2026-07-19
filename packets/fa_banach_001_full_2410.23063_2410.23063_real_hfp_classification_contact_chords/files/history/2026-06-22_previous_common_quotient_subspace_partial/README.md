# Candidate Partial Result: Common Quotient-Subspace Obstruction For HFP

Status: `candidate partial`

Source paper: Guillaume Aubrun and Alexander Muller-Hermes, *Limit formulas
for norms of tensor power operators*, arXiv:2410.23063.

## Target

Conjecture 5.2 of the source paper asks whether a pair `(X,Y)` of real Banach
spaces has the Hilbert space factorization property (HFP) only in the trivial
cases where `X` or `Y` is a Hilbert space. The source also gives the equivalent
two-dimensional convex-body formulation as Conjecture 5.5.

This packet proves a common quotient-subspace subcase. It is not a full answer
to Conjecture 5.2.

## Result

Let `X` and `Y` be real Banach spaces. Suppose there is a finite-dimensional
real Banach space `E` which is not Hilbertian, such that `E` is isometric to a
quotient of `X` and also isometric to a subspace of `Y`. Then `(X,Y)` fails
HFP.

In particular, every finite-dimensional non-Hilbert real Banach space `E`
gives a diagonal obstruction: `(E,E)` fails HFP. In the two-dimensional
convex-body formulation, the conjecture is true in the linearly equivalent
case: if `K` and `L` are linearly equivalent centrally symmetric planar convex
bodies and one is not an ellipse, then the hypothesis of Conjecture 5.5 fails.

## Proof Intuition

The source proves that HFP is inherited by quotients of the domain and
subspaces of the range. Thus any common finite-dimensional quotient-subspace
`E` would itself have to make `(E,E)` an HFP pair. But the identity on `E`
measures exactly the Banach-Mazur distance from `E` to Euclidean space through
the Hilbert factorization norm. A non-Hilbert finite-dimensional `E` has
distance strictly larger than one, while the operator norm of its identity is
one.

## Evidence And Files

- `source_paper.pdf`: local copy of arXiv:2410.23063.
- `figures/hfp_conjecture_crop.png`: source Conjecture 5.2 on PDF page 9.
- `figures/open_problem_crop.png`: source Conjecture 5.5 on PDF page 10.
- `main.tex`: full packet proof.
- `solution_packet.pdf`: rendered proof packet.

## Search Bounds

Before packaging, the cheap indexes were searched for `2410.23063`, HFP,
Hilbert space factorization, nuclear tensorization, tensor power operators,
and convex-body ellipse formulations. A web search for the exact HFP
conjecture language and local corpus search for the HFP/NTP terminology found
the source paper and the earlier Aubrun--Muller-Hermes tensor-power paper, but
no indexed run packet for this target and no obvious later answer to the real
HFP conjecture.

## Limitations

The result only applies when the same non-Hilbert finite-dimensional Banach
space appears as a quotient of `X` and a subspace of `Y`. The general case of
two unrelated non-Hilbert spaces remains open here.

## Human Review Notes

Recommended checks:

- Verify the use of the source inheritance proposition for HFP under quotients
  and subspaces.
- Verify that `gamma_2(id_E)` equals the Banach-Mazur distance from finite-
  dimensional `E` to Euclidean space.
- Confirm that this should be counted only as a partial subcase, not as a
  full solution of Conjecture 5.2.

