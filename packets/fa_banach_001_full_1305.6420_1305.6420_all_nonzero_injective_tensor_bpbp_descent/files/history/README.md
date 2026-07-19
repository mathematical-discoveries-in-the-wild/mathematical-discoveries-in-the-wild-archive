# History

This folder preserves the intermediate packets that led to the current full
qualitative solution. They are intentionally nested inside the full packet and
are not independent durable results in the run index.

## Stages

1. `packets/01_unital_ck_subspace_partial/`
   - Initial partial result.
   - Proved same-modulus BPBp descent when `E` is a closed linear subspace of
     `C(K)` containing `1_K`.

2. `packets/02_state_norming_unit_strong_partial/`
   - Stronger partial result.
   - Replaced the concrete unital `C(K)` hypothesis by the abstract
     state-norming-unit / spear-vector condition.

3. Parent packet `../../`
   - Current full qualitative result.
   - Proves BPBp descent for every nonzero Banach space `E`, with modulus loss
     `eta(epsilon/2)`. Retains the state-norming-unit case as the same-modulus
     refinement.

The historical PDFs are review aids only. The ledger and registry point to the
parent full packet.
