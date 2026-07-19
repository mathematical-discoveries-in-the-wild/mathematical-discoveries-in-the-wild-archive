# Counterexample: inner Jordan derivations need not be norm dense

Status: `counterexample_likely_valid`

Source paper: Fatmah B. Jamjoom, Antonio M. Peralta, and Akhlaq A. Siddiqui, *Jordan weak amenability and orthogonal forms on JB*-algebras*, arXiv:1411.2712.

## Target

Remark 3.16 asks about determining whether, for a JB*-algebra `J`, the inner Jordan derivations on `J` are norm-dense in the set of all Jordan derivations on `J`. The preceding Remark 3.15 records that `K(H)` already has Jordan derivations into `K(H)^*` which are not inner in the Jordan sense.

This packet strengthens that example to a norm-closure obstruction.

## Counterexample

Let `H = ell_2(N)` and let `A = K(H)`, regarded as a JB*-algebra with product `a o b = (ab+ba)/2`. Identify `A^*` with the trace class `S_1(H)`.

For `T in S_1(H)`, define

```text
delta_T(a)(b) = Tr(T(ab-ba)).
```

Then `delta_T : A -> A^*` is a Jordan derivation. If `T` has nonzero trace, for example if `T` is a rank-one projection, then `delta_T` is not in the norm closure of the inner Jordan derivations.

The reason is that each finite inner Jordan derivation is implemented by a trace-class commutator, hence by a trace-zero trace-class operator. Conversely, the trace is continuous in the derivation norm: `|Tr(T)| <= ||delta_T||`. Thus every norm limit of inner Jordan derivations has trace-zero implementer, while `delta_P` for a rank-one projection `P` has trace `1` and distance at least `1` from the whole inner-Jordan closure.

## Files

- `main.tex`: full counterexample packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of arXiv:1411.2712.
- `figures/open_problem_crop.png`: source crop containing Remark 3.15 and the norm-density problem in Remark 3.16.

## Search Bounds

Before promotion, the run indexes were searched for `1411.2712`, `Jordan weak amenability`, `inner Jordan derivations`, `norm dense`, `norm-dense`, `K(H)`, `trace`, and close variants. Later local sources citing the source paper were checked around Jordan/triple derivation approximation statements. Web searches on 2026-06-29 for exact and close variants of `inner Jordan derivations norm dense K(H)` and `Jordan weak amenability inner Jordan derivations norm dense` found no separate exact resolution.

## Human Review Notes

Recommended review focus:

- Check the computation turning a finite inner Jordan derivation on `K(H)` into an associative dual derivation implemented by `(Sc-cS)/4`.
- Check the trace-continuity estimate `|Tr(T)| <= ||delta_T||`, especially the partial-isometry argument using disjoint finite-rank projections.
- Confirm that the source problem permits the concrete JB*-algebra `K(ell_2)`.
