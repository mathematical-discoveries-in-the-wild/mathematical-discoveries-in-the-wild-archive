# Verification notes

## Admissibility

- \(f(a)=(a-1)^2\) on \([0,\infty)\), extended by \(+\infty\) on
  \(( -\infty,0)\), is the source's Tsallis-2 entropy. It is proper, convex,
  lower semicontinuous, and has unique minimizer \(1\).
- \(K(x,y)=e^{-(x-y)^2/2}\) is the source's Gaussian radial kernel with
  bandwidth one. It is bounded, characteristic, smooth, and
  \(K(x,\cdot)\in C_0(\mathbb R)\).
- \(\delta_x\in\mathcal P_2(\mathbb R)\) for every \(x\).

## Scalar minimization

For \(\nu=\delta_0\), finite divergence forces the competitor measure to be
\(a\delta_0\), \(a\ge0\), because the Tsallis-2 recession constant is
infinite. With \(c=e^{-x^2/2}\),
\[
 D_{f,\delta_0}^{\lambda}(\delta_x)
 =\min_{a\ge0}\left[(a-1)^2+
   \frac{1+a^2-2ac}{2\lambda}\right].
\]
The unconstrained minimizer
\[
 a_\lambda(x)=\frac{2\lambda+c}{2\lambda+1}
\]
is positive, so it is also the constrained minimizer. Substitution gives
\[
 H_\lambda(x)=
 \frac{(1-c)(c+4\lambda+1)}{2\lambda(1+2\lambda)}.
\]

## Curvature calculation

Rewrite
\[
 H_\lambda(x)=
 \frac{1-e^{-x^2}}{2\lambda(1+2\lambda)}
 +\frac{2(1-e^{-x^2/2})}{1+2\lambda}.
\]
For \(g_a(x)=1-e^{-ax^2}\),
\[
 g_a''(x)=2a e^{-ax^2}(1-2ax^2).
\]
Thus \(g_1''(1)=-2/e\) and \(g_{1/2}''(1)=0\), whence
\[
 H_\lambda''(1)=-\frac{1}{e\lambda(1+2\lambda)}.
\]

The same identities were checked symbolically with SymPy. It returned
`value_check = 0` after subtracting the minimized quadratic from the displayed
closed form, and
`Hxx_at_1 = -exp(-1)/(lam*(2*lam + 1))`.

## Generalized-geodesic check

For endpoints \(\delta_{1-h}\) and \(\delta_{1+h}\), every admissible
three-plan in the definition of a generalized geodesic has its second and
third coordinates fixed. Hence every such generalized geodesic is
\[
 t\longmapsto\delta_{1+(2t-1)h},
 \qquad W_{\boldsymbol\alpha}^2=4h^2.
\]
If \(E_\lambda\) is \(\kappa_\lambda\)-convex along generalized geodesics,
the midpoint inequality yields
\[
 H_\lambda(1+h)+H_\lambda(1-h)-2H_\lambda(1)
 \ge \kappa_\lambda h^2.
\]
Divide by \(h^2\) and let \(h\downarrow0\) to obtain
\(\kappa_\lambda\le H_\lambda''(1)\).

## Boundary of the claim

The calculation disproves a uniform *global* lower bound on generalized-
geodesic convexity moduli. It does not disprove convergence of the particular
flows, nor local convexity estimates along selected trajectories.
