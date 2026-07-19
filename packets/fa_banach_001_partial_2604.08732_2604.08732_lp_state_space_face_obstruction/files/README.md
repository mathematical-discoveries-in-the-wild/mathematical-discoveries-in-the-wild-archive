# Partial packet: norming-face obstruction for `L^p` state spaces

Source paper: arXiv:2604.08732, *weak*-weak points of continuity on the state spaces*.

Result type: partial answer to Problem 3.18.

## Target

Problem 3.18 asks for an analogue, when `1<p<infty`, of the paper's
characterization of weakly compact state spaces in `L^1(mu,X)`.

This packet records a non-reflexive obstruction for constant functions. It is
complementary to the existing reflexive-domain packet
`partial/2604.08732_reflexive_Lp_state_spaces_weak_compact/`.

## Packet result

Let `(Omega,Sigma,mu)` be a probability space, let `1<p<infty`, and let `q`
be conjugate to `p`. For `x in S_X`, put `f(omega)=x`. If the state space

```text
S_f = { g in B_{L^q(mu,X*)} : integral g(w)(x) dmu(w) = 1 }
```

is weakly compact in `L^q(mu,X*)`, then the norming face

```text
F_x = { x* in B_{X*} : x*(x)=1 }
```

is weakly compact in `X*`.

Consequently, any Banach space with a non-weakly-compact norming face gives a
non-weakly-compact `L^p` state space. In particular, for `X=ell_1` and
`x=e_1`, the face `{a in B_{ell_infty}: a_1=1}` is not weakly compact, so the
state space of the constant `e_1` function is not weakly compact.

## Files

- `solution_packet.pdf`: human-readable proof packet.
- `main.tex`: LaTeX source for the packet.
- `source_paper.pdf`: original arXiv PDF, reused from the reflexive packet.
- `figures/open_problem_crop.png`: screenshot crop of the open-problem statement.
- `code/check_constant_face_obstruction.py`: finite-truncation check of the
  constant-face inclusion.

## Status

This is not a full characterization of Problem 3.18. It gives a clean necessary
condition for weak compactness of state spaces of constant functions and a
genuinely non-reflexive negative example.
