# Partial Result: Block-Diagonal Formal-Identity Approximation

Status: `partial_result_likely_valid`.

Source: Anna Kaminska, Alexey I. Popov, Eugeniu Spinu, Adi Tcaciuc, and
Vladimir G. Troitsky, "Norm closed operator ideals in Lorentz sequence
spaces", arXiv:1108.6026.

## Question Addressed

After proving the `p=1` case, the source asks whether Corollary 6.7 remains
valid for `p>1`. Equivalently, for `1<p<infty`, if
`T: ell_p -> d_{w,p}` is strictly singular, must `T` be norm approximable by
operators of the form `jS`, where `j: ell_p -> d_{w,p}` is the formal identity?

## Result

Yes for the block-diagonal subcase. If the columns `T f_n` have pairwise
disjoint successive supports, then every strictly singular such operator
`T: ell_p -> d_{w,p}` lies in the norm closure of `{jS : S in L(ell_p)}`.

The full source question for arbitrary strictly singular operators remains
open here.

## Mechanism

The source already proves that strict singularity forces the column sequence
`(T f_n)` to be almost lengthwise bounded. For block-diagonal operators, keeping
the `N` largest coordinates in each column gives disjoint `N`-sparse columns.
Those columns define a bounded `ell_p -> ell_p` operator, while the discarded
tails define a small `ell_p -> d_{w,p}` operator by the disjoint upper
`p`-estimate in Lorentz sequence spaces.

## Verification

- Source question crop: `figures/open_question_crop.png`.
- Source PDF copied as `source_paper.pdf`.
- LaTeX packet compiled to `solution_packet.pdf`.
- A finite sanity check for the disjoint estimate is included in
  `code/check_disjoint_estimate.py`.
- Local indexes were searched for the arXiv id and relevant Lorentz/operator
  ideal keywords. A web search on 2026-07-03 found the source paper but no
  exact later answer to the `p>1` question.

