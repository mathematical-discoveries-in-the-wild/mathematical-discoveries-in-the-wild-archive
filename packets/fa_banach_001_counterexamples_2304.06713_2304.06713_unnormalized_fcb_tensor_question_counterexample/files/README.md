# Counterexample packet: unnormalised FCB tensor-network question

Status: candidate counterexample, likely valid, narrow scope.

Source: Francisco Escudero Gutierrez, *Influences of Fourier Completely Bounded Polynomials and Classical Simulation of Quantum Algorithms*, arXiv:2304.06713.

## Result

Question 4.5 in the source asks, literally, whether for every polynomial `p` of degree at most `d` there is a Boolean-behavior tuple `(u,v,A)` whose degree-`d` correlations recover each Fourier coefficient divided by `poly(d, MaxInf[p])`.

Read without a normalization hypothesis on `p`, this is false.  Add an arbitrary constant `M` to a fixed nonconstant linear polynomial.  The maximum influence is unchanged, but the empty-parity Fourier coefficient becomes `M`.  Every correlation of a tuple of unit vectors and contractions has absolute value at most `1`, so the required empty-parity correlation is impossible once `M` is larger than the proposed denominator.

## Scope

This packet does **not** refute the normalized FCB influence conjecture or the Aaronson--Ambainis conjecture.  It only records that the printed auxiliary tensor-network Question 4.5 needs a normalization such as `||p||_{fcb,d} <= 1`, or some denominator that also controls the constant Fourier coefficient.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: locally rendered source paper from the arXiv source bundle.
- `figures/open_problem_crop.png`: crop of Question 4.5 from the source paper.
