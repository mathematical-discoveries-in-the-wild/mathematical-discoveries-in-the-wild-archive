# Verification report

## Verdict

`candidate_partial_likely_valid`

The packet gives a complete negative answer to the minimality half of Problem
7.2. The maximality half remains open, so the source problem is only partially
resolved.

## Structural proof audit

1. **Central kernels are admissible.** The canonical isometry
   `ell_1 tensor_pi ... tensor_pi ell_1 = ell_1(N^n)` reduces every central
   linearization to an operator `ell_1 -> ell_2`. Grothendieck's theorem makes
   it absolutely 1-summing, hence absolutely p-summing for every `p>=1`.

2. **The atomic norm is complete.** For each fixed component, every normalized
   atom has strongly p-summing norm at most one. Therefore synthesis defines a
   contraction from an `ell_1` space into the Banach ideal `L_ss,p`. Its kernel
   is closed, and the range with quotient norm is Banach. This avoids the gap
   that would arise from using only finite atomic sums.

3. **Multi-ideal normalization and inclusions.** Pre/postcomposition is absorbed
   in the outer factors. The canonical scalar monomial has a cost-one atomic
   representation and strongly summing norm one, so the atomic norm is exactly
   one. Both `L_d,p` and the atomic hull embed contractively in `L_ss,p`; hence
   their Banach quotient sum does as well.

4. **Cross-arity stability.** Scalar multiplication is implemented by appending
   `x -> phi(x)e_1` and a norm-one tensor contraction. Differentiation is
   implemented by partially evaluating the central kernel; its linearization
   is the original linearization after a bounded rank-one tensor insertion.
   These operations preserve summable atomic representations.

5. **Inclusion theorem.** The linear inclusion theorem gives
   `pi_q(A_tilde)<=pi_p(A_tilde)` for `p<=q`, so every p-atom is a q-atom.
   Combined with the known dominated inclusion theorem, this gives
   `M_p -> M_q`.

6. **Desired-family coincidence axioms.** Every map `(ell_1)^n -> ell_2` is
   itself a central generator of `G_1`, proving the required Grothendieck
   coincidence. The source observes that the sandwich
   `L_d,p -> M_p -> L_sm,p` supplies the Dvoretzky--Rogers property.

## Separation audit

- For an atom on `(ell_2)^3`, every domain factor `B_j:ell_2->ell_1` is compact
  by Pitt's theorem. Hence `||B_j e_i||_1->0`, so the atom is diagonal-null.
  The property passes to the atomic completion because an `ell_1` tail is
  uniformly small in operator norm.

- If a p-dominated scalar trilinear form has at least `m` diagonal coefficients
  of modulus `epsilon`, the domination inequality gives

  ```text
  epsilon m^(3/p) <= ||D||_d,p w_p(e_1,...,e_m;ell_2)^3.
  ```

  The exact weak-p norm is `m^(1/p-1/2)` for `p<2` and `1` for `p>=2`.
  The inequality fails as `m->infinity` in both regimes. Thus the dominated
  part is diagonal-null too.

- The bounded diagonal form `Delta(x,y,z)=sum_i x_i y_i z_i` has
  `Delta(e_i,e_i,e_i)=1`. It is strongly p-summing for every p because every
  scalar form appears, after normalization, in the defining supremum. This
  proves strictness for every `p>=1`.

## Literature and artifact checks

- Cheap local indexes and bounded exact-phrase web searches found no duplicate
  answer to the minimality question.
- The source PDF is present and the crop shows all of Problem 7.2 with context.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  succeeds.
- The resulting six PDF pages were rendered to PNG and visually inspected.
- No computational experiment is used as proof.

## Recommended human focus

Check the atomic quotient convention, the csm/cud tensor contractions, and the
normalization of the dominated inequality. Those are the only nontrivial
bookkeeping points; the separating example is then rigid.
