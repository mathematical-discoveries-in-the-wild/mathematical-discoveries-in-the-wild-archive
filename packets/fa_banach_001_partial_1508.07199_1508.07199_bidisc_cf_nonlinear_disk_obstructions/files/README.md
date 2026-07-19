# Nonlinear Disk Obstructions for the Bidisc CF Problem

Status: `partial_result_likely_valid`

Source target: arXiv:1508.07199, Rajeev Gupta, "The Carath\'eodory-Fej\'er Interpolation Problems and the von-Neumann Inequality".

## Result

The source asks what extra properties on the polynomials \(p_1,p_2\), beyond
\(\|\mathscr T(M_{p_1},M_{p_2})\|\le 1\), ensure that the corresponding
operator-valued polynomial is in the CF class.

This packet records a new elementary obstruction obtained by testing a
candidate bidisc Schur extension on nonlinear analytic disks.  For
\[
p(z_1,z_2)=a_{10}z_1+a_{01}z_2+a_{20}z_1^2+a_{11}z_1z_2+a_{02}z_2^2,
\]
solvability of the degree-two bidisc CF problem implies, in addition to the
source's D-slice condition,
\[
|a_{10}|+|a_{02}|\le 1-|a_{01}|^2,\qquad
|a_{01}|+|a_{20}|\le 1-|a_{10}|^2.
\]

Consequently the two-term family \(p_{a,b}(z_1,z_2)=a z_1+b z_2^2\) is solved
exactly:
\[
p_{a,b}\text{ has a CF extension if and only if } |a|+|b|\le 1.
\]

This gives an infinite family of examples satisfying the source's necessary
condition \(|p_2|+|p_1|^2\le 1\) but failing the CF problem whenever
\[
0<|a|<1,\qquad 1-|a|<|b|\le 1-|a|^2.
\]
The source example \(a=1/\sqrt2,\ b=1/2\) is one endpoint case in this family.

## Files

- `main.tex`: human-readable proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local source PDF.
- `figures/open_problem_crop.png`: crop of the source example and open question.
- `code/verify_disk_obstructions.py`: small numerical sanity checker for the
  disk inequalities and the two-term classification boundary.

## Human Review

Recommended review focus: check that substituting the nonlinear disks
\((z_1,z_2)=(\alpha t^2,\beta t)\) and \((\alpha t,\beta t^2)\) into an
arbitrary admissible extension cannot receive order-one or order-two
contributions from the tail \(q\), and that the one-variable Schur coefficient
inequality is applied with the correct coefficients.
