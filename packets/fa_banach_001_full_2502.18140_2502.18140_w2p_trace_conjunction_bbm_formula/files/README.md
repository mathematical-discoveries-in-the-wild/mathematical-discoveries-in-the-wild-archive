# Full Solution Packet: a \(W^{2,p}\) Trace-Conjunction BBM Formula

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Jean Van Schaftingen, “Trace conjunction inequalities,”
  arXiv:2502.18140 (2025), published in *Academy of Romanian Scientists.
  Annals. Series on Mathematics and its Applications* 17 (2025), 321–342.
- Open Problem 1 is on page 3 of the arXiv PDF, immediately after formula
  (1.8).
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

For every \(N\ge 2\), \(1\le p<\infty\), and real-valued
\(u\in W^{2,p}(\mathbb R^N_+)\), the packet proves

```text
lim_{s -> 1-} (1-s)
 ∫_{R^{N-1}} ∫_{R^N_+}
 |Tu(x')-u(y)|^p / |(x',0)-y|^{N+sp} dy dx'

= [pi^((N-1)/2) Gamma((p+1)/2)
   / (p Gamma((N+p)/2))]
  ∫_{R^{N-1}} |T grad u(x')|^p dx'.
```

This affirmatively answers the source paper’s first open problem by giving a
concrete nonhomogeneous Sobolev class on which its smooth trace-conjunction
Bourgain–Brezis–Mironescu formula remains valid. The class is not claimed to
be optimal.

## Proof mechanism

After polar coordinates about each boundary point, the energy is a Mellin
average of the \(L^p\)-norms of the boundary ray quotients

```text
Q_r^omega =
 [u(·+r omega', r omega_N)-Tu]/r.
```

Because `grad u` lies in `W^{1,p}`, its horizontal slices converge strongly
to `T grad u` in `L^p`. The fundamental theorem along boundary rays therefore
gives

```text
sup_omega ||Q_r^omega - T grad u · omega||_p -> 0.
```

The Mellin kernel concentrates at `r=0`, the angular beta integral supplies
the exact constant, and the nonhomogeneous `L^p` norms of `u` and `Tu` make
the `r>=1` contribution `O(1-s)`. The same argument works at `p=1`.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: real crop of page 3 of the source PDF.
- `code/verify_constants.py`: independent numerical and symbolic checks of
  the Mellin normalization and angular constant.
- `verification.md`: verifier output and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

Bounded searches on July 23, 2026 used arXiv and general web indexes with the
exact source title, arXiv id `2502.18140`, the quoted phrase “suitable
Sobolev space,” and close variants involving “trace conjunction,”
“Bourgain–Brezis–Mironescu,” and `W2p`. They found the source preprint and its
published repository record, but no later paper answering Open Problem 1 or
proving this \(W^{2,p}\) extension. The run’s cheap indexes likewise contained
no result or attempt for this arXiv id before this reservation. Novelty
confidence is moderate pending a specialist citation search.

## Scope and human review focus

- The packet fully answers Open Problem 1 in its literal existence form; it
  does not identify the largest possible Sobolev or Besov class.
- It does not answer the source paper’s separate converse problem about
  recovering a weak normal derivative from finite limiting energy.
- Expert review should focus on the \(L^p\)-valued fundamental theorem along
  oblique rays, the uniformity in the hemisphere direction, and the
  large-radius kernel bound.

