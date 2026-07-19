# Upper Bound For Asymptotic Freeness Of `ell_nu^infty(mu)`

Status: partial result.

Source paper: Jarno Talponen, *Unconditional and bimonotone structures in high
density Banach spaces*, arXiv:1604.04408.

Target question: Section 6 asks, for infinite cardinals `nu < mu` and
`lambda < 2^nu`, for the least `kappa = kappa(lambda,nu,mu)` such that
`ell_nu^infty(mu)` is `(lambda,kappa)`-asymptotically free.

Result: for every `lambda < 2^nu` and every uncountable regular
`kappa > 2^nu`, the space `ell_nu^infty(mu)` is `(lambda,kappa)`-a.f. In
particular, whenever `2^nu < kappa <= mu`, this gives the same scale of upper
bound asked for in the source's final remarks.

Packet contents:

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: screenshot crop containing the final-remarks
  question.
- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build outputs.

Human review notes:

The proof is a support-counting refinement of Talponen's proof of Theorem 4.4.
If `Z` has density at most `lambda < 2^nu`, then the union of supports of a
dense set in `Z`, together with the support of the test vector `x`, has size
strictly below `2^nu`. The corresponding coordinate band in
`ell_nu^infty(mu)` has density at most `2^nu`; since this is below `kappa`,
the projected weakly convergent chain stabilizes inside that band, and the
same max-norm argument proves asymptotic freeness.

This does not compute the exact least `kappa(lambda,nu,mu)` and gives no lower
bound. The remaining open part is whether the threshold can be lowered below
`(2^nu)^+` in any cardinal regimes.
