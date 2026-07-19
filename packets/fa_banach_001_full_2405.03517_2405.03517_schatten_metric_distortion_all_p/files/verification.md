# Verification report

Verdict: **candidate full solution likely valid**.

## Claim audited

For a finite regular graph `G` with normalized adjacency gap `delta>0`, the
proof establishes

```text
h_tilde_{S_p}(G) >= (delta/K)^(1/p)       for 1 <= p <= 2,
h_tilde_{S_p}(G) >= delta/(14p)           for p >= 2,
```

with universal `K`. Consequently

```text
D_{n,S_p} = Theta(max{1,log(n)/p})        for every 1 <= p < infinity.
```

## Independent audit of the new `1 <= p <= 2` argument

1. **Choice of origin.** If `B=E_ij ||f_i-f_j||_p^p`, averaging over the
   second vertex gives an origin `o` with
   `E_i ||f_i-f_o||_p^p <= B`. Translation preserves all pairwise and edge
   distances.

2. **Forward Mazur estimate.** Ricard's theorem applied to `M_{p,2}` gives
   `||M(x)-M(y)||_2 <= A||x-y||_p^(p/2)`. In the quantitative proof the
   relevant constant depends on the target exponent, which is fixed at `2`;
   hence one `A` works for all `p in [1,2]`.

3. **Inverse Mazur estimate.** Since `M_{2,p}` inverts `M_{p,2}`, its
   unit-ball Lipschitz estimate and homogeneity give
   `||x-y||_p <= A max(||x||_p,||y||_p)^(1-p/2)||M(x)-M(y)||_2`.
   Ricard's quantitative constant is absolute times `2/p`, hence uniform for
   `p in [1,2]`.

4. **Weighted averaging.** Put `q=2-p`, `r_i=||f_i-f_o||_p`,
   `d_ij=||f_i-f_j||_p`, and `C=E d_ij^2/(r_i^q+r_j^q)`. Holder with
   exponents `2/p` and `2/q` gives

   ```text
   B <= C^(p/2) (E(r_i^q+r_j^q)^(p/q))^(q/2)
     <= 2^(p/2) C^(p/2) B^(q/2).
   ```

   Because `p+q=2`, division gives exactly `C >= B/2`. This remains valid at
   `p=1`; `p=2` is handled directly in Hilbert space.

5. **Hilbert transfer.** The inverse estimate squared and the weighted lemma
   yield `E_pairs ||M(x_i)-M(x_j)||_2^2 >= B/(2A^2)`. The forward estimate
   gives edge Hilbert energy at most `A^2` times the original edge
   `p`-energy. Hilbert Poincare, with the normalizations used in the source,
   is `pair_energy <= edge_energy/delta`. Therefore
   `B <= (2A^4/delta) edge_p`.

6. **Endpoint.** At `p=1`, the Mazur map is `M_{1,2}(x)=u|x|^(1/2)` and its
   inverse is `M_{2,1}`. Every exponent in the weighted lemma is finite and
   no interpolation or limiting argument is used.

## Audit of the `p >= 2` argument

1. For the lazy walk `Q=(I+P)/2`, the centered Hilbert norm is
   `(1-delta/2)^k`, while `||Q^k-J||_infinity <= 2`.
2. Noncommutative complex interpolation gives
   `||Q^k-J||_p <= 2^(1-2/p)(1-delta/2)^(2k/p)`.
3. The selected `k=O(p/delta)` makes this norm at most `1/2`.
4. Centering and Jensen control all-pairs energy by `k`-step energy.
5. A path of `k` lazy increments loses `k^p` before taking the `p`th root,
   hence exactly a factor `k` afterward.
6. The resulting constant is `h_tilde >= delta/(14p)`.

## Distortion consequence

A fixed-degree expander has a positive fraction of pairs at graph distance
`Omega(log n)`. After a distortion-`D` embedding is rescaled to be
nonexpanding, the edge-energy root is at most `1` and the pair-energy root is
`Omega(log n/D)`. The graph bounds yield `D=Omega(log n)` for `p<=2` and
`D=Omega(log n/p)` for `p>=2`; `D>=1` completes the lower bound. Matousek's
upper bound into `ell_p`, the diagonal isometry `ell_p -> S_p`, and the
Frechet embedding for `p>=log n` give the matching upper bound.

## Computational sanity check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2405.03517_schatten_metric_distortion_all_p/code/check_constants.py
```

The script checks the weighted inequality (including `p=1`), the exact
Hilbert Poincare normalization, finite matrix Mazur transforms, and the
high-`p` interpolation/path estimates. Passing finite tests is only a
consistency check; the proof is analytic.

## Remaining reviewer focus

The principal external dependency is the quantitative, uniform form of
Ricard's Mazur-map estimates. Review the constants in his Lemma 2.6 and the
two `2 x 2` reductions leading to the main theorem. Once that input is
accepted, the weighted-energy and graph-normalization steps are elementary
and explicit. The proof does not claim the source's stronger comparison for
graphs with vanishing spectral gap.
