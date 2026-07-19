# Literature-Implied Answer: Improved `ell_1^n` Helly Radius

## Source Question

- Source paper: G. Ivanov, *On Banach Spaces with the Helly Approximation Property*, arXiv:2603.22743.
- Target: the finite-dimensional statement that the bound
  `r_k(ell_1^n) <= C sqrt(log n / k)` is optimal.
- Screenshot: `figures/source_conjecture_crop.png`.
- Source PDF retained as `source_paper.pdf`.

## Status

This is filed as `literature_implied_answer`, not as an original lower-bound
solution.  The supporting paper arXiv:2207.03614 is separate and older; it
does not discuss the Helly paper, but its approximate-Caratheodory bound
passes through the Helly paper's own dual reduction.

## Answer

Let `h_k(ell_1^n)` denote the best no-dimensional Helly radius in the source
paper's sense. Reis--Rothvoss prove

```text
ac_k(B_infty^n, B_infty^n) <= C sqrt(log(2n/k) / k).
```

The dual reduction in arXiv:2603.22743 gives

```text
h_k(ell_1^n) <= 3 ac_k(B_infty^n, B_infty^n).
```

Therefore, for `1 <= k <= n`,

```text
h_k(ell_1^n) <= C' sqrt(log(2n/k) / k).
```

In particular, the source paper's `sqrt(log n / k)` upper bound is not
uniformly optimal in `k` as written: taking `k=n` gives an `O(1/sqrt n)`
radius, whereas a matching `sqrt(log n/n)` lower bound would be larger by
`sqrt(log n)`.

## Limitations

- This does not prove the sharp lower bound for `ell_1^n`.
- This does not refute an interpretation of the source conjecture restricted
  to ranges where `k` is much smaller than `n`.
- The result is a literature-implied sharpening, not a new proof of
  Reis--Rothvoss or of the Helly paper.

## Files

- `solution_packet.pdf`: rendered human-facing packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original source paper.
- `supporting_paper_2207.03614.pdf`: supporting approximate-Caratheodory paper.
- `figures/source_conjecture_crop.png`: source conjecture screenshot.
- `figures/supporting_corollary_crop.png`: supporting corollary screenshot.
- `code/crop_evidence.py`: regenerates the evidence crops.
- `code/check_implication.py`: checks the expected PDF snippets.
