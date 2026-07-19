# Real-line transitive Lipschitz maps have hypercyclic linearizations

Status: full_solution_likely_valid.

Source target: Abbar, Coine, and Petitjean, *On the dynamics of
Lipschitz operators*, arXiv:2011.10800, Remark 4.4.

Supporting topological input: Bau-Sen Du, *Continuous transitive maps on the
interval revisited*, arXiv:1701.02589, Theorems 4 and 6.

## Result

The real-line question in Remark 4.4 has an affirmative answer. Let
`f:R -> R` be Lipschitz and topologically transitive, and suppose that `f` has
a fixed point. Point `R` at such a fixed point, so that the Lipschitz-free
linearization `widehat f` is defined on `F(R)`. Then `widehat f` is weakly
mixing, hence hypercyclic. Moreover `widehat f` has dense periodic points, so
it is Devaney chaotic.

## Idea of the Proof

The source paper proves the compact-interval analogue by using a
Barge-Martin/Sy decomposition. The paper then says that no comparable
decomposition is known for unbounded intervals.

Du's theorem supplies exactly the missing interval dynamics. For a continuous
transitive map on any real interval, either a same-side fixed-point condition
holds, which is equivalent to mixing, or there is a unique fixed point and the
map swaps the two sides, while the square is transitive on each side and has
at least two fixed points. In the second case, Du's mixing equivalence applied
to each closed half-line makes the two restricted square maps mixing.

Under the standard identification `F_z(R) = L^1(R)`, the two half-lines give
the direct-sum splitting `L^1((-\infty,z]) + L^1([z,\infty))`. Thus
`widehat{f^2}` is a direct sum of two mixing operators. Hence `widehat f` is
weakly mixing by Ansari's power theorem applied to `widehat f + widehat f`.
Du also gives dense periodic points for `f`, and the source paper's periodic
point proposition transfers this density to `widehat f`.

## Scope

This packet answers only the real-line transitive-map question from Remark
4.4. It does not solve the separate question, earlier in arXiv:2011.10800,
about whether there exists a Lipschitz operator which is hypercyclic but fails
the Hypercyclicity Criterion.

The result is a literature-assisted synthesis: Du's interval theorem is a
known pre-existing theorem, but it does not state the Lipschitz-free operator
consequence or explicitly answer arXiv:2011.10800. The packet records the
transfer proof.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2011.10800.
- `supporting_paper_1701.02589.pdf`: local copy of Du's supporting paper.
- `figures/open_problem_crop.png`: source Remark 4.4.
- `figures/supporting_theorem4_part1_crop.png`,
  `figures/supporting_theorem4_part2_crop.png`: Du Theorem 4.
- `figures/supporting_theorem6_part1_crop.png`,
  `figures/supporting_theorem6_part2_crop.png`: Du Theorem 6.
- Ledger: `runs/fa_banach_001/ledger/results/2011.10800_real_line_transitive_lipschitz_linearization.json`.

## Novelty Check

The run's cheap indexes had no exact prior packet for arXiv:2011.10800 or this
real-line dynamical question. Adjacent Lipschitz-free/operator packets for
arXiv:2310.08965 and arXiv:2512.05640 are unrelated.

Web/arXiv searches on 2026-06-30 for exact phrases around "transitive
Lipschitz map", "F(R)", "widehat f", "hypercyclic", and "unbounded intervals"
found the source paper and general interval-dynamics references, but no later
paper explicitly answering Remark 4.4. The proof materially uses Du's earlier
Theorems 4 and 6, so the novelty confidence is: new operator consequence /
transfer proof, not a new interval-dynamics theorem.

