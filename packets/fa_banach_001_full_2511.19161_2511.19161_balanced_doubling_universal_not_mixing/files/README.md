# Full result candidate: balanced doubling case for random products

Status: full solution candidate, likely valid pending expert review.

Source paper: Valentin Gillet, *Linear dynamics of random products of weighted
shifts*, arXiv:2511.19161.

Targeted open case: in the noncommuting example on `X = ell_p` or `X = c_0`
with weights

```text
w_l = 1 + 1/(l+1),    v_l = 1 - 1/(l+1),
```

the source paper says it remains unknown what happens when
`Omega = T`, `tau` is the doubling map, `A_1 = [0,1/2)`,
`A_2 = [1/2,1)`, and `mu(A_1)=mu(A_2)=1/2`.

Result: for every `1 <= p < infinity`, and also for `X = c_0`, the random
product sequence is universal/weakly mixing for almost every point of the
circle, but it is not mixing for almost every point.

Mechanism: the logarithm of the relevant product is a centered harmonic
Bernoulli moving average plus a bounded deterministic term. A two-sided
stationary comparison process has unbounded support in both directions and is
ergodic. Its finite one-sided version differs on a zero-density set, so the
actual logarithmic product has limsup `+infinity` and liminf `-infinity` almost
surely. The source criterion then gives universality/weak mixing, while the
negative liminf rules out mixing.

Files:

- `main.tex` / `solution_packet.pdf`: full-result packet.
- `source_paper.pdf`: local copy of arXiv:2511.19161.
- `figures/open_problem_crop.png`: crop of the source open-case sentence.
- `code/make_open_problem_crop.py`: reproducible crop helper.

Review focus: check the transfer from the two-sided stationary linear process
to the finite one-sided logarithmic products, especially the zero-density
estimate for the negative-time tail.
