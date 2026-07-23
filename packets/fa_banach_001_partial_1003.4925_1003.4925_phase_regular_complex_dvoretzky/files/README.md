# Sharp complex Dvoretzky theorem under phase-increment regularity

Status: **substantial partial result; likely valid; send to human review**.

Source: Guillaume Aubrun, Stanisław Szarek, and Elisabeth Werner,
*Hastings's additivity counterexample via Dvoretzky's theorem*,
arXiv:1003.4925, page 6.

## Source question

The source proves the sharp complex Dvoretzky theorem for a 1-Lipschitz
**circled** function \(f:S_{\mathbb C^n}\to\mathbb R\): a random complex
subspace of dimension \(c n\varepsilon^2\) sees oscillation at most
\(\varepsilon\).  It asks whether circledness, meaning
\(f(e^{i\theta}x)=f(x)\), can be removed completely.

## Result

For an \(L\)-Lipschitz function define its phase-increment modulus
\[
D_{\mathbb T}(f)=
\sup_{\omega\in\mathbb T\setminus\{1\}}
\frac{\operatorname{Lip}(z\mapsto f(\omega z)-f(z))}
     {|\omega-1|}.
\]
There are absolute constants \(c,C>0\) such that if
\[
k\leq c\,n\frac{\varepsilon^2}{(L+D_{\mathbb T}(f))^2},
\]
then a random \(k\)-dimensional complex subspace \(E\) satisfies
\[
\sup_{z\in S_E}|f(z)-\mathbb Ef|\leq\varepsilon
\]
with probability at least
\[
1-C\exp\!\left(
-c\,n\frac{\varepsilon^2}{(L+D_{\mathbb T}(f))^2}\right).
\]

This contains the source's circled theorem as \(D_{\mathbb T}(f)=0\), but also
allows genuinely non-circled functions.

In particular, if \(f\) is the restriction of a real-valued \(C^{1,1}\)
function \(F\) on a neighborhood of the closed unit ball with
\[
\|\nabla F\|_\infty\leq L,\qquad
\operatorname{Lip}(\nabla F)\leq H,
\]
then
\[
D_{\mathbb T}(f)\leq L+H.
\]
Thus the optimal \(k\asymp n\varepsilon^2\) dependence holds uniformly for
non-circled \(C^{1,1}\) functions when \(L,H\) are bounded absolutely.

## Proof mechanism

For two sphere points \(x,y\), rotate \(y\) by a phase \(\omega\) so that
\(\langle x,\omega y\rangle\) is nonnegative real.  Split
\[
f(Ux)-f(Uy)
=\bigl[f(Ux)-f(U\omega y)\bigr]
+\bigl[f(\omega Uy)-f(Uy)\bigr].
\]

The first term is exactly the aligned increment from Schechtman's proof: after
conditioning, Lévy concentration gives subgaussian scale
\(L|x-\omega y|/\sqrt n\).  The second term has mean zero and, by the
phase-increment hypothesis, subgaussian scale
\(D_{\mathbb T}(f)|\omega-1|/\sqrt n\).  Both chord lengths are bounded by a
universal multiple of \(|x-y|\).  Hence \(f(Ux)\) is a subgaussian process
with increment metric
\[
\frac{L+D_{\mathbb T}(f)}{\sqrt n}|x-y|.
\]
Dudley chaining gives expected oscillation
\(O((L+D_{\mathbb T}(f))\sqrt{k/n})\), and concentration on the unitary group
gives the stated high-probability estimate.

## Limitations and novelty check

The general source question remains open.  An arbitrary Lipschitz function
can have \(D_{\mathbb T}(f)=\infty\): small phase shifts may change its local
slope at order one.  The theorem isolates this as the precise obstruction in
the chaining proof rather than bypassing it.

A bounded search on 23 July 2026 covered the exact source sentence and
combinations of `circledness`, `complex Dvoretzky`, `phase increment`,
`C1,1`, and `Lipschitz gradient`.  Aubrun--Szarek's later monograph still
records only removal above a logarithmic small-\(\varepsilon\) threshold and
states that dropping that threshold is unknown.  No statement of the
phase-increment criterion or the \(C^{1,1}\) corollary was located.  Novelty
confidence is moderate, not definitive.

## Verification

The proof is analytic and self-contained modulo standard Lévy concentration,
Dudley chaining, and concentration on the unitary group.  The packet checks:

- the conditional mean-zero argument for the aligned increment;
- the real-gradient calculation proving
  \(D_{\mathbb T}(f)\leq L+H\);
- the phase-alignment chord inequalities; and
- the constants needed to pass from expected supremum to high probability.

Files:

- `main.tex`: full proof and scope audit;
- `solution_packet.pdf`: compiled proof;
- `source_paper.pdf`: original paper;
- `figures/open_problem_crop.png`: exact source passage.

Ledger:
`ledger/results/1003.4925_phase_regular_complex_dvoretzky.json`.
