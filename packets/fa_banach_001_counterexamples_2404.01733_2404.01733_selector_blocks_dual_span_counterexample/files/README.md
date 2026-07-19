# Counterexample Packet: Selector Blocks Refute the Dual Span Question

Run: `fa_banach_001`

Result type: `counterexample`

## Source Problem

- Piotr Borodulin-Nadzieja, Barnabas Farkas, Sebastian Jachimek, Anna
  Pelczar-Barwacz, *The Zoo of combinatorial Banach spaces*,
  arXiv:2404.01733.
- Local PDF: `source_paper.pdf`.
- Source location: Question 6.1, page 25.
- Evidence crops:
  - `figures/definition_crop.png`: definition of `W(H)` and the weak-star
    norming fact.
  - `figures/open_problem_crop.png`: Question 6.1.

Question 6.1 asks whether, for every hereditary finite cover `F`,

```text
norm-closed span(W(overline(F))) = X_F^*
```

or even

```text
norm-closed conv(W(overline(F))) = B(X_F^*).
```

## Result

Both assertions fail.

Let the underlying set be a disjoint union of finite blocks

```text
Omega = union_k I_k,    |I_k| = m_k -> infinity.
```

Let `F` be the hereditary family of all finite selectors:

```text
F = { E finite subset Omega : |E cap I_k| <= 1 for every k }.
```

Then

```text
X_F = (direct sum_k ell_infty^{m_k})_{ell_1}
```

and

```text
X_F^* = (direct sum_k ell_1^{m_k})_{ell_infty}.
```

The functional `u` whose restriction to each block is the uniform vector
`(1/m_k, ..., 1/m_k)` lies in `B(X_F^*)`. However, every finite linear
combination of elements of `W(overline(F))` has, on each block, support size
bounded by the number of terms in the combination. Choosing a block much
larger than that number gives `ell_1`-distance at least `1/2` from the uniform
block vector. Hence `u` is not in the norm-closed span, and therefore not in
the norm-closed convex hull either.

## Proof Intuition

The family `F` allows a functional in `W(overline(F))` to choose at most one
coordinate from each block. A finite combination of such functionals can use
only finitely many coordinates per block, with a uniform bound equal to the
number of terms in the combination. The dual unit ball, however, contains
blockwise probability vectors spread evenly over arbitrarily large blocks.
Uniformly spread mass on larger and larger blocks cannot be approximated in
the `ell_infty(ell_1)` dual norm by vectors with a bounded number of atoms in
each block.

## Verification Notes

- `F` is hereditary and covers the underlying countable set.
- The closure `overline(F)` consists exactly of all, finite or infinite,
  selectors meeting each block in at most one point.
- The norm identity
  `||x||_F = sum_k ||x|_{I_k}||_infty` holds first on `c_00` and then by
  completion.
- The dual identification follows from standard duality for an `ell_1` sum of
  finite-dimensional spaces.
- If `y` is a linear combination of `r` selector-sign functionals, then
  `supp(y|_{I_k})` has size at most `r` for every `k`. For `m_k>2r`,
  `||u|_{I_k}-y|_{I_k}||_1 >= (m_k-r)/m_k > 1/2`.

## Search Bounds

- Checked local `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv` for `2404.01733`,
  `closed convex hull`, `dual span`, `lambda-property`, and related
  combinatorial-Banach terms.
- Web search was run for the source title, arXiv id, `W(overline(F))`,
  dual-ball span language, and the lambda-property phrasing. It found the
  source paper but no later direct answer to Question 6.1.
- Adjacent local packets on combinatorial spaces, Schreier spaces, and
  isometry groups were checked via index hits; none covered this dual-span
  question.

## Limitations

- This packet answers Question 6.1 negatively for the norm-closed span and
  norm-closed convex hull assertions.
- It does not decide whether some smaller class of combinatorial families,
  such as compact families, has the asserted property.
- It does not address the lambda-property independently. The follow-up
  implication in Question 6.1 no longer follows because the preceding
  norm-closure assertions are false.

## Files

- `README.md`: this summary.
- `main.tex`: full proof packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source Question 6.1.
- `figures/definition_crop.png`: source definition of `W(H)`.
- `tmp/`: render intermediates.

## Human Review Recommendation

Check the direct-sum identification and the support-counting obstruction. These
are the only substantive steps; the rest is unpacking the definitions from
Question 6.1.
