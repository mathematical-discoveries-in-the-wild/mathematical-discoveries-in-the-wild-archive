# A radial-twist counterexample to the Abel-average question

Status: `candidate_full_counterexample_likely_valid`

Source: F. Bracci, Y. Kozitsky, and D. Shoikhet, *Abel averages and
holomorphically pseudo-contractive maps in Banach spaces*, arXiv:1311.6698;
J. Math. Anal. Appl. 423 (2015), no. 2, 1580-1593,
DOI 10.1016/j.jmaa.2014.10.079.

## Result

The source question has a negative answer, already for `X=C` and `D=B`, the
open unit disc.

Set

- `a=sqrt(7)/5` and `b=3/5`;
- `phi(r)=0` for `r<=a`, interpolate continuously and linearly from `0` to
  `pi/3` on `[a,b]`, and set `phi(r)=pi/3` for `r>=b`;
- `h(z)=(1-2 exp(i phi(|z|)))z`.

Then `h` is continuous, hence weakly closed, and

`Re <h(z),z*> = (1-2 cos(phi(|z|)))|z|^2 <= 0`,

so it is 0-dissipative. Moreover

`(I-h)(z)=2 exp(i phi(|z|))z`

is globally injective on `B` and its inverse on `B` is the holomorphic map
`Phi_1(w)=w/2`.

However, put `exp(i psi)=(2+i sqrt(3))/sqrt(7)` and

- `z_1=sqrt(7)/5`,
- `z_2=(3/5)exp(-i psi)`.

These are distinct points of `B`, but

`(I-(1/2)h)(z_1)=(I-(1/2)h)(z_2)=3sqrt(7)/10 in B`.

Thus the Abel average at `alpha=1/2` is not even single-valued, while the
average at `alpha_0=1` exists, is holomorphic, and maps `B` into itself.

## Files

- `main.tex`: complete counterexample proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:1311.6698.
- `figures/open_problem_crop.png`: source PDF page 13 crop containing the
  complete question.
- `verification_report.md`: explicit hypothesis-by-hypothesis audit.
- `code/check_counterexample.py`: optional floating-point sanity check; the
  packet proof uses exact arithmetic and does not depend on it.

## Relation to the previous partial result

The separate upward-propagation theorem remains valid: an Abel average at
`alpha_0` forces all averages for `alpha>=alpha_0`. This example shows that
the direction `0<alpha<alpha_0` can fail and therefore closes the original
question negatively.

## Literature status

A bounded novelty search used the exact question, the source title and
authors, arXiv:1311.6698, `weakly closed 0-dissipative Abel average`, and
counterexample/negative-answer variants. No later answer or matching
construction was found. The question is reproduced as open in Section 5.5
of M. Elin, S. Reich, and D. Shoikhet, *Numerical Range of Holomorphic
Mappings and Applications* (Birkhauser, 2019). Novelty confidence is
moderate-high within the searched sources, but not a claim of exhaustive
bibliographic priority.

## Human review recommendation

Review as a likely valid full negative answer. The essential checks are the
support-functional calculation, global injectivity of `I-h`, the fact that
its inverse restricts to `w/2` on `B`, and the exact two-point collision for
`I-(1/2)h`.

