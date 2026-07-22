# No uniform polynomial exponent gap for positive Kreiss semigroups on L2

Status: `partial_result_likely_valid`

## Source question

Loris Arnold and Clement Coine, *Growth rate of eventually positive Kreiss
bounded C0-semigroups on Lp and C(K)*, arXiv:2207.08443, Question 3.9(2),
ask whether every uniformly eventually positive Kreiss bounded C0-semigroup on
an Lp-space, `1 < p < infinity`, satisfies

```text
||T_t|| = O(t^(1-epsilon))
```

for some `epsilon in (0,1)`.

## Partial result

There is no exponent gap that depends only on the ambient exponent, already
for `p=2`. More precisely, for every `delta in (0,1)` there is a positive
Kreiss bounded C0-semigroup `(S(t))` on an L2-space such that

```text
||S(n)|| >= (1/3)(n+1)^(1-delta)    for every integer n >= 0.
```

Consequently, if this semigroup has a bound
`||S(t)|| = O(t^(1-epsilon))`, then necessarily `epsilon <= delta`.
As `delta` is arbitrary, no positive universal gap `epsilon_2` works for all
positive Kreiss bounded C0-semigroups on L2.

The construction suspends the positive Cesaro-bounded weighted-shift examples
of Bonilla and Muller, arXiv:1912.07931, Theorem 2.3. Given their positive
operator `T` on a Hilbert lattice `H`, put

```text
(S(t)f)(s) = T^floor(s+t) f(s+t-floor(s+t)),   0 <= s < 1,
```

on `L2([0,1);H)`. The packet proves directly that this is a positive C0
semigroup, that discrete Cesaro boundedness of `T` implies continuous Cesaro
boundedness of `S`, and that `||S(n)||=||T^n||`. Arnold--Coine Proposition 2.6
then converts positivity plus continuous Cesaro boundedness into Kreiss
boundedness.

## Verification

- The self-contained suspension estimates are in `main.tex` and the compiled
  `solution_packet.pdf`.
- `verification.md` gives an adversarial step-by-step verifier report.
- `source_paper.pdf` is arXiv:2207.08443; the full-width crop of Question
  3.9 is in `figures/open_problem_crop.png`.
- `supporting_paper_1912.07931.pdf` is the Bonilla--Muller source for the
  positive discrete examples.
- No computation is used in the promoted proof. The crucial identities checked
  in review are the formula for the integral of the suspension over an integer
  time interval and the equality `||S(n)||=||T^n||`.

## Scope and novelty

This does **not** answer the per-semigroup question: it remains possible that
each individual semigroup has some positive exponent gap depending on that
semigroup. It proves only that such a gap cannot be uniform across the class.

A bounded check through 2026-07-22 covered arXiv:2207.08443,
arXiv:1912.07931, arXiv:1912.10507, arXiv:2302.14135, and arXiv:2405.16371,
plus searches for positive Cesaro/Kreiss bounded power growth and suspension
semigroups. No explicit statement of this continuous-time sharpness corollary
was found. Novelty confidence is moderate-low because the suspension is
standard and the discrete examples are known; the value is the exact
connection to Question 3.9(2).

Human review should focus on the continuous Cesaro estimate in Lemma 2 of the
packet and on the use of Arnold--Coine Proposition 2.6. If those are accepted,
the lower bound and the no-uniform-gap conclusion are immediate.
