# Positive inputs suffice for induced Schatten quasi-norms

Status: `candidate_full_likely_valid`

Source: Jan Kochanowski, Omar Fawzi and Cambyse Rouzé,
*Two-Indexed Schatten Quasi-Norms with Applications to Quantum Information
Theory*, arXiv:2604.14055.

## Result

The source asks whether every completely positive map satisfies

```text
||Phi||_{q -> p} = ||Phi||^+_{q -> p}
```

for `0 < p,q < 1`, where `+` restricts the input to positive semidefinite
matrices. The packet proves the equality for every `0 < p,q <= infinity`.
In fact, 2-positivity is enough.

For arbitrary `X`, polar decomposition gives the positive block matrix

```text
[ |X*|   X  ]
[  X*   |X| ].
```

Applying `id_2 tensor Phi` preserves positivity. Positive block
factorization therefore gives a contraction `K` such that

```text
Phi(X) = Phi(|X*|)^(1/2) K Phi(|X|)^(1/2).
```

Generalized Schatten Holder, valid for arbitrary positive exponents, yields

```text
||Phi(X)||_p
 <= ||Phi(|X*|)||_p^(1/2) ||Phi(|X|)||_p^(1/2).
```

Since `X`, `|X|`, and `|X*|` have the same singular values, division by the
common Schatten `q` quasi-norm proves that the ratio at `X` is no larger than
the positive-input norm.

## Scope

- This fully answers the ordinary induced Schatten `q -> p` question in the
  source's Summary and Outlook.
- It does not answer the separate question about completely bounded mixed
  two-indexed quasi-norms.
- It does not address the source's interpolation conjecture or
  infinite-dimensional extensions.

See `main.tex` and `solution_packet.pdf` for the full proof and
`verification.md` for the adversarial audit. The source question appears on
page 49 of `source_paper.pdf`.

Cheap run indexes and a bounded primary-source search found the norm-range
result cited by the source but no record of this quasi-norm extension. This
is not an exhaustive novelty certification.

Human review recommendation: **send to a specialist in operator spaces or
matrix analysis**. The key review points are the all-exponent Schatten
Holder step and the precise boundary between the ordinary and completely
bounded mixed-norm questions.
