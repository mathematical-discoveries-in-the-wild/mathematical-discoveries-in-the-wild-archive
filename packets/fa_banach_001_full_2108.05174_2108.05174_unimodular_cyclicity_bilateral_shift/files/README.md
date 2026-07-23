# Full unimodular cyclicity via a bilateral fixed-space dilation

- Result type: candidate full solution.
- Source: Jochen Glück, *A note on the fixed space of positive contractions*,
  arXiv:2108.05174.
- Target: Open Problem 3.4 on source page 6.
- Answer: affirmative, with the full eigenspace dimension estimate.
- Additional result: the analogous dimension estimate for the generator of a
  positive contractive \(C_0\)-semigroup.
- Packet PDF: `solution_packet.pdf`.
- Source PDF: `source_paper.pdf`.
- Evidence: `figures/open_problem_crop.png`.
- Verification report: `verification_report.md`.
- Ledger:
  `runs/fa_banach_001/ledger/results/2108.05174_unimodular_cyclicity_bilateral_shift.json`.

## Claim

Let \(E\) be a monotonically complete complex Banach lattice with the Fatou
property, and let \(T\) be a positive contraction on \(E\). For every
\(\lambda\in\mathbb T\) and \(k\in\mathbb Z\),

```text
dim ker(lambda - T) <= dim ker(lambda^k - T).
```

The proof passes to `ell-infinity(Z; E)` and defines

```text
(Sx)_n = T x_{n-1},    (Rx)_n = x_{n+1}.
```

The source paper's main theorem makes `Fix(S)` a Banach lattice. The bilateral
shift `R` commutes with `S`, so its restriction to `Fix(S)` is a lattice
automorphism. The map

```text
z |-> (lambda^n z)_{n in Z}
```

is a linear bijection from `ker(lambda - T)` to
`ker(lambda - R|Fix(S))`. The standard dimension inequality for a lattice
automorphism therefore transfers back to `T`.

## Verification

- `ell-infinity(I; E)` is shown directly to inherit monotone completeness and
  the Fatou property for every index set `I`.
- Both directions of the eigenspace identification are written out
  coordinatewise.
- The lattice-power dimension lemma is recalled, including the finite
  linear-independence argument that handles its nonlinear power map.
- The same construction over `ell-infinity(R; E)` proves the dimension
  estimate for semigroup-generator eigenspaces anticipated after Corollary 3.5
  of the source.
- The packet compiled and every rendered page was visually inspected.

Reproduce the source crop and packet from this directory with:

```bash
conda run --no-capture-output -n sandbox python code/make_open_problem_crop.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

## Novelty check

On 23 July 2026, bounded searches used the arXiv id and exact title, the exact
Open Problem 3.4 wording, and combinations of `positive contraction`,
`monotonically complete`, `Fatou property`, `peripheral point spectrum`,
`cyclicity`, and `bilateral shift`. The local 2000-2026 source corpus and
web/arXiv-oriented searches found no later claimed answer. Novelty confidence
is moderate, not definitive.

## Human review focus

Review the use of Theorem 3.1 on `ell-infinity(Z; E)` and the eigenspace
identification by coordinate zero. For the additional semigroup estimate,
check that the common fixed space of the commuting family `(S_t)` is used and
that lattice powers remain simultaneous translation eigenvectors.
