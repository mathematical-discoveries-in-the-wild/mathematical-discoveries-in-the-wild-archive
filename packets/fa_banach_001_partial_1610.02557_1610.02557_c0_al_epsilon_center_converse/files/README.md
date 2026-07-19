# Partial result: `C_0(K)` and AL-space epsilon-center converse

Status: `partial_result_likely_valid`

Source paper: Timur Oikhberg and Pedro Tradacete, *Almost band preservers*,
arXiv:1610.02557.

## Target question

In Section 4 the source paper defines the `epsilon-center`
`epsilon-Z(X)` and notes that every operator in `epsilon-Z(X)` is
`epsilon`-band preserving. The paper asks whether the converse implication
holds in general.

The source itself later proves weaker approximation/center consequences in
some settings, for example a `2 epsilon` center conclusion on compact `C(K)`
spaces via approximation by a band-preserving multiplication operator. This
packet records a sharper partial converse in the canonical sup-norm function
space cases.

## Result

Let `K` be locally compact Hausdorff and let `epsilon >= 0`. Every linear
`epsilon`-band preserving map

```text
T : C_0(K) -> C_0(K)
```

belongs to `epsilon-Z(C_0(K))`. Equivalently, there is `lambda >= 0` such that
for every `f` in the unit ball of `C_0(K)`,

```text
|| ( |Tf| - lambda |f| )_+ ||_infty <= epsilon.
```

The same `epsilon` constant holds for AL-spaces: if `X` is an AL-space and
`T : X -> X` is linear and `epsilon`-BP, then `T in epsilon-Z(X)`.

The constant `epsilon` is sharp already on `ell_infty^2`.

## Proof idea

For `C_0(K)`, automatic continuity from the source paper makes `T` bounded.
For each point `t`, represent the bounded scalar functional
`f -> Tf(t)` by a regular Radon measure `mu_t`. Split off the atom at `t`,
`mu_t = a_t delta_t + nu_t`. The `epsilon`-BP property forces every function
vanishing at `t` to have `|Tf(t)| <= epsilon ||f||`; using regularity of
`nu_t`, this implies `||nu_t|| <= epsilon`. Therefore

```text
|Tf(t)| <= |a_t| |f(t)| + epsilon ||f||
```

and `sup_t |a_t| <= ||T||`. This is exactly the epsilon-center inequality.

For AL-spaces, use the source paper's duality proposition: `T^*` is
`epsilon`-BP on the AM-space `X^*`, identify that AM-space with a compact
`C(K)`, apply the function-space result, and dualize the epsilon-center
property back to `X`.

## Novelty and limitations

- This is not a full solution to the source paper's general Banach-lattice
  converse problem.
- It sharpens the source paper's stated compact `C(K)` consequence from
  `2 epsilon-Z(C(K))` to `epsilon-Z(C(K))`.
- It extends the same sharp constant to locally compact `C_0(K)` spaces and
  to AL-spaces.
- Local index searches for `1610.02557`, `almost band preservers`,
  `epsilon-center`, `epsilon-BP`, `band preserving`, `ABP`, `orthomorphism`,
  and related terms found no existing run packet for this result. A bounded
  web search for exact title/keyword combinations found the source arXiv
  record and no later exact resolution.

## Files

- `main.tex` - proof packet source.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - source paper.
- `figures/open_problem_crop.png` - crop of the Section 4 question.
- `code/render_open_problem_crop.py` - reproducible crop script.

## Human review recommendation

Recommended for human review as a likely valid partial result. The main point
to check is the `C_0(K)` measure argument near a non-isolated point; it is a
direct locally compact adaptation of the source paper's compact `C(K)` proof.
