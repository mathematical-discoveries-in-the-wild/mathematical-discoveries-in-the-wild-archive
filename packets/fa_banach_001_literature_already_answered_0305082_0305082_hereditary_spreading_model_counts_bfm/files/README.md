# Literature Already Answered: Hereditary Counts of Spreading Models

Status: `literature_already_answered`

## Source Questions

- Source paper: G. Androulakis, E. Odell, Th. Schlumprecht, and N. Tomczak-Jaegermann, "On the structure of the spreading models of a Banach space", arXiv:math/0305082.
- Locations: TeX labels `qst3.3` and `qst3.5`; printed as Questions 3.15 and 3.17 on pages 19-20 of the source PDF.
- Covered questions:
  - If every infinite-dimensional subspace admits `ell_1` and `ell_2` spreading models, must there be more, perhaps uncountably many, mutually non-equivalent spreading models?
  - For each `n`, is there a Banach space whose every subspace has exactly `n` different spreading models?
  - Is there a Banach space whose every subspace has exactly countably many different spreading models?

## Supporting Answer

- Supporting paper: Kevin Beanland, Daniel Freeman, and Pavlos Motakis, "The stabilized set of `p`'s in Krivine's theorem can be disconnected", arXiv:1408.0265.
- Location: Theorem 1 on page 2 and the explicit AOST discussion on page 3 of the supporting PDF.

Theorem 1 constructs, for every finite set `F` or every increasing sequence together with its limit `F`, a reflexive Banach space with an unconditional basis whose block subspaces have precisely the `ell_p` spreading-model behavior specified by `F`. The authors then explicitly state that this theorem solves the AOST questions about exactly `n` spreading models, exactly countably infinitely many spreading models, and whether hereditary `ell_1`/`ell_2` spreading models force uncountably many models.

In particular:

- choosing finite `F` with `|F| = n` gives the exactly-`n` examples;
- choosing `F` to be an increasing sequence and its limit gives countably infinitely many models;
- choosing `F = {1,2}` gives hereditary `ell_1` and `ell_2` spreading models without uncountably many models.

## Scope

This packet records a later literature answer, not an original proof. It covers the hereditary counting questions in AOST Questions 3.15 and 3.17. It does not resolve the other source-paper questions about stabilizing all spreading models, realizable posets for `SP_omega(X)`, consequences of finite/countable `SP_omega(X)`, or the unique-spreading-model classicality question.

## Files

- `source_paper.pdf`: arXiv:math/0305082.
- `supporting_paper_1408.0265.pdf`: arXiv:1408.0265.
- `main.tex` and `solution_packet.pdf`: compact status note.
