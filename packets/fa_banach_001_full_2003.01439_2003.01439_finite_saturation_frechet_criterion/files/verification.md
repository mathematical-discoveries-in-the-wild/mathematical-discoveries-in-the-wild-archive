# Verification report

## Claimed result

For a bounded uniformly discrete pointed metric space `M` and a norm-one
convex series

`mu = sum_i lambda_i m_(x_i,y_i)`, with all `lambda_i > 0`,

the packet proves that `mu` is a point of Frechet differentiability of
`F(M)` if and only if the finite metric collapse numbers `Delta_n` defined in
the packet converge to zero. This is a full positive answer to Question 1 on
p. 15 of arXiv:2003.01439. The packet separately records the literature
answer to Question 2.

## Proof audit

1. **Nonemptiness of the finite saturation polytopes.** A norming
   `f in S_Lip_0(M)` exists by Hahn--Banach. Equality in the positive convex
   series forces `f(m_(x_i,y_i))=1` for every `i`, so each `P_n` and `E_n` is
   nonempty.

2. **Exact envelope diameter.** Any 1-Lipschitz extension of finite data `a`
   lies pointwise between `L_a` and `U_a`. Both envelopes are themselves
   normalized 1-Lipschitz extensions. Taking two independently chosen data
   `a,b in P_n`, and swapping them to account for absolute values, proves
   `diam_infinity(E_n)=Delta_n` with no compactness assumption on `M`.

3. **Norm comparison.** If `theta=inf_(x != y)d(x,y)>0` and
   `D=diam(M)<infinity`, then for normalized functions
   `||u||_infinity <= D ||u||_L` and
   `||u||_L <= (2/theta)||u||_infinity`. Thus collapse in uniform norm and
   collapse in Lipschitz norm are equivalent.

4. **Frechet smoothness implies collapse.** Every `g in E_n` has
   `g(mu) >= 1-2r_n`, where `r_n=sum_(i>n)lambda_i`. Since `r_n -> 0`, the
   faces `E_n` lie in successively thin dual-sphere slices. Smulyan's lemma
   therefore forces their Lipschitz-norm diameters, and hence `Delta_n`, to
   vanish.

5. **Finite correction lemma.** The normalized 1-Lipschitz data on the finite
   set `S_n` form a compact polytope. If the first `n` saturation deficits
   tend to zero but the distance to `P_n` does not, a convergent subsequence
   has a limit in `P_n`, a contradiction. This gives a modulus
   `omega_n(eta)->0`.

6. **Global correction.** If finite data `v` are uniformly close to
   `a in P_n`, then their lower and upper envelopes are uniformly close.
   Clamping a global Lipschitz function `g` between `L_a` and `U_a` produces
   `h in E_n` with `||g-h||_infinity` no larger than the finite-data error,
   hence small Lipschitz-norm error by uniform discreteness.

7. **Collapse implies Frechet smoothness.** A function in a thin norming
   slice has weighted total saturation deficit less than the slice width;
   positivity of the weights makes every one of the first `n` deficits
   small. The correction lemma puts the whole thin slice near `E_n`. First
   choosing `n` with small `diam(E_n)`, and then shrinking the slice, makes
   the slice diameter arbitrarily small. Smulyan's lemma completes the proof.

## Stress tests

- **Infinite star / `ell_1`.** For `M={0,1,2,...}` with
  `d(0,k)=1` and `d(j,k)=2`, and
  `mu=sum 2^(-k) delta_k`, saturating finitely many coordinates leaves every
  later coordinate free in `[-1,1]`. Hence `Delta_n=2` for every `n`, in
  agreement with the known failure of Frechet differentiability.

- **Finite support.** Once all molecules in a finite representation have
  been included, the criterion says precisely that their common saturated
  face has a unique Lipschitz extension. This agrees with the finite-support
  characterization in the source paper.

- **Source Example 3.7.** In the source's convergent-geometry example,
  saturation of longer prefixes traps all remaining point values in
  intervals whose width tends to zero. Thus `Delta_n -> 0`, consistent with
  the example's Frechet differentiability.

- **Repeated points or pairs.** `S_n` is treated as a set. Compatibility of
  repeated constraints follows from the global norming function, so the
  proof does not require distinct pairs across indices.

## Literature and novelty check

- Cheap local indexes: searched for `2003.01439`, the exact title,
  `Frechet differentiability`, `convex series`, `infinite support`,
  `metric characterization`, and related variants. No prior run result for
  this question was found.
- Bounded web searches: exact wording of Question 1 and variants using
  `finite saturation`, `finite extension polytope`, `McShane`, `Whitney`,
  and `Lipschitz-free space`. No exact later answer was found.
- The search did find Aliaga--Pernecka--Smith, arXiv:2302.13951, published in
  *J. Funct. Anal.* 287 (2024), 110560. Their uniformly discrete result
  answers Question 2 negatively and is included as a supporting source.
- Novelty confidence for the Question 1 criterion: **moderate**, because the
  searches were bounded and equivalent terminology may exist.

## Artifact verification

- Source crop includes the lead-in and complete text of both questions.
- The final PDF is compiled from `main.tex` with all references internal or
  included in the packet.
- Mathematical proof is symbolic; no numerical computation is used as
  evidence.
- Final visual page-by-page inspection: completed on 2026-07-21. All six
  pages were rendered at 150 dpi and inspected individually. The title/status
  box, source crop, displayed formulas, theorem statements, proof endings,
  and references are legible and remain inside the page margins. The LaTeX
  log contains no unresolved references, overfull boxes, or warnings.

## Human review requested

Check especially:

1. the equality `diam_infinity(E_n)=Delta_n`;
2. the compact finite-face correction and McShane--Whitney clamping step;
3. the conversion between uniform and Lipschitz norm; and
4. priority/novelty under terminology different from finite saturation
   collapse.
