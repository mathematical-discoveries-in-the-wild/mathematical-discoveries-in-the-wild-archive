# Both `p<1` atomic-block questions fail on an atomic filtration

Status: `counterexample_likely_valid`  
Source: J. M. Conde-Alonso and J. Parcet, *Atomic blocks for noncommutative martingales*, arXiv:1407.5451, Problem 3.1 (page 17).

For every `0<p<1` and `1<q<infinity`, the packet constructs one countably atomic probability space with a fixed filtration such that

- `H^p_{atb,q}` contains an explicit `L_p` function whose martingale square function is not in `L_p`, so `H^p_{atb,q} != H_p` even as sets; and
- a bounded decaying sum of level signs defines a continuous functional on `H_p` but has infinite displayed `Lambda_{p,q}` norm, so `H_p^* != Lambda_{p,q}` for the class stated in the source.

The mechanism is a rare-recovery martingale. On a block of mass `w`, its terminal `L_p` cost and proposed atomic-block cost are both of order `w^(1/p) epsilon^(1/p-1)`, while its square-function cost remains of order `w^(1/p)`. The filtration activates disjoint gadgets successively, so every finite martingale stage is integrable; taking `epsilon_n -> 0` then separates the spaces.

## Files

- `main.tex` / `solution_packet.pdf`: complete statement and proof.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page 17 with the definition and Problem 3.1.
- `code/verify_counterexample.py`: numerical sanity checks of all displayed finite-block formulas.

## Verification and novelty

The proof is exact and does not rely on computation. The verifier checks the conditional expectations, the subatom normalization, the `L_p` and square-function formulas, and the divergent/convergent series for several parameters. A bounded search of arXiv and the run indexes using the exact notation, paper title, and `(p,q)`-atomic-block phrases found no later resolution of Problem 3.1.

Human review should focus on the intended meaning of equality in Problem 3.1 and on the global jump term in the paper's displayed `Lambda_{p,q}` norm. The first counterexample is set-theoretic and therefore does not depend on a norm-equivalence interpretation.
