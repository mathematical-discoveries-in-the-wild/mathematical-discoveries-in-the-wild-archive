# Partial packet: unbounded uniformly continuous epigraph domains

- Source: Sahiba Arora, Jochen Glueck, and Felix L. Schwenninger,
  "The lattice structure of negative Sobolev and extrapolation spaces",
  arXiv:2404.02116.
- Extracted target: after the bounded-domain proof in Section 3, the authors
  say that they do not know whether the same result holds for unbounded
  domains, perhaps under a uniformity assumption on the continuous boundary.
- Packet status: `partial_result_likely_valid`.
- Packet path:
  `runs/fa_banach_001/solutions/partial/2404.02116_unbounded_epigraph_negative_sobolev_partial/`.

## Result

The boundedness assumption can be removed for global epigraph domains with
uniformly continuous boundary. More precisely, let

```text
Omega = { (x',t) in R^{d-1} x R : t > F(x') }
```

where `F:R^{d-1}->R` is uniformly continuous, let `p,q in (1,infty)` be
Holder conjugates, and let `k>=1`. If the positive cone in
`W_0^{k,q}(Omega)` is generating, then the conclusion of the source's
bounded-domain theorem holds for this unbounded `Omega`: the span of the
positive cone in `W^{-k,p}(Omega)` is a KB-space/Banach lattice under an
equivalent span norm, and the canonical copy of `L^p(Omega)` is a lattice
ideal whose embedding is a lattice homomorphism.

The same proof applies after rigid motions and to subgraphs by reflection.

## Proof Idea

The source bounded-domain proof first uses compactness of the closed domain to
push every local boundary patch a little into the domain, and then mollifies.
For a uniformly continuous global epigraph one can replace this finite-cover
step by a single upward translation. Given a small vertical shift `epsilon_n`,
uniform continuity supplies a radius `r_n` such that convolution at scale
`r_n` cannot cross the boundary after the shift. Translation and mollification
then converge strongly on both `L^q(Omega)` and `W_0^{k,q}(Omega)`, giving the
positive approximation operators needed by the source's abstract theorem.

## Scope

This is not a solution of the source's separate generating-cone open problem.
The theorem keeps exactly that hypothesis. It also does not cover arbitrary
unbounded continuous-boundary domains; the uniform geometry used here is the
global uniformly continuous epigraph structure.

## Evidence And Verification

- `source_paper.pdf` is the source arXiv PDF.
- `figures/unbounded_question_crop.png` shows the source passage on PDF page
  12.
- `code/make_unbounded_question_crop.py` regenerates the crop.
- `solution_packet.pdf` is built from `main.tex`.

## Novelty Check

Before promotion, the cheap run indexes were searched for `2404.02116` and
core terms including negative Sobolev spaces, extrapolation spaces, unbounded
domains, uniformly continuous boundary, and epigraphs. No exact duplicate was
found. Local full-source searches only surfaced the source passage itself and
bibliographic citations to the paper, not an answer to this unbounded-domain
question.

## Human Review Focus

Check the zero-extension step for `W_0^{k,q}(Omega)` and the final assertion
that smooth functions with support contained in the epigraph and a local
boundary buffer are in `W_0^{k,q}(Omega)` by cutoff at infinity. The packet
states this in the standard Sobolev convention used by the source.
