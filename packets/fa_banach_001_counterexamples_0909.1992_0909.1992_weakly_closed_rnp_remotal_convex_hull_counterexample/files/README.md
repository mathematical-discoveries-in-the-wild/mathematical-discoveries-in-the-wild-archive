# Counterexample: weakly closed remotality need not pass from convex hull to the set

Status: candidate counterexample, likely valid.

Source: arXiv:0909.1992, Miguel Martin and T. S. S. R. K. Rao, *On remotality for convex sets in Banach spaces*.

## Question Answered

Remark 8 asks whether, for a weakly closed bounded set `E` in a Banach space, remotality of `K = closure(conv(E))` from a point implies remotality of `E` from that point.  The authors also ask whether the answer is positive for RNP sets.

## Result

The answer is negative, even with `K` an RNP set.  In

```tex
X = R \oplus_\infty \ell_2 \oplus_\infty c_0
```

let `s_n=(1,...,1,0,...)` be the summing basis of `c_0`, let `e_n` be the Hilbert basis of `ell_2`, fix `c=1/2`, and set `a_n=n/(n+1)`.  Define

```tex
E = { (a_n,  a_n e_n,  c s_n), (a_n, -a_n e_n, -c s_n) : n in N }.
```

Then `E` is weakly closed and bounded, `sup_{x in E} ||x||=1`, and no point of `E` has norm `1`.  However the midpoint of each signed pair is `(a_n,0,0)`, so `(1,0,0)` belongs to the norm-closed convex hull `K` of `E`.  Thus `K` is remotal from `0`, while `E` is not.  Since `X^*` is separable, `X` has the Radon-Nikodym property; hence the closed bounded convex set `K` is an RNP set.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: compiled local copy of arXiv:0909.1992 from the available source.
- `source_paper.tex`: local source used to compile the source paper.

## Verification

No computation is needed.  The main point is weak closedness of `E`: the `c_0` summing-basis tag has no weak cluster point in `c_0`; any hypothetical weakly convergent subnet with indices tending to infinity would have all coordinates eventually equal to the same nonzero sign, forcing a limit outside `c_0`.

Novelty checks on 2026-07-01 searched the run indexes, local parsed arXiv corpus, and web phrases around `"remotality" "weakly closed" "closed convex hull"` and the exact source question.  No later answer to this specific weakly closed/RNP question was found.

## Review Focus

Check the weak-closedness proof and the interpretation of "RNP sets" in the source remark.  The construction makes the closed convex hull a closed bounded convex subset of a separable-dual Banach space, hence an RNP set in the usual sense.
