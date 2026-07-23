# Joint J-strict continuity of the multiplier Jordan product

- Result type: candidate full solution.
- Source: Francisco J. Fernandez-Polo, Jorge J. Garces, Lei Li, and Antonio M. Peralta, *On the strict topology of the multipliers of a JB*-algebra*, arXiv:2210.13353, RACSAM 117 (2023), Paper 146.
- Target: Questions Q1 and Q2 on source page 25.
- Answer: affirmative to both questions.
- Packet PDF: `solution_packet.pdf`.
- Source PDF: `source_paper.pdf`.
- Evidence: `figures/open_questions_crop.png`.
- Verification report: `verification_report.md`.
- Exact identity check: `code/check_albert_identities.py`.
- Ledger: `runs/fa_banach_001/ledger/results/2210.13353_jstrict_product_joint_continuity.json`.

## Claim

For every JB*-algebra `A`, the Jordan product on its multiplier algebra
`M(A)` is separately J-strict continuous. If two norm-bounded nets converge
J-strictly, then their product net converges J-strictly to the product of
their limits. Thus Questions Q1 and Q2 both have affirmative answers.

The central estimate is obtained from a positive contractive approximate unit
`e` and `c=1-e`. Every self-adjoint multiplier has the decomposition

```text
z = L_e z + R_e z,
R_e z = U_c z,
L_e z = 2(e o z) - 2(e o z) o e + e^2 o z in A.
```

For a J-strict-null net, `L_e z` tends to zero in norm for each fixed `e`.
The remaining quadratic tails satisfy the exact Jordan identity

```text
U_c x o U_c y = U_c(U_{x,y}(c^2)).
```

The source paper's fundamental quadratic identity and standard JB inequality
then give, for positive `a`,

```text
||a o (U_c x o U_c y)||^2
    <= 9 ||x||^2 ||y||^2 ||a|| ||U_c(a)||.
```

Since `||U_{1-e}(a)||` tends to zero along the approximate unit, the
tail-tail term is uniformly J-strict-small on bounded sets.

## Verification

- The proof is algebraic and analytic; computation is not used as proof.
- The two quadratic identities used in the localization argument were also
  checked in 40 exact random trials in the exceptional 27-dimensional real
  Albert algebra. This specifically guards against accidentally using an
  identity valid only in special Jordan algebras.
- The complete packet was compiled and every rendered page was visually
  inspected.
- Reproduce the source crop and exact identity check from the packet
  directory with:

```bash
conda run --no-capture-output -n sandbox python code/make_open_questions_crop.py
conda run --no-capture-output -n sandbox python code/check_albert_identities.py
```

## Novelty check

On 23 July 2026, bounded searches used the arXiv id, exact title, exact
question phrases, `Jordan product J-strict topology multipliers`, and the
published DOI `10.1007/s13398-023-01476-w` with citation-oriented variants.
The searches found the source paper and bibliographic mirrors but no later
paper claiming either answer. This is bounded negative evidence, so novelty
confidence is moderate rather than definitive.

## Human review focus

The key review points are the polarization proof of the tail-product identity
and the uniform tail estimate. Both are written out in the packet rather than
being delegated to computation. A second useful check is that the passage
from self-adjoint to complex elements uses only involution invariance of the
J-strict seminorms.
