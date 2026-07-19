# Literature-already-answered packet: non-commutative Khintchine for 0 < p < 1

Status: `literature_already_answered`

This packet records an exact later-literature answer. It is not claimed as a
new proof by the pipeline. The 2008 source paper leaves open the validity of
the non-commutative Khintchine inequality for `0 < q < 1`; the 2014
supporting paper explicitly says that this case remained open in the source
paper and proves the inequalities for all `0 < p < 1`.

## Source

- arXiv:0810.5705
- Gilles Pisier, *Remarks on the non-commutative Khintchine inequalities for
  0<p<2*, November 14, 2008.
- Local PDF: `source_paper.pdf`.

## Target question

The source paper defines the non-commutative Khintchine inequality `(0.1)` for
`1 <= q <= 2` and explains that the extrapolation argument proves lower
exponents down to `p >= 1`. On page 3 of the source PDF, Pisier writes that
the result could not then be proved for `0 < p < 1`, because Step 3 was
missing, and leaves open the validity of `(0.1)` for `0 < q < 1`.

The same obstruction is revisited after the proof of Theorem 1.1: the paper
invokes Junge-Parcet for `p >= 1`, but says it is unknown whether the required
estimate `(1.6)` remains true when `0 < p < 1`.

## Later answer

- arXiv:1412.0222
- Gilles Pisier and Eric Ricard, *The non-commutative Khintchine inequalities
  for 0<p<1*.
- Local PDF: `supporting_paper_1412.0222.pdf`.

The supporting paper's abstract states that it proves Khintchine inequalities
in non-commutative `L_p` spaces for all `0 < p < 1`. Its introduction names
the 2008 source as `[25]`, says the `q < 1` case remained open there, and
states that the goal is to prove that case. Corollary 2.2 then states that
`K_q => K_p` remains valid for any `0 < p < 1`; in particular the
non-commutative Khintchine inequality holds for every `0 < q < 1`.

## Scope

This packet only records the later answer to the main `0 < q < 1`
non-commutative Khintchine inequality from `(0.1)`, including the Rademacher
setting and the generalized sequences covered by the later theorem. It does
not claim to settle the source paper's distinct questions about best possible
sizes of operator subspaces, `sigma(q)` versus `sigma(q)_cb` sets, or other
side questions.

## Files

- `main.tex`: compact LaTeX status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source paper arXiv:0810.5705.
- `supporting_paper_1412.0222.pdf`: later paper giving the explicit answer.
- `tmp/`: LaTeX build intermediates only.

## Human review note

The human check should focus on the exact identification of the source
inequality `(0.1)` with the later paper's `K_p`/`K_q` formulation and
Corollary 2.2, and on the scope restriction above.
