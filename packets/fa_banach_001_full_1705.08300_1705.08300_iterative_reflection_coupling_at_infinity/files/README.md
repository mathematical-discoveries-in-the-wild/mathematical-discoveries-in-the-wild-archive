# Candidate full solution: iterative reflection coupling at infinity

Status: candidate full solution, likely valid pending human review.

Source paper: Elisabetta Candellero and Wilfrid S. Kendall, "Coupling of Brownian motions in Banach spaces", arXiv:1705.08300.

Open problem addressed: Question 18 of the source paper asks whether, for an abstract Wiener space \(W^* \hookrightarrow H \hookrightarrow W\), two \(W\)-valued Brownian motions started from arbitrary points of \(W\) can always be coupled at time infinity.

Claim: yes. The packet proves that density of the Cameron-Martin space \(H\) in \(W\) already suffices. Approximate the initial displacement by a summable sequence of Cameron-Martin corrections, remove one correction at a time by a standard Cameron-Martin reflection coupling, insert deterministic synchronous waiting periods so the stage times diverge, and use a one-dimensional gambler's-ruin tail estimate plus Borel-Cantelli to show the Banach-norm difference tends to zero almost surely.

Files:

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1705.08300.
- `figures/open_problem_crop.png`: crop of Question 18.
- `figures/reflection_definition_crop.png`: crop of the Cameron-Martin reflection definition used in the construction.

Novelty check performed:

- Cheap run indexes searched for arXiv id, title, and coupling keywords: no existing solution, attempt, registry, or proof-gap hit.
- Local parsed corpus searched for the exact coupling-at-infinity phrases and abstract-Wiener keywords: no answer found beyond the source paper and target-pool metadata.
- Web search queried `"coupling at time infinity" "abstract Wiener space"`, `"Brownian coupling at time infinity" "Banach"`, `"Coupling of Brownian motions in Banach spaces" "open question"`, `"Cameron-Martin" "coupling at time infinity" Brownian`, and close variants. The only relevant hit found was the source arXiv page.

Reviewer focus:

- Check carefully that the stage-by-stage predictable Cameron-Martin reflections preserve the second marginal as a \(W\)-valued Brownian motion. The packet gives the standard finite-dimensional-projection/local-martingale argument and reduces each finite time interval to finitely many ordinary Cameron-Martin reflection couplings.
- Check that the Borel-Cantelli estimate is insensitive to the possible large Cameron-Martin norms of the correcting vectors; the proof uses only their summable \(W\)-norms.

Ledger record: `runs/fa_banach_001/ledger/results/1705.08300_iterative_reflection_coupling_at_infinity.json`.
