# Exact trace-tail formula for the De Blasi measure

Status: `candidate_full_solution_likely_valid`

Source: J. Hamhalter, O. F. K. Kalenda, A. M. Peralta, and H. Pfitzner, *Measures of weak non-compactness in preduals of von Neumann algebras and JBW*-triples*, arXiv:1901.08056. Question 12.1 on PDF page 54 asks for a trace formula for the De Blasi measure in a semifinite von Neumann predual, at least for finite sigma-finite von Neumann algebras.

## Candidate full answer to the finite sigma-finite clause

Let `M` be a finite sigma-finite von Neumann algebra and choose a faithful normal finite trace `tau`. Identify `M_*` with `L1(M,tau)`. For a bounded set `A` define

`u_tau(A) = lim_{delta down to 0} sup_{h in A} sup{ ||h e||_1 : e projection, tau(e) <= delta }`.

The packet proves the exact identity

`omega(A) = u_tau(A)`.

The lower estimate follows because relatively weakly compact subsets of the predual are uniformly small on small-trace right projections. This is derived directly from the source paper's single-control-state characterization (Theorem 11.1(b')). For the reverse estimate, truncate each density spectrally at height `c`. The truncation lies in a common bounded `L2`-ball, hence in a relatively weakly compact subset of `L1`, and the discarded tail is exactly `h e` for a projection with trace at most `sup_A ||h||_1/c`.

This settles the explicit fallback in Question 12.1. It does not settle the general semifinite case with `tau(1)=infinity`, where a second trace-tightness term is expected.

## Files

- `main.tex` and `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Question 12.1 from page 54.
- `code/render_open_problem_crop.py`: reproducible crop renderer.
- `code/verify_trace_tail.py`: finite-matrix sanity checks for the spectral truncation identities and inequalities.

## Verification

Run from this packet directory:

```bash
python code/verify_trace_tail.py
```

The script checks 240 random complex matrices across dimensions 2, 3, 5, and 8 and multiple truncation levels. It is a sanity check, not part of the proof.

Human review should focus on the use of Theorem 11.1(b') to establish uniform right-tail smallness and on the identification of the `L2`-ball as a weakly compact subset of `L1` for a finite trace.
