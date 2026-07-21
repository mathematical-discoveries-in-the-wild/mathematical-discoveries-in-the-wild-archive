# Diverging bandwidth suffices for the singular-continuous lower bound

**Status:** candidate strong partial result, likely valid, awaiting human review  
**Source:** Matthew J. Colbrook, *Computing Spectral Measures and Spectral Types*, arXiv:1908.06721v3 (2021), Theorem 5.1 and its open question on page 6.  
**Packet:** `solution_packet.pdf`  
**Ledger:** `runs/fa_banach_001/ledger/results/1908.06721_diverging_bandwidth_sc_lower_bound.json`

## Result

Let \(f:\mathbb N\to\mathbb N\) satisfy \(f(n)>n\). Colbrook proves that computing the singular-continuous spectrum on \(\Omega_{f,0}\) cannot be done with two nested limits when
\[
f(n)-n\ge \sqrt{2n}+\tfrac12,
\]
and asks whether the growth condition can be dropped.

This packet proves the same \(\Delta_3^G\) exclusion under the much weaker hypothesis
\[
f(n)-n\longrightarrow\infty.
\]
The proof replaces the paper's triangular enumeration of countably many Jacobi rays by a variable-width round-robin enumeration adapted to \(f\). It also proves that divergence of \(f(n)-n\) is necessary for *any* enumeration of countably many disjoint infinite rays satisfying the \(\Omega_{f,0}\) cut constraints. Thus the new hypothesis is sharp for the source paper's direct-sum reduction.

The bounded-bandwidth case, including tridiagonal operators \(f(n)=n+1\), is not resolved. It requires a different spectral encoding rather than a better enumeration of the same direct sum.

## Verification

- The formal proof is in `main.tex` and the rendered `solution_packet.pdf`.
- `figures/open_problem_crop.png` is a full-width crop of source page 6 containing the exact question.
- `code/check_round_robin.py` checks the cut inequalities for a slowly diverging sample bandwidth and is a sanity check only.
- The local registry, solutions, attempts, and proof-gap indexes contained no record for arXiv:1908.06721 or this exact bandwidth strengthening.
- A bounded web/arXiv search on 2026-07-21 used the exact source sentence and the phrases `singular continuous spectrum`, `Delta_3`, `SCI`, `bandwidth`, and `Colbrook`. It found the source paper and related computational papers, but no separate settlement of this hypothesis. This is not an exhaustive literature review.

## Human-review focus

Check the phase-transition gap calculation in Lemma 1 and the passage from the cut inequality to membership in \(\Omega_{f,0}\). Once those are confirmed, the remainder is exactly the lower-bound reduction already written in the source proof of Theorem 5.1.
