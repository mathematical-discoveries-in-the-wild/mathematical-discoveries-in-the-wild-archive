# Counterexample Packet: Initial Sign Vectors in `c0`

Run: `fa_banach_001`
Agent: `agent_lane_01`
Status: candidate counterexample; likely valid pending human review

## Source

- Paper: Ondrej Kurka, "Tsirelson-like spaces and complexity of classes
  of Banach spaces", arXiv:1612.09334.
- Source target: Remark 5.9(iii), page 21.
- Local source PDF: `source_paper.pdf`.
- Open-question evidence crop: `figures/open_problem_crop.png`.

Remark 5.9(iii) asks whether a Banach space `X` must have the Schur
property if there is a subset `W` such that
`\overline{co} W = B_X` and every weakly convergent sequence of elements
of `W` is norm convergent.

## Claimed Contribution

The answer is negative. Let `X = c0`, and let `W` be the union of all
finite initial sign cubes

```text
W_n = { (eps_1,...,eps_n,0,0,...) : eps_i in {-1,1} }.
```

Then `\overline{co} W = B_{c0}` because each finite cube
`[-1,1]^n` is the convex hull of its sign vertices and finite-support
vectors are dense in `B_{c0}`.

Every weakly convergent sequence in `W` is norm convergent. If the
lengths of such a sequence were unbounded, a subsequence with lengths
tending to infinity would converge coordinatewise to a vector whose
every coordinate has modulus one, impossible in `c0`. Therefore the
lengths are bounded, so the sequence lies in a finite set and is norm
convergent.

However, `c0` does not have the Schur property: its unit vector basis is
weakly null but not norm null.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: screenshot crop of Remark 5.9(iii)
  from page 21 of the source paper.
- `tmp/`: LaTeX build outputs.

## Verification

Build command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The proof uses only the standard facts that `c0^* = ell_1`, weak
convergence in `c0` implies coordinatewise convergence, and the canonical
basis of `c0` is weakly null.

## Human Review Notes

The main review point is whether the source question imposes any hidden
extra condition on `W` beyond the displayed convex-generation and
weak-sequential condition. Under the statement printed in Remark 5.9(iii),
the construction is a direct counterexample.
