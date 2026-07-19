# Partial result: Cauchy `B_1^n` separation reduction

Status: candidate partial result, likely valid, pending expert review.

Source paper: Shahar Mendelson, Emanuel Milman, and Grigoris Paouris,
*Generalized Dual Sudakov Minoration via Dimension Reduction - A Program*,
arXiv:1610.09287.

Targeted challenge: the conclusion identifies Part 1 of the program as the
main remaining challenge and says it is significant even for `K = B_1^n`,
requiring measures on the Grassmannian other than Haar.

Result: Cauchy-stable random linear maps give a one-sided separation reduction
for `B_1^n` in dimension `m = ceil(k)` for `e^k` separated points, while
retaining mass for measures with `mu(B_1^n) >= e^{-q}`, `q <= k/2`. The loss is
`R = O(k log k)`, so this is not the constant-loss Part 1 needed by the source
program.

Files:

- `main.tex` / `solution_packet.pdf`: partial-result packet.
- `source_paper.pdf`: local copy of arXiv:1610.09287.
- `figures/open_problem_crop.png`: stitched crop of the page 40-41 challenge.
- `code/make_open_problem_crop.py`: reproducible crop helper.

Review focus: correctness of the Cauchy tail estimates is straightforward; the
main question is whether the `O(k log k)` loss can be reduced or made compatible
with the program by changing the target body.
