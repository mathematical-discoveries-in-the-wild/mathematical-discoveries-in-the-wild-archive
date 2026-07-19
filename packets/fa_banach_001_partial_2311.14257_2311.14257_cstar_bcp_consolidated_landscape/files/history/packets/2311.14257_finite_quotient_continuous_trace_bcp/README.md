# Finite-Dimensional Quotients of Separable-Fibre Continuous-Trace Algebras Have BCP

Status: likely valid partial result.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

Let

```text
0 -> I -> A -> F -> 0
```

be exact, where `F` is finite dimensional and `I` is continuous trace with
separable nonzero elementary fibres. Then

```text
Prim(I) has a countable pi-basis  =>  A has UBCP.
```

Conversely, if `A` has BCP, then `Prim(I)` has a countable pi-basis. Hence in
this finite-dimensional quotient continuous-trace class,

```text
A has BCP  <=>  A has UBCP  <=>  Prim(I) has a countable pi-basis.
```

This removes the extra "ideal is uniformly norming in A" hypothesis from the
previous packet `2311.14257_norming_finite_quotient_bcp`.

## Key Idea

The apparent quotient-dominant obstruction is exactly the annihilator summand.
Let

```text
J = Ann_A(I) = {a in A : aI = Ia = 0}.
```

The canonical action `A -> M(I)` has kernel `J`, and the Busby map
`tau:F -> Q(I)` has kernel `q(J)`. Since `F` is finite dimensional, `J` is
finite dimensional. Its identity is a central projection, so `J` splits off
orthogonally.

Enlarge the ideal to

```text
I# = I direct_sum J.
```

Then `I#` is still continuous trace with separable fibres and the same
countable pi-base condition. The quotient `A/I#` has injective Busby map into
`Q(I)`. Injective C*-homomorphisms are isometric, so the ideal fibres now see
the quotient norm. Thus `I#` is uniformly norming in `A`, and the earlier
matrix-block ballast theorem applies.

## Why It Matters

This closes the finite-dimensional quotient wall for the positive
continuous-trace/separable-fibre program. The old proof handled only extensions
where the ideal already saw a fixed fraction of every norm. The new proof shows
that the only way this can fail is a finite-dimensional direct summand, which
can be absorbed into the ideal without changing the continuous-trace/pi-base
input.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the Busby-kernel identity `ker tau = q(Ann_A(I))`;
- the finite-dimensional annihilator split and centrality of its unit;
- the claim that the quotient after removing the annihilator has injective,
  hence isometric, Busby map;
- the norming calculation for `I# = I direct_sum Ann_A(I)`.

If these steps survive review, the remaining frontier is no longer
finite-dimensional quotients, but finite composition series and broader
Fell/type-I or arbitrary C*-algebra classification.
