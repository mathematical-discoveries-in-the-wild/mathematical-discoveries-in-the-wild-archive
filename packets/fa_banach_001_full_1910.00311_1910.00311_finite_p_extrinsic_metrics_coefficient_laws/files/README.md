# Finite-p extrinsic metrics via coefficient laws

Status: `candidate_full_solution_likely_valid` for the closing question of
arXiv:1910.00311v1 (PDF page 24).

The source gives explicit descriptions of three extrinsic metrics for
`p = infinity` and says that no similar descriptions are known for other
`p`.  This packet gives exact formulas for every finite `1 <= p < infinity`.

## Result

A finite family of maps from finite-dimensional spaces into `L_p[0,1]` is
encoded exactly by the joint probability law of its coefficient-vector
functions.  Isometric embedding constraints become scalar `p`-moment
identities.  Under this correspondence:

- `partial_(X,Lp)` is an infimum, over moment-constrained couplings of two
  dual coefficient vectors, of the diagonal difference operator norm;
- `gamma_(k,Lp)` is the infimum of the Hausdorff gap between the two
  coordinate unit balls in the joint `L_p` seminorm;
- `d_(k,Lp)` is the infimum of the `L_q -> L_p` norm of the explicit kernel
  `K(s,t) = a_0(s)(a_1(t)) - b_0(s)(b_1(t))`, subject to the prescribed
  `GL(k)` orbit moment constraints.

Every admissible law is realizable on `[0,1]`, so these are equalities, not
relaxations.  The source's Theorem 3.11 transfers the formulas to its
finite-support extrinsic metrics on their original domains.

## Packet contents

- `solution_packet.pdf`: theorem, proof, scope, and review notes.
- `source_paper.pdf`: arXiv:1910.00311v1.
- `figures/open_problem_crop.png`: the closing question on PDF page 24.
- `code/finite_atomic_checks.py`: random finite-atomic regression checks.

## Novelty and limitation

Local run/corpus searches and bounded exact-phrase, title, author, and arXiv
web searches on 2026-07-21 found no later answer.  Novelty confidence is
moderate rather than definitive.

The only interpretive limitation is the word `explicit`: these are exact
finite-dimensional moment/coupling formulas, not closed elementary formulas
in the input norms.  Human review should especially check that this matches
the source authors' intended level of explicitness, as well as the complex
duality convention and the Theorem 3.11 transfer.
