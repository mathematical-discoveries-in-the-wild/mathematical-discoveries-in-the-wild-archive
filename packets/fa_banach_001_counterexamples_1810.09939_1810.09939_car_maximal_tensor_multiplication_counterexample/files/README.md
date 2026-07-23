# Counterexample: Maximal-Tensor Multiplication Fails on the CAR Algebra

Status: `candidate_counterexample_likely_valid_needs_human_review`

Source: Yang Liu, *Hypergeometric function and Modular Curvature I. --
Hypergeometric functions in Heat Coefficients*, arXiv:1810.09939.  In Section
2, PDF page 5, Liu says it is "still inconclusive" whether algebraic
multiplication extends continuously to the maximal C*-tensor product, and
cites Section 3 of Matthias Lesch's arXiv:1405.0863.  Lesch explicitly
suspects that interesting non-extension examples exist.

## Claimed contribution

The CAR algebra supplies such an example.  Let

```text
A = M_{2^infinity} = direct limit (M_2 tensor ... tensor M_2).
```

For every `n >= 1`, Lesch's `(n+1)`-fold multiplication map

```text
mu_n : A algebraic_tensor ... algebraic_tensor A -> A
       a_0 tensor ... tensor a_n |-> a_0 ... a_n
```

does not extend boundedly to the maximal C*-tensor product.  Consequently,
the associated contraction map cannot have the joint maximal-tensor
extension contemplated by Liu and Lesch.

More generally, the same proof works for every unital nuclear C*-algebra
containing matrix subalgebras `M_d` for unbounded values of `d`.

## Proof mechanism

The CAR algebra is nuclear, so its maximal and minimal C*-tensor powers
coincide.  It contains a unital copy of `M_d` for every `d=2^r`.  Inside
`M_d algebraic_tensor M_d`, put

```text
z_d = sum_{j=1}^d e_{1j} tensor e_{j1}.
```

On `C^d tensor C^d`, this is the partial isometry

```text
xi_j tensor xi_1 |-> xi_1 tensor xi_j,
```

and it vanishes on the orthogonal complement of the displayed initial
space.  Hence `||z_d|| = 1`.  Minimal-tensor injectivity and nuclearity keep
this norm equal to one inside `A tensor_max A`.  But

```text
mu_1(z_d) = sum_j e_{1j}e_{j1} = d e_{11},
```

whose norm is `d`.  Padding `z_d` by identity tensors gives the same
obstruction for every higher multiplication map.

## Verification

The finite checker constructs `z_d` as a `d^2 x d^2` matrix and verifies its
operator norm, partial-isometry identity, and multiplication image:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1810.09939_car_maximal_tensor_multiplication_counterexample/code/verifier.py
```

It passes exactly for `d=2,4,8,16`: tensor norm `1`, multiplication norm `d`,
and zero residual in both algebraic identities.  This computation is a
sanity check; the proof for all `d=2^r` is symbolic.

Verifier focus:

- Confirm the use of nuclearity to identify every finite maximal and minimal
  tensor power of the CAR algebra.
- Confirm minimal-tensor injectivity for the matrix subalgebra inclusion.
- Confirm that evaluation of the contraction map at identity tensors recovers
  multiplication, so the multiplication obstruction also rules out the
  proposed contraction extension.

## Novelty and scope

The bounded check on 2026-07-22 covered the four lightweight run indexes;
arXiv:1810.09939 and arXiv:1405.0863; exact searches for `multiplication map`
with `maximal C*-tensor product`; and close searches using `CAR`, `UHF`,
`nuclear`, `minimal tensor product`, and `subhomogeneous`.  It also inspected
Vaes--Van Daele, *Hopf C*-algebras*, arXiv:math/9907030, which states that
multiplication generally need not extend to the **minimal** C*-tensor product,
and Van Daele's 2020 survey, which notes that the norms for `M_d` grow with
`d`.  A 2021 MathOverflow discussion gives a spatial-tensor obstruction for
`B(H)`.  None of the checked sources stated the explicit CAR/UHF example or
used nuclearity to turn it into a maximal-tensor counterexample.

Thus the mathematical claim has high confidence, but novelty has only
moderate confidence: the construction is elementary once the matrix witness
and nuclearity are placed together.  The packet gives a negative answer *in
general* and supplies a separable, unital, simple, nuclear example.  It does
not classify all C*-algebras for which multiplication extends, and it does
not decide the extension question for the particular noncommutative tori
used elsewhere in Liu's paper.

Human review recommendation: send to an operator-algebra/tensor-product
reviewer.  The proof is short; the main review issue is literature novelty,
not the matrix calculation.

Files:

- `source_paper.pdf`: arXiv:1810.09939.
- `supporting_paper_1405.0863.pdf`: Lesch's source discussion.
- `figures/open_problem_crop.png`: Liu, PDF page 5, complete source passage.
- `main.tex`, `solution_packet.pdf`: formal counterexample packet.
- `VERIFICATION.md`: proof and novelty audit.
- `code/verifier.py`: finite-dimensional sanity check.

