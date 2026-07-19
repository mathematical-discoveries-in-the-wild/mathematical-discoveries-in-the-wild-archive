# Partial Result: Noninteger Holder Critical Line Has No RKHS Sandwich

Status: `partial_subsumed_by_full_holder_zygmund_critical_border_map`

Supersession note: this noninteger-alpha obstruction is now subsumed by the
full Holder-Zygmund critical border packet at
`runs/fa_banach_001/solutions/full/2312.14711_holder_zygmund_critical_border_map/`,
which removes the noninteger-alpha restriction using finite differences.

Source paper: Max Scholpple and Ingo Steinwart, "Which Spaces can be Embedded in Reproducing Kernel Hilbert Spaces?", arXiv:2312.14711.

## Result

The source proves that an RKHS sandwich

```text
Hol^alpha([0,1]^d) -> H -> Hol^beta([0,1]^d)
```

is impossible when `alpha - beta < d/2`, and it leaves the critical line
`alpha - beta = d/2` open.

This packet proves a broad negative theorem on that frontier:

```text
Let d >= 1, beta > 0, alpha = beta + d/2, and alpha not be an integer.
Then the inclusion Lambda^alpha([0,1]^d) -> Lambda^beta([0,1]^d)
is not cotype 2, where Lambda^s denotes the Holder-Zygmund space
B^s_{infty,infty}.
Consequently there is no RKHS H with
Lambda^alpha([0,1]^d) -> H -> Lambda^beta([0,1]^d).
```

Here `Lambda^alpha` is the classical Holder space because `alpha` is
noninteger. The theorem only assumes the domain smoothness `alpha` is
noninteger; `beta` may be integer or noninteger, with integer target endpoints
understood in the Holder-Zygmund sense.

## Proof Mechanism

The proof stacks compactly supported dyadic smooth bumps across scales. At
scale `j`, there are about `2^{jd}` disjoint bumps, each normalized with
height `2^{-j alpha}`. Signed sums over arbitrary finite sets of these bumps
stay uniformly bounded in `C^alpha` because `alpha` is noninteger and the
highest Holder seminorm admits the usual low-scale/high-scale split.

In the target space, every bump has `C^beta` norm at least
`c 2^{-j(alpha-beta)}`. On the critical line `alpha-beta=d/2`, the square-sum
over one dyadic level is bounded below by a fixed positive constant. Taking
the first `m` levels forces the target square-sum to grow like `sqrt(m)` while
the Rademacher domain norm stays bounded. Hence the inclusion is not cotype 2.
Scholpple and Steinwart show that any intermediate RKHS sandwich would make
the inclusion 2-factorable, hence cotype 2, so no such RKHS exists.

## Remaining Frontier

This does not classify every critical Holder-to-Holder endpoint. The remaining
border cases are the integer-domain-smoothness cases `alpha in N`. These are
genuinely delicate: the bundled companion packet already shows the one
dimensional endpoint `alpha=1`, `beta=1/2` is positive via the Sobolev RKHS
`H^1([0,1])`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2312.14711.
- `figures/open_problem_crop.png`: source crop showing the border-case
  statement in the original paper.

## Novelty / Duplicate Check

The run indexes were searched for `2312.14711`, `Holder`, `critical`,
`alpha-beta=d/2`, `cotype`, and `2-factor`. Existing hits are the full
bounded-kernel endpoint packet and the one-dimensional companion partial
packet; no duplicate noninteger critical-line packet was found.

Bounded web searches on June 16, 2026 for the source title plus `border cases`,
for `Holder RKHS alpha-beta=d/2 border cases`, for `Holder-Zygmund RKHS
B_{infty,infty} border`, and for `B^s_{infty,infty} 2-factorable RKHS Holder
critical border` found the source arXiv record and nearby RKHS papers, but no
exact later answer to this noninteger Holder-to-Holder critical line.

## Human Review Recommendation

Review the multiscale bump lemma carefully. The main verification points are:
the signed `C^alpha` bound for noninteger `alpha`, the target scaling lower
bound for integer and noninteger `beta`, and the cotype-2 implication from the
source paper's RKHS factorization theorem.
