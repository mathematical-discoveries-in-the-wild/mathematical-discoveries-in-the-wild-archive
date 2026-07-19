# Verifier report

Status: **PASS for the stated real-scalar full characterization; human expert review required.**

Target: Question 6.6 of arXiv:2210.05114, asking which Banach spaces admit an isometric embedding into some `C(K)` whose image fails stable phase retrieval.

## Claim-by-claim audit

1. **Real overlap/SPR equivalence — pass.** For real lattice elements, `abs(abs(u+v)-abs(u-v)) = 2(abs(u) wedge abs(v))`. Substituting `f=u+v`, `g=u-v` converts the SPR inequality exactly into `min(||u||,||v||) <= C ||abs(u) wedge abs(v)||`. Normalizing the smaller vector and using monotonicity of the lattice infimum proves that the optimal constant is the reciprocal of the unit-sphere overlap. No factor two is lost.

2. **Universal extreme-boundary lower bound — pass.** Hahn–Banach makes `J*:M(K)->E*` a metric quotient. In the fibre over an extreme `e*`, an extreme measure is also extreme in the whole measure ball; over the reals it is a signed point mass. Thus every extreme functional is a signed evaluation of every isometric `C(K)` representation, exactly as in source Lemma 6.8.

3. **Canonical compactum — pass.** `K_E=weak-star closure(ext B_{E*})` is a compact Hausdorff subset of the weak-star compact dual ball. Evaluation at each `x in E` is weak-star continuous. Krein–Milman implies that the extreme points norm `E`, so the evaluation map `J_E:E->C(K_E)` is a linear isometry, without separability or metrizability assumptions.

4. **Attainment of the lower bound — pass.** For fixed unit `x,y`, the function `e* -> min(abs(e*(x)),abs(e*(y)))` is weak-star continuous. Its supremum over the closure equals its supremum over the extreme points. Taking the infimum over unit pairs proves `ov(J_E)=Delta(E)` exactly.

5. **Necessary and sufficient criterion — pass.** Every isometric embedding has overlap at least `Delta(E)`, while the canonical embedding has overlap exactly `Delta(E)`. Hence a non-SPR isometric embedding exists if and only if `Delta(E)=0`. The canonical embedding witnesses the converse.

6. **Worst-case constant — pass.** Since the optimal SPR constant of an embedding is exactly the reciprocal of its overlap, all embeddings have constant at most `1/Delta(E)` and the canonical embedding attains equality. The convention `1/0=infinity` correctly includes non-SPR spaces.

7. **Finite-dimensional corollary — pass.** Compactness of the product of unit spheres and of the closed extreme boundary makes the defining infimum attain its value. Zero overlap is therefore equivalent to one fixed pair for which every extreme functional annihilates at least one member.

## Scope and adversarial failure modes

- The theorem is restricted to **real** Banach spaces. For complex SPR, absence of almost-disjoint pairs is not a sufficient characterization, so the proof must not be transferred verbatim.
- The result is isometric, as is the source question. `Delta(E)` need not be invariant under arbitrary Banach-space isomorphisms.
- The compact space `K_E` can be nonmetrizable; Question 6.6 permits arbitrary compact Hausdorff `K`.
- The criterion is intrinsic but uses the extreme boundary of the dual ball. A reviewer may judge that the informal phrase “which Banach spaces” sought a classification in more familiar geometric classes; this is a scope/interpretation question, not a gap in the equivalence proved.
- The one-sided inequality is already source Lemma 6.8. The new logical content is sharp canonical attainment, the reverse implication, and the exact optimal-constant formula.

## Novelty audit

Local run indexes and bounded exact-phrase/title/author searches were checked. Full text relevant to arXiv:2504.06693, 2512.08110, and 2512.08114 was searched. No matching extreme-boundary attainability theorem or resolution of source Question 6.6 was located. This is not an exhaustive originality guarantee.

## Recommended human checks

1. Verify the intended meaning of “which Banach spaces” in Question 6.6 and whether an intrinsic necessary-and-sufficient invariant is accepted as a full answer.
2. Recheck the strict-quotient fibre argument for arbitrary compact Hausdorff `K`.
3. Search for the canonical extreme-boundary construction under the terminology “boundary”, “James boundary”, or “Choquet boundary”.
