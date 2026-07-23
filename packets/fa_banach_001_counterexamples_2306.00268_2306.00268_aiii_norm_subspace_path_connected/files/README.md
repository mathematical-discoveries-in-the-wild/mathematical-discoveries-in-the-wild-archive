# The norm-subspace AIII mobility-gap space is path connected

Status: **full negative result / counterexample likely valid; subject to human
review**.

Chung and Shapiro propose the operator-norm subspace topology as one possible
repair for their tentative one-dimensional mobility-gap space. In class AIII,
that repair collapses the classification completely.

For

```text
L_Lambda = {A in B(H) : [Lambda,A] is compact},
```

define the exact off-diagonal-block version of their tentative v2 space by

```text
M_Lambda = {
  A in L_Lambda :
  dim ker(A), dim ker(A*) are finite,
  polar(A) is in L_Lambda
}.
```

With the operator-norm subspace topology,

```text
pi_0(M_Lambda) = {point}.
```

Thus the tentative AIII Hamiltonian space itself is norm path connected, not
`Z`-classified. The mechanism is compact attenuation: strong paths of local
polar parts become norm paths after multiplication by a compact injective
positive operator.

There is also an explicit index-changing path within genuinely dynamically
localized Hamiltonians. Let `D delta_n = 2^(-|n|) delta_n`. Finite cyclic
shifts converge strongly to the bilateral shift `R`; after multiplying by
`D`, this becomes a norm-continuous path from `D` to `R D`. The polar
half-space index jumps from `0` to `-1`.

The earlier essential-gap theorem remains as the sharp boundary: local
Fredholm blocks have components `Z^2`, and their ordinary-index-zero sector
has components `Z`. Compact attenuation leaves that Fredholm space, which is
exactly why the index can collapse without an essential gap.

## Contents

- `solution_packet.pdf`: complete path-connectedness proof, explicit
  dynamically localized counterexample, and essential-gap comparison.
- `source_paper.pdf`: Chung--Shapiro, arXiv:2306.00268.
- `figures/open_problem_crop.png`: the source's proposed repairs.
- `code/verify_compact_attenuation.py`: finite-window checks of the cyclic
  approximants and norm collapse; it is not used as proof.
- `verification_report.md`: mathematical and computational audit.

Ledger:
`runs/fa_banach_001/ledger/results/2306.00268_aiii_norm_subspace_path_connected.json`.
