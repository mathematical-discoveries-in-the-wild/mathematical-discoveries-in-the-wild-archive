# 1804.05660 symmetric Nakano lambda-unbounded example

Status: likely valid full answer to Problem 4.8 of the source paper.

Source: Richard J. Smith and Stanimir Troyanski, `Approximation of norms on
Banach spaces`, arXiv:1804.05660.

## Claim

Problem 4.8 asks whether there is a nondecreasing sequence `p_k`, with
`p_1 >= 1` and `p_k -> infinity`, such that one of two test suprema is infinite
in the symmetric Nakano space `h^S_(p_k)(Gamma)`.

This packet gives an affirmative answer: for every infinite `Gamma` there is a
nondecreasing integer-valued block sequence `p_k -> infinity` such that

```text
sup_n || sum_{k=1}^n e_{gamma_k} / lambda(k) || = infinity
```

in `h^S_(p_k)(Gamma)`.

## Idea

Take `p_k` constant and equal to `m` on very long consecutive blocks. For
indices `k` far enough inside the `m`th block, the current block dominates the
defining equation for `lambda(k)`, which gives

```text
lambda(k)^(-m) >= 1 / (2 (k - N_{m-1})).
```

The modular of `sum e_gamma_k / lambda(k)` at trial radius `m` therefore
contains a harmonic block contribution of size roughly
`log(L_m/R_m)/(2 m^m)`. Choosing the block length `L_m` much larger than
`R_m exp(m^m)` forces this contribution above `1`, so the norm of the partial
sum exceeds `m`. Since `m` is arbitrary, the supremum is infinite.

## Files

- `main.tex` - self-contained proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv source paper PDF.
- `figures/open_problem_crop.png` - crop of Problem 4.8 in the source paper.

## Verification

The proof is deterministic and does not rely on computation. It was checked
against the source definitions at lines 687-754 of the parsed TeX and the
rendered source PDF page 20. Bounded novelty search used exact phrases from
Problem 4.8 and related terms (`h^S_(p_n)`, `lambda(k)`, symmetric Nakano);
no direct later answer was found in the quick web search.

Human review should focus on the two elementary estimates for `lambda(k)` inside
a long constant block and on the use of the Nakano modular lower bound from the
identity ordering of the chosen coordinates.
