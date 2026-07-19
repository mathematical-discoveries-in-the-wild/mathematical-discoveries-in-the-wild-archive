# Literature-Implied Partial Answer: Operator-Norm Convexification Case

Status: `literature_implied_answer (partial subcase)`

Source paper: Javier Alejandro Chavez-Dominguez, *Uniform homeomorphisms
between spheres of unitarily invariant ideals*, arXiv:2305.07169.

Source question: In Section 4, immediately after Theorem
`thm-homeomorphism-convexification`, the author remarks that it is not known
whether the theorem's restriction `p >= 3` is needed, and suspects it is not.
The restriction comes from Jocić's Theorem 3.1; if the missing `1 < p < 3`
case of that inequality held, the theorem would follow in that range.

Supporting theorem: Aleksandrov and Peller, *Operator Hölder-Zygmund
functions*, arXiv:0907.3049, Section 10, Theorem `fcc`, proves operator-norm
Hölder estimates for quasicommutators
`f(A)R - R f(B)` of self-adjoint operators.

Identification: Taking `f(t)=sign(t)|t|^{1/p}` gives an operator-norm
estimate for the inverse Mazur map on self-adjoint block reductions:

```text
||f(A)R - Rf(B)|| <= C_p ||AR - RB||^{1/p} ||R||^{1-1/p}.
```

With `B` replaced by `-B`, this is exactly the anticommutator estimate needed
for the `E = c0` unitarily invariant ideal, i.e. compact operators with the
operator norm.  The forward uniform continuity of `G_p` for all `p >= 1` is
already proved in the source paper.  Hence the `p >= 3` restriction is not
needed in this operator-norm subcase.

Scope limitation: This does not prove the source theorem for arbitrary
unitarily invariant ideals when `1 < p < 3`; Aleksandrov--Peller's cited result
is an operator-norm theorem, not a symmetric-ideal norm theorem.

Files:

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: arXiv:2305.07169.
- `supporting_paper_0907.3049.pdf`: arXiv:0907.3049.
