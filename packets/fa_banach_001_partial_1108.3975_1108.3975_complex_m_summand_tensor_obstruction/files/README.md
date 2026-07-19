# Partial solution packet: complex M-summand obstruction

## Source

- Paper: Veronica Dimant, Daniel Galicer, Ricardo Garcia,
  *Geometry of integral polynomials, M-ideals and unique norm preserving
  extensions*
- arXiv: `1108.3975`
- Source question: Question 2.7 asks whether, for complex Banach spaces, a
  nontrivial M-ideal `X` in `Y` can have
  `\hat\otimes^{k,s}_{epsilon_{k,s}} X` as an M-ideal in
  `\hat\otimes^{k,s}_{epsilon_{k,s}} Y`.

## Classification

- Status: `partial_result_likely_valid`
- Result type: partial negative answer.
- Scope: all nontrivial complex M-summands `Y = X \oplus_\infty Z`, `k >= 2`.

## Result

If `X` and `Z` are nonzero complex Banach spaces and
`Y = X \oplus_\infty Z`, then the canonical subspace

```text
\hat\otimes^{k,s}_{epsilon_{k,s}} X
```

is not an M-ideal in

```text
\hat\otimes^{k,s}_{epsilon_{k,s}} Y
```

for every `k >= 2`.

Thus any positive example for Question 2.7, if one exists, must be a proper
non-summand M-ideal phenomenon. The most obvious complex escape from the real
negative theorem is ruled out.

## Proof Idea

The finite model is `X = C e_1` inside `Y = ell_infty^2`. In the polynomial
model for the symmetric injective tensor norm,

```text
||p|| = sup { |p(z,w)| : |z| + |w| <= 1 }.
```

Normalize `p_0(z,w)=C_k z^{k-1}w` to have norm one. If a nonzero pure term
`delta z^k` is added, the norm jumps above one. Taking three unit pure terms
`omega_j z^k`, with `omega_j` the cubic roots of unity, forces every attempted
correction `lambda z^k` to miss at least one of them by distance at least one.
This violates the three-ball characterization of M-ideals.

For a general M-summand `Y=X \oplus_\infty Z`, choose unit vectors in `X` and
`Z` and norming functionals. The induced contractive projection from `Y` onto
their two-dimensional span lifts to a contractive symmetric tensor projection,
so the same finite obstruction would be inherited from any hypothetical
global M-ideal structure.

## Files

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/question_2_7_complex_m_ideal_crop.png`: crop of Question 2.7.
- `code/verify_obstruction.py`: small numerical/symbolic sanity check for the
  monomial norm jump.
- `tmp/`: render/build intermediates.

## Limitations

This is not a full negative answer to Question 2.7. It proves the negative
answer for M-summands, not for arbitrary proper M-ideals. A positive example,
if it exists, must use a genuinely non-complemented M-ideal.
