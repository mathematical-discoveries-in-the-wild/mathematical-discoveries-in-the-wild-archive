# Full Solution Packet: Two-Sided Inverse-Gaussian Square Bounds Characterize UMD

- status: candidate full solution, likely valid
- run: `fa_banach_001`
- model: `GPT5.6`
- agent: `agent_lane_10`
- source arXiv id: `2102.13381`
- source paper: Víctor Almeida, Jorge J. Betancor, Juan C. Fariña, and Lourdes Rodríguez-Mesa, *Littlewood-Paley-Stein Theory and Banach Spaces in the Inverse Gaussian Setting*
- target passage: arXiv PDF page 33, the remark following Theorem 1.5

## Result

The answer to the source question is affirmative.

Let `X` be an order-continuous Köthe function space and `1<p<infinity`.
Retain the first estimate in Theorem 1.5(ii), namely the upper
inverse-Gaussian Poisson square-function estimate for `X`, and replace the
upper estimate for `X*` by the proposed reverse estimate for `X`. Then `X` is
UMD. Conversely, UMD implies both estimates. Thus the modified condition is
equivalent to UMD.

The point that makes this a full answer is that the source's proposed
replacement does **not** discard the first estimate in Theorem 1.5(ii). Its
hypothesis is therefore a two-sided square-function estimate for `X`.

## Method

For a compactly supported finite tensor `F`, put
`f_epsilon(x)=F(x/epsilon)`. The inverse-Gaussian measure rescales to
`exp(epsilon^2 |z|^2) dz`, while the rescaled generator is

```text
B_epsilon = -Delta/2 - epsilon^2 z dot grad.
```

The packet proves directly, using the source paper's kernel estimates, that
the norm of the rescaled inverse-Gaussian Poisson square function converges to
the norm of the Euclidean Poisson square function.

- On `|x|<rho`, every pair `(x,y)` meeting the shrinking support is in the
  local region. The source comparison kernel gives an error bounded after
  rescaling by
  `epsilon^(1/2) I_(1/2)(||F||_X)`. Its `L^p` norm on the expanding ball
  tends to zero for every `p>1`.
- On `|x|>=rho`, the input and output are uniformly separated. On a compact
  annulus the square kernel is bounded. Far away, the source's explicit
  global estimate `(A2)` gives a Gaussian majorant belonging to
  `L^p(gamma_-1)`. The normalized tail is
  `O(epsilon^(n(1-1/p)))`.

Passing the assumed upper and lower inequalities through this limit yields a
two-sided Euclidean Poisson lattice-square estimate for `X`. The
Xu-Hytönen characterization then gives UMD.

## Files

- `main.tex`: full proof packet
- `solution_packet.pdf`: rendered proof packet
- `source_paper.pdf`: local copy of arXiv:2102.13381
- `figures/open_problem_crop.png`: genuine crop of the source question
- `verification.md`: line-by-line dependency and edge-case audit

## Novelty Check

The run indexes were searched for the arXiv id, paper title, inverse-Gaussian
square functions, UMD, reverse estimates, and removal of the dual-space
condition. Adjacent Littlewood-Paley-Stein packets do not address this exact
question.

Bounded external searches on 2026-07-23 used the exact phrase
`"replace the condition involving the dual space"`, the full paper title
together with `UMD reverse estimate`, and close inverse-Gaussian
square-function formulations. They found the arXiv paper and its 2023
Potential Analysis publication, but no later paper explicitly answering the
remark. The open-access published version was also checked directly: the
question remains verbatim on published PDF page 43, so it was not removed or
answered during peer review. This is evidence rather than a guarantee of
novelty.

## Human Review Focus

The main item to check is the tangent lemma in `main.tex`, especially the use
of the source's global estimate `(A2)` to obtain an `L^p(gamma_-1)` majorant
uniformly for the shrinking input support. The local error exponent and all
three regimes of its radial integral are written out explicitly.
