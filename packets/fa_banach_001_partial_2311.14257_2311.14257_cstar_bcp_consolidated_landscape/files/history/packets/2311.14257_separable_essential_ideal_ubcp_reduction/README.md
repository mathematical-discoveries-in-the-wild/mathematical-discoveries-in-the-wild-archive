# Separable Essential Ideals Force UBCP

Status: likely valid partial result and reduction.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Main Results

The packet proves a new general positive mechanism:

```text
If a C*-algebra A contains a separable essential ideal I, then A has UBCP.
```

The proof is uniform and does not assume Type I structure.  For `a in S_A`,
essentiality embeds `A` isometrically into `M(I)`, so a positive contraction
`e in I` can be chosen with `||ae|| > 7/8`.  A countable dense set in the unit
ball of `I` approximates `ae`.  The C*-identity estimate
`||1-2e|| <= 1` gives the fixed-radius cover.

The packet also records the precise shape of any hypothetical C*-algebra
counterexample to `BCP => UBCP`:

- it cannot contain a separable essential ideal;
- if `C` is a countable set witnessing BCP through the exact
  BCP/countable-capture equivalence, then the sequence quotient
  `ell_infty(A)/c_0(A)` contains a unit vector that captures the diagonal copy
  of `C`.

## Why It Matters

This subsumes the elementary positive cases where a countable reservoir is
visible: separable C*-algebras, `B(H)` for separable `H`, multiplier algebras
over separable essential ideals, and countable products through their
separable `c_0`-sum ideals.

It also gives a clean remaining wall.  To prove the full C*-algebra
`BCP => UBCP` statement, it is enough to show that every C*-algebra with BCP
contains a separable essential ideal, or otherwise rule out the asymptotic
capture phenomenon isolated here.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: source paper, arXiv:2311.14257.
- `supporting_paper_2111.04921.pdf`: Liu-Liu-Lu-Zheng BCP/UBCP reference.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the multiplier-norm step `||a|| = sup_e ||ae||` over positive contractions
  in an essential ideal;
- the estimate `||a - 2d|| <= ||a(1-2e)|| + 2||ae-d|| < 9/8`;
- the sequence-quotient diagonal proof, especially the rational scalar
  approximation used to turn non-UBCP into exact line capture in the quotient.
