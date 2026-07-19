# Counterexample packet: `P(omega_1)` fails in arity 3

Status: likely valid counterexample.

Source paper: Andrew Swift, "Coarse embeddings into `c_0(Gamma)`", arXiv:1703.01891.

Target question: Problem 2 in Section 5 asks whether Theorem B is true for `omega_1`, equivalently whether property `P(omega_1)` holds for all finite arities.

Result: No. There is a ZFC coloring `sigma:[omega_1]^3 -> omega_1` such that:
- for every pair `F in [omega_1]^2`, the set of colors on triples extending `F` is finite;
- every color class consists only of triples containing the color ordinal itself, so no two same-colored triples are disjoint.

Thus both alternatives in `P(omega_1)` fail for `n=3`.

Core construction: for each countable ordinal `gamma`, fix an enumeration of `gamma` by natural numbers. For `alpha < beta < gamma`, color `{alpha,beta,gamma}` by whichever of `alpha` and `beta` appears earlier in the enumeration attached to `gamma`.

Files:
- `main.tex`: proof packet source.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of arXiv:1703.01891.
- `figures/open_problem_crop.png`: crop of the source open-problem block.

Ledger: `runs/fa_banach_001/ledger/results/1703.01891_pomega1_n3_counterexample.json`.
