# Internal Appendix: Deficit-Summand Route For `dim Z(X)`

Source: V. Kadets, M. Martin, and R. Paya, "Recent progress and open questions
on the numerical index of Banach spaces", arXiv:math/0605781.

Target: Problem 27, the possible values of `dim Z(X)` for finite-dimensional
real Banach spaces.

Canonical packet: `solutions/full/0605781_dim_zx_five_classification/`.
This appendix is superseded development material for the all-dimensional part
of the `dim Z(X)` cluster, not a separate current solution packet. The main
canonical packet now treats Problem 27 only as a conditional route. This
appendix should not be read as a proof of Problem 27.

Important correction, 2026-06-14: the appendix uses an older
deficit-summand formulation requiring an independent/proper invariant
summand. That formulation is not valid in general: for example
`U(2) <= SO(4)` on `C_R^2` has `dim U(2)=4` and `w(4)=5>4`, but the real
representation is irreducible. The corrected route must allow `W=V`, must not
require `W` to be `G`-invariant, and must include a strict enlargement clause.
The root packet now records this as the corrected defective-subspace theorem.

## Former Conditional Claim

The appendix proved, conditionally on the Small-Module Lemma, that the possible
values are exactly

```text
{ sum_j binom(k_j,2) : sum_j k_j = n }.
```

The Small-Module dependency is not currently closed at automatic-proof
standard; the product tensor case remains the main expansion target. The old
conditional appendix is retained only for provenance and verifier scripts.

The Centralizer Coupling Lemma is proved in
`main.tex` by elementary triangular-number interval bounds.  The verifier
`code/centralizer_interval_symbolic.py` stress-tests those bounds.

## Why This Matters

The Banach-space enlargement idea remains promising after correction: a
subgroup fixing `W^\perp` and acting sphere-transitively on `W` forces the
norm slices over `W` to be radial. However, the old independent proper summand
statement is too strong and should not be used.

## Evidence

Included scripts:

- `code/weyl_small_irrep_scan.py`: classical Weyl-dimension scan through rank
  `80`; it finds no suspicious small irreducible rows after real/quaternionic
  bookkeeping.
- `code/centralizer_coupling_scan.py`: checks the full centralizer interval
  inequality for dangerous atoms with `k<=300` and multiplicity `m<=300`; it
  finds no failures.
- `code/centralizer_interval_symbolic.py`: checks the two triangular-weight
  bounds used in the written centralizer proof through `p,m<=500` and verifies
  the real/quaternionic centralizer families exactly over the same range.

Commands:

```sh
conda run --no-capture-output -n sandbox python code/weyl_small_irrep_scan.py
conda run --no-capture-output -n sandbox python code/centralizer_coupling_scan.py
conda run --no-capture-output -n sandbox python code/centralizer_interval_symbolic.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

## Human Review Recommendation

For current review, start with the root `solution_packet.pdf`, not this
appendix. Use this appendix to audit the older centralizer-coupling route and
the verifier scripts.
