# Full answer: p-ABS expansion classes

Status: `full_solution_likely_valid`

Source target: K. Mahesh Krishna and P. Sam Johnson, *Expansion of approximate Bessel sequences to approximate Schauder frames for Banach spaces*, arXiv:2102.03288.

## Result

The source asks:

```text
For which classes of Banach spaces, p-approximate Bessel sequences can be expanded to a p-ASF?
```

This packet gives the full classification.

For `1 <= p < infinity`, the following are equivalent for a Banach space `X`:

- every `p`-approximate Bessel sequence for `X` can be expanded to a `p`-approximate Schauder frame;
- `X` admits a `p`-approximate Schauder frame;
- `X` is isomorphic to a complemented subspace of `ell^p`.

The proof is formal but useful. If `X` already has one `p`-ASF, convert it to a Parseval `p`-ASF and use it to add the missing operator `I - S_{f,tau}` to any p-ABS frame operator `S_{f,tau}`. Conversely, expanding the zero p-ABS gives a p-ASF. The operator characterization of p-ASFs from arXiv:2010.10514 then identifies exactly the complemented subspaces of `ell^p`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: rendered source arXiv paper.
- `supporting_paper_2010.10514.pdf`: rendered supporting characterization paper.
- `figures/open_problem_crop.png`: crop of the source definition/question/partial theorem.
- `figures/supporting_p_asf_characterization_crop.png`: crop of the supporting p-ASF characterization theorem.

## Novelty check

The cheap run indexes were searched for `2102.03288`, `p-approximate Bessel`, `p-ASF`, `expanded to a p-ASF`, and `complemented subspace ell^p`. They showed related p-ASF packets for different papers but no duplicate of this expansion classification. Exact-phrase web searches for the source question and the complemented-`ell^p` answer did not surface a later explicit answer.

This result uses a known characterization theorem from arXiv:2010.10514 as a decisive ingredient, but the packet supplies the missing expansion-equivalence step for the question in arXiv:2102.03288.

