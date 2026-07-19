# 2101.01994 -- uniform algebras and the complex Mazur-Ulam property

Status: literature_implied_answer (partial subcase)

## Source question

Original paper: Osamu Hatori, Shiho Oi, Rumi Shindo Togashi,
*Tingley's problems on uniform algebras*, arXiv:2101.01994.

In Section 8, the authors write that they conjecture a uniform algebra satisfies
the Mazur-Ulam property.  In the same remark they explain that their Theorem 2.1
settles only the case where the target is again a uniform algebra; the full
Mazur-Ulam-property formulation allows the target to be an arbitrary Banach
space.

## Supporting literature

Supporting paper: Osamu Hatori, *The Mazur-Ulam property for uniform algebras*,
arXiv:2107.01515.

The later paper cites the original Hatori--Oi--Shindo Togashi uniform-algebra
Tingley theorem and proves Theorem 4.2: every uniform algebra satisfies the
complex Mazur-Ulam property.  This answers the natural complex-target reading
of the source conjecture: every surjective isometry from the unit sphere of a
uniform algebra onto the unit sphere of an arbitrary complex Banach space has a
real-linear homogeneous extension.

## Scope limitation

This is not a full answer to the real-target Mazur-Ulam property.  The
supporting paper explicitly says in its final remarks that it merely proves the
complex Mazur-Ulam property and still conjectures the full Mazur-Ulam property
for uniform algebras, more generally for closed subalgebras of `C_0(Y,C)`.

The remaining gap is not just wording.  The later proof's real-space criterion
requires, for each real face functional `p`, the identity
`M_{p,alpha}={a in S: p(a)=alpha}` for all real `alpha`.  For the real Banach
space underlying a complex uniform algebra, the natural face functionals are
`p=Re(gamma delta_x)`.  If `f(x)=i` and `p=Re delta_x`, then `p(f)=0`, but `f`
is at distance at least `sqrt(2)` from the face `f(x)=1`, so it is not in
`M_{p,0}`.  Thus the same criterion does not automatically settle the full
real-target conjecture.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2101.01994.
- `supporting_paper_2107.01515.pdf`: arXiv:2107.01515.
- `source_2101.01994.tex.gz`, `supporting_source_2107.01515.tex.gz`: local arXiv source archives.

