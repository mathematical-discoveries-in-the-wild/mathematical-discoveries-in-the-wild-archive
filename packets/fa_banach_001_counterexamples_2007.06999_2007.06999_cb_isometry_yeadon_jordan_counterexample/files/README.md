# Counterexample packet: cb isometry with non-cb Yeadon Jordan part

Status: candidate counterexample likely valid; needs human review of the
operator-space direct-sum bookkeeping, but the mechanism is explicit and uses
only the source paper's own transpose cb-norm fact.

Source paper: Cedric Arhancet, "A characterization of completely bounded
normal Jordan *-homomorphisms on von Neumann algebras", arXiv:2007.06999.

Targeted open problem: Section 5, Conjecture 5.1 and the Fundamental
Conjecture 5.2.  The source asks whether a completely bounded isometry
`T:L^p(M)->L^p(N)` for finite `M`, semifinite `N`, and `p != 2` must split as
a complete-isometry part plus an `n`-minimal part; equivalently, it asks
whether complete boundedness of an isometry `T=wbJ` forces the Yeadon Jordan
homomorphism `J` to be completely bounded.

Result: for every `1 <= p < infinity`, `p != 2`, the packet constructs finite
von Neumann algebras

`M = product_{m>=2} M_m` and `N = product_{m>=2} (M_m direct-sum M_m)`

with finite faithful normal traces, and a positive isometry

`T((x_m)) = ((c_m x_m, d_m x_m^T))_m`

where `d_m=m^(-|1-2/p|)` and `c_m=(1-d_m^p)^(1/p)`.  The transpose weights
make `T` completely bounded with cb norm at most `2^(1/p)`, while the Yeadon
Jordan homomorphism `J((x_m))=((x_m,x_m^T))_m` is not completely bounded.
Moreover `T` is not a complete isometry on any matrix summand `M_m` with
`m>=2`, so the structural decomposition in Conjecture 5.1 cannot exist.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2007.06999.
- `source_paper.tex`: local parsed source TeX used to verify labels/lines.
- `figures/open_problem_crop.png`: crop of Section 5 and Conjectures 5.1--5.2.
- `code/make_open_problem_crop.py`: reproduces the source crop.
- `code/check_block_estimates.py`: numerical sanity check of the scalar
  coefficient identities and inequalities; not used as proof.

Novelty check: cheap run indexes were searched for `2007.06999`, the title,
`completely bounded isometries`, `Yeadon factorization`, `normal Jordan`, and
`n-minimal`; no exact duplicate or later answer packet was found.  Web searches
on 2026-07-18 for exact phrases around Conjectures 5.1--5.2 and the Yeadon
factorization found the source and related citations, but no later resolution.

Human-review focus: verify the standard identification of matrix-level
`L^p` direct sums used in the cb estimate.  The counterexample deliberately
uses positive scalar weights so that the Yeadon support condition
`s(b)=J(1)` is satisfied.
