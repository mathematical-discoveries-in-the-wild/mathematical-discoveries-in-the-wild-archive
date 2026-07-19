# Closed-Range Subcase For Dense Small Periodic Sets

Status: partial_result_likely_valid

Source paper: Rodrigo Cardeccia and Santiago Muro, "Arithmetic progressions and chaos in linear dynamics", arXiv:2003.07161.

Target question: Question 4.2 asks whether every hypercyclic operator with dense small periodic sets is necessarily chaotic, and more generally whether dense small periodic sets force dense periodic points.

## Result

Let `T` be a bounded linear operator on a Banach space `X`. If `T` has dense small periodic sets and every operator `I - T^n`, `n >= 1`, has closed range, then the periodic points of `T` are dense in `X`. In particular, under the same closed-range hypothesis, a hypercyclic operator with dense small periodic sets is chaotic.

## Proof Mechanism

Dense small periodic sets give, inside any small ball, an orbit segment under some power `S = T^k` that never leaves the ball. Cesaro averages of that orbit remain in the ball and satisfy

```text
(I - S) z_N = (x - S^N x) / N -> 0.
```

Thus the ball contains approximate fixed points of `S`. If `I - S` has closed range, the quotient inverse estimate for `I - S : X / ker(I - S) -> ran(I - S)` turns approximate fixed points into nearby true fixed points. Those true fixed points are `k`-periodic for `T`.

## Scope And Limitations

This is not a full answer to Question 4.2. The argument deliberately assumes closed range for all `I - T^n`. The remaining difficult case is precisely when the dense small periodic sets only produce approximate fixed points for powers whose `I - T^k` has nonclosed range.

The previous Lipschitz-free linearization counterexample route was also checked against arXiv:2011.10800. It remains blocked because free-space linearization can create dense periodic vectors even when the original Lipschitz map has non-dense periodic points.

## Files

- `main.tex` - proof packet source.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local source paper PDF.
- `figures/open_problem_crop.png` - crop of Question 4.2 from the source paper.

## Verification

The packet was rendered with `latexmk`. The proof uses only the source paper's definition/equivalence for dense small periodic sets and the standard Banach closed-range quotient estimate.
