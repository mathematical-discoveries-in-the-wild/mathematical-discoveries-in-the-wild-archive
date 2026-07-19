# Verification report

Candidate: arXiv:2107.03211, Problem 4.8

## Claim checked

For `X = beta N` and `E = c_00` with its inherited `ell_1` norm, neither
`C_p(X)` nor `E` has JNP, while `C_p(X,E)` has JNP and contains a complemented
copy of `(c_0)_p`.

## Verdict

`likely valid` (full counterexample), confidence 94/100, pending specialist
review.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| `C_p(beta N)` has no JNP | external + independently reduced | Explicitly recorded in arXiv:2003.06764. The packet also reduces it to the normalized finite-measure characterization, Grothendieck's theorem for `ell_infinity`, Hahn--Banach, and Schur's theorem for `ell_1`. |
| `c_00` has no JNP | valid | The weighted lower-semicontinuous gauge gives a barrel that defeats every infinite-dimensional set; finite-dimensional barrel-bounded sets force uniform convergence. |
| Definition and continuity of `S` | valid | For `a in c_0`, only finitely many `|a_n|` exceed any epsilon; the complement of that finite set is a clopen neighborhood of every remainder point. |
| `D(f)` belongs to `c_0` | valid | `f(beta N)` is norm-compact. The uniformly bounded coordinates `pi_n` converge pointwise to zero on `c_00`, hence uniformly on that compact set. |
| Continuity of `D` | valid | The target has pointwise topology; every coordinate is `pi_n` after evaluation at `n`. |
| Complementability | valid | `D S = id`, so `S D` is a continuous projection. |
| Direct JNP witness | valid | `Phi_n(f)=pi_n(f(n))` is weak-star null; on the barrel-bounded set `{S(e_n)}`, its uniform seminorm is at least one. |

## Adversarial checks

- The extension `S(a)` does not require completeness of `c_00`: it is given
  explicitly and its continuity at the remainder is proved directly.
- Compactness of `f(beta N)` is compactness inside the normed space `c_00`,
  which is enough for the finite-net proof; completeness is not used.
- A pointwise-closed barrel in `(c_0)_p` is norm-closed because norm
  convergence implies pointwise convergence. It is therefore a barrel in the
  Banach space `c_0`, so Baire's theorem makes it a norm neighborhood.
- The sequence of diagonal functionals uses infinitely many points of `X` and
  infinitely many linearly independent coefficients, exactly escaping the
  earlier finite-slice theorem.
- The construction works over both real and complex scalars.

No finite computation is relevant to this topological counterexample.

## Packet QA

`main.tex` was compiled with

`latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`.

The resulting four-page `solution_packet.pdf` was rendered at 140 dpi. All
four pages were visually inspected after the final bibliography and page-break
adjustments. The final log contains no undefined citations, overfull boxes, or
underfull boxes, and the rendered pages have no clipping, overlap, unreadable
glyphs, or orphaned theorem headings. The source crop is readable at normal
review zoom.

## Novelty audit

Search date: 2026-07-19.

Searched:

- run `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and
  `proof_gaps/index.tsv`;
- exact source title, arXiv:2107.03211, `Problem 4.8`, and author names;
- `C_p(X,E) JNP converse`, `C_p(beta omega,c_00)`, `neither factor has JNP`,
  `beta omega eventually zero sequences`, and notation variants;
- arXiv:2003.06764 and the 2024 published source page.

Found: the two known no-JNP ingredients and the original paper, whose
published version still labels the converse unknown. Not found: a later paper
explicitly answering Problem 4.8, or the diagonal complemented-copy
construction in this packet.

Novelty conclusion: plausible but not certified.

## Human review recommendation

Send to a specialist. Check first the compact-range lemma and then the
barrel-boundedness of the unit vectors in `(c_0)_p`; these are the only points
where the locally convex topology is doing nonstandard work.
