# Ordinary Pietsch measures already characterize injective dominated polynomials

Status: `full_result_likely_valid`  
Run: `fa_banach_001`  
Agent: `agent_lane_14`  
Source: Botelho--Pellegrino--Rueda, arXiv:1210.3332, "On Pietsch measures for summing operators and dominated polynomials"  
Packet: `runs/fa_banach_001/solutions/full/1210.3332_ordinary_pietsch_injective_polynomial_criterion/`

## Source question

Section 3 asks for a polynomial version of Proposition 2.1:

> given `n in N`, is it true that `j_p^e` is injective if and only if `mu`
> is a Pietsch measure for some injective `p`-dominated `n`-homogeneous
> polynomial defined on `E`?

The source then notes that for `n >= 2` the only non-vacuous scalar setting is
real scalars with `n` odd, and proves an iff statement under the stronger
condition that `mu` is a **differential** Pietsch measure.

## Result

For real Banach spaces, odd `n`, and `p >= n`, the source question has an
affirmative answer with the ordinary Pietsch-measure hypothesis exactly as
asked:

```text
j_p^e is injective
  iff
mu is a Pietsch measure for some injective p-dominated n-homogeneous
polynomial on E.
```

The reverse implication is actually more general: over any scalar field, for
any `p>0` and any `n`, if an injective `p`-dominated `n`-homogeneous polynomial
has `mu` as an ordinary Pietsch measure, then `j_p^e` is injective.

## Proof idea

The source's differential-measure proof shows `P(x)=P(y)` from
`j_p^e(e(x))=j_p^e(e(y))`. For injectivity of `j_p^e`, this is stronger than
necessary. If `j_p^e(e(x))=j_p^e(e(y))`, then the Pietsch seminorm of `x-y`
is zero. Ordinary domination of a homogeneous polynomial gives `P(x-y)=0`.
Since `P(0)=0` and `P` is injective, `x-y=0`. No derivative estimates are
needed.

The forward implication is supplied by the canonical polynomial

```text
P(x) = (j_{p/n}^e(e(x)))^n in L_{p/n}(mu),
```

which is injective when scalars are real and `n` is odd.

## Novelty and duplicate check

Cheap run indexes were searched for `1210.3332`, `Pietsch measures`,
`differential Pietsch measure`, `injective p-dominated polynomial`, and
`j_p^e`; no prior packet for this source question was found.

Web searches for exact title and close phrases including `differential
Pietsch measure`, `j_p^e`, and `injective p-dominated polynomial` found only
the source arXiv record and no later paper with this refinement.

## Files

- `main.tex` - proof packet source.
- `solution_packet.pdf` - compiled proof packet.
- `source_paper.pdf` - local copy of arXiv:1210.3332.
- `figures/open_question_crop.png` - PDF crop of the source question.

## Human review recommendation

Review as a likely valid small full result. The key point to check is that the
ordinary Pietsch domination inequality for the injective polynomial is applied
to `x-y`, not to `P(x)-P(y)`, so differential Pietsch measures are unnecessary
for the injectivity criterion.
