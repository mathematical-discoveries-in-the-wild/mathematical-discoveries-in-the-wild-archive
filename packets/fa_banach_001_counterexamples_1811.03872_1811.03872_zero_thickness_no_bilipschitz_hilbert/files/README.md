# Counterexample: Zero Thickness Does Not Force a Hilbert Bi-Lipschitz Embedding

Status: `counterexample`

Source problem paper: A. Margaris and J. C. Robinson,
*Embedding properties of sets with finite box-counting dimension*,
arXiv:1811.03872.

## Target

The source paper asks whether thickness zero is enough to prove the existence
of a nonlinear bi-Lipschitz embedding into a Euclidean or Hilbert space.

## Result

No. There is a compact subset `X` of a Banach space `B` such that

```text
tau(X,B) = 0
```

but `X` has no bi-Lipschitz embedding into any Hilbert space. In particular it
has no bi-Lipschitz embedding into any Euclidean space.

## Construction

Let `Q_m = {0,1}^m` with the Hamming metric. Embed `Q_m` isometrically into
`E_m = ell_infty(Q_m)` by the pointed Kuratowski map

```text
iota_m(x) = (d_m(x,y) - d_m(0,y))_{y in Q_m}.
```

Let

```text
B = (direct sum_m E_m)_{c0},    R_m = 2^{-m^3},    s_m = R_m / m.
```

Put a scaled copy `s_m iota_m(Q_m)` in the `m`th coordinate block and define

```text
X = {0} union union_m s_m iota_m(Q_m).
```

The radii of the blocks tend to zero so fast that `X` has upper
box-counting dimension zero. Since the thickness exponent is always bounded
above by box-counting dimension, `tau(X,B)=0`.

## Obstruction

If `X` embedded bi-Lipschitzly into a Hilbert space with distortion `D`, then
each block would give a Hilbert embedding of the Hamming cube `Q_m` with the
same distortion `D`.

Enflo's cube inequality gives a lower bound `c_H(Q_m) >= sqrt(m)` for the
Hilbert distortion of the `m`-dimensional Hamming cube. Since `m` is
unbounded, no uniform `D` can exist.

## Evidence

- `figures/open_problem_crop.png`: the source paper's two open questions,
  including the zero-thickness bi-Lipschitz question, PDF page 20.
- `source_paper.pdf`: local copy of arXiv:1811.03872.
- `solution_packet.pdf`: full proof packet.

## Scope

This is a negative answer to the Hilbert target in the source question, hence
also to the Euclidean target. The ambient Banach space in the counterexample is
a `c0`-sum of finite-dimensional `ell_infty` spaces.

## Human Review Notes

Recommended review focus:

- Check that the pointed Kuratowski maps are isometric for the Hamming metric.
- Check the box-counting estimate: at scale between `R_{M+1}` and `R_M`, only
  the first `M` finite blocks need individual covering, so the logarithmic
  covering growth is `O(M)` while `-log R_M` is `Theta(M^3)`.
- Check the Hilbert obstruction via Enflo's cube inequality.
