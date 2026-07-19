# Strengthened Partial/Audit Packet: Square Stability Versus Hyperplane Stability

Source: F. Albiac and J. L. Ansorena, *Unconditional structure of Banach
spaces with few operators*, arXiv:2603.07324.

Result type: `partial`

Status: stronger partial/audit result, likely valid, pending human review. The
main Question 2.15 remains open.

## Source Question

Question 2.15 asks whether there is a Banach space `X` such that

```text
X is isomorphic to X^2, but X is not isomorphic to X plus one scalar dimension.
```

Equivalently, can square stability hold while hyperplane stability fails?

## Upgrade Summary

The earlier active packet recorded only a route obstruction: inside the usual
Gowers-Maurey proper-set-of-spreads framework, one cannot have countably many
exact binary Cuntz spread pairs; hence the fresh-pair Fredholm-index swindle
does not solve Question 2.15.

The June 23 report keeps that obstruction but strengthens and audits it:

- it identifies the omitted closure-under-products/adjoints clause in the old
  proof and repairs the argument under the weaker displayed definition;
- it extends the no-go theorem from binary pairs to exact fixed finite arity;
- it proves an address-rigidity/double-commutation obstruction for exact spread
  families;
- it gives Fredholm-index and `K_0` reformulations, including the rank-one
  idempotent test under square stability;
- it reduces possible full solutions to concrete routes involving
  Gowers-Maurey `S_m`/`H_m`, the Kalton-Peck space `Z_2`, and complex
  realification with essential incomparability.

The report explicitly does not solve the source question and records no located
full proof or counterexample through June 22, 2026.

## Files

- `main.tex`: consolidated strengthened partial/audit packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of the original source paper.
- `figures/source_question_page_15.png`: source crop containing Question 2.15.
- `figures/source_question_page_16.png`, `figures/source_question_page_17.png`:
  adjacent source context preserved from the earlier packet.
- `evidence/2026_06_23_square_hyperplane_report/`: supplied TeX/PDF report.
- `history/2026_06_23_pre_upgrade/`: previous June 14 packet files.
- `tmp/`: LaTeX build intermediates and rendered QA pages.

## Human Review

Recommended checks:

- verify the repaired weak-proper binary proof and the finite-arity extension;
- check that the address-rigidity corollary really requires double commutation;
- review the `K_0` rank-one criterion and its dependence on square stability;
- verify the conditional `Z_2` parity theorem and the realification parity
  theorem;
- confirm the packet’s conservative classification: strong partial/audit, not
  full solution.
