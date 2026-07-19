# Full Packet: Stability Implies Formula Oscillation Stability

Run: `fa_banach_001`

Agent: `agent_lane_19`

Status: `claimed_full_solution_referee_expanded_human_review_needed`

Source target: James Hanson, *Indiscernible Subspaces and Minimal Wide Types*,
arXiv:2004.03062, Question 4.3.

## Result

This packet claims a positive answer to Hanson Question 4.3:

> If `T` is a stable Banach theory, then every unary formula is oscillation
> stable on models of `T`.

The proof uses a formula-aware version of the Krivine-Maurey/Raynaud stable
type argument. Instead of trying to pull an infinite Hilbert subspace out of
the Dvoretzky-Milman ultrapower construction, it runs the minimal conic-class
argument directly in an enriched one-variable type space over the original
subspace `Y` and the parameter of the formula.

## Referee Expansion Update

The 2026-06-16 referee pass found and repaired one genuine compression in the
first packet: a far-out subsequence argument does not by itself control vectors
involving the early basis elements of the closed span. The proof now uses a
block extraction lemma. The induction maintains approximate enriched type,
not merely approximate norm and `phi` value, on finite nets of each initial
span; this is what lets the estimates pass to the whole closed subspace.

The Raynaud/Krivine-Maurey transfer is also expanded into explicit steps:
enriched convolution, minimal conic class, common continuity point, spreading
model comparison, approximate eigenvectors, and the multiplicative norm
classification producing the `ell_p` norm.

## Key Mechanism

The enriched type space records the usual norm-type coordinates together with
the values of all relevant stable unary formula coordinates, including
`phi(sigma_c(...),a)` for normalized linear combinations. Stability makes
convolution of enriched types well defined and commutative. The
Krivine-Maurey/Raynaud minimal conic-class theorem then gives an `ell_p` type
equality

```text
c_1 tau * ... * c_n tau = ||c||_p tau
```

as equality of enriched types, not only as equality of norm types. Therefore,
when `||c||_p=1`, the `phi` coordinate of every normalized finite combination
equals the one-vector value. A block extraction gives an actual
infinite-dimensional subspace of the original `Y`.

## History Folder

Older 2004.03062 work has been absorbed into `history/` so this full packet is
the canonical top-level result:

- `history/absorbed_packets/2004.03062_hilbert_operator_qf_oscillation_stability/`
  contains the earlier Hilbert-operator partial packet.
- `history/absorbed_packets/2004.03062_stability_wap_pullback_reduction/`
  contains the earlier WAP conditional packet.
- `history/attempts/` contains the scratch attempts that led to the
  formula-aware KM/Raynaud route.
- `history/agent_states/` contains the lane-state trail for the pushes and
  referee pass.

## Review Focus

The proof should be reviewed most carefully at two places:

- Proposition `formula-aware Raynaud type`: the exact KM/Raynaud proof is
  transferred from norm types to enriched stable formula coordinates.
- Lemma `block extraction`: the type equality is converted into an actual
  infinite-dimensional closed subspace, using blocks rather than a bare
  subsequence.

The earlier false route is explicitly avoided: symmetric uniformly continuous
Hilbert-sphere colorings need not flatten just from small coordinates. The
proof uses stability of the normalized pullback formulas, not bare symmetry.

## Files

- `main.tex` / `solution_packet.pdf`: claimed full proof packet.
- `source_paper.pdf`: Hanson arXiv:2004.03062.
- `supporting_wap_grothendieck_1306.5852.pdf`: Ben Yaacov on stability and definability.
- `supporting_bragaswift_km_types_1704.04468.pdf`: accessible KM/Raynaud type-space exposition.
- `supporting_shelah_usvyatsov_minimal_types_1402.6513.pdf`: background on stable Banach types.
- `figures/open_problem_crop.png`: crop of Hanson Question 4.3.
