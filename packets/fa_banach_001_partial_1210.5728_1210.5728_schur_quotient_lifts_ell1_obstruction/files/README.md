# Partial Result: Schur Quotients Force `ell_1` in Lopez-Abad Superspaces

Status: `partial_result_likely_valid`.

Source target: J. Lopez-Abad, "A Bourgain-Pisier construction for general Banach spaces", arXiv:1210.5728.

Target passage: the introduction notes that it remains unknown how to remove separability in the Freeman-Odell-Schlumprecht embedding theorem, or even whether a nonseparable Bourgain-Delbaen space exists, meaning a nonseparable `L_infinity` space containing no isomorphic copies of `c_0` or `ell_1`.

Partial obstruction proved here: any Banach-space extension

`0 -> X -> Y -> Q -> 0`

with `Q` infinite-dimensional and Schur has `ell_1` as a subspace of `Y`. Hence every Lopez-Abad / nonseparable Bourgain-Pisier superspace whose quotient is infinite-dimensional Schur necessarily contains `ell_1`; this construction route cannot produce the desired nonseparable `L_infinity` space avoiding both `c_0` and `ell_1`.

Idea: every infinite-dimensional Schur space contains `ell_1` by Rosenthal's `ell_1` theorem. Copies of `ell_1` lift through quotient maps because `ell_1` is projective.

Scope: this is not a negative answer to the full nonseparable Bourgain-Delbaen problem. It only excludes the Schur-quotient Lopez-Abad/Bourgain-Pisier construction class from being a no-`ell_1` example.

Files:
- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1210.5728.
- `supporting_paper_2604.11832.pdf`: later source confirming the nonseparable Bourgain-Pisier/Lopez-Abad Schur-quotient context.

Ledger record: `runs/fa_banach_001/ledger/results/1210.5728_schur_quotient_lifts_ell1_obstruction.json`.
