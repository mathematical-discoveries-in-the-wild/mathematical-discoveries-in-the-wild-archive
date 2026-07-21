# Verification report

**Verdict:** candidate strong partial result, likely valid, suitable for expert review.

## Proof audit

1. The phase cutpoints exist because `h(n) -> infinity` gives a tail on which `h >= k+1`; moving finitely farther enforces the required congruence.
2. Within phase `k`, consecutive positions of an active ray differ by `k`. At the transition to phase `k+1`, the old-ray gap is again exactly `k` because the phase length is a multiple of `k`.
3. For an edge `p < q` beginning in phase `k` and every crossed cut `p <= n < q`, one has `q-n <= k <= h(n)`, hence `q <= f(n)`. This is exactly `(I-P_{f(n)}) H P_n = 0` for the flattened nearest-neighbor direct sum.
4. Conversely, every already-started infinite ray contributes a distinct endpoint in `{n+1,...,f(n)}` across cut `n`; therefore the number of started rays is at most `f(n)-n`, forcing divergence. This establishes route-sharpness.
5. The remainder of the proof is the source paper's Theorem 5.1 lower-bound reduction: the Krutikov-Remling dichotomy detects infinite columns, and the fixed flattening preserves finite-information evaluation for both `Lambda_1` and `Lambda_2`.

## Finite sanity check

Command:

```text
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1908.06721_diverging_bandwidth_sc_lower_bound/code/check_round_robin.py
```

Output:

```text
phases=14
positions=16386
adjacent_ray_edges=16372
cut_constraints=212816
all finite cut constraints passed
```

This computation is not used as proof.

## Packet checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/pdfs main.tex` succeeded.
- The final log has no overfull boxes, underfull boxes, undefined references, or warnings.
- All five pages were rendered to PNG and visually inspected; no clipping, overlap, or unreadable text was found.
- The source-question crop includes the entire Theorem 5.1 singular-continuous bullet and the sentence asking whether the growth condition can be dropped.

## Remaining review focus

An expert should confirm that the source's discrete-output conversion for the `SCI_G=3` decision problem composes unchanged with the new fixed enumeration. The packet cites rather than recopies that standard final subargument.
