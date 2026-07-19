# Full Critical Border Map: Holder-Zygmund and Classical Endpoint Conventions

Status: `full_holder_endpoint_convention_classification_likely_valid`

Source paper: Max Scholpple and Ingo Steinwart, "Which Spaces can be Embedded in Reproducing Kernel Hilbert Spaces?", arXiv:2312.14711.

## Result

This packet closes the critical Holder-Zygmund/Besov line left open by the
source:

```text
Let d >= 1, beta > 0, alpha = beta + d/2.
Then the inclusion
Lambda^alpha([0,1]^d) -> Lambda^beta([0,1]^d)
is not cotype 2, where Lambda^s = B^s_{infty,infty}.
Consequently there is no RKHS H with
Lambda^alpha([0,1]^d) -> H -> Lambda^beta([0,1]^d).
```

This removes the noninteger-alpha restriction from the earlier partial packet.
The proof uses finite differences rather than the classical `C^{n,theta}`
seminorm, so integer Zygmund smoothness is included.

The packet also gives the complete purely classical endpoint convention map:

```text
Interpret C^s classically: C^{k,theta} for noninteger s=k+theta and
ordinary C^m for integer s=m.

At alpha - beta = d/2, beta > 0, an RKHS sandwich
C^alpha([0,1]^d) -> H -> C^beta([0,1]^d)
exists if and only if alpha is an integer and beta is not an integer.
```

Equivalently, the positive classical cases are exactly the odd-dimensional
critical endpoints with integer domain smoothness. They are realized by
`H^m`. If both endpoint exponents are integers, the packet proves a negative
result using a derivative version of the Fourier-character/Bessel obstruction.

Thus the critical border is convention-sensitive. The Zygmund/Besov endpoint
`B^m_{infty,infty}` is too large at integer smoothness. The smaller classical
integer domain fits into the Sobolev RKHS `H^m` exactly when the target
smoothness is noninteger; if the target is also a classical integer `C^l`,
derivative evaluations force the critical lattice-sum contradiction.

## Proof Mechanism

For the negative theorem, take smooth dyadic bumps
`phi_{j,k}(x)=2^{-j alpha} phi(2^j x-k)`. Signed sums across all scales have
uniform `Lambda^alpha` norm. The finite-difference estimate is

```text
||Delta_h^r g_j||_infty
  <= C min(2^{-j alpha}, |h|^r 2^{j(r-alpha)})
```

and summing over levels gives `O(|h|^alpha)`. In the target space, every bump
has `Lambda^beta` norm at least `c 2^{-j(alpha-beta)}`. On the critical line
each level contributes a constant amount to the cotype square-sum, so the
first `m` levels force growth like `sqrt(m)` while the Rademacher domain norm
stays bounded. Hence the inclusion is not cotype 2.

The positive classical-integer statement is standard Sobolev embedding:
`C^m` and `C^{m-1,1}` embed into `H^m`, and
`H^m = B^m_{2,2}` embeds critically into
`B^{m-d/2}_{infty,infty}=Lambda^{m-d/2}` when `m>d/2`. If `m-d/2` is
noninteger this target is classical `C^{m-d/2}`.

For integer target `C^l`, the proof uses derivative evaluations on Fourier
characters. If `C^m -> H -> C^l` factored through a Hilbert space at
`m-l=d/2`, Bessel's inequality would force bounded partial sums of
`sum |n|^{-d}`, which is impossible.

## Files

- `main.tex`: full proof and border map.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2312.14711.
- `figures/open_problem_crop.png`: source crop showing the border-case
  statement.

## Novelty / Duplicate Check

The run indexes were searched for `2312.14711`, `Holder-Zygmund`, `Besov`,
`B_infty_infty`, `alpha-beta=d/2`, `critical`, `integer alpha`, `C^m`,
`C^l`, `cotype`, and `2-factor`. Existing hits were the bounded-kernel
endpoint full packet, the one-dimensional companion packet, and the
noninteger-alpha partial packet now subsumed by this result.

Bounded web searches on June 16, 2026 for the source title plus
`Holder-Zygmund border`, for `B^s_{infty,infty} cotype Hilbert factorization`,
for `Besov B_{infty,infty} 2-factorable`, and for `Holder-Zygmund RKHS
critical d/2` found the source arXiv record but no exact later answer to this
critical Zygmund line. Additional searches for `C^m Hilbert factorization C^l
critical Sobolev embedding`, `C^m reproducing kernel Hilbert C^l critical`,
and `Holder critical RKHS C^m C^l` found no exact classical endpoint
classification.

## Human Review Recommendation

Review as a likely valid full result for both the Holder-Zygmund/Besov
critical line and the purely classical endpoint convention. The main checks
are the finite-difference multiscale estimate, the target lower bound, the
derivative-character obstruction for `C^m -> C^l`, and the use of the source
paper's RKHS-to-cotype obstruction.
