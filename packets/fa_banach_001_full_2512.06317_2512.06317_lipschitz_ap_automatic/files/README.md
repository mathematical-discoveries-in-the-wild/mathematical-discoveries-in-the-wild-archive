# Full Solution Packet: arXiv:2512.06317 Lipschitz AP Is Automatic

## Classification

`full`

## Source

- arXiv:2512.06317
- Title: "Approximation property in terms of Lipschitz maps via tensor product approach"
- Source PDF: `source_paper.pdf`
- Open-question screenshot: `figures/open_problem_crop.png`

## Targeted Question

The final open-question list asks for:

- examples of Banach spaces without `Lip-a.p` or `Lip-p.a.p`;
- conclusions about the reverse arrows in the implication diagram involving
  `a.p`, `p.a.p`, `Lip-a.p`, and `Lip-p.a.p`.

## Result

With the definitions used in the paper, every Banach space has `Lip-a.p` and
`Lip-p.a.p` for every `1 <= p < infinity`. More generally, for any pointed
metric space `M`, any Banach space `X`, and any `f in Lip_0(M,X)`, finite-rank
Lipschitz maps approximate `f` uniformly on compact subsets.

Consequences:

- there are no Banach spaces without `Lip-a.p`;
- there are no Banach spaces without `Lip-p.a.p`;
- `Lip-a.p => a.p` is false, using Enflo's space without the classical AP;
- `Lip-p.a.p => a.p` is false, again using Enflo's space;
- for `1 <= p <= 2`, `p.a.p => a.p` is false, since Karn-Sinha gives `p.a.p`
  for every Banach space in that range and Enflo's space lacks AP.

## Proof Idea

On a compact subset of the range, build a finite-dimensional Lipschitz
approximation of the identity using a finite net and Lipschitz partition
functions. Extend the finite-dimensional-valued Lipschitz map from the compact
subset to the whole Banach space by extending scalar coordinates with McShane's
theorem. Composing this extension with the original Lipschitz map gives a
finite-rank Lipschitz approximant.

The key point is that the definitions in the source do not require a uniform
bound on the Lipschitz constants of the approximating finite-rank maps.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: real screenshot crop of the source
  open-question list.
- `code/make_open_problem_crop.py`: reproduces the screenshot crop.
- `code/check_partition_construction.py`: numerical smoke check for the
  finite partition construction on a compact sample.

## Literature Check

Web check on 2026-06-08 found the arXiv page for `2512.06317` with only the
initial version listed. No later paper explicitly answering this final
open-question list was found in the quick check used for this packet.
