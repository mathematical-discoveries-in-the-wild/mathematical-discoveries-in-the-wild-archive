# Diagonal universality and a Hilbert–Schmidt sufficient class

Status: `candidate_partial_likely_valid_human_review_needed`

This packet addresses Problem 1.5 of Or Shalom’s arXiv:2302.12857. It proves two complementary partial results:

- with normalized Haar measure and arbitrary bounded operator, the natural diagonal form represents **every** bounded sequence on the group;
- for any probability measure and any Hilbert–Schmidt operator, the full two-variable form is an ordinary correlation of two commuting actions, and its diagonal is a multicorrelation sequence.

The arbitrary bounded non-Hilbert–Schmidt case remains open. The source’s two-variable/one-variable ambiguity is stated explicitly in the packet.

## Files

- `solution_packet.pdf` — review packet
- `main.tex` — self-contained LaTeX source
- `verification.md` — explicit adversarial verifier report
- `source_paper.pdf` — arXiv:2302.12857v1
- `figures/open_problem_crop.png` — source Problem 1.5
- `figures/source_equation_2.png` — equation referenced by the problem
- `code/make_source_crops.py` — reproducible source-crop renderer

## Build

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

To regenerate the evidence crops from `source_paper.pdf`:

```sh
conda run --no-capture-output -n sandbox python code/make_source_crops.py
```

## Review priority

High-value checks are the intended diagonal reading of the source problem, the bilinear Hilbert–Schmidt kernel convention, and whether either observation already occurs in the literature under different terminology. This should not be reclassified as a full solution without treating arbitrary bounded operators.
