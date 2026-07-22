# The arbitrary-measure isomorphic Busemann--Petty constant has order `sqrt(n)`

Status: `candidate_full_likely_valid`

Source: Alexander Koldobsky, Michael Roysdon, and Artem Zvavitch,
*Comparison Problems for Radon Transforms*, arXiv:2305.17796, page 5,
equation (7) and the sentence immediately following it.

## Claimed full resolution

Let `C_n` be the least constant such that, for every non-negative continuous
even density `f` and every pair of origin-symmetric convex bodies `K,L` in
`R^n`,

`int_(K cap H) f <= int_(L cap H) f` for every central hyperplane `H`

implies

`int_K f <= C_n int_L f`.

The packet proves that there is an absolute `c>0` such that

`c sqrt(n) <= C_n <= sqrt(n)`.

The upper bound is the theorem of Koldobsky--Zvavitch. The new part is the
matching lower bound, which answers the source question about optimality in
order.

## Idea of the proof

Klartag--Livshyts constructed an even smooth probability density `p` and a
symmetric convex body `A` with bounded volume radius such that every affine
hyperplane has `p`-mass `O(1/sqrt(n))`, while a fixed positive amount of the
mass lies in `A`. Their explicit Gaussian-mixture construction contains a
further positioning fact: all Gaussian centers have norm at least `c n`.
Consequently a fixed positive amount of the mass lies in

`A \ (R sqrt(n) B_2^n)`

for every fixed `R` and all sufficiently large `n`.

Take `D=R sqrt(n) B_2^n`, with `R` a sufficiently large absolute constant.
Because `A` contains an absolute multiple of `sqrt(n) B_2^n` and
`|A|^(1/n)=O(1)`, a double-cone estimate gives

`|A cap H| <= O(sqrt(n)) |A|`.

Choosing `R` large makes `(D\A) cap H` occupy at least half of `D cap H` for
every central hyperplane. Put the Klartag--Livshyts density, after a continuous
cutoff, on `A\D`; put a very small continuous comparison density on `D\A`.
The supports are disjoint. Scaling the second density makes all of its central
sections dominate the first density's sections. Its total mass is only

`O(n^(-1/2)) * |D|/|D cap H| = O(n^(-1/2))`,

whereas the first mass is bounded below. This yields the ratio
`Omega(sqrt(n))` with one common continuous even density.

## Verification

The detailed proof is in `main.tex` and `solution_packet.pdf`. The finite
script

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2305.17796_isomorphic_bpgm_sqrt_n_sharp/code/verify_scaling.py
```

checks the unit-ball gamma-function ratio used in the final estimate and the
resulting `n^(-1/2)` scaling for dimensions 5 through 10,000. The proof is
analytic and does not depend on this computation.

## Novelty check and limitations

A bounded search on 2026-07-21 covered the source paper, arXiv:1405.0567,
arXiv:1912.00880, arXiv:1810.06189, the local 2000--2026 source corpus, and web
queries for `isomorphic Busemann-Petty same measure sqrt n optimal` and close
variants. It found the known sharp result for the *two-measure* comparison
problem, but no matching lower bound for the same-measure constant. A 2025
paper on extensions of the arbitrary-measure Busemann--Petty problem did not
advertise this optimality result in its title or abstract. Novelty confidence
is moderate, not definitive.

The result determines the dimension dependence up to universal constants; it
does not determine the exact best constant. It also relies on the explicit
positioning in the Klartag--Livshyts construction, not merely on the abstract
statement of their sharp slicing theorem.

## Human review recommendation

Prioritize three points: (1) the lower bound on every Gaussian center in the
Klartag--Livshyts construction; (2) the double-cone bound on every central
section of `A`; and (3) the uniform Dini approximation of `1_(D\A)` by
continuous even cutoffs. If these pass, the density construction is a full
order-sharp resolution of the extracted problem.

