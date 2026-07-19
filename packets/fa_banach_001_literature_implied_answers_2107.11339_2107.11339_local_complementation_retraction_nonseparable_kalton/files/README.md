# Literature-implied answer: local complementation vs Lipschitz retraction

Status: `literature_implied_answer (nonseparable negative; separable case open)`

Source target: Antonio Aviles, Gonzalo Martinez-Cervantes, Abraham Rueda
Zoca, *Local complementation in Banach spaces and its preservation under free
constructions*, arXiv:2107.11339.

## Identification

The source Introduction, page 2, recalls Kalton's problem asking whether local
complementation is equivalent to the existence of a Lipschitz retraction
`r: X -> Y`.  The paper then proves equivalence with a weaker
Lipschitz-local-complementation notion, not with an actual retraction onto
`Y`.

For the broad formulation without separability, the answer is already
negative by known literature after a direct identification:

```text
Kalton gives a nonseparable Banach space E which is not a Lipschitz retract
of E**.
Local reflexivity locally 1-complements every Banach space E in E**.
Therefore E subset E** is locally complemented but not a Lipschitz retract.
```

This is an implied answer rather than an explicit answer to arXiv:2107.11339:
the supporting papers do not present themselves as resolving that exact
sentence in the source paper.

## Supporting evidence

- arXiv:2106.13554, page 4, states that a closed subspace `Y` locally
  complemented in `X` is a Lipschitz retract of `X` iff `Y` is a Lipschitz
  retract of its bidual, and notes that the separable bidual-retraction
  problem remains open.
- arXiv:2311.13289, page 4, records Kalton's nonseparable Banach space not
  Lipschitz retract of its bidual and combines it with local reflexivity to
  produce a Banach-space local-retract/non-Lipschitz-retract example.

## Scope

This packet answers only the broad nonseparable form negatively.  It does not
settle the separable Lindenstrauss/Benyamini-Lindenstrauss bidual-retraction
problem.  That separable target is already represented in the run by the prior
attempt `runs/fa_banach_001/attempts/1606.03926_lindenstrauss_bidual_retraction_attempt.md`.

## Files

- `source_paper.pdf`: arXiv:2107.11339.
- `supporting_paper_2106.13554.pdf`: Hajek-Quilis reduction/context.
- `supporting_paper_2311.13289.pdf`: explicit Kalton/local-reflexivity
  implication.
- `main.tex`, `solution_packet.pdf`: compact status note.
