# Counterexample Packet: 1612.03808 Remark 3.3

Status: `counterexample_likely_valid`

Source: Antonin Prochazka and Abraham Rueda Zoca, "A characterisation of octahedrality in Lipschitz-free spaces", arXiv:1612.03808.

Target: Remark 3.3 asks whether assertion (3), a relaxed extension property with constant `1/(1-r-epsilon)`, implies assertion (1), the corresponding Whitley-thickness/molecule assertion with lower bound `2-r-epsilon`.

Claim: No. For `r=2/5`, the metric space from the source paper's Example 3.6 satisfies assertion (3), in the natural small-epsilon range where the denominator is positive, but fails assertion (1).

## Construction

Let

```text
M = {0,z} union {x_n : n in N}
```

with distances `d(0,z)=2` and every other distance between distinct points equal to `1`. This is exactly the metric space used in Example 3.6 of the source paper to show failure of LTP.

For each finite `N0 subset M`, choose distinct `u=x_i`, `v=x_j` outside `N0`. Then `d(u,s)=d(v,s)=1` for all `s in N0`. If `L=1/(1-r-epsilon)`, then for `r=2/5` one has `L>3/2` whenever `0<epsilon<1-r`. Every 1-Lipschitz `f:N0 -> R` has oscillation at most `2`, so the intervals permitting the assignments `g(u)=a`, `g(v)=a-1` intersect. The explicit inf-extension formula then gives assertion (3).

Assertion (1) fails for the two unit vectors `mu=(delta_0-delta_z)/2` and `-mu`: for every molecule `m_uv`, at least one of `||mu+m_uv||` and `||-mu+m_uv||` is at most `3/2`. Since `2-r=8/5`, taking `epsilon=1/20` makes the requested lower bound `31/20>3/2`, impossible.

## Verification

- `code/verify_norm_bounds.py` solves the finite Arens-Eells transport linear programs for the four representative molecule types and confirms `max_m min(||mu+m||, ||-mu+m||)=3/2`.
- `figures/open_problem_crop.png` is a crop of the source paper passage containing Remark 3.3.
- `solution_packet.pdf` contains the formal proof.

## Novelty Check

Cheap run indexes were searched for `1612.03808`, the title, `octahedrality in Lipschitz-free`, `Remark 3.3`, `thick3`, `thick1`, `Whitley`, and `long trapezoid`. No prior packet for this arXiv id or target was found.

External web searches on 2026-06-20 included exact and near-exact phrases:

- `"We do not know whether" "thick3" "thick1"`
- `"assertion (3)" "assertion (1)" "Lipschitz-free"`
- `"Whitley's thickness index" "Lipschitz-free" "long trapezoid"`
- `"long trapezoid property" "Whitley" "thickness"`
- `"A characterisation of octahedrality in Lipschitz-free spaces" "Remark 3.3"`

These returned the source paper or no answer to the Remark 3.3 question.

## Human Review Recommendation

Review the quantifier convention for assertion (3): the source states `epsilon>0`, but the Lipschitz constant `1/(1-r-epsilon)` is meaningful only when `epsilon<1-r`. Under this necessary reading, the counterexample is complete.
