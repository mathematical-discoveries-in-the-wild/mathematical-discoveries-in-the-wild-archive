# High convolution powers of circle GMC have Holder densities

Result type: `partial`

Status: candidate rigorous partial answer, likely valid pending expert review.

## Source problem

Garban and Vargas, arXiv:2311.04027, list the open problem: “When are the
convolutions of `M_gamma` Holder functions?” Lin--Qiu--Tan later established
the exact Fourier dimension predicted by Garban--Vargas.

## Claimed contribution

Let

```text
D_gamma = 1-gamma^2                    for gamma < 1/sqrt(2),
D_gamma = (sqrt(2)-gamma)^2            for gamma >= 1/sqrt(2).
```

For every integer `q >= 1`, the `q`-fold convolution has a `C^{k,alpha}`
density whenever

```text
k + alpha < q D_gamma / 2 - 1,
```

where `k` is a nonnegative integer and `0 < alpha < 1`. In particular, every
subcritical circle GMC has a Holder convolution power, and

```text
q_0(gamma) = floor(2/D_gamma) + 1
```

is an explicit guaranteed choice.

The proof is deterministic after the exact Fourier-dimension input:
convolution raises each Fourier coefficient to its `q`th power, after which a
weighted Fourier series is absolutely summable.

## Files

- `main.tex`: proof source.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: Garban--Vargas, arXiv:2311.04027.
- `supporting_fourier_dimension.pdf`: Lin--Qiu--Tan, arXiv:2505.03298.
- `figures/open_problems_crop.png`: exact source question.
- `verification.md`: proof audit and review focus.
- `tmp/pdfs/`: rendered pages used for visual QA.

## Scope

This is a partial answer. It proves sufficient convolution powers and all
regularity exponents forced by pointwise Fourier decay. It does not establish
that the threshold is necessary or resolve endpoint cases.

## Novelty check

Bounded searches on July 22, 2026 used the exact source question together
with “GMC convolution Holder density,” “convolution powers,” and the later
Fourier-dimension papers. No prior statement of this corollary was found.
Novelty confidence is moderate pending specialist review.
