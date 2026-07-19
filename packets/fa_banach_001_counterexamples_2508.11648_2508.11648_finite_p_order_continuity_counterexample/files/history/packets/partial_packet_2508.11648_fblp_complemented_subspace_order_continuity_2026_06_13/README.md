# Partial Result: Complemented-Range Order Continuity For `FBL^(p)`

Run: `fa_banach_001`

Source paper: Youssef Azouzi and Wassim Dhifaoui, "Order denseness in free
Banach lattices", arXiv:2508.11648.

Target: the finite-`p` part of the source paper's discussion of
Oikhberg--Taylor--Tradacete--Troitsky Theorem 3.4.  The source explains that
the published proof of order continuity for closed-subspace inclusions used
an order-density assertion that fails in infinite dimension; it proves the
result for `p=infty` and says that for other values of `p` the question
remains open.

Status: candidate partial result.  The closed-subspace problem is solved here
when the subspace is complemented, and more generally when the operator has a
bounded left inverse.  This does not settle arbitrary closed subspaces.

## Claim

Let `1 <= p <= infinity`.  If `T:F -> E` has a bounded left inverse
`R:E -> F`, then the induced lattice homomorphism

```text
bar T : FBL^(p)[F] -> FBL^(p)[E],   bar T f = f o T*
```

is order continuous.  Hence, if `F` is a complemented subspace of `E`, the
inclusion-induced homomorphism `FBL^(p)[F] -> FBL^(p)[E]` is order continuous
for every `p`.

## Packet Files

- `source_paper.pdf`: local copy of the arXiv PDF.
- `figures/open_problem_crop.png`: crop of the passage saying the finite-`p`
  case remains open.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet, if LaTeX rendering succeeds.

## Human Review Recommendation

Check the functorial orientation of the induced maps and the construction of
the operator `S` fixing `T(F)`.  Those are the only real moving parts: once
`S T = T` and `S* R* y* = x*` are verified, the order-continuity argument is
a short pullback contradiction.
