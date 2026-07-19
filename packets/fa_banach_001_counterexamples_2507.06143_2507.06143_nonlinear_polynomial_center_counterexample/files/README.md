# Counterexample packet: nonlinear polynomial Daugavet center question

Status: claimed counterexample, likely valid, needs human review.

Source target: Sheldon Dantas, Miguel Martin, and Yoel Perreau, *The Daugavet property is equivalent to the polynomial Daugavet property*, arXiv:2507.06143.

Question addressed: after proving that every linear Daugavet center is a polynomial Daugavet center, the authors ask whether the same conclusion follows for a non-null polynomial `Q` satisfying

```text
||Q + T|| = ||Q|| + ||T||
```

for every rank-one linear operator `T`.

Result: No. Over either `R` or `C`, take `X=Y=K` and `Q(z)=z^2`. Then `Q` satisfies the displayed equality against every rank-one linear operator, but it is not a polynomial Daugavet center, because the rank-one polynomial `P=-Q` gives `||Q+P||=0` while `||Q||+||P||=2`.

Files:
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2507.06143.
- `figures/open_problem_crop.png`: source crop for the question.
- `code/verify_scalar_example.py`: numerical smoke check for the scalar formula.

Novelty check: searched exact phrases around `polynomial Daugavet center`, `rank-one linear`, and the source title on 2026-06-20. The only direct hit found was the source arXiv paper.

Review recommendation: check that the source definition of rank-one polynomial allows scalar polynomial multiples `p(x)y_0`; with that definition, the perturbation `P=-Q` is rank-one and the counterexample is immediate.
