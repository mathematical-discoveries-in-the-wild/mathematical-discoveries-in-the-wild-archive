# Von Neumann Algebras: BCP Failure Equals Countable Capture

Status: likely valid partial result / full countable-capture classification
inside von Neumann algebras.

Source target: arXiv:2311.14257, Question 3.

## Result

For a von Neumann algebra `M`, the following are equivalent:

```text
M has countable capture
M fails BCP
M is not atomic and separably represented
```

The source paper proves the BCP part: a von Neumann algebra has BCP/UBCP iff
it is atomic and can be represented on a separable Hilbert space. This packet
adds the capture equivalence.

## Key Ideas

- Countable capture always implies failure of BCP.
- If `M` has an atomless summand, the source singular-state lemma gives, for
  each center `x_n`, a singular state norming `x_n^* x_n`. A standard
  singular-functional projection lemma gives one nonzero projection killed by
  all these states; that projection is the common capture direction.
- If `M` is atomic but not separably represented, either it has uncountably
  many atomic summands, so primitive topology gives capture, or it has a
  nonseparable Hilbert summand `B(H)`, where a projection orthogonal to a
  separable reducing/norming subspace gives capture.

## Scope

This fully classifies countable capture for von Neumann algebras. It does not
settle all C*-algebras, but it confirms that in the von Neumann class the
negative side of the source BCP classification is exactly the countable-capture
side.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the common projection lemma for countably many singular states;
- the atomless singular-state capture proof;
- the atomic nonseparably represented case split;
- the reliance on the source paper's von Neumann BCP theorem.
