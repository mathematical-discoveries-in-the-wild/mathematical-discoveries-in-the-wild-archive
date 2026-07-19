# Historical Partial Packet: Schatten Upper Bound

Status: historical/superseded. This was the first partial result obtained in
the push on arXiv:2512.13249. It has been absorbed into the full packet at:

`runs/fa_banach_001/solutions/full/2512.13249_schatten_sharp_decay/`

Historical claim:

`Theta_{S_p(H)}(n) <= n^{-1/p}` for every infinite-dimensional Hilbert space
`H`, every `1 <= p < infinity`, and every `n`.

How it was superseded: the full packet adds the missing lower bound using the
contractively complemented diagonal copy of `ell_p` inside `S_p(H)`, giving
`Theta_{S_p(H)}(n) asymp n^{-1/p}` for `1 < p < infinity`. It also records
the optimal AUS exponent `min(p,2)`.

Contents:

- `main.tex`: historical upper-bound-only writeup.
- `partial_upper_bound_packet.pdf`: rendered historical writeup.
- `tmp/`: LaTeX build outputs for the historical writeup.

This folder is intentionally nested under the full packet so it is not a
separate durable result in the run indexes.
