# Literature-Already-Answered Packet: Positivity of the Real `ell_p` Numerical Index

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Vladimir Kadets, Miguel Martin, Rafael Paya, *Recent progress and open
  questions on the numerical index of Banach spaces*, arXiv:math/0605781.
- Local PDF: `source_paper.pdf`.
- Evidence image: `figures/open_problem_crop.png` (page 3).

Problem 1 asks:

```text
Is n(ell_p) positive for every p != 2?
```

The source records the problem after Theorem 1, which states

```text
n(L_p[0,1]) = n(ell_p) = inf_m n(ell_p^m)
```

and `n(L_p(mu)) >= n(ell_p)` for every positive measure `mu`.

## Supporting Answer Source

- Miguel Martin, Javier Meri, Mikhail Popov, *On the numerical index of real
  `L_p(mu)`-spaces*, arXiv:0903.2704.
- Local PDF: `supporting_paper_0903.2704.pdf`.
- Evidence image: `figures/supporting_answer_crop.png` (page 6).

## Status

The 2006 problem is answered affirmatively by arXiv:0903.2704.

Corollary 3 of the supporting paper proves that for every real `L_p(mu)` space,
`1<p<infty`,

```text
n(L_p(mu)) >= M_p/(12 e),
```

where

```text
M_p = max |t^(p-1)-t|/(1+t^p) > 0
```

for `p != 2`. Corollary 4 then states explicitly that `n(L_p(mu))>0` for
`1<p<infty`, `p != 2`, and says this answers a question also posed in
`[7, Problem 1]`; reference `[7]` is the 2006 Kadets--Martin--Paya survey.

Taking `mu` to be counting measure on `N` gives the affirmative answer for
real `ell_p` in the nontrivial range `1<p<infty`, `p != 2`. The endpoints
`p=1` and `p=infty` are already standard in the 2006 source because `L`-spaces
and `M`-spaces have numerical index `1`.

## Verification Notes

- Same-paper check: the answer is not in arXiv:0605781; that paper states the
  positivity of `n(ell_p)` as Problem 1.
- Separate-source check: arXiv:0903.2704 is a later paper. Its Corollary 4
  explicitly says it answers `[7, Problem 1]`, and `[7]` is the 2006 source.
- Exact identification: the supporting result is stronger than the original
  target, since it proves positivity for every real `L_p(mu)` with
  `1<p<infty`, `p != 2`; `ell_p` is obtained by taking counting measure.

## Search Bounds

- Checked local run indexes and registry for `0605781`, `0903.2704`,
  `n(ell_p)>0`, `positive numerical index`, and the neighboring
  two-dimensional `ell_p` formula.
- Read the original source passage in `data/parsed/arxiv_sources/0605781`.
- Web search located arXiv:0903.2704, whose arXiv abstract states the
  lower bound and nonzero conclusion.
- Downloaded and inspected arXiv:0903.2704; page 6 contains the explicit
  answer statement and citation to `[7, Problem 1]`.

## Limitations

- This is not an original proof from the run.
- This packet records only the positivity of the real infinite-dimensional
  `ell_p` numerical index. It does not claim the neighboring equality
  `n(ell_p)=n(ell_p^2)` or the complex two-dimensional formula.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact review packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_0903.2704.pdf`: later answer source.
- `figures/open_problem_crop.png`: original problem page image.
- `figures/supporting_answer_crop.png`: supporting corollary page image.
- `tmp/`: local render intermediates.

## Human Review Recommendation

Verify the bibliographic identification `[7] = Kadets--Martin--Paya 2006` in
arXiv:0903.2704 and the one-line specialization from real `L_p(mu)` to
`ell_p`.
