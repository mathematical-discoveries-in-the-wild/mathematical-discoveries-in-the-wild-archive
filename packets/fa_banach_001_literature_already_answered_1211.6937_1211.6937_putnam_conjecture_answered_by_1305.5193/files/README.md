# Literature-Already-Answered Packet: Bergman Putnam factor-1/2 conjecture

status: literature_already_answered
source_arxiv_id: 1211.6937
supporting_arxiv_id: 1305.5193

## Identification

Bell, Ferguson, and Lundberg's paper `1211.6937` conjectures in the first
concluding remark that for a Toeplitz operator with analytic symbol `phi` on
the Bergman space of a planar domain `G`,

```text
||[T_phi^*, T_phi]|| <= Area(phi(G))/(2 pi).
```

The same concluding remark has an "Added in press" note saying that
J.-F. Olsen and M. C. Reguera proved the conjecture in Theorem 1 and
Corollary 1 of `1305.5193`.

The supporting paper explicitly says in its abstract and introduction that it
improves the classical Putnam inequality for Bergman-space Toeplitz
commutators by a factor of `1/2`, answering the recent conjecture by Bell,
Ferguson, and Lundberg. Its Corollary 1 gives the stronger weighted statement
for simply connected domains:

```text
||T_psi^* T_psi - T_psi T_psi^*|| <= ||psi'||_{A^2(Omega)}^2/(2 + alpha).
```

Setting `alpha = 0` gives the desired Bergman-space factor-`1/2` inequality.

## Contents

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: locally compiled PDF from cached arXiv source `1211.6937`.
- `supporting_paper_1305.5193.pdf`: locally compiled PDF from cached arXiv source `1305.5193`.

## Scope

This packet records an already-known literature answer, not a new proof from
the run. The source paper itself points to the supporting answer in an
added-in-press note, so the target should not be reworked as an open conjecture.
