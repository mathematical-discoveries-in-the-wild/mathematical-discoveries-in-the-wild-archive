# 2604.23864 endpoint complex Sobolev interpolation in dimension one

- `status`: candidate partial result likely valid
- `agent_id`: `agent_lane_08`
- `lane`: 8
- `date`: 2026-07-03
- `source arXiv`: 2604.23864
- `source paper`: Hugues Moyart, *Bourgain's method for K-closedness in the semicommmutative setting*
- `packet`: `solution_packet.pdf`

## Claim

For the one-dimensional torus, including the semicommutative case
`N = L_\infty(T) \bar\otimes M`, the endpoint complex interpolation problem for the homogeneous
Sobolev couple has an affirmative answer:

```tex
[W_{1,1}(N), W_{1,\infty}(N)]_\theta = W_{1,p}(N),
\qquad 1/p = 1-\theta,\quad 0<\theta<1,
```

with equivalent norms, under the standard homogeneous Sobolev identification modulo constants used
in the source paper.

## Scope

This is a partial result only. The source paper's open endpoint problem remains open in dimensions
`d >= 2`. In higher dimensions the gradient range is the curl-free/mean-zero range of the Leray
projection, and the simple proof below would require endpoint boundedness of that projection on
`L_1` and `L_\infty`.

## Verification

The proof reduces the one-dimensional Sobolev couple through the derivative map to the zero-mean
subcouple of `(L_1(N), L_\infty(N))`. That subcouple is the range of `I - E`, where `E` is the
trace-preserving conditional expectation onto constant functions. Since this projection is bounded
on both endpoints, complex interpolation of complemented subcouples gives the result.

No computational checks are needed.

## Search Notes

Checked local run indexes for `2604.23864`, `W_{1,1}`, `W^{1,1}`, Sobolev endpoint interpolation,
zero-mean, and Leray terms; no prior packet for this target was found. Bounded web search for
endpoint complex interpolation of `W^{1,1}` and `W^{1,\infty}` found no exact one-dimensional
semicommutative packet-level match. Novelty confidence is moderate because the argument is an
elementary reduction and may be folklore.

## Files

- `source_paper.pdf`: source paper PDF from arXiv.
- `figures/open_problem_crop.png`: crop of the source open-problem sentence on page 4.
- `main.tex`: packet source.
- `solution_packet.pdf`: rendered packet.
