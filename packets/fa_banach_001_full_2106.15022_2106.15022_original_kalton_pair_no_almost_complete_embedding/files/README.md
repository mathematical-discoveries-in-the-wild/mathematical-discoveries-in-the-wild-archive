# Full candidate solution for the original Kalton operator-space pair

Status: `full_solution_likely_valid_pending_human_review`

Source: Bruno M. Braga, *Towards a theory of coarse geometry of operator
spaces*, arXiv:2106.15022, Theorem 1.8 and the paragraph immediately following
it (PDF page 4).

## Claimed answer

For the exact spaces in the source construction,

`X = (R cap C) direct-sum ker(tilde Q)` and `Y = Z(Q)`,

where `Q : L_infty[0,1] -> R cap C` is the standard complete quotient, `X`
does **not** almost completely isomorphically embed into `Y`.

The proof establishes the stronger general obstruction

`R cap C` does not almost completely embed into
`(direct sum_j MIN(E_j))_ell_1`

for any sequence of Banach spaces `(E_j)`.

![Theorem 1.8 and the source question](figures/open_problem_crop.png)

## Proof mechanism

1. Weakly compact subsets of a Banach-valued `ell_1` sum have uniformly small
   coordinate tails. This is proved by mapping disjoint bad blocks into scalar
   `ell_1` and using the Schur property.
2. A finite family of seminorms on an infinite Hilbert space can be
   simultaneously stabilized on any prescribed finite dimension. The packet
   gives a finite-net proof from Levy concentration.
3. For an orthonormal basis of an `n`-dimensional subspace, the corresponding
   row has norm `sqrt(n)` in `R cap C`, while its image in a minimal coordinate
   has norm exactly the scalar operator norm of that coordinate restriction.
4. A finite coordinate head is therefore uniformly bounded on a carefully
   chosen row. The scalar-small tail remains bounded at level `n` because
   `||A_n|| <= n||A||`.
5. In the original `Z(Q)`, every quotient-coordinate map from `R cap C` is
   compact. Passing to a completely isometric infinite-dimensional Hilbert
   subspace removes the quotient part and reduces to the minimal-sum theorem.

The final estimates give a bounded image norm against the required lower
bound `a sqrt(n)`.

## Verification report

Verdict: `likely valid`, pending human review.

- The tail lemma is self-contained and valid for arbitrary coordinate Banach
  spaces.
- The simultaneous stabilization argument is finite at every stage; the
  rapidly growing intermediate dimensions cause no problem in an
  infinite-dimensional Hilbert space.
- The minimal row identity is an exact consequence of the definition of
  `MIN(E)`.
- The exponent `n^(-3/2)` compensates exactly for the amplification loss `n`
  and the input row norm `sqrt(n)`.
- The compact quotient-coordinate reduction and the complete distortion `2`
  regrouping estimate were re-audited with slack in all constants.
- No computation is used.

Primary human-review focus: Lemma 2 (simultaneous stabilization), Lemma 3
(minimal row identity), and estimate (11) for the coordinate regrouping map.

## Search and novelty scope

On 2026-07-19, the four local lightweight indexes, the local sources of
arXiv:2106.15022 and arXiv:2211.11854, and bounded external primary-source
searches were checked using the exact question phrase, the arXiv id/title,
`R cap C`, `almost complete isomorphic embedding`, `minimal`, and `ell_1-sum`,
as well as the authors Braga and Oikhberg. No proof of the exact original pair
or the stronger minimal-sum obstruction was found.

Braga--Oikhberg, arXiv:2211.11854, gives a different-space existential
strengthening based on `MAX(L_1) -> MIN(ell_2)`. It addresses the motivation
of the source question but does not resolve the exact
`L_infty -> R cap C` pair.

The novelty search is bounded evidence, not a guarantee.

## Files

- `main.tex`: self-contained formal proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: source-statement evidence.
- `tmp/pdfs/`: PDF renderings used for visual QA.
- `history/`: the earlier compact quotient-coordinate partial packet, now
  absorbed into this proof.

## References

1. B. M. Braga, *Towards a theory of coarse geometry of operator spaces*,
   arXiv:2106.15022.
2. B. M. Braga and T. Oikhberg, *Coarse geometry of operator spaces and
   complete isomorphic embeddings into ell_1 and c_0-sums of operator
   spaces*, arXiv:2211.11854.
3. G. Pisier, *Introduction to Operator Space Theory*, Cambridge, 2003.
4. F. Albiac and N. J. Kalton, *Topics in Banach Space Theory*, 2nd ed., 2016.
5. M. Ledoux, *The Concentration of Measure Phenomenon*, AMS, 2001.
