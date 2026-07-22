# Sharp threshold for low-smoothness Schatten commutators

Status: `candidate_full_result_likely_valid; human_review_needed`

Source: Zhenguo Wei and Hao Zhang, *Complex median method and Schatten class
membership of commutators*, arXiv:2411.05810v2 (2024).

## Result

For `1<p<2` and under the source's general one-dimensional standard-kernel
hypotheses, the implication

```text
b in B_p(R)  =>  [T,M_b] in S_p(L_2(R))
```

holds for every admissible `T` exactly when

```text
alpha > 1/p - 1/2.
```

The strict positive range is already proved inside Section 5.1 of the source.
The packet constructs counterexamples for

```text
0 < alpha <= 1/p - 1/2,
```

including the critical line.

## Construction

Choose compactly supported smooth orthonormal wavelets inside two separated
fixed intervals. At scale `j`, couple `N_j asymp 2^j` input wavelets to the
same number of output wavelets using a Sylvester Hadamard matrix, with kernel
coefficient

```text
gamma_j = 2^(-j(1+alpha)).
```

The scale block has `N_j` singular values of size
`2^(-j(alpha+1/2))`. The full kernel remains `C^alpha`: its scale pieces have
sup norm `O(2^(-j alpha))` and Lipschitz constant
`O(2^(j(1-alpha)))`, and splitting at `2^j |x-x'| asymp 1` gives the desired
Holder estimate.

A single smooth symbol equals one on all output wavelets and zero on all
input wavelets, so the commutator is exactly `-T`. Its Schatten mass is

```text
sum_j 2^(j[1-p(alpha+1/2)]),
```

which diverges precisely at and below the threshold. The operator is still
Hilbert--Schmidt because `alpha>0`.

## Packet contents

- `main.tex` and `solution_packet.pdf`: full sharp-threshold proof.
- `source_paper.pdf`: arXiv:2411.05810v2.
- `figures/open_problem_crop.png`: source question on page 6.
- `code/verify_hadamard_blocks.py`: exact finite matrix checks.
- `verification_report.md`: proof audit and checker output.

Human review should focus on the wavelet selection, the low/high scale Holder
estimate, the orthogonal singular-value decomposition, and matching the
source's positive range to the same hypotheses.
