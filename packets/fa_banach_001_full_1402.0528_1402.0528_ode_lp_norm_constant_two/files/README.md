# 1402.0528: sharp constant two for ODE-determined variable exponent norms

- arXiv id: `1402.0528`
- source title: `ODE to L^p norms`
- source author: Jarno Talponen
- packet status: `candidate_full_solution_likely_valid`
- target: the open problem after Proposition 3.1 / before Proposition 3.2 asking whether
  `1/2 ||f||_1 <= ||f||_{p(.)} <= 2 ||f||_infty` always holds for the ODE-determined norm.

## Result

The suspected inequalities hold whenever the ODE-determined norm is defined:

```text
(1/2) ||f||_1 <= ||f||_{p(.)} <= 2 ||f||_infty.
```

The constants are sharp in the sense indicated by the examples in the source
paper immediately before the question.

## Packet Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper rendered from the local arXiv TeX.
- `figures/open_problem_crop.png`: rendered source page containing the open problem.
- `code/render_open_problem_page.sh`: helper command used to regenerate the source page image.

## Verification Notes

The proof is analytic and uses no numerical verification.  The upper bound is
a one-line sharpening of the source paper's exponential estimate: once the ODE
profile reaches `||f||_infty`, its derivative is at most `||f||_infty`, not
merely at most the profile.  The lower bound follows from the source
comparison with the Nakano norm and Young's inequality.

Review should check that the statement is understood in the source paper's
standard convention: if `||f||_infty=+infty`, the upper bound is vacuous; for
bounded nonzero `f`, the proof applies directly.
