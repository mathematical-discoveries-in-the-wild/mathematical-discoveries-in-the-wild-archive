# Atom at zero disproves the positive-level persistence conjecture

**Status:** `literature_implied_answer (full counterexample to Remark 3)`.

The source paper, arXiv:2112.04820, conjectures that the persistence
exponent is positive for every positive level and every spectral measure in
its class `M`. A separate 2026 paper by Naomi Feldheim, Ohad Feldheim, and
Stephen Muirhead proves polynomial persistence asymptotics for nondegenerate
stationary Gaussian fields whose spectral measure has an atom at zero. It
cites the source paper but does not explicitly identify this consequence.

In dimension one, take

\[
  \rho=a\delta_0+e^{-\lambda^2}\,d\lambda,\qquad a>0.
\]

Then `rho` lies in the source classes `L` and `M`, because it has finite
log-moment and `rho'(0)=+infinity`. The 2026 universality theorem, applied at
any fixed level above the conjecture's level, gives persistence probability
`T^{-sqrt(pi)/a+o(1)}` on an interval of length comparable to `T`. Hence the
exponential persistence exponent exists and equals zero, contradicting the
claimed strict positivity.

This is recorded as a literature-implied answer rather than a new result:
the later theorem supplies the decisive asymptotic, while the identification
with Remark 3 is made here.

## Files

- `solution_packet.pdf`: compact identification and implication.
- `source_paper.pdf`: arXiv:2112.04820v3.
- `supporting_paper_2605.20587.pdf`: the separate 2026 supporting paper.
- `figures/open_problem_crop.png`: Remark 3 from source PDF page 3.
- `figures/definitions_crop.png`: source definitions of `L` and `M`.
- `main.tex`: packet source; build and render intermediates are in `tmp/`.

## Scope and review focus

The implication uses Theorem 3(iv) of arXiv:2605.20587 and its statement that
the result holds at arbitrary fixed levels. Using a slightly higher level
avoids any distinction between strict and weak persistence inequalities.
Human review should confirm that level extension and the one-dimensional
specialization. The elementary degenerate example `rho=delta_0` already gives
the same contradiction directly, but the packet foregrounds the later
nondegenerate literature result.

Ledger: `runs/fa_banach_001/ledger/results/2112.04820_atom_zero_persistence_conjecture_disproved.json`.
