# Literature-Implied Partial Answer: Nonseparable Bourgain-Pisier L-infinity Spaces

Status: `literature_implied_answer (partial subcase)`

Run: `fa_banach_001`

Source/open-problem paper: arXiv:1709.09646, J. C. Ferrando, J. Kakol,
M. Lopez-Pellicer, and W. Sliwa, "On the separable quotient problem for
Banach spaces."

Supporting paper: arXiv:2604.11832, Kartik Patri, "Mazur's Separable Quotient
Problem for Nonseparable Bourgain-Pisier L-infinity Spaces."

## Claim Recorded

Problem `mazur` in arXiv:1709.09646 asks whether every infinite-dimensional
Banach space has an infinite-dimensional separable quotient.

The supporting paper gives an affirmative answer for a specific nonseparable
class:

> If `Y` is a nonseparable Bourgain-Pisier `L_infinity` space over an
> infinite-dimensional Banach space `X`, constructed by the Lopez-Abad method,
> then `Y` admits a quotient isomorphic to `c_0`.

This is an infinite-dimensional separable quotient, so it resolves the Mazur
problem on this class. It does not solve the global separable quotient problem.

## Identification

Patri proves a general criterion: if an `L_infinity` space `Y` contains a
subspace `X` such that `Y/X` is infinite-dimensional and has the Schur
property, then `Y` has a quotient isomorphic to `c_0`. Lopez-Abad's
Bourgain-Pisier construction produces an `L_infinity` space `Y` over `X` with
`Y/X` infinite-dimensional and Schur. Combining these statements gives a
`c_0` quotient for every nonseparable Bourgain-Pisier `L_infinity` space in
that construction.

The supporting author explicitly presents the result as a resolution of
Mazur's separable quotient problem for this class, but does not appear to be
answering arXiv:1709.09646 specifically. This packet therefore records an
agent-identified literature implication for a partial subcase.

## Evidence Locations

- arXiv:1709.09646, Introduction, Problem `mazur` in the source TeX lines
  161--163: "Does any infinite-dimensional Banach space have a separable
  (infinite dimensional) quotient?"
- arXiv:1709.09646, abstract: the classic separable quotient problem remains
  open and the paper surveys known positive classes.
- arXiv:2604.11832, Introduction, Theorem `general`: an `L_infinity` space
  with an infinite-dimensional Schur quotient has `c_0` as a quotient.
- arXiv:2604.11832, Introduction, Corollary `lopezabad`: every nonseparable
  Bourgain-Pisier `L_infinity` space over `X` constructed via the Lopez-Abad
  method admits `c_0` as a quotient.
- arXiv:2604.11832, Conclusion: the paper states that Mazur's problem is
  resolved for the Lopez-Abad nonseparable Bourgain-Pisier `L_infinity` class.

## Search Notes

Local run searches for `1709.09646`, `separable quotient`, `quotient problem`,
`strongly normal`, `Bourgain-Pisier`, `Lopez-Abad`, and `L_infinity` found no
prior packet for this subcase. Web searches on 2026-06-16 found arXiv:2604.11832
as a recent supporting paper and did not reveal a full resolution of Mazur's
general problem.

## Limitations

This is a literature-status packet, not a new proof. It covers only the
Lopez-Abad/nonseparable Bourgain-Pisier `L_infinity` class and the slightly
broader `L_infinity`-with-Schur-quotient criterion from the supporting paper.
It does not address arbitrary Banach spaces, the equivalent Schauder-basis or
quasi-complement formulations in arXiv:1709.09646, or the survey's separate
prompt about non-reflexive spaces not containing a copy of `ell_1`.

