# Laakso Wasserstein \(L_1\)-Distortion Answered by arXiv:2602.14852

Status: `literature_already_answered`

## Source problem

Florent Baudier, Chris Gartland, and Thomas Schlumprecht,
*L1-distortion of Wasserstein metrics: a tale of two dimensions*,
arXiv:2208.13879.

Remark 2 on arXiv PDF page 3 says that, for graphs of dimension strictly
between 1 and 2 such as the iterated Laakso graphs
\(\mathrm{La}_1^{\oslash n}\), the authors do not know how to prove any
nontrivial lower bound for the \(L_1\)-distortion of the corresponding
1-Wasserstein spaces.

## Explicit later answer

Chris Gartland and Mikhail Ostrovskii,
*Lower Estimates for L1-Distortion of Transportation Cost Spaces*,
arXiv:2602.14852.

The later paper explicitly says on arXiv PDF page 5 that, before its work,
unboundedness was unknown for several slash powers including the Laakso
graphs. Its Corollary 4.21 on arXiv PDF page 26 proves the quantitative bound
\[
  c_1\!\left(\mathrm{TC}(\mathrm{La}^{\oslash n})\right)
  \geq \frac{2-\sqrt 2}{8}\,n .
\]
Because finite transportation-cost space, Lipschitz-free space, and
1-Wasserstein distortion have the same relevant \(L_1\)-distortion here,
this is exactly the requested nontrivial lower bound. Together with the
universal logarithmic upper bound and
\(\log |V(\mathrm{La}^{\oslash n})|=\Theta(n)\), it is asymptotically sharp.

The supporting paper explicitly recognizes that it is resolving this
previously open Laakso case; this is not a new agent result.

Files:

- `source_paper.pdf`: arXiv:2208.13879.
- `supporting_paper_2602.14852.pdf`: the separate answering paper.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

Ledger:
`runs/fa_banach_001/ledger/results/2208.13879_laakso_wasserstein_l1_answered_by_2602.14852.json`.
