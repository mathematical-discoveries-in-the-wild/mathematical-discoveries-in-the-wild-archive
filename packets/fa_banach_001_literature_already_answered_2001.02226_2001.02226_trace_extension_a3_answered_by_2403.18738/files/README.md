# Literature Status: 2001.02226 Open Problem A3

status: literature_already_answered

## Source Problem

- Source: Petru Mironescu and Jean Van Schaftingen, "Trace theory for Sobolev mappings into a manifold", arXiv:2001.02226; published in Ann. Fac. Sci. Toulouse Math. (6) 30 (2021), 281--299.
- Location: Introduction, Open Problem A3.
- Question: for \(4 \le p < m\), assuming \(\pi_1(N), \ldots, \pi_{\lfloor p-2\rfloor}(N)\) finite and \(\pi_{\lfloor p-1\rfloor}(N)\) trivial, does \(W^{1-1/p,p}(B^{m-1},N)\) have the extension property?

## Supporting Answer

- Supporting paper: Jean Van Schaftingen, "The extension of traces for Sobolev mappings between manifolds", arXiv:2403.18738.
- Decisive result: Theorem 1.1 / `theorem_extension_halfspace`, together with the collar formulation Theorem 1.1'.
- Status: positive answer. The theorem characterizes surjectivity of the trace for \(1<p<m\): the trace is onto exactly when \(\pi_1(N),\ldots,\pi_{\lfloor p-2\rfloor}(N)\) are finite and \(\pi_{\lfloor p-1\rfloor}(N)\) is trivial. It also gives a linear energy estimate in the half-space and collar settings.

## Identification

Open Problem A3 is the local subcritical trace-extension problem after the known topological and analytical obstructions are imposed. The 2024 supporting paper states that it gives a complete answer to trace surjectivity and proves the half-space/collar theorem under precisely those hypotheses. Since \(4 \le p < m\) is a subrange of \(1<p<m\), the theorem answers A3 affirmatively.

The source paper itself explains that trace theory has local versions in which \(\mathbb{R}^{m-1}\) is replaced by a Lipschitz domain and then focuses on the unit ball. The supporting half-space/collar theorem is therefore the standard local model corresponding to the ball formulation of A3.

## Scope

This packet is not a new proof by the run. It records that the target is already answered in later literature. It covers Open Problem A3 and the adjacent linear-estimate question in the local half-space/collar setting. The broader global manifold statement in the supporting paper has an additional skeleton-extension condition on \((M,\partial M)\), so it is not restated here as the same local A3 claim.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2001.02226.
- `supporting_paper_2403.18738.pdf`: arXiv:2403.18738.
- Ledger: `runs/fa_banach_001/ledger/results/2001.02226_trace_extension_A3_answered_by_2403.18738.json`.

