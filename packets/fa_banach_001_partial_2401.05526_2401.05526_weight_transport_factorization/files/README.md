# Same-weight transport for weighted factorization

Status: partial_result_likely_valid

Source paper: Tomasz Kiwerski and Jakub Tomaszewski, "Arithmetic,
interpolation and factorization of amalgams", arXiv:2401.05526.

Source prompt: Section 8.b, "Factorization of generalized weighted spaces",
asks for abstract analogues of weighted factorization results for generalized
weighted spaces X_w.

## Result

Let w be a positive weight on (0,infty), let W(t)=int_0^t w(s) ds, assume
W(t)<infty for each t and W(infty)=infty, and write tau=W^{-1}. For any
Banach ideal space X define the transported weighted copy

    X^[w] = { f : f o tau in X },   ||f||_{X^[w]} = ||f o tau||_X.

When X is rearrangement invariant, this is isometric to the generalized
weighted space X_w used in the source paper. For Banach ideal spaces X and Y,
the map T_w f = f o tau gives isometric identifications

    M(X^[w],Y^[w]) = M(X,Y)^[w]

and

    X^[w] odot M(X^[w],Y^[w])
      is isometric to
    X odot M(X,Y).

Consequently,

    Y^[w] = X^[w] odot M(X^[w],Y^[w])

if and only if

    Y = X odot M(X,Y),

with the same product constants. Thus every unweighted factorization theorem
from the source paper has an immediate common-weight transported analogue
whenever the same W-change of variables is the intended weighting.

## Full-push reduction

The Cesaro side does not transport to the ordinary Cesaro construction unless
W is linear. Under T_w, the space C(X^[w]) is carried isometrically onto the
optimal domain C_tau X of the weighted Hardy operator

    H_tau g(s) = tau(s)^{-1} int_[0,s] |g(r)| d tau(r).

Consequently,

    C(X^[w]) = X^[w] odot M(X^[w], C(X^[w]))

is equivalent to

    C_tau X = X odot M(X, C_tau X).

For w=1 this is exactly the unweighted Section 8.a problem
C X = X odot M(X,C X), so a blanket full answer to the abstract weighted-Cesaro
problem would already solve that earlier open problem.

## Scope limits

This is not a full solution to all of Section 8.b. It covers the same-weight
transported version of generalized weighted spaces. It does not solve:

- different weights on the two factors;
- multiplier/factorization questions after an additional symmetrization step,
  such as abstract Lorentz spaces Lambda_{X,w};
- the general factorization of the weighted Hardy optimal domain C_tau X
  through X;
- the harder Section 8.e problem of identifying M(Ces_M,Ces_N) for Orlicz
  function spaces.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of the source prompt on page 76.
