# Polynomial-Window Obstruction to the Delta0 Weak-Compactness Criterion

Status: partial_result_likely_valid.

Source:
- Pascal Lefevre, Daniel Li, Herve Queffelec, Luis Rodriguez-Piazza, "A criterion of weak compactness for operators on subspaces of Orlicz spaces", arXiv:0806.4204, submitted 2008-06-25.
- Local PDF: `source_paper.pdf`.

Source question:
- On page 5, just before Theorem 4, the paper asks whether the condition `Psi in Delta^0` is actually necessary for the weak compactness characterization `(W)` on subspaces of the Morse-Transue space `M^Psi`.
- Evidence crop: `figures/open_question_crop.png`.

Partial result:
- Fix `1 <= p < q < infinity`. Suppose `Psi` dominates `x^q` eventually, but has a subsequence `x_n -> infinity` with `Psi(x_n) <= C x_n^q` and `Psi(x_n) / x_n^p -> infinity`.
- Then the natural inclusion `J_q : M^Psi -> L^q` is weakly compact, but it fails the fixed-`p` estimate `(W_p)`.
- The proof uses normalized indicators `f_n = x_n 1_{A_n}` with `P(A_n)=1/Psi(x_n)`: their `M^Psi` norm is `1`, their `L^p` norm tends to `0`, but their `L^q` norm stays bounded below.

Scope and limitations:
- This is not a full solution to the source's necessity question for `Delta^0`.
- It gives a reusable obstruction for non-`Delta^0` Orlicz functions with polynomial-window behavior and extends the mechanism of the source's Remark 3.
- It does not refute the possibility that some non-`Delta^0` Orlicz functions still satisfy an appropriately interpreted weak compactness criterion.

Ledger:
- `runs/fa_banach_001/ledger/results/0806.4204_polynomial_window_delta0_obstruction.json`
