# Verification report

Candidate: type-(B) part of Question 4.10 in arXiv:1303.4844.

## Claim Checked

Every self-adjoint compact operator `T` satisfying `T=-JTJ` is `[Y*,Y]` for
some compact `Y` satisfying `Y=-JY*J`, with
`||Y|| <= sqrt(2)||T||^(1/2)`.

## Verdict

**Likely valid.** No gap or contradictory small case was found.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Spectral symmetry | valid | `TJ=-JT` sends each real `lambda` eigenspace antiunitarily onto the `-lambda` eigenspace. |
| `J`-real basis for a pair | valid | `(u+Ju)/sqrt(2)` and `i(u-Ju)/sqrt(2)` are orthonormal and fixed by `J`; the target block is `i lambda L12`. |
| Two-dimensional route | invalid, correctly rejected | `so(2,C)` is abelian, so a nonzero pair must be enlarged. |
| Three-dimensional formula | valid | Symbolic multiplication gives `[Y*,Y]=i lambda L12`; triangle inequality gives the claimed bound. |
| Four-dimensional formula | valid | All bracket identities and cross-term cancellations were checked symbolically. |
| Finite odd number of pairs | valid | Finite rank on infinite-dimensional `H` gives an infinite-dimensional `J`-invariant kernel; it contains a `J`-fixed unit vector. |
| Infinite block sum | valid | Compactness of `T` gives block target norms tending to zero; the uniform square-root estimate makes the block solution norms tend to zero. |
| Algebra membership | valid | Each block is skew-symmetric in a `J`-real basis; the orthogonal sum therefore satisfies `Y=-JY*J`. |
| Spectral corollary | valid | Necessity is automatic from algebra membership; sufficiency follows by realizing the symmetric null multiset and applying the theorem. |

## Counterexample Search

The exact block formulas were checked symbolically. Orthogonally conjugated
random targets were tested in dimensions 3 and 4 across eigenvalue scales from
approximately `1e-8` to `1e4`.

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1303.4844_type_b_self_commutator_solution/code/verify_blocks.py \
  --cases 1000 --seed 13034844
```

Output:

```text
symbolic checks: PASS
random cases: 1000 (seed=13034844)
maximum relative commutator residual: 1.263e-15
maximum ||Y||/sqrt(||T||): 1.000000000000
claimed upper bound: sqrt(2)=1.414213562373
random checks: PASS
```

The computation checks only the finite identities and norm estimate. The
infinite-dimensional conclusion is proved by the direct-sum argument and is
not established by the numerical test.

## Novelty Check

Search date: 2026-07-19.

Local search:

- `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and
  `proof_gaps/index.tsv`;
- terms: `1303.4844`, exact title, `type B`, `orthogonal Lie algebra`,
  `self-commutator`, and `[X*,X]`.

Primary-source external search:

- exact Question 4.10 wording and the source authors/title;
- `type (B) self-commutator compact operators`;
- `orthogonal Lie algebra compact operators self-commutator`;
- `[X*,X]=A` together with type B / orthogonal operator algebra;
- later structural work on the orthogonal Lie algebra of operators.

No later paper explicitly answering the type-(B) question was located. This
is a bounded search and does not certify historical priority.

## External Dependencies

- Compact self-adjoint spectral theorem: standard and used exactly as stated.
- Real orthogonal normal form for real skew-symmetric matrices: standard;
  only dimensions 3 and 4 are used.

## Human Review Recommendation

Send to human. The main review targets are the formula signs, the odd
finite-rank case, and the inference from vanishing block norms to compactness.
