# Verification report

Date: 2026-07-23  
Agent: `agent_lane_04`  
Model: `GPT5.6`

## Main theorem audit

- Verified the exact equivalence between the source's tentative AIII v2
  Hamiltonians and off-diagonal blocks `A` satisfying:
  `A` local, `ker(A)` and `ker(A*)` finite, and `polar(A)` local.
- Checked the polar deformation
  `U((1-s)|A|+s U*U)` at the kernel, on its orthogonal complement, and at
  both endpoints.
- Checked finite kernel/cokernel pairing for `U+sJ`; for `s>0` its polar part
  is `U+J`, and only finite-dimensional defects change.
- Proved the strong path lemma by finite-dimensional unitary extensions that
  agree with the target isometry on an increasing dense family.
- Proved compact smoothing directly by finite-rank approximation.
- Checked all local-algebra memberships using closure under adjoint,
  multiplication, continuous functional calculus, and finite-rank
  perturbation.
- Audited the coisometry case by applying the isometry construction to the
  adjoint.

## Explicit counterexample audit

- Defined finite cyclic shifts `C_N` that converge strongly to the bilateral
  right shift `R`.
- Chose interpolation paths which agree with `R` on increasing coordinate
  subspaces.
- Verified the exact estimate
  `||(U_t-R)D|| <= 2^(1-N)` on the `N`-th tail interval.
- Verified `polar(U_t D)=U_t` because `D` is positive, injective, and has
  dense range.
- Checked the half-space indices: finite-rank perturbations of the identity
  have index `0`, whereas `R` has index `-1`.
- Checked dynamic localization through
  `H_t = diag(I,U_t) H_D diag(I,U_t)*`; outside a finite coordinate set the
  Borel functional calculus is onsite, and the endpoint has propagation one.
- Checked uniform finite spectral multiplicity for eigenvalues
  `+/- 2^(-|n|)`.

## Computational verification

Command:

```text
/opt/homebrew/Caskroom/miniforge/base/envs/sandbox/bin/python \
  code/verify_compact_attenuation.py
```

The script checks unitarity of the finite cyclic approximants, agreement with
the shift on the growing interior subspaces, exact recovery of the polar
unitary after attenuation, and geometric decay of `||(C_N-R)D||`.
Finite windows are diagnostic only; the proof is infinite dimensional.

## Literature boundary

Primary-source searches included arXiv:1811.07997, arXiv:2306.00268,
arXiv:2406.05385, and arXiv:2602.12512. No exact path-connectedness theorem
or compact-attenuation counterexample was located. Part III still postpones
the mobility-gap Hamiltonian/projection connection.

Novelty confidence is **moderate**. The smoothing mechanism is classical,
but its application gives a direct full resolution of the raw norm-subspace
proposal in the tentative AIII v2 space.

## Scope

The result is complete for class AIII under the source's tentative v2
conditions and raw operator-norm subspace topology. It does not classify all
ten symmetry classes or topologies which control localization constants,
polar parts, or Fermi projections.
