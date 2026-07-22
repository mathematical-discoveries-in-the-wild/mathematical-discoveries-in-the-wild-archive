# Counterexample: abstract isometry does not force exterior equivalence

Status: `counterexample_likely_valid`

Source: Alonso Delfín, Carla Farsi, and Judith Packer, *Twisted crossed
products of Banach algebras*, arXiv:2509.24106.  The question occurs on PDF
page 4, in the final paragraph of the introduction.

## Claimed contribution

The literal converse question has a negative answer for every
`p in [1,infinity) \ {2}` (indeed, the construction also works for `p=2`).
Let

```text
G = C_2 = {e,s},                 A = C^3 = C({1,2,3}),
alpha_s = coordinate action of (12),
beta_s  = coordinate action of (23),
sigma = omega = 1.
```

The actions are conjugate by the coordinate automorphism `phi` induced by
`(123)`.  Therefore applying `phi` pointwise,

```text
(Phi f)(x) = phi(f(x)),
```

extends to an isometric algebra isomorphism

```text
F_r^p(G,A,alpha,1) -> F_r^p(G,A,beta,1).
```

Nevertheless the actions are not exterior equivalent.  Since `A` is unital
and commutative, `M(A)=A` and every `Ad(theta_x)` is the identity; exterior
equivalence would therefore force `alpha_x=beta_x` for every `x`.

## Proof mechanism

Conjugacy gives the algebraic crossed-product isomorphism.  The only point
that needs care is the reduced norm.  Given any nondegenerate, sigma-finite,
contractive `L^p` representation `pi_0` of `A`, set
`rho_0=pi_0 o phi^{-1}`.  This is a bijection of the coefficient
representations used to define the two reduced norms.  The regular coefficient
operators satisfy

```text
rho_0(beta_x^{-1}(phi(a))) = pi_0(alpha_x^{-1}(a)),
```

and, because both twists are trivial, the regular group operators are the same
left translations.  Hence the integrated operators for `f` and `Phi f` are
identical.  Taking suprema over the paired representation classes proves exact
equality of the reduced norms.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2509.24106_abstract_isometry_not_exterior_equivalence/code/verify_finite_model.py
```

The exact checker verifies the permutation relation, inequality of the two
actions, the entire six-dimensional algebraic multiplication table under
`Phi`, and the regular integrated-operator identity on a faithful finite
coefficient representation.  The representation-class argument in the packet
is what proves the universal reduced-norm statement.

Verifier focus:

- Confirm that the source question imposes no coefficient-fixing or
  grading-preserving condition on the isomorphism.
- Check the pairing `rho_0=pi_0 o phi^{-1}` in the reduced-norm proof.
- Check that commutativity of `A` makes the first exterior-equivalence identity
  force equality of the actions.

## Novelty and scope

The bounded novelty check on 2026-07-22 covered the run's cheap indexes, the
exact arXiv id and title, and arXiv searches combining `twisted Lp crossed
product`, `exterior equivalence`, `converse`, `isometric isomorphism`,
`conjugate actions`, and `coefficient automorphism`.  It inspected the source
paper and nearby primary arXiv results on twisted and transformation-group
`L^p` crossed products.  No paper explicitly giving this counterexample or
resolving the literal converse was found.

Novelty confidence is moderate rather than high: the obstruction is elementary
and standard in spirit.  The packet settles only the abstract-isomorphism
question as written.  It does **not** settle a strengthened rigidity question
in which the isomorphism must fix or preserve the canonical copy of `A`, or
preserve a grading/coaction.

Human review recommendation: a short operator-algebra review should focus on
the intended meaning of “an isometric isomorphism” in the source question and
the reduced-norm representation pairing.  Mathematically, the construction is
finite and exact.

Files:

- `source_paper.pdf`: arXiv:2509.24106.
- `figures/open_problem_crop.png`: the question on source PDF page 4.
- `main.tex`, `solution_packet.pdf`: full counterexample packet.
- `VERIFICATION.md`: verification report and adversarial checks.
- `code/verify_finite_model.py`: exact finite checker.
