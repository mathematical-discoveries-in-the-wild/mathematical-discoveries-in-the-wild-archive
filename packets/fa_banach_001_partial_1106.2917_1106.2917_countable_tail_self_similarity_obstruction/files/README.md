# Countable-tail self-similarity obstruction for Koszmider's cube-not-square route

Status: `partial_result_likely_valid`

Source target: arXiv:1106.2917, Piotr Koszmider, *A C(K) Banach space which does not have the Schroeder-Bernstein property*.

## Result

Koszmider asks in the introduction whether a space of the form `C(K)` can be isomorphic to its cube but not to its square. The source then describes the main construction `X_+=C(K_+)`, where `K_+` is the Stone space of a countable-tail Boolean algebra

```text
D_+ = { a in product_n A_n : a_n belongs to C_n for all but finitely many n }.
```

This packet proves that this whole countable-tail template is automatically self-similar under every finite partition of the block index set. In particular, for Koszmider's actual `K_+`,

```text
C(K_+) is isometric to C(K_+)^r for every finite r >= 1.
```

So the natural `K_+` construction, and any finite-cycle variant with the same countably repeated tail condition, cannot yield a `C(K)` space that is isomorphic to its cube but not to its square.

## Scope

This is not a full answer to Koszmider's open problem. It rules out a specific and natural construction route: countably many pair-isomorphic blocks with an "eventually in the matching subalgebra" compactification condition.

The global existence of a compact `K` with `C(K) ~= C(K)^3` but `C(K) !~= C(K)^2` remains open here.

## Packet contents

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1106.2917.
- `figures/open_problem_crop.png`: page 2 crop showing the source open problem and the beginning of the `K_+` construction.

## Verification notes

The proof is purely algebraic/topological. It identifies `D_+(N)` with the Boolean product of its restrictions to any finite partition of `N` into infinite pieces; each restriction is again a copy of `D_+(N)`. Stone duality converts this Boolean product into a finite topological disjoint sum, and `C` of a finite disjoint sum is the corresponding finite `l_infty` direct sum isometrically.

Bounded novelty check: exact local source search for "isomorphic to its cube", "not isomorphic to its square", and close variants found the Gowers-Maurey phenomenon, square-negative `C(K)`/`C_0(K)` examples, and the prior lane attempt, but no later `C(K)` cube-not-square resolution.
