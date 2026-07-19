# Low-p Zero-Boundary Result for Sobolev-to-BV Extension Domains

Source paper: Tapio Rajala and Zheng Zhu, "Zero volume boundary for extension
domains from Sobolev to BV", arXiv:2205.10801, published in Revista
Matematica Complutense, DOI 10.1007/s13163-024-00485-6.

Status: likely valid partial result for Question 1.3. This packet does not
settle the full range
`1 < p <= (n-1)/(n-2)`. It proves the zero-boundary conclusion in the
subrange

```text
1 < p < n/(n-1).
```

For `n >= 3`, this is a genuine subrange of the Rajala-Zhu open interval and
removes the 1-fatness assumption there. For `n = 2`, the source paper already
proves zero boundary for all `p` by planar 1-fatness.

## Result

Let `Omega` be a bounded `(W^{1,p},BV)`-extension domain in `R^n`, `n >= 2`.
If

```text
1 < p < 1* = n/(n-1),
```

then `|partial Omega| = 0`.

## Idea

The proof combines two ingredients:

- Rajala-Zhu's BV set function for `(W^{1,p},BV)` extension domains, which
  gives local BV extensions with variation controlled by a quasiadditive
  set function.
- The Koskela-Mishra density/annular iteration method for
  `(W^{1,p},W^{1,q})` extension domains, adapted with the critical BV
  Sobolev-Poincare exponent `1* = n/(n-1)`.

The method works exactly while `p < 1*`. At `p = 1*`, the small-density
absorption exponent vanishes; beyond it, this route gives no contradiction.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2205.10801.
- `supporting_paper_2409.01170.pdf`: local copy of the Koskela-Mishra
  supporting paper.
- `figures/open_problem_page.png`: rendered PDF page containing Question 1.3.
- `tmp/`: LaTeX build intermediates.

## Novelty Check

Run indexes were searched for arXiv:2205.10801 and close phrases involving
`(W^{1,p},BV)`, zero-volume boundary, Sobolev-to-BV extension domains, and
Question 1.3. Web search on 2026-07-18 found the source paper and the later
Koskela-Mishra `(p,q)` theorem, but no exact `(W^{1,p},BV)` theorem removing
1-fatness even in the low-p subrange. Because the argument is a close
adaptation of the 2025 iteration method, human review should treat the
novelty as "plausibly new or at least not explicitly indexed", not as a
confirmed publication-level priority claim.

## Human Review Recommendation

Review as a partial theorem. The main checks are:

1. the BV Sobolev-Poincare min-estimate for a BV function taking values 1 on
   `B(x,r/2) cap Omega` and 0 on the annulus `A_{r,2r,Omega}`;
2. the exponent arithmetic in the small-density absorption, especially the
   use of `p < n/(n-1)`;
3. the reuse of the Koskela-Mishra annular iteration after the BV min-estimate
   is established.
