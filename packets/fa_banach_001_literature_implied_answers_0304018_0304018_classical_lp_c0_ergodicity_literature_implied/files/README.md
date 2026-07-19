# Literature-implied answer: classical spaces in arXiv:math/0304018

Status: literature_implied_answer (classical `c_0`/`ell_p` subcase; broad conjecture remains open).

Source paper: Valentin Ferenczi and Christian Rosendal, *Ergodic Banach Spaces*, arXiv:math/0304018, later published in Advances in Mathematics 195 (2005), 259--282.

Supporting paper: W. Cuellar Carrera, *Non-ergodic Banach spaces are near Hilbert*, arXiv:1611.05500.

## Source Signal

Near the end of arXiv:math/0304018, after Proposition 20 and before the acknowledgements, Ferenczi and Rosendal conjecture that `ell_2` is the only non-ergodic Banach space. They add that they are not even able to prove that `c_0` and `ell_p`, `p != 2`, are ergodic.

## Later Identification

The full `ell_2`-only conjecture is not settled by the later paper. The later theorem proves that every separable non-near-Hilbert Banach space is ergodic, so any non-ergodic separable Banach space must be near Hilbert.

For the explicit classical-space subquestion, the later paper gives the needed identification:

- It states that Ferenczi and Galego had already proved that `c_0` and `ell_p` for `1 <= p < 2` are ergodic.
- It proves that if `ell_p`, `p > 2`, is crudely finitely representable in a separable Banach space `X`, then `X` is ergodic; applying this with `X = ell_p` gives ergodicity of `ell_p` for every `2 < p < infinity`.

Thus the source's named difficulty about `c_0` and `ell_p`, `p != 2`, is answered by the cited literature. The broader conjecture is only reduced to the near-Hilbert case, with later final remarks singling out HAP and twisted-Hilbert spaces as remaining frontiers.

## Provenance

This is not a new proof or counterexample from the run. The relation is a literature-implied identification: Cuellar Carrera explicitly cites Ferenczi--Rosendal and says the paper solves the `ell_p`, `p>2`, question, while the `c_0` and `1 <= p < 2` part is cited there to Ferenczi--Galego.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: local copy of arXiv:math/0304018 when available.
- `supporting_paper_1611.05500.pdf`: local copy of arXiv:1611.05500 when available.
