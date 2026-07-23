# Counterexample to the Hardy-space norm conjecture

agent_id: agent_lane_08  
run_id: fa_banach_001  
arxiv_id: 2511.08000  
source: Catherine Bénéteau, Raymond Cheng, Christopher Felder, Dmitry
Khavinson, Myrto Manolaki, and Konstantinos Maronikolakis, *Metric
projections, zeros of optimal polynomial approximants, and some extremal
problems in Hardy spaces*, arXiv:2511.08000v2  
status: `counterexample_likely_valid`

## Result

Conjecture 4.3 is false, even when the nonconstant inner function does not
vanish at the origin. Take

```text
p = 4,
f(z) = 1/2 - 3z + 2z^3 - z^5,
J(z) = (z - 1/4)/(1 - z/4).
```

Then `f(0)=1/2`, `J` is a nonconstant Blaschke factor, and `J(0)=-1/4`.
Exact Parseval calculations give

```text
||1-Jf||_4^4 = 1344927/4096,
inf_{|c|=1} ||1-cf||_4^4 = 5697/16.
```

The second number exceeds the first by `113505/4096`. Hence for every
unimodular constant `c`,

```text
||1-Jf||_4 < ||1-cf||_4,
```

which is the strict reverse of the conjectured conclusion.

## Mechanism

At the even exponent `p=4`, Parseval turns each fourth power into the squared
`H^2` norm of a square. For the constant phase `c`, the exact answer is a
quadratic in `x=Re(c)` and its minimum on `[-1,1]` is explicit. For the
Blaschke factor `J`, inner-multiplier isometry reduces the calculation to one
finite coefficient pairing.

## Files

- `main.tex` - self-contained proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv v2 source paper.
- `figures/open_problem_crop.png` - source-page crop of Conjecture 4.3.
- `code/verify_counterexample.py` - exact rational verifier; no quadrature.
- `code/make_open_problem_crop.py` - reproducible source crop.

## Novelty check

The run indexes were searched for the arXiv id, title, Hardy-space norm
inequality, inner functions, and zeros of optimal polynomial approximants.
Bounded web searches on 2026-07-23 checked the current arXiv v2 record, the
published Canadian Journal of Mathematics record, the exact conjecture phrase,
`Conjecture 4.3`, and close OPA/Hardy-space terms. They found the source and
background OPA papers, but no later proof, counterexample, correction, or
explicit resolution of Conjecture 4.3.

## Scope

This disproves Conjecture 4.3 exactly. It does not by itself construct an
optimal polynomial approximant with a zero in the disk, so the broader
zero-free OPA question remains open.

## Review recommendation

Likely valid exact counterexample. Human review should check the Parseval
expansion, especially the mixed coefficient
`<f,Jf^2>=353249/16384`. The supplied verifier recomputes every rational
quantity independently.
