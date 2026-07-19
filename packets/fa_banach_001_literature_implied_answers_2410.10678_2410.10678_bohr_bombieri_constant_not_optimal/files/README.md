# Bohr-Bombieri Constant Improvement

Status: literature-implied answer, partial scope.

Source paper: Hanna Blazhko, Daniil Homza, Felix L. Schwenninger, Jens de
Vries, and Michal Wojtylak, *The algebraic numerical range as a spectral set
in Banach algebras*, arXiv:2410.10678.

Target question: Example 6.3 asks whether the constant `2 sqrt(3) / 3` in
inequality (6.1) is optimal, and then asks the stronger constant-1 question.

Result: the constant in (6.1) is not optimal.  The Bohr-Bombieri majorant
formula gives

```text
B(1/2) = 6 - 2 sqrt(6) < 2 sqrt(3) / 3.
```

Thus the source estimate for the direct-sum example improves to
`6 - 2 sqrt(6)`.  The stronger question asking for a norm-one operator that is
polynomially bounded with constant `1` and has `Psi(T)=infinity` remains open
in this packet.

Packet contents:

- `source_paper.pdf`: original arXiv PDF.
- `supporting_paper_2503.16313.pdf`: accessible supporting paper that records
  the Bohr-Bombieri formula and cites the 1962 source.
- `figures/open_problem_crop.png`: crop of Example 6.3 and the open question.
- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: rendered packet.
- `code/verify_constants.py`: exact symbolic/numeric check of the constants.
- `tmp/`: LaTeX build outputs.

Human review notes:

The only imported mathematical fact is the Bohr-Bombieri formula for the
classical majorant function on `[1/3, 1/sqrt(2)]`.  At `r=1/2`, it yields the
constant above.  The operator-theoretic step is just
`||f((1/2)L)|| <= sum |a_k| 2^{-k}` for the unilateral shift, plus the
existing Hilbert block estimate for `E`.
