# Partial Result: Grothendieck Compacta With Scattered Closed Separable Subsets

- status: partial_result_likely_valid
- source paper: arXiv:1208.2207, Aviles--Plebanek--Rodriguez, "On Baire measurability in spaces of continuous functions"
- source target: Problem G asks whether `Ba(C_p(K)) != Ba(C_w(K))` whenever `C(K)` is Grothendieck and `K` is infinite.
- packet path: `runs/fa_banach_001/solutions/partial/1208.2207_grothendieck_scattered_separable_subsets`
- ledger: `runs/fa_banach_001/ledger/results/1208.2207_grothendieck_scattered_separable_subsets.json`

## Result

If `K` is an infinite compact space, `C(K)` is Grothendieck, and every closed separable subspace of `K` is scattered, then

`Ba(C_p(K)) != Ba(C_w(K))`.

This proves Problem G for the class of Grothendieck compacta whose closed separable subspaces are scattered. In particular it applies whenever every closed separable subspace of `K` is countable.

## Proof Intuition

The source paper already gives the two pieces that almost meet. First, Baire equality forces every probability measure on `K` to be carried by a closed separable subset. Second, if `C(K)` is Grothendieck and `K` is infinite, then there is a probability measure on `K` that is not carried by any countable subset. The extra hypothesis bridges the gap: on a scattered compact space every Radon probability is countably supported. Thus a closed separable carrier would force countable support, contradicting the Grothendieck-source measure.

## Provenance

- `source_tex/source_1208.2207.tex`: parsed TeX for the source paper.
- Local arXiv PDF was not present in `data/raw/arxiv`; the packet uses the parsed source TeX as provenance.

## Search Evidence

Cheap indexes were searched for `1208.2207`, Baire measurability, `C_p`, `C_w`, Grothendieck, and sequential closure keywords. No existing packet or attempt for this source target was found.

## Limitations

This is not a full answer to Problem G. It does not handle Grothendieck compacta with non-scattered closed separable subspaces. The remaining obstruction is exactly whether every Grothendieck compactum admits a non-countably-supported probability measure that avoids all closed separable carriers, or whether Baire equality can fail by a different mechanism.
