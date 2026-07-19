# Full Result Packet: `d_z` divergence isometries on qubits

Run: `fa_banach_001`

Result type: `full_result`

Status: promoted proof, likely valid. This packet gives a complete
classification of qubit state-space isometries for the quantum Wasserstein
divergence `d_z`. It answers the `d_z` half of the final open-problem remark in
arXiv:2408.09879. It does not address the separate `d_{xz}` question.

## Source Problem

- Richard Simon and Daniel Virosztek, *Isometries of the qubit state space with
  respect to quantum Wasserstein distances*, arXiv:2408.09879.
- Local source inspected:
  `data/parsed/arxiv_sources/2408.09879/main.tex`, especially the definitions
  around lines 145--146, Theorem `thm:Dz-main` around lines 301--306, and the
  final open-problem remark around line 448.
- Local PDF: `source_paper.pdf`.
- Open-problem crop: `figures/open_problem_crop.png`.

The source paper classifies `d_sym` isometries under a pure-state hypothesis
and completely classifies `D_z` isometries. Its final remarks ask for the
corresponding structure of qubit state-space isometries for the divergences
`d_{xz}` and `d_z`.

## Result

Let `rho` have Bloch vector `b_rho=(x,y,z)`. A self-map
`Phi:S(C^2)->S(C^2)` preserves the quantum Wasserstein divergence `d_z` if and
only if

```tex
|b_{Phi(rho)}| = |b_rho|
```

for every state `rho`, and either

```tex
(b_{Phi(rho)})_3 = (b_rho)_3 \quad\text{for all rho}
```

or

```tex
(b_{Phi(rho)})_3 = -(b_rho)_3 \quad\text{for all rho}.
```

Thus the `d_z`-isometries have exactly the same Bloch-coordinate
classification as the `D_z`-isometries in Theorem `thm:Dz-main` of the source
paper.

## Proof Mechanism

The two pole states `p_+=(I+sigma_z)/2` and `p_-=(I-sigma_z)/2` are the unique
diameter pair for `d_z`. Their distances from an arbitrary state recover the
third Bloch coordinate and the `D_z` self-distance:

```tex
d_z^2(rho,p_t)=2-2tz-\frac12 F_z(rho),
\qquad t=\pm1,
```

where

```tex
F_z(rho)=D_z^2(rho,rho)
       =\frac{2(x^2+y^2)}{1+\sqrt{1-|b_rho|^2}}.
```

Taking the difference of the two squared pole distances recovers `z` up to the
global pole swap; taking their sum recovers `F_z`. For fixed `z`, the displayed
formula for `F_z` is strictly increasing as a function of the Bloch radius.
Hence a `d_z`-isometry preserves the Bloch radius and globally either fixes or
flips the `z` coordinate. The converse follows from the source paper's
`D_z`-classification theorem plus the fact that `F_z` depends only on the
Bloch radius and `z^2`.

## Verification

- `main.tex` contains the proof in manuscript form.
- `tmp/verify_dz_formulas.py` checks the self-distance formula by explicit
  vectorization for random Bloch vectors and checks the monotonicity used in
  the proof.
- `solution_packet.pdf` is the rendered proof note.

## Novelty Check

Local cheap indexes were searched for `2408.09879`, the paper title, `d_z`,
`d_{xz}`, `Wasserstein divergence`, and single-observable Wasserstein
isometries; no prior packet for this target was found. A bounded web search
for exact phrases around `"d_z" "Wasserstein divergence" isometries` and
`"quantum Wasserstein divergences" "d_z" "d_xz" isometries` found the source
paper and a June 2026 paper on single-observable quantum Wasserstein
isometries for distances `D_A`, not a classification for divergences `d_A`.

Human-review focus: verify the normalization of the self-distance formula
against the cost matrix `C_z=diag(0,4,4,0)`. The formula in this packet gives
`F_z=2` for a pure equatorial state, matching the unique product coupling.
