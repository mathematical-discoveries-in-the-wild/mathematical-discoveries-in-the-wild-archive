# Full Packet: Schlumprecht Szlenk-Radius Converse

Result type: `full`

Status: candidate full solution.

Source paper:

- Tomasz Kochanek and Marek Miarka, "When is the Szlenk derivation of a
  dual unit ball another ball?", arXiv:2409.05516.
- Local source PDF: `source_paper.pdf`.

## Claim

The source paper proves an upper bound for `r_{S*}(epsilon)` in
Schlumprecht's space and asks whether the converse inequality holds.

This packet gives a candidate affirmative answer:

```text
r_{S*}(epsilon)
  = inf_n (log_2(n+2)-epsilon/2)/log_2(n+1),  0<epsilon<2.
```

Equivalently, the upper bound in Proposition 6 of the source paper is sharp
for Schlumprecht's space.

## Key Scalar Estimate

For the recursive implicit norm estimate, the scalar majorant must be
normalized by the restriction being estimated. The key estimate is:

```text
M_alpha(s) + min{phi(k-1)t, phi(k)t - s}
  <= phi(k) M_alpha(t).
```

The revised packet proves this estimate from a logarithmic product lemma for
`phi(n)=log_2(n+1)` and its increments.

## Proof Mechanism

The proof has three main steps.

1. Prove a product lemma:
   `phi((i+1)(j+1)) <= phi(i+1) phi(j+1)` and the analogous inequality for
   logarithmic increments.
2. Use that lemma to prove the strengthened scalar majorant estimate above.
3. Apply the scalar estimate recursively to show that if
   `||x||_S < a_alpha`, then for all sufficiently far coordinates `N`,
   both `x + alpha e_N` and `x - alpha e_N` remain in the Schlumprecht unit
   ball. The weak-null far-coordinate perturbations then give the reverse
   Szlenk-radius inclusion.

## Verification

- `solution_packet.pdf` is the polished human-review packet.
- `main.tex` is the LaTeX source for the packet.
- `figures/open_problem_crop.png` is a full-width screenshot crop from page 9
  of the source paper showing the open problem.
- `code/check_scalar_and_finite_cases.py` numerically checks the scalar
  estimate and representative finite Schlumprecht norm cases.
- The verification script was run with:

```text
conda run --no-capture-output -n sandbox python code/check_scalar_and_finite_cases.py
```

It passed on the promoted packet, including strengthened scalar checks on the
configured grid/random tests and finite-support Schlumprecht norm tests.

## Supporting Material

- `supporting_proof_note.tex`: external proof note supplied before the
  final packet was polished.
- `supporting_proof_note.pdf`: rendered version of that note.

These are kept for provenance. The canonical packet for review is
`solution_packet.pdf`.

## References

- Tomasz Kochanek and Marek Miarka, "When is the Szlenk derivation of a dual
  unit ball another ball?", arXiv:2409.05516.
- Thomas Schlumprecht, "An arbitrarily distortable Banach space", Israel J.
  Math. 76 (1991), 81--95.

## Novelty Check

A bounded web/literature search on June 14, 2026 found the arXiv source paper
and related Szlenk/Schlumprecht references, but did not find a later paper
proving this exact converse formula. Human review should still treat this as
a candidate result until independently checked.

## Human Review Notes

Review should focus first on:

- the logarithmic product lemma,
- the strengthened scalar estimate,
- the local-majorant recursion in the far-coordinate perturbation lemma,
- the final passage from finite-support vectors to the Szlenk derivation.

If those four points hold, the packet gives the full converse inequality and
therefore the exact formula for `r_{S*}(epsilon)`.
