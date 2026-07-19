# Literature-Implied Answer: internal almost probabilities lift to probabilities

Run: `fa_banach_001`

Result type: `literature_implied_answer`

Status: full affirmative answer to the auxiliary lifting questions in
arXiv:2112.13955, via the classical Kalton-Roberts stability theorem for
nearly additive set functions.

## Source Problem

- Haosui Duanmu, David Schrittesser, and William Weiss, *Loeb Extension and
  Loeb Equivalence II*, arXiv:2112.13955.
- Local source inspected: `data/parsed/arxiv_sources/2112.13955/loebsec.tex`,
  especially the questions around lines 234--341.
- Local PDF: `source_paper.pdf`.
- Open-question crop: `figures/open_problem_crop.png`.

The paper proves the hyperfinite case of Keisler-Sun Question 3 and gives an
internal almost probability measure in the general case. It then asks:

- whether every internal almost probability space is close to an internal
  probability space;
- whether the almost probability in Theorem `amsinternalapprox` can be replaced
  by an internal probability measure when `H subset Loeb(F)`.

## Answer

Yes, interpreting the displayed almost-additivity condition in the intended
disjoint finite-additivity sense. Every internal almost probability measure is
uniformly infinitesimally close to an internal finitely additive probability
measure on the same internal algebra.

Consequently, the internal almost probability measure constructed in Theorem
`amsinternalapprox` can be replaced by an internal probability measure. Thus
Question `internalapprox` has an affirmative answer:

```tex
H \subset \overline F
quad\Longrightarrow\quad
exists internal probability P on H such that
(Omega,H,P) is Loeb equivalent to (Omega,F,mu).
```

This does not by itself settle the full original Keisler-Sun Question 3 for
arbitrary Loeb-equivalent internal probability spaces, because that still
requires proving `H subset Loeb(F)` in the general non-hyperfinite setting.

## Supporting Theorem

The decisive external input is Theorem 4.1 of:

N. J. Kalton and J. W. Roberts, *Uniformly exhaustive submeasures and nearly
additive set functions*, Transactions of the American Mathematical Society
278 (1983), 803--816, DOI `10.1090/S0002-9947-1983-0701524-4`.

In the needed form, there is a universal constant `K` such that every
`epsilon`-additive real set function on a Boolean algebra is uniformly within
`K epsilon` of a finitely additive signed measure. A positivity correction
turns this into approximation by a finitely additive probability when the
original set function is `[0,1]`-valued and normalized.

## Verification

- `main.tex` gives the proof note.
- `solution_packet.pdf` is the rendered packet.
- Local and web novelty checks found no prior packet or explicit Loeb-paper
  answer to these auxiliary questions.

Human-review focus: check that the source's intended definition of internal
almost probability is disjoint approximate additivity. Without disjointness,
item (2) in the displayed definition is inconsistent already for `A=B=X`.
