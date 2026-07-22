# TEPROG weak convergence without global strict convexity

- Result type: candidate full solution, with an interpretation-separating counterexample.
- Source: Daniel Reem, Simeon Reich, and Alvaro De Pierro, *A Telescoping Bregmanian Proximal Gradient Method Without the Global Lipschitz Continuity Assumption*, arXiv:1804.10273v4, JOTA 182 (2019), 851--884.
- Target: Remark 6.4 on pages 11--12.
- Packet PDF: `solution_packet.pdf`.
- Source PDF: `source_paper.pdf`.
- Evidence: `figures/open_problem_crop_page11.png` and `figures/open_problem_crop_page12.png`.
- Verification report: `verification_report.md`.
- Ledger: `runs/fa_banach_001/ledger/results/1804.10273_teprog_weak_convergence_without_global_strictness.json`.

## Claim

The weak convergence conclusion of Theorem 6.1 remains valid after deleting only the requirement that the Bregman generator be strictly convex on all of `dom(b)`. Assumption 5.2 is enough: two weak cluster points lie in `C`, hence in a common nested telescopic set `S_N`, and `b` is strongly convex there. The limiting-difference identity forces their two directed Bregman divergences to be zero, while local strong convexity forces the cluster points to coincide.

In fact, the proof needs only Bregman separation on the weak cluster set. Conversely, if the intended relaxation also deletes local strong convexity/separation on the telescopic sets, weak convergence can fail even in `R^2`: with a generator flat in one coordinate and zero objective, arbitrary proximal choices can alternate forever in the flat coordinate.

## Proof intuition

The source proof invokes global strict convexity only at its last uniqueness-of-cluster-points step. Everything before that step already shows that the iterates are bounded, every weak cluster point is a minimizer in `C`, and `B(q,x_k)` converges for every cluster point `q`. For two cluster points `q_1,q_2`, the limiting-difference property gives

```text
B(q_2,q_1) = ell_2 - ell_1,
B(q_1,q_2) = ell_1 - ell_2.
```

Convexity makes both quantities nonnegative, so both vanish. Since the nested sets cover `C`, the two points lie together in some `S_N`; strong convexity on `S_N` gives `B(q_2,q_1) >= (mu_N/2)||q_2-q_1||^2`. Thus they are equal.

## Verification

- Verdict: likely valid; candidate full answer under the literal retained TEPROG hypotheses.
- The proof is analytic and uses no numerical evidence.
- The exact use of strict convexity in the source Lemma 8.1 was traced and replaced by the local strong-convexity estimate above.
- The flat-direction counterexample was checked against every framework condition it claims to retain; it intentionally violates Assumption 5.2, which is precisely the point of the interpretation split.
- Reproduce the evidence crops with:

```bash
conda run --no-capture-output -n sandbox python code/make_open_problem_crops.py
```

## Novelty check

On 2026-07-22, bounded searches used the exact source title, arXiv id, the quoted open-question phrase, `TEPROG weak convergence strict convexity`, and close variants. The 13 works in the OpenAlex citation list for DOI `10.1007/s10957-019-01509-8` were screened by title and available abstract/metadata. No later work claiming this exact answer was found. This is a bounded negative search, so novelty confidence is moderate rather than definitive.

## Human review focus

Check that Remark 6.4 is read with Assumption 5.2 retained, as its statement says, and verify the one-line first-order consequence of strong convexity on `S_N`. Also assess whether the source authors informally intended to remove Assumption 5.2 despite not saying so; the packet's second theorem handles that broader reading negatively.
