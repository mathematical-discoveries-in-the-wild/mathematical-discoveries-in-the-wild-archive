# Conditional Packet: WC-James Wide-(s) Bridge

Run: `fa_banach_001`  
Agent: `agent_lane_18`  
Date: 2026-06-15  
Source problem: Beanland--Causey--Freeman--Wallis, arXiv:1507.06285, Question 9.3.

## Status

`conditional_reduction`, not a full solution.

If the isolated bridge lemma below is proved, then the raw weak-compactness
cutoff classes

```text
{ A : WC(A,X,Y) <= omega^{omega^eta} }
```

are norm-closed operator ideals for every `eta >= 1`. Together with the source
paper's `WC <= omega` super weak compactness result and the existing finite
packet ruling out finite cutoffs `n >= 2`, this gives the expected positive
side of the principal cutoff pattern. The bridge lemma remains unproved here.

## Conditional Dependency

The needed bridge is:

```text
If j(A^* B_{Y^*}, epsilon) > omega * alpha,
then WC(A,X,Y,K) has order > alpha for some K.
```

Equivalently, high Causey James convex-separation rank should yield a lower
raw summing-basis WC tree after one `omega` loss. The finite evidence comes
from Rosenthal's finite `lambda`-wide-(s) and triangular-array selection
results in arXiv:math/9610209.

## What Is Proved Conditionally

Assuming the bridge for `alpha = omega^{omega^eta}` and `eta >= 1`, the packet
proves:

- `WC <= omega^{omega^eta}` implies Causey's `J <= omega^{omega^eta}`.
- Causey's theorem then gives closure under sums and norm limits.
- The elementary inclusion `WC(A) <= J(A)` transfers the sum back to the raw
  `WC` cutoff.

## Why This Is Useful

The previous full-solution push identified Causey's James index as the right
adjacent theorem but lacked a route back from convex separation to summing
domination. Rosenthal's wide-(s) paper supplies the missing finite language:
finite wide-(s) sequences are the quantitative form of raw WC nodes, and
triangular arrays are the finite form of James separation. The remaining task
is exactly the transfinite tree lift of that finite extraction.

## Files

- `main.tex`: conditional reduction note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv:1507.06285 source paper.
- `supporting_paper_1508.02065.pdf`: Causey's James index paper.
- `supporting_paper_math_9610209.pdf`: Rosenthal's wide-(s) paper.
- `figures/open_problem_crop.png`: crop of Question 9.3 from the source paper.

## Human Review Recommendation

Review the bridge lemma first. A proof should likely combine:

1. positive convex block closure of Causey's `J(A,epsilon)` trees,
2. the BCFW `omega*alpha -> alpha` tree blocking/basicization argument, and
3. Rosenthal's finite triangular-to-wide-(s) extraction.

If that tree lift fails, look for a well-founded James-tree-style reflexive
space with large `J` but unexpectedly small raw `WC`; such an example would
break the conditional route.
