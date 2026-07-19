# Compact Lipschitz operators have only the periodic root spectrum

Status: full_solution_likely_valid.

Source target: Abbar, Coine, and Petitjean, *A note on the spectrum of
Lipschitz operators and composition operators on Lipschitz spaces*,
arXiv:2310.08965.

## Result

The first final open question of the source paper has an affirmative answer.
Let \(M\) be a complete pointed metric space and let \(f:M\to M\) be a
base-point-preserving Lipschitz map. If the Lipschitz operator
\(\widehat f:\mathcal F(M)\to\mathcal F(M)\) is compact, and if \(A\) is the
set of all periods of nonzero periodic points of \(f\) (as in the source
paper's Corollary 3.1 notation), then \(A\) is finite
and
\[
   \sigma(\widehat f)\setminus\{0\}
   = \sigma(C_f)\setminus\{0\}
   = \bigcup_{n\in A}\mathbb U_n .
\]

This removes the boundedness / flat-at-infinity hypotheses from the source
paper's main non-weighted spectral description.

## Idea of the Proof

The source paper already proves the conclusion when \(M\) is bounded or when
\(f\) is flat at infinity. For a compact \(\widehat f\), the compactness
characterization from Abbar--Coine--Petitjean, *Compact and weakly compact
Lipschitz operators*, arXiv:2110.03231, gives three metric facts: bounded
sets have totally bounded images, \(f\) is uniformly locally flat, and a
tail condition \(P_3\).

The key extra observation is that \(P_3\) is enough for the only part of
flatness at infinity used in the source's cutoff argument. Namely, far out in
the domain, whenever at least one image is also far out, the quotient
\[
d(fx,fy)/d(x,y)
\]
is uniformly small. Otherwise one could choose escaping pairs with escaping
images and a quotient bounded below; \(P_3\) would force an accumulation point
of the image pairs, impossible because one image coordinate escapes.

Using the same tail cutoff operators as the source paper, this conditional
tail-flatness forces every nonzero eigenvector of \(\widehat f\) to have
bounded support. Once the support is bounded, radial flatness lets us choose
a large closed ball invariant under \(f\). On that bounded restriction the
source corollary applies, so the nonzero eigenvalue is a root of unity coming
from a periodic point. Compactness then makes the set of periods finite.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2310.08965.
- `supporting_paper_2110.03231.pdf`: compactness characterization source.
- `figures/open_problem_crop.png`: crop of the source open question.
- `source_2310.08965.tex.gz`, `supporting_source_2110.03231.tex.gz`: local
  arXiv source archives.
- Ledger: `runs/fa_banach_001/ledger/results/2310.08965_compact_unbounded_lipschitz_spectrum.json`.

## Novelty Check

Cheap run indexes had no prior packet for arXiv:2310.08965 or this spectral
question. Web searches on 2026-06-29 for exact phrases around "spectrum of
Lipschitz operators", "compact Lipschitz operator", "unbounded", and "roots
of unity" returned the source paper but no later answer. The proof uses
known compactness criteria from arXiv:2110.03231 and the source paper's own
cutoff/support tools, but the final unbounded compact case does not appear
to be stated in either paper.
