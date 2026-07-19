# Partial Result: Davis-Wielandt index one for real ell_p^2, 2 <= p <= 8

Status: partial_result_likely_valid

Source paper: P. Bhunia, D. Sain, K. Paul, "On the Davis-Wielandt shell of an operator and the Davis-Wielandt index of a normed linear space", arXiv:2006.15323.

## Result

For the real two-dimensional space \(X=\ell_p^2\), if \(2\le p\le 8\), then
\[
  \eta_{dw}(X)=1.
\]
This gives a concrete family for part (i) of the source paper's final open question, which asks for a characterization of spaces satisfying \(\eta_{dw}(X)=1\).

The witness is the rank-one nilpotent
\[
  T(a,b)=(0,a).
\]
It has \(\|T\|=1\) and \(dw(T)=1\).

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - source arXiv paper.
- `code/verify_scalar_inequality.py` - numerical sanity check for the scalar inequality.

## Novelty Check

The cheap run indexes had no exact packet for `2006.15323` or for Davis-Wielandt index computations. A web search for `"Davis-Wielandt index" "eta_dw"` and close variants found the source paper but no later computation of \(\eta_{dw}(\ell_p^2)\). This packet is a partial subcase, not a full characterization.

## Human Review Recommendation

Review the scalar inequality lemma. The rest of the proof is a direct substitution into the source definitions.
