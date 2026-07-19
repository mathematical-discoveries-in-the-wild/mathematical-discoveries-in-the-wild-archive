# A full answer to Question 8.4 via `Fin tensor Fin`

Status: `candidate_full_solution_likely_valid`; independent human review is
recommended.

Question 8.4 of Sobota--Zuchowski asks whether an ideal on `omega` can have the
Local-to-Global Boundedness Property for lower semicontinuous submeasures
`(LGBPl)` while failing the corresponding property for arbitrary submeasures
`(LGBPs)`.

The answer is affirmative. On the countable set `omega x omega`, let

`J = {A : {n : A_n is infinite} is finite} = Fin tensor Fin`.

The row-counting submeasure

`rho(A)=|{n : A_n is infinite}|`

is finite but unbounded on `J`, so `J` fails `(LGBPs)`. On the other hand, if
an lsc submeasure is finite on `J`, a finite-tail diagonal argument forces it
to be bounded on the whole ground set. Thus `J` has `(LGBPl)`.

The argument is entirely in ZFC and transports to an ideal on `omega` through
any bijection `omega -> omega x omega`.

## Files

- `solution_packet.pdf`: complete proof and review notes.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:2510.19744.
- `figures/open_problem_crop.png`: Question 8.4 on PDF page 47.
- `verification.md`: analytic and visual verification record.

## Scope and novelty

This fully answers Question 8.4 as written. A bounded search of the run
indexes, arXiv, and the web found the source and general work on
`Fin tensor Fin`, but no later answer or the same LGBPl/LGBPs separation. The
novelty conclusion is provisional rather than exhaustive.
