# Partial solution packet: moduli of the `ell_r` basis in `FBL^p[ell_r]` for `r,p>2`

## Source

- Paper: T. Oikhberg, M. A. Taylor, P. Tradacete, V. G. Troitsky,
  *Free Banach lattices*
- arXiv: `2210.00614`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `partial`
- Target: Remark 9.48 asks what the closed span of
  `(|delta_{e_k}|)` is in `FBL^(p)[ell_r]` when `r,p in (2,infty)`.
- Packet claim: for `2<r,p<infty`, the sequence
  `(|delta_{e_k}|)` in `FBL^(p)[ell_r]` is equivalent to the unit vector
  basis of `ell_s`, where
  `1/s = 1/r + 1/p`.

## Main input

The proof reduces the free-lattice norm to Garling's theorem on absolutely
`p`-summing diagonal maps between sequence spaces:

```text
pi_p(diag(a_k): ell_{r'}^n -> ell_1^n)  ~  ||a||_s,
1/s = 1/r + 1/p,  2<r,p<infty.
```

The source paper itself already points to Garling's diagonal theorems as the
right tool for the `p=1` computations, but leaves the `r,p>2` free
`p`-convex case open.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `figures/open_remark_9_48_crop.png`: crop showing the open remark.
- `tmp/`: LaTeX build output.

## Verification notes

The proof is short once two facts are accepted:

1. The `FBL^(p)` norm of `sum a_k |delta_{e_k}|` is the `p`-summing norm of
   `diag(a_k): ell_{r'} -> ell_1`.
2. Garling's diagonal theorem gives the displayed `ell_s` estimate.

Because the source paper notes that Garling's Theorem 9 has typographical
issues, human review should check the quoted diagonal theorem carefully.
The exponent is consistent with the known `p=2` endpoint
`1/s=1/r+1/2` and with the `p=infty` AM-space endpoint `s=r`.
