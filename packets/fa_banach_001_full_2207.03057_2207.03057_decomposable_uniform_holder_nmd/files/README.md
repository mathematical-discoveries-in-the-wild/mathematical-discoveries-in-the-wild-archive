# Candidate Full Subquestion Solution: Uniform Holder Nonexpansive Maps

Run: `fa_banach_001`

Source paper: Cleon S. Barroso, "Holder-contractive mappings, nonlinear
extension problem and fixed point free results", arXiv:2207.03057.

Target: final Open Questions, items `(2)` and `(3)` on page 19.

Status: human reviewed; proof appears correct. This gives affirmative answers
for every decomposable Banach space covered by the input uniformly Lipschitzian
construction, including the Hilbert-isomorphic case, the unconditional-basis
case, and the James-space case. The arbitrary reflexive case remains open here.

## Claim

For every `alpha in (0,1)`, if `X` is decomposable as `X=Y \oplus Z` with
both `Y` and `Z` infinite-dimensional, then `B_X` admits a fixed-point-free
uniformly `alpha`-Holder nonexpansive self-map with null minimal displacement.

Consequently:

- the source paper's item `(2)` has an affirmative answer for every
  infinite-dimensional Banach space isomorphic to a Hilbert space;
- item `(3)` has an affirmative answer for every infinite-dimensional Banach
  space with an unconditional basis, hence in particular for every reflexive
  space with an unconditional basis.
- the James-space case is also covered, since James space is decomposable. This
  consequence was missed in the automatic packet.

## Packet Files

- `source_paper.pdf`: local copy of the arXiv PDF.
- `figures/open_problem_crop.png`: crop of the final open questions.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet, if LaTeX rendering succeeds.
- `human_review.tex`: human verification note source.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: solution packet followed by the human verification
  note.
- `code/verify_scaling_lemma.py`: numerical sanity check for the scalar
  scaling inequality used in the proof.

## Main Dependency

The proof uses the already-packaged decomposable-space result from
`solutions/partial/2307.12958_decomposable_tube_uniformly_lipschitz_q2/`:
if `X=Y \oplus Z` with both summands infinite-dimensional, then `B_X` carries
a fixed-point-free uniformly Lipschitzian self-map with null minimal
displacement.

The new step is a small-ball scaling lemma that converts such a map into a
uniformly `alpha`-Holder nonexpansive map with constant `1`.

## Human Review

Human review completed. The proof appears correct and the method is sound. The
key point is that a previous packet already supplied the fixed-point-free
uniformly Lipschitzian map with null minimal displacement on the unit ball of
every decomposable Banach space. The present packet then performs a small-ball
scaling argument to obtain a uniformly `alpha`-Holder nonexpansive map.

The review also notes a bibliographic typo in the automatic packet: the source
paper is authored only by Cleon S. Barroso, not by Cleon S. Barroso and Valdir
Ferreira.

The central estimate is: for a radial retraction `R_r` with Lipschitz constant
at most `2`, the iterates satisfy

```text
||V^n x - V^n y|| <= min(2M ||x-y||, 2r),
```

where `M = sup_n Lip(U^n)`. The choice of `r` makes the right-hand side at
most `||x-y||^alpha` for all `x,y in B_X`.
