# Cantor Product with Rank-One Cotangent Module

Result type: `full`

Status: candidate full affirmative solution, likely valid pending expert
review.

Source paper:

- Martin Kell, “On Cheeger and Sobolev differentials in metric measure
  spaces,” arXiv:1512.00828; Rev. Mat. Iberoam. 35 (2019), no. 7,
  2119–2150.
- Question location: page 25, immediately before Theorem 3.21.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

Let `C` be the middle-thirds Cantor set with standard Cantor measure `nu`.
For every `1 < p < infinity`, the compact Euclidean product

```text
M = [0,1] x C,
m = Lebesgue x nu
```

is doubling and is not a Lipschitz differentiability space, while

```text
D(E_p) = L^p(C,nu; W^{1,p}([0,1])),
E_p(f) = integral |partial_x f|^p dm.
```

Consequently its `L^p`-cotangent module is exactly `L^p(M,m) dx`: it is
nontrivial and has constant local dimension one. This affirmatively answers
the source question with `N=1`.

The non-differentiability argument uses Bate’s independent Alberti
representations. The Cantor coordinate has derivative zero along every
Lipschitz curve fragment, so its chart differential would have to vanish;
vertical Cantor difference quotients are nevertheless identically one.

## Files

- `main.tex`: complete proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: the source arXiv paper.
- `supporting_paper_bate_1208.1954.pdf`: decisive Alberti-representation
  theorem used in the proof.
- `figures/open_problem_crop.png`: crop of the exact source question.
- `verification.md`: build and review notes.
- `tmp/`: LaTeX intermediates and page renders used for visual QA.

## Novelty check

Bounded local-index and web searches on July 22, 2026 used arXiv:1512.00828,
the exact source title, and close combinations of “Cantor,” “cotangent
module,” “Sobolev module,” “rank one,” and “differentiability space.” They
found the source and background/citation material but no direct answer or
occurrence of this product example. Novelty confidence is moderate pending a
specialist search.

## Human review focus

Please check:

- the exact identification of the relaxed energy and its full domain;
- the passage from the energy formula to the isometric rank-one module;
- the application of Bate’s Theorem 7.8 and the chart chain rule to the
  Cantor-coordinate function.
