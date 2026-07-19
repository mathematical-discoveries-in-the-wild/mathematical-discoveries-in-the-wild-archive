# Literature Already Answered: LSZ right-2 sequence-space conjecture

Status: `literature_already_answered`

Source paper: Leonard Cadilhac, "Majorization, Interpolation and noncommutative Khintchine inequalities", arXiv:1812.03861.

Supporting answer: Leonard Cadilhac, Fedor Sukochev, Dmitriy Zanin, "Lorentz-Shimogaki-Arazy-Cwikel Theorem revisited", arXiv:2009.02145.

## Source Question

The source signal is Conjecture 1 in the introduction of arXiv:1812.03861, quoting Levitina-Sukochev-Zanin: if `E` is a quasi-Banach symmetric sequence space, then `E` is right-2-monotone exactly when `E` is an interpolation space between `ell^p` and `ell^2` for some `p in (0,2]`.

Cadilhac's 2018/2020 paper itself solves the analogous function-space formulation and records partial sequence-space progress, but it explicitly says the missing sequence-space reverse implication is obstructed by the fact that the couple `(ell^p, ell^q)` was not known in general to be Calderon.

## Answer Identification

The later Cadilhac-Sukochev-Zanin paper arXiv:2009.02145 explicitly says it resolves the Levitina-Sukochev-Zanin conjecture in the affirmative. Its Theorem 1.2 states, for every quasi-Banach sequence space `E subset ell_infty` and every `q >= 1`, that the following are equivalent:

- there exists `p < q` such that `E in Int(ell^p, ell^q)`;
- `E` satisfies the tail-majorization monotonicity property `|v|^q \prec\prec_t |u|^q => v in E` with a norm bound;
- the same implication without the norm-bound clause.

For `q = 2`, this is exactly the right-2 monotonicity characterization quoted in arXiv:1812.03861, with Cadilhac-Sukochev-Zanin's tail-majorization notation matching the source paper's right-majorization orientation.

## Scope And Provenance

This packet records a literature answer, not an original proof or new partial result from the run. The supporting authors explicitly identify the problem as the conjecture of Levitina and the last two authors, and they state that they resolve it in the affirmative.

The scope is full for the source conjecture as quoted in arXiv:1812.03861 with `q=2`. The packet does not claim any new theorem beyond identifying the later literature resolution.

## Literature Check

Searches performed on 2026-06-19:

- Local run indexes for `1812.03861`, `Levitina`, `Sukochev`, `Zanin`, `right-2-monotone`, `majorization`, `Khintchine`, and `Calderon`.
- Local arXiv source/title pools for the same phrases.
- Web search for `"Levitina" "Sukochev" "Zanin" "right-2-monotone"`, `"right-2-monotone" "symmetric sequence space"`, and `"Levitina, Sukochev and Zanin" conjecture sequence spaces interpolation ell^p ell^2`.

The search found arXiv:2009.02145 as the decisive explicit answer, and arXiv:2106.03083 as a corroborating later paper describing a simple positive solution and the Calderon-Mityagin connection.

## Files

- `source_paper.pdf`: arXiv:1812.03861.
- `supporting_paper_2009.02145.pdf`: arXiv:2009.02145.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered compact status note.
