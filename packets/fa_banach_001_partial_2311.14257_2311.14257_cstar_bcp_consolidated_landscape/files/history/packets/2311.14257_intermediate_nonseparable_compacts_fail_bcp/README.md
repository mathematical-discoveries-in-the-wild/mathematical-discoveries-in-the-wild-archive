# Intermediate Algebras over Nonseparable Compacts Fail BCP

Status: likely valid partial obstruction; subsumed as a special case by
`2311.14257_type_i_complete_bcp_classification`.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

Let `H` be a nonseparable Hilbert space, and let `A` be any C*-algebra with

```text
K(H) subset A subset B(H).
```

Then `A` fails BCP.

Equivalently, if a C*-algebra has a faithful irreducible representation on a
nonseparable Hilbert space and the represented algebra contains the compacts,
then it fails BCP.

## Key Idea

Given countably many proposed centers `a_n`, choose a separable reducing
subspace `L` for all of them such that the compressions `a_n|_L` still have
the full norms `||a_n||`.  This is done by starting with countably many
almost-norming vectors for each `a_n` and closing under all words in the
operators `a_n` and `a_n^*`.

Since `H` is nonseparable, `L^\perp` is nonzero.  Put a rank-one projection
`p` in `L^\perp`; then `p in K(H) subset A`, `||p||=1`, and the untouched
`L`-block gives

```text
||p-a_n|| >= ||a_n|_L|| = ||a_n||
```

for every `n`.  Thus `p` escapes every ball `B(a_n,||a_n||)`.

## Why It Matters

This substantially strengthens the earlier finite-dimensional extension
obstruction `K(H)+F`: no multiplier directions inside `B(H)` can repair BCP
once the compact ideal is nonseparable and faithfully represented.

The complete Type I classification packet globalizes this reducing-subspace
argument to every open trivial continuous-trace patch with nonseparable
fibre.

It does not yet settle every Type I algebra with a nonseparable irreducible
representation, because such a representation may only be a quotient
representation, and BCP is not quotient stable.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the construction of the separable reducing subspace `L`;
- the equality `||a_n|_L|| = ||a_n||`;
- the block-diagonal norm computation for `p-a_n`;
- the use of the standard equivalent BCP formulation with balls
  `B(a_n,||a_n||)`.
