# Partial Result: Even-p norm-attainment bound for arXiv:1608.00755

Status: `partial_result_likely_valid`

Source paper: Debmalya Sain, "On the norm attainment set of a bounded linear operator", arXiv:1608.00755.

## Result

For real \(X=\ell_p^2\) with even integer \(p\ge 4\), if \(T\in\mathcal L(X)\) is not a scalar multiple of an isometry, then
\[
  |M_T|\le p.
\]

In particular, the optimal bound for the first non-Hilbert even case \(X=\ell_4^2\) is exactly \(4\). The upper bound follows from a non-negative homogeneous binary form multiplicity argument; the lower bound is attained by \(H(x,y)=(x+y,x-y)\).

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source open question.
- `code/verify_p4_example.py`: numerical sanity check for the sharp \(p=4\) example.

## Novelty Check

Cheap run indexes had no prior packet for arXiv:1608.00755. The adjacent later paper arXiv:1806.01051 only improves Sain's general estimate to \(4(4p-3)\). Web searches for the exact open question and the bound \(2(8p-5)\) did not surface a later solution.

This is a partial result: odd \(p\) remains open, and the exact optimum for even \(p\ge 6\) is not claimed.

## Human Review Recommendation

Check the algebraic step that a non-negative homogeneous binary form has each real zero line with even multiplicity. The rest is a direct degree count plus an explicit \(\ell_4^2\) example.
