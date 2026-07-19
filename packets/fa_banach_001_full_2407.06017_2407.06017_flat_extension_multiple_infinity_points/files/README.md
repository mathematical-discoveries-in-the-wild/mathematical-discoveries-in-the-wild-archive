# Full solution packet: multiple real points at infinity force non-flat moments

Status: candidate full solution, likely valid

## Source problem

Lorenzo Baldi, Grigoriy Blekherman, and Rainer Sinn, *Nonnegative
Polynomials and Moment Problems on Algebraic Curves*, arXiv:2407.06017.
After Example 7.2.3 the authors conjecture that the failure of ordinary flat
extension occurs for every affine plane cubic having at least two real points
at infinity.

## Result

The conjecture holds under the standing assumptions of the source (smooth and
totally real projective closure).

For every degree parameter d and every connected projective real locus with at
least two distinct real points at infinity, the packet constructs a moment
functional L whose projective Caratheodory number is 3d but whose affine
Caratheodory number is 3d+1. Therefore L has no positive flat extension.
The disconnected case was already supplied by Theorem 7.2.4 of the source, so
the two cases together prove the conjecture.

The new construction chooses a reduced totally real divisor in the degree-6d
linear system through two prescribed infinity points. A residue theorem gives
the unique linear dependence among its evaluation functionals. Its coefficients
alternate in sign around the connected real elliptic curve, placing the two
chosen infinity points in opposite positive representations. Generic choice of
the divisor makes the resulting functional interior, and the source's
two-decomposition lemma then shows that these are its only minimal projective
representations. Both meet infinity, while the source's finite-avoidance lemma
provides an affine representation with one additional atom.

## Files

- solution_packet.pdf: review-ready proof.
- main.tex: self-contained LaTeX source.
- source_paper.pdf: current arXiv source PDF.
- figures/open_conjecture_crop.png: complete source evidence.
- code/numerical_circuit_check.py: auxiliary d=1 circuit check.
- tmp/: compilation and rendering intermediates.

## Human review focus

The main checks are the circle-configuration lemma for the prescribed divisor,
the alternating sign in the residue relation, and the use of the source's
exactly-two-representations lemma. The numerical file is only a sanity check and
is not used in the proof.

