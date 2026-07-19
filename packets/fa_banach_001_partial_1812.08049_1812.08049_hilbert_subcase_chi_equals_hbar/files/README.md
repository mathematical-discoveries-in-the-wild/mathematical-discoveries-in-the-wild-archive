# Partial Result: Hilbert-Space Case of `chi_{p,X} = hbar_{p,X}`

Status: `partial_result_likely_valid`

Source paper: Ivan Yaroslavtsev, *On strongly orthogonal martingales in UMD Banach spaces*, arXiv:1812.08049.

## Result

The source paper asks whether the equality
`chi_{p,X} = hbar_{p,X}`, known there for `X = R`, holds for every
UMD Banach space `X`.

This packet proves the equality for every nonzero real Hilbert space `H` and
every `1 < p < infinity`:

```text
chi_{p,H} = hbar_{p,H} = hbar_{p,R}.
```

The proof uses Gaussian scalarization to show that the Hilbert transform on
`L^p(R;H)` has the same norm as the scalar Hilbert transform, then combines
the scalar-line lower bound for `chi` with Yaroslavtsev's upper bound
`chi_{p,X} <= hbar_{p,X}`.

## Scope

This is a genuine partial subcase, not a full solution of the source problem.
It does not address non-Hilbert UMD spaces, and therefore does not settle the
linear `beta_{p,X}` versus `hbar_{p,X}` comparison problem mentioned in the
source.

The argument is short and standard-looking; novelty confidence is modest. It is
still useful run memory because no exact local packet or web hit was found for
the `chi_{p,H}` Hilbert-space subcase.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:1812.08049.
- `figures/open_problem_crop.png`: page-3 crop of the source open-problem paragraph.
- `code/crop_open_problem.py`: reproducible PyMuPDF crop helper.

## Checks

- Cheap indexes searched for `1812.08049`, strongly orthogonal martingales,
  `chi_{p,X}`, `hbar_{p,X}`, Hilbert transform, and UMD terms.
- Web search for exact `chi_{p,X}`/`hbar_{p,X}` phrases found the source paper
  but no later exact answer.
- The adjacent local `1805.03948` attempt concerns broader Hilbert-transform
  and Burkholder-function constant problems; it does not duplicate this
  Hilbert-space `chi = hbar` subcase.
