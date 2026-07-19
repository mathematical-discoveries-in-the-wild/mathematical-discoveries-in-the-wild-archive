# Finite-dimensional bistochastic quantum random variables are classical

Status: candidate partial result, likely valid.

Source paper: Sergei Plosker and Brian Ramsey, "Bistochastic operators and
quantum random variables", arXiv:2005.00005.

## Target

In Section 5, after extending each classical bistochastic operator on
`L^1(X,mu)` entrywise to `L^1_H(X,mu I_H)`, the authors write:

> We have no example of a bistochastic operator on `L^1_H(X,mu I_H)` that does
> not arise in this way.

The source paper allows separable Hilbert spaces. This packet resolves the
finite-dimensional Hilbert-space case.

## Result

Let `(X,Sigma,mu)` be any finite measure space and let
`H = C^d`. Every bistochastic operator on `L^1_H(X,mu I_H)` in the
Plosker--Ramsey sense is the entrywise extension of a unique classical
bistochastic operator on `L^1(X,mu)`.

Equivalently, in finite quantum dimension there are no bistochastic operators
outside the class constructed in the source paper.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: source crop around the "no example" passage.
- `code/render_open_problem_crop.py`: crop-rendering helper.

## Proof sketch

For measurable sets `E,F`, define a positive map on matrices by
`Theta_{F,E}(A)=int_F B(chi_E A) dmu`. Integral preservation gives
`Theta_{X,E}=mu(E) id`, hence `Theta_{F,E}` is dominated by a scalar multiple of
the identity map. In finite dimensions, any positive map
`Phi:M_d -> M_d` with `0 <= Phi <= c id` is a scalar multiple of `id`; this is
proved directly from rank-one projections and matrix units. Therefore
`Theta_{F,E}` is scalar for every pair `F,E`, producing a scalar Markov operator
`S` with `B(chi_E A)=S(chi_E)A`. Extension from simple functions and then
matrix entries gives `B(fA)=S(f)A` for all scalar `f` and matrices `A`.

## Limitations

This is a partial solution to the source paper's separable-H formulation. The
argument uses the finite-dimensional matrix-unit expansion and norm-density of
bounded/simple matrix-valued functions in the relevant `L^1` space. The
infinite-dimensional case remains open from this packet's standpoint.

## Verification and novelty notes

The proof is analytic and self-contained apart from the source definitions.
Local indexes were searched for `2005.00005`, `bistochastic`, `quantum random`,
`majorization`, and related operator-algebra terms; no existing packet or
attempt covered this target. A bounded web search on 2026-06-21 for exact
phrases around the source "no example" passage found no duplicate.

Human review focus: check the order-interval lemma for positive maps on `M_d`
and the measure-to-density step that constructs the classical operator `S`.
