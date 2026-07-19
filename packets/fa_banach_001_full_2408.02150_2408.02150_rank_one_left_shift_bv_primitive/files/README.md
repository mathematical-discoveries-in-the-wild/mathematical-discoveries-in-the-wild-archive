# Candidate Full Result: BV Primitive Description for Rank-One Sun-Dual Controls

- **Run:** `fa_banach_001`
- **Agent:** `agent_lane_14`
- **arXiv:** `2408.02150`
- **Source paper:** Sahiba Arora and Felix L. Schwenninger, *Admissible operators for sun-dual semigroups*
- **Source location:** Proposition 5.3 and Remark 5.4(c), page 14 of the arXiv v3 PDF
- **Status:** `candidate_full_solution_likely_valid_needs_human_review`

## Claim

For the nilpotent left-shift semigroup on
`X^sun = {b in C([0,1]) : b(1)=0}`, the source paper's rank-one
`C`-admissible control characterization can be simplified exactly as asked in
Remark 5.4(c):

```text
B_C(C, X^sun, (L(t))) =
{ C' : C in L(X_1,C) and C'(1)=partial b for some b in X^sun cap BV([0,1]) }.
```

## Idea

The source characterization says `C'(1)=partial b=widetilde partial c` for
some continuous `b in X^sun` and some `c in BV([0,1])`. Restricting
`widetilde partial c` to compactly supported test functions gives a finite
Radon measure on `(0,1)`. Hence the distributional derivative of the continuous
function `b` is a finite measure, so `b` is automatically of bounded variation.

Conversely, if `b in X^sun cap BV([0,1])`, integration by parts for BV functions
shows `partial b = widetilde partial b`: the boundary term at `1` vanishes
because `b(1)=0`, and the boundary term at `0` vanishes because the
`widetilde D` test functions vanish at `0`.

## Files

- `main.tex` - proof packet
- `solution_packet.pdf` - compiled packet
- `source_paper.pdf` - source paper PDF compiled from the local arXiv v3 source
- `figures/open_problem_crop.png` - crop of page 14 containing Proposition 5.3 and Remark 5.4(c)

## Verification

- Source paper compiled locally from `data/parsed/arxiv_sources/2408.02150`.
- Packet compiled with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

No computational check was needed.

## Novelty Check

Local indexes were searched for `2408.02150`, the title, `admissible operators`,
`sun-dual`, `zero-class`, `BV`, `partial b`, and related semigroup terms. No
prior local packet or attempt for this exact question was found.

Web searches on 2026-07-19 for the exact title, `C'(1)=partial b`, `sun-dual
semigroups zero-class assumption p=1`, and close variants found the arXiv v3
source and publication metadata for the journal version, but no later paper or
erratum resolving Remark 5.4(c).

## Review Focus

Human review should check the interpretation of equality between `partial` and
`widetilde partial` in the source notation. Under the standard distributional
interpretation used in the source, the BV boundary-term argument proves the
claimed simplification.
