# The Sequence-Quotient Reflection Theorem Fails for Compact Operators

Status: likely valid counterexample to an agent-generated intermediate lemma,
not a counterexample to arXiv:2311.14257.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
C*-algebra BCP/UBCP classification.

## Main Point

The proposed shortcut

```text
asymptotic countable capture in A_infty
  => actual countable capture in A
```

is false even when `A=K(ell_2)` and the countable set is a BCP witness.

Let `A=K(ell_2)` and let `C` be a countable dense subset of the unit sphere of
`A`.  Then:

1. `C` is a BCP witness for `A`;
2. there is `v in ell_infty(A)/c0(A)` such that
   `dist(Delta(c), C v)=||c||` for every `c in C`;
3. there is no `u in S_A` such that `dist(c, C u)=||c||` for every `c in C`.

Thus sequence-quotient capture is too weak to reflect back to `A`.

## Why This Matters

The previous push suggested that `BCP => UBCP` might follow by reflecting the
UBCP-negation diagonal capture from `A_infty` back to `A`.  This packet shows
that such reflection is false in the strongest naive form, even for a
separable C*-algebra that has UBCP.

So the full problem remains open, and the proof must use something more
specific than bare diagonal capture in the sequence quotient.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source Question 3.

## Review Focus

Check the compact-operator limit

```text
lim_n ||a - lambda p_n|| = max(||a||, |lambda|)
```

for rank-one projections `p_n` onto an orthonormal basis.  This is the whole
engine of the counterexample.

