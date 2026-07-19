# Partial solution packet: `c0`-sums and the real Lipschitz numerical index

## Source

- Paper: Antonio P\'erez-Hern\'andez, *Lipschitz vs Linear Numerical Index in certain Banach spaces*
- arXiv: `2507.18208`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `partial`
- Target question: the real Banach-space conjecture asking whether `n_L(X)=n(X)` for every real Banach space.
- Packet claim: if `X=(\oplus_{\gamma\in\Gamma}X_\gamma)_{c0}` is a real `c0`-sum of separable real Banach spaces, then `n_L(X)=n(X)`.

## Relation to the source paper

The source paper proves equality for real separable Banach spaces and real dual Banach spaces. This packet adds a nonseparable class by observing that a norm-one Lipschitz map on a `c0`-sum can be tested, up to an arbitrary loss, on a countable coordinate sub-sum. That sub-sum is separable, so the source paper's Theorem 2.1 applies.

The proof also uses the standard formula

```text
n((\oplus_{\gamma\in\Gamma} X_\gamma)_{c0}) = inf_{\gamma\in\Gamma} n(X_\gamma).
```

This formula is flagged as the main external structural input for human review.

## Files

- `main.tex`: LaTeX source for the human-review packet.
- `solution_packet.pdf`: compiled review packet.
- `figures/open_question_page2_crop.png`: source screenshot showing the central question.
- `figures/real_case_conjecture_page3_crop.png`: source screenshot showing the real-case conjecture.
- `figures/separable_theorem_page4_crop.png`: source screenshot showing the separable theorem used as input.
- `tmp/`: LaTeX build output and temporary verification renders.

## Verification notes

No numerical experiment is needed. The check is a structural proof:

1. In a `c0`-sum, each vector has countable support.
2. A nearly norm-attaining pair for a Lipschitz map therefore lives, together with its two image vectors, in a countable coordinate sub-sum.
3. The projected Lipschitz map on that countable sub-sum has almost the same Lipschitz norm and no larger Lipschitz numerical radius.
4. The countable sub-sum is separable, so the source paper's separable theorem applies.
5. The standard `c0`-sum numerical-index formula compares the numerical index of the countable sub-sum with the full space.
