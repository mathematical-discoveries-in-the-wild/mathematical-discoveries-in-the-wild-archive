# Literature-Already-Answered Packet: super-reflexive density-size separated sets

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: later literature explicitly answers the super-reflexive question raised
in the source paper and strengthens the quasi-reflexive theorem.

## Original Source

- Tomasz Kania and Tomasz Kochanek, *Uncountable sets of unit vectors that are
  separated by more than 1*, arXiv:1503.08166; Studia Math. 232 (2016),
  19--44.
- Local PDF: `source_paper.pdf`.

## Supporting Answer Source

- Petr Hajek, Tomasz Kania, and Abraham Russo, *Separated sets and Auerbach
  systems in Banach spaces*, arXiv:1803.11501; Trans. Amer. Math. Soc. 373
  (2020), 3113--3145.
- Local PDF: `supporting_paper_1803.11501.pdf`.

## Status Match

The source paper proves that nonseparable quasi-reflexive spaces have
uncountable `(1+)`-separated subsets of the unit sphere, and that
nonseparable super-reflexive spaces have uncountable `(1+epsilon)`-separated
subsets. In Remark 3.7 it gives a reflexive singular-density example where the
supremum defining `eo(X)` is not attained at density `d(X)`, then asks what
happens in the super-reflexive case.

The supporting paper explicitly cites this remark and answers that question:
if `X` is super-reflexive, then `S_X` contains a symmetrically
`(1+epsilon)`-separated subset of cardinality `dens X`. It also considerably
strengthens the quasi-reflexive clause: every infinite-dimensional
quasi-reflexive space has a symmetrically `(1+)`-separated subset of
cardinality `dens X`, with a uniform epsilon version for regular/uncountable
cofinality cardinals below the density.

## Scope

This packet does not claim a solution of the fully general nonseparable
Kottman problem for arbitrary Banach spaces. That broader question is tracked
elsewhere in the run memory, including the later Koszmider negative answer for
the broad nonseparable form.

## Verification Notes

- Same-paper check: arXiv:1503.08166 raises the super-reflexive cardinality
  issue in Remark 3.7; it does not answer it there.
- Separate-source check: arXiv:1803.11501 cites the Kania--Kochanek paper and
  explicitly says its super-reflexive maximal-density theorem answers the
  question from Remark 3.7.
- Duplicate check: the run has a separate packet for the later broad
  nonseparable Kottman negative answer, but no existing packet for this exact
  `1503.08166` Remark 3.7 / maximal-density strengthening.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable status note.
- `solution_packet.pdf`: rendered status packet.
- `source_paper.pdf`: original source paper.
- `supporting_paper_1803.11501.pdf`: later answer source.

