# Sharp `L_q/L_4` inequality for every even `q`

Status: `partial_solution_likely_valid`

Source: Yam Eitan, *The centered convex body whose marginals have the
heaviest tails*, arXiv:2110.14382, Conjecture 16 on page 10.

## Result

For every centered real log-concave random variable `X` and every even
integer `q>4`,

```text
||X||_q / ||X||_4 <= ||Gamma||_q / ||Gamma||_4,
```

where `Gamma=E-1` and `E` is standard exponential.  Equivalently, for
`q=2m`,

```text
||X||_(2m) / ||X||_4 <= (!(2m))^(1/(2m)) / 9^(1/4).
```

Thus Conjecture 16 is proved for the infinite anchored family `p=4` and all
even `q>4`, extending the source paper's finite computer verification
`p,q<100`.  In Eitan's one-parameter extremal family, equality occurs only at
the two centered-exponential endpoints.  The packet does not claim the full
equality classification for arbitrary `X`, because the quoted reduction
theorem is stated only as an inequality.

## Proof mechanism

Eitan reduces the log-concave problem to

```text
X_z=((1-z)/2) Gamma - ((1+z)/2) Gamma',   0<=z<=1.
```

Writing `y=z^2` and `r_(2m)(y)=E X_z^(2m)`, the moment generating function is

```text
exp(z t)/(1+z t-(1-z^2)t^2/4).
```

The proof shows directly that

```text
2 r'_(2m)(y) r_4(y) - m r'_4(y) r_(2m)(y) >= 0
```

on `[0,1]`.  After removing the endpoint factor `1-y`, every coefficient is
positive.  The all-orders coefficient proof uses an exact change of
variables, two elementary generating-function recurrences, and an explicit
positive formula for the only four exceptional low-degree terms.  No finite
search is used in the proof.

Files:

- `solution_packet.pdf`: theorem and complete proof.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page containing Conjecture 16.
- `code/verify_p4_coefficients.py`: exact finite regression checks for the
  identities and signs used in the proof.

Novelty check: arXiv searches for the exact `p=4` subcase and the later
papers arXiv:2211.05210, arXiv:2505.00944v2, and arXiv:2602.03058 found no
prior all-even-`q` result.  The 2026 final version arXiv:2505.00944v2 still
describes Eitan's conjecture as known only for `p=2` and for even
`p,q<=100`.  Novelty confidence is bounded, not exhaustive.

Human review recommendation: check the coefficient-extraction change
`v -> w/(1-w)`, the four-low-coefficient calculation, and the use of Eitan's
one-parameter reduction.  The symbolic verifier is corroboration only.
