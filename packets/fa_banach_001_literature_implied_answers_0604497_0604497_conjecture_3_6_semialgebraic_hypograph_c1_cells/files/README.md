# Literature-implied answer: Conjecture 3.6 on semialgebraic hypographs

Status: `literature_implied_answer (full resolution of Conjecture 3.6)`

## Original conjecture

Vern I. Paulsen and James P. Solazzo, *Interpolation and Balls in
`C^k`*, arXiv:math/0604497, Conjecture 3.6 (arXiv PDF page 26), ask:

> Let `f:[0,1] -> R` be continuous and nonnegative, and let
> `C={(x,y):0<=x<=1, 0<=y<=f(x)}`. If `f` is nondifferentiable at
> infinitely many points, must `C` fail to be semialgebraic?

## Identification and proof

Yes. If `C` were semialgebraic, its upper vertical-fiber endpoint would
also be semialgebraic by Tarski-Seidenberg:

```text
graph(f) = {(x,y) in C : there is no t>y with (x,t) in C}.
```

Thus `f` would be a semialgebraic function. The semialgebraic `C^1` cell
decomposition theorem partitions `[0,1]` into finitely many point cells and
interval cells on each of which `f` is `C^1`. Hence `f` can be
nondifferentiable only at finitely many partition points, a contradiction.

For a precise accessible statement, Bhardwaj and van den Dries,
*On the Pila-Wilkie theorem*, arXiv:2010.14046, Theorem A.14 (PDF page 35),
gives `C^1` cell decomposition for definable functions. Semialgebraic sets
and functions are definable in the real field, so it applies directly.

This is an agent-identified implication of a classical semialgebraic
regularity theorem, not a new theorem. Paulsen-Solazzo's Proposition 3.7 is
therefore no longer conditional on Conjecture 3.6. This packet does not
independently audit the `O_3`/`O_4` dimension inconsistency in the wording and
proof surrounding their Conjecture 3.5 and Proposition 3.7.

## Search status

A bounded search through 22 July 2026 checked the run indexes, the local arXiv
corpus for the exact title/authors/conjecture wording, exact web searches for
the conjecture and the `P_{a,c}` construction, and later papers citing the
source. No later paper explicitly resolving Conjecture 3.6 was found. The
decisive known ingredient is general `C^1` cell decomposition.

## Files

- `source_paper.pdf`: arXiv:math/0604497.
- `supporting_paper_2010.14046.pdf`: accessible statement of `C^1` cell
  decomposition.
- `main.tex`, `solution_packet.pdf`: compact status note and proof.
