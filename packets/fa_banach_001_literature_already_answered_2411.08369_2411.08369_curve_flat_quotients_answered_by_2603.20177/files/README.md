# Literature Already Answered

Status: `literature_already_answered`

Source/open-problem paper:
- Gonzalo Flores, Mingu Jung, Gilles Lancien, Colin Petitjean,
  Antonin Prochazka, Andres Quilis, *On curve-flat Lipschitz functions
  and their linearizations*, arXiv:2411.08369, Remark 6.9.

Supporting answer paper:
- Jaan Kristjan Kaasik, Andres Quilis, *Curve-flat functions and
  Lipschitz quotients*, arXiv:2603.20177, Theorem B and Theorem 3.1.

## Identification

Flores--Jung--Lancien--Petitjean--Prochazka--Quilis observe in
Remark 6.9 that their example has curve-flat quotient isometric to
`[0,1]`, and propose studying for which non-purely-1-unrectifiable
compact metric spaces `K` there is a compact metric space `M` with
`M_CF = K`.

Kaasik--Quilis explicitly cite this question in the introduction of
arXiv:2603.20177. They first note that their complete-space exact
construction is not compact except for finite targets, then say that
they modify it "in order to solve this" in the compact setting. The
result obtained is not literal exact realization for every compact
target: for every compact metric space `M`, every countable ordinal
`alpha`, and every `epsilon > 0`, they construct compact `N` whose
`alpha`-order curve-flat quotient is `(1+epsilon)`-isometric to `M`;
Theorem 3.1 further gives exact isometry for finite targets, geodesic
targets, and gapped segments.

## Scope

This packet records a literature answer with scope:

- approximate compact realization for all compact metric spaces, with
  arbitrarily small bi-Lipschitz distortion;
- exact compact realization for the stated classes in Theorem 3.1
  (finite, geodesic, and gapped-segment compact spaces);
- no claim here that exact first-order compact realization holds for
  every compact metric space.

## Files

- `source_paper.pdf`: arXiv:2411.08369 source/open-problem paper.
- `supporting_paper_2603.20177.pdf`: arXiv:2603.20177 answer paper.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

Ledger:
`runs/fa_banach_001/ledger/results/2411.08369_curve_flat_quotients_answered_by_2603.20177.json`
