# Partial packet: reflexive `L^p` state spaces

Source paper: arXiv:2604.08732, *weak*-weak points of continuity on the state spaces*.

Result type: partial answer to Problem 3.18, plus a counterexample to the naive
`L^1`-style singleton analogue.

## Target

Problem 3.18 asks for an analogue, when `1<p<infty`, of the paper's
characterization of weakly compact state spaces in `L^1(mu,X)`.

## Packet result

For `1<p<infty`, if `X` is reflexive and `mu` is finite, then every state
space

```text
S_f = { g in L^q(mu,X*)_1 : integral g(w)(f(w)) dmu(w) = 1 }
```

with `f in S(L^p(mu,X))` is weakly compact in `L^q(mu,X*)`.

Moreover, this does not reduce to the `L^1` singleton phenomenon. For
`X = ell_1^2`, `f(w)=e_1`, and any measurable `h` with `|h|<=1`, the function
`g_h(w)=(1,h(w)) in ell_infty^2` belongs to `S_f`. Thus `S_f` is weakly compact
but not a singleton, even in dimension two.

## Files

- `solution_packet.pdf`: human-readable proof packet.
- `main.tex`: LaTeX source for the packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of the paper's
  open-problem statement.
- `code/check_lp_state_space_example.py`: finite-partition numerical check of
  the two-dimensional example.

## Status

This does not solve the full non-reflexive `L^p(mu,X)` problem. It records the
complete reflexive-domain case and explains why the direct analogue of the
paper's `L^1` singleton conclusion is false for `p>1`.
