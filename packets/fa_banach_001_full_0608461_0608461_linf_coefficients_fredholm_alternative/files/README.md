# Candidate Full Solution: \(L^\infty\) couplings in the Kmit-Recke Fredholm alternative

Status: `candidate_full_solution_likely_valid`

This packet addresses arXiv:math/0608461, Kmit and Recke, "Fredholm Alternative for Periodic-Dirichlet Problems for Linear Hyperbolic Systems." The targeted question is Remark 14 on printed page 18: whether the hypothesis \(b,c \in BV(0,1)\) in Theorem 1 can be weakened to \(b,c \in L^\infty(0,1)\).

Claim: yes. In the original two-equation, time-independent setting, Theorem 1 remains true for \(a,b,c,d \in L^\infty(0,1)\) under the same nonresonance condition.

Main mechanism: the original proof uses \(BV\) only to integrate by parts and get a \(1/(1+|k|)\) factor in the compactness proof of \((BA^{-1})^2\). The packet replaces this with a uniform Riemann-Lebesgue lemma over normalized \(H^1\)-bounded diagonal solution factors, giving a high-mode decay factor \(\mu_k \to 0\), which is enough for the same finite-tail compactness argument.

Files:

- `main.tex` - human-readable proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of the source paper.
- `figures/open_problem_crop.png` - crop of Remark 14 from the source PDF.
- `code/README.md` - notes on verification/code status.

Human review focus: verify the uniform oscillatory lemma and compare the final estimate with the source proof around equation (4.10). The packet does not address the separate time-dependent coefficient question in Remark 15.
