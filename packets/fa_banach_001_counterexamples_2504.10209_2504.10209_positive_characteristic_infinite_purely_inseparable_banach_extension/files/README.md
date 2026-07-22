# An infinite algebraic Banach field extension in characteristic p

Status: `counterexample_likely_valid` (full negative answer to Remark 7.3,
subject to human review).

Source: Feliks Rączka, *Continuity of differential operators for
nonarchimedean Banach algebras*, arXiv:2504.10209v1.  Lemma 7.2 proves in
characteristic zero that an algebraic field extension `K ⊂ L`, with `L` a
Banach `K`-algebra, must be finite.  Remark 7.3 asks whether the lemma remains
true in characteristic `p>0`.

The answer is no.  Put

`k = F_p(u_1,u_2,...)`, `L = k((t))`, and `K = L^p`.

Then

`K = k^p((t^p)) = F_p(u_1^p,u_2^p,...)((t^p))`.

With the inherited `t`-adic absolute value, both `K` and `L` are complete
nontrivially valued nonarchimedean fields, and `L` is a Banach `K`-algebra.
Every `x∈L` satisfies `X^p-x^p`, so `L/K` is purely inseparable of exponent
one.  For every `N`, the `p^N` monomials
`u_1^{e_1}...u_N^{e_N}` (`0≤e_i<p`) are linearly independent over `K`.
Consequently `[L:K]` is infinite.

The proof does not answer the paper's broader request for a positive-
characteristic analogue of its automatic-continuity theorem.  It settles only
the exact extension question in Remark 7.3, by counterexample.

Files:

- `solution_packet.pdf`: full proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original paper.
- `figures/open_problem_crop.png`: source Remark 7.3.
- `verification.md`: adversarial proof and novelty audit.

Human-review recommendation: verify the identity `L^p=k^p((t^p))` and the
infinite-degree argument first.  They are the only substantive algebraic
points; the norm and completeness checks are then immediate.
