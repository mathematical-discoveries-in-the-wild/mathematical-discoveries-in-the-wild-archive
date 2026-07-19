# Cwikel plus-minus lattice isometry

Status: `candidate_full_likely_valid`

Run: `fa_banach_001`  
Agent: `agent_lane_04`  
Source paper: Michael Cwikel, arXiv:1502.00986v2

## Result

This packet proves the isometry conjectured in Remark 4.1 of Cwikel's paper:

\[
\|\cdot\|_{\langle X_0,X_1\rangle_{\theta,(0)}}=
\|\cdot\|_{[X_0,X_1]_\theta}
\]

for couples of complexified Banach lattices of measurable functions on the same measure space.

## Key mechanism

The previous partial packet proved the result when both endpoint lattice norms are order continuous. The full proof replaces that assumption with Shestakov's theorem: Calderon's complex interpolation space is the closure of \(X_0\cap X_1\) in the Calderon product norm.

The norm-one plus-minus estimate is first proved for bounded logarithmic-ratio Calderon bands. For elements in \(X_0\cap X_1\), the unbounded ratio tails are small in plus-minus norm by placing each tail at a midpoint parameter. Then the estimate passes to the Shestakov closure.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered full packet.
- `source_paper.pdf`: local copy of arXiv:1502.00986v2.
- `supporting_yuan_1405.5735.pdf`: supporting reference for the Shestakov closure theorem.
- `supporting_cwikel_kalton_9210206.pdf`: supporting reference connecting the lattice case and plus-minus literature.
- `figures/open_problem_crop.png`: source crop of Cwikel Remark 4.1.
- `history/partial_order_continuous_packet_2026_06_23/`: superseded partial packet.

## Verification focus

Check Lemma 3 in `main.tex`, especially the tail estimates for \(h\in X_0\cap X_1\), and verify the cited Shestakov closure theorem applies to Cwikel's intended class of complexified Banach lattices.
