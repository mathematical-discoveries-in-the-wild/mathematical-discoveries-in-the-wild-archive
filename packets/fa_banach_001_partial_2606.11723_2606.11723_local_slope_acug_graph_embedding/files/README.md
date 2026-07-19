# Local-slope ACUG transfer to the graph compactification

- **Run:** `fa_banach_001`
- **Source:** arXiv:2606.11723, *Affine Approximation in Finite Nagata Dimension and Applications to Lipschitz-free spaces*, M. Jung, C. Petitjean, A. Prochazka, A. Quilis.
- **Target:** Question 1 on page 34 of the source PDF: if a compact metric space admits a superreflexive ACUG structure, must it embed bi-Lipschitzly into a compact quasiconvex metric space with a superreflexive ACUG structure?
- **Status:** partial result, likely valid.

## Result

The packet proves an affirmative answer under a stronger, local-slope version of ACUG.
Besides continuous upper gradients along rectifiable curves in `M`, the approximating subspaces are required to carry a linear continuous majorant for small secants in `M`.

Under this hypothesis, the source paper's graph space `G_epsilon(M)` inherits a superreflexive ACUG structure, so `M` embeds isometrically into a compact `(1+epsilon)`-quasiconvex metric space with superreflexive ACUG.

## Why This Is Useful

The proof isolates the missing point in the full question. Ordinary ACUG controls variation along curves already present in `M`; the graph construction creates many new short edges between nearby points of `M`. To put a continuous upper-gradient device on the graph, one must also control the secant slopes of the approximants on those new edges.

This packet shows that once that local-slope control is available, the rest of the embedding argument works.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local source PDF.
- `figures/open_question_page34.png`: crop of the source question.

## Remaining Gap

The full Question 1 remains open here. The unresolved step is whether every compact metric space with a superreflexive ACUG structure can be upgraded to the local-slope ACUG hypothesis used in this packet, or whether there is an ACUG space where such a secant-control upgrade fails.
