# Bounded Dyadic Profiles with Full Absolute Achievement Set

status: partial_result_likely_valid

source: arXiv:1802.10535, Jacek Marchwicki and V\'aclav Vlas\'ak, "Subsums of conditionally convergent series in finite dimensional spaces"

packet: `runs/fa_banach_001/solutions/partial/1802.10535_bounded_dyadic_profiles_full_absolute_achievement/solution_packet.pdf`

## Result

Fix `0 < alpha < 1`. Let `odd(n)` be the odd part of `n`, and let `a` be any positive function on the odd integers bounded above and away from zero. Then the sequence

`u_n = (-1)^(n+1) (1/n, a(odd(n))/n^alpha)`

has full absolute achievement set: `A_abs(u_n) = R^2`.

Equivalently, this gives a positive answer to the source paper's Problem 3.1 for every `f(n) = n^alpha / a(odd(n))` with a bounded positive odd-part profile.

The packet also gives a genuinely conditionally convergent non-power family: take `a(k)=A` for odd `k=1 mod 4` and `a(k)=B` for odd `k=3 mod 4`. When `A != B`, `f` is not a constant multiple of a power.

## Proof Mechanism

- Exact dyadic scaling on each odd-part ray constructs horizontal blocks whose second coordinate cancels.
- Whole dyadic rays construct pure negative vertical blocks.
- A sparse exact harmonic-subsum lemma makes the horizontal construction absolutely summable.
- A greedy subsum lemma fills the vertical coordinate.
- A finite subsum moves any target into the quadrant reached by the two block constructions.

## Scope

This is a partial sufficient family, not a characterization of all functions in Problems 3.1 and 3.2. The theorem does not require the full vector series to converge; the separate two-valued corollary verifies conditional convergence for an explicit non-power family.

## Verification

- The proof is self-contained apart from the standard no-gap subsum argument, which is reproved in the packet.
- The source-paper question crop is in `figures/open_problem_crop.png`.
- The source PDF is stored as `source_paper.pdf`.
- No computational proof step is used.

## Novelty Check

The run indexes were searched for arXiv:1802.10535, achievement sets, odd parts, dyadic profiles, and the displayed family. Bounded primary-source searches checked the source paper and arXiv:1604.07575 and arXiv:1705.06472. No exact bounded odd-part-profile theorem was found.

## Human Review Recommendation

Review as a likely valid partial theorem. Check especially the sparse exact harmonic-sum lemma, disjointness and absolute cost of the dyadic blocks, and the finite shift into the southeast quadrant.
