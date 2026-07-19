# Partial Result: An Anisotropic Coordinate Lift Preserves the No-Convex-Equivalent Obstruction

## Source Problem

- Source paper: Gerhard Schindl, *On inclusion relations of weighted L^p-type spaces defined in terms of weight function matrices*, arXiv:2510.05469.
- Location: final paragraph before the references, rendered page 46.
- Source signal: the author asks to transfer the Section 7 construction of a one-dimensional Beurling-Bjorck/Petzsche-Vogt weight with no equivalent `(omega_4)` representative to the higher-dimensional anisotropic setting.

## Result

For every `d >= 2`, the one-dimensional bad equivalence class from Section 7 has an explicit non-radial anisotropic lift

`Omega(x_1,...,x_d) = rho(|x_1|) + 2 rho(|x_2|) + rho(|x_3|) + ... + rho(|x_d|),`

where `rho` is the continuous subadditive representative equivalent to the source weight. This `Omega` is continuous, subadditive, non-radial, has the anisotropic `(omega_3)` lower growth required in the source paper, and has all exponential integrability checks needed for weighted Fourier spaces.

Moreover, under the natural multivariable analogue of `(omega_4)` requiring convexity of
`u -> Sigma(e^{u_1},...,e^{u_d})`, no equivalent representative `Sigma` can satisfy this convexity condition. Freezing all but one coordinate recovers a one-dimensional convex representative equivalent to `rho`, contradicting Section 7 of the source paper.

## Scope

This is a partial/natural-formulation answer, not a claim that every possible anisotropic formulation in the cited literature is settled. The packet isolates the coordinate-log-convex analogue most directly corresponding to the role of `(omega_4)` in the paper.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: rendered source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source question/goal.
- `code/make_crop.py`: reproducible crop script.

## Verification

- Source PDF rendered locally from the arXiv source.
- Crop generated with `conda run --no-capture-output -n sandbox python code/make_crop.py`.
- Packet rendered with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`.
- Bounded duplicate search: local run indexes and cheap source indexes were searched for `2510.05469`, `anisotropic convex`, `coordinate log convex`, `log-convex anisotropic`, and `Beurling Bjorck anisotropic`; no existing packet for this coordinate-lift result was found.

## Human Review Recommendation

Review the exact anisotropic convexity convention desired by the source authors. Under the coordinate-log-convex convention stated in the packet, the proof is short and likely valid.
