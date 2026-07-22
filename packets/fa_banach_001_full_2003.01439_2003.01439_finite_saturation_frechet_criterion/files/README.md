# Full solution packet: finite saturation collapse characterizes Frechet differentiability

Status: `candidate_full_solution_likely_valid` (full positive answer to
Question 1 of arXiv:2003.01439, pending human review)

Source: Ramon J. Aliaga and Abraham Rueda Zoca, *Points of differentiability
of the norm in Lipschitz-free spaces*, arXiv:2003.01439, Questions 1 and 2 on
p. 15 of the arXiv PDF (published in *Journal of Mathematical Analysis and
Applications* 489 (2020), 124171).

## New result

Let `M` be bounded and uniformly discrete, let

\[
 \mu=\sum_{i=1}^{\infty}\lambda_i m_{x_i y_i}\in S_{\mathcal F(M)},
 \qquad \lambda_i>0,\quad \sum_i\lambda_i=1,
\]

and put `S_n={0,x_1,y_1,...,x_n,y_n}`. Let `P_n` be the finite polytope of
all 1-Lipschitz data `a:S_n -> R`, vanishing at the base point, which
saturate the first `n` oriented pairs:

\[
 a(x_i)-a(y_i)=d(x_i,y_i)\qquad(i\le n).
\]

For `a in P_n`, form its lower and upper McShane--Whitney extensions

\[
 L_a(z)=\max_{s\in S_n}(a(s)-d(s,z)),\qquad
 U_a(z)=\min_{s\in S_n}(a(s)+d(s,z)),
\]

and define the metric collapse number

\[
 \Delta_n=\sup_{a,b\in P_n}\sup_{z\in M}(U_a(z)-L_b(z)).
\]

The packet proves the exact criterion

\[
 \boxed{\ \mu\text{ is a point of Frechet differentiability of }
 \mathcal F(M)\quad\Longleftrightarrow\quad \Delta_n\longrightarrow0.\ }
\]

Every object in `Delta_n` is determined by finitely many points, their
distances, and the given convex-series representation. The condition is
independent of the enumeration because either side is equivalent to Frechet
differentiability. This gives the requested metric characterization for
infinite support.

## Proof mechanism

Let `E_n` be the face of the dual Lipschitz unit ball consisting of functions
that saturate the first `n` molecules. The envelope formulas give the exact
identity

\[
 \operatorname{diam}_{\|\cdot\|_\infty} E_n=\Delta_n.
\]

Uniform discreteness and boundedness make the uniform and Lipschitz norms
equivalent on `Lip_0(M)`. If `mu` is Frechet smooth, every `E_n` lies in an
increasingly thin norming slice because the coefficient tail tends to zero;
Smulyan's lemma then forces `Delta_n -> 0`.

Conversely, a compactness lemma for the finite Lipschitz polytope says that
data which almost saturate the first `n` pairs can be corrected uniformly to
data in `P_n`. McShane--Whitney clamping lifts that finite correction to a
global function in `E_n`. Hence any sufficiently thin norming slice lies
near the small-diameter face `E_n`, so its Lipschitz-norm diameter tends to
zero. Smulyan's lemma gives Frechet differentiability.

## Status of Question 2

Question 2 asked whether, for bounded uniformly discrete `M`, a Frechet
smooth point could fail to be a convex series of molecules. Aliaga,
Pernecka, and Smith later proved the stronger fact that **every** element of
`F(M)` is a convex series of molecules whenever `M` is uniformly discrete.
Thus Question 2 has the known answer **no**; this literature fact is clearly
separated from the new proof of Question 1.

## Packet contents

- `main.tex` and `solution_packet.pdf`: self-contained theorem and proof.
- `source_paper.pdf`: the source paper containing the two questions.
- `supporting_paper_2302.13951.pdf`: the later paper settling Question 2.
- `figures/open_problem_crop.png`: full-context crop of both source questions.
- `verification.md`: proof audit, sanity checks, novelty bounds, and reviewer
  focus.

## Novelty and review

The run's cheap indexes were searched for the arXiv id, title, and the core
Frechet-differentiability and convex-series terms. Bounded exact-phrase and
close-variant web searches were then performed for a metric characterization
using finite extensions, saturation, and McShane--Whitney envelopes. No
later answer to Question 1 was located. The search did locate the 2024 answer
to Question 2. This is not an exhaustive priority search, so novelty
confidence for the new criterion is **moderate**.

Recommended expert-review focus: the finite-face correction lemma, the exact
envelope formula for `diam E_n`, and whether an equivalent criterion already
appears under different terminology.
