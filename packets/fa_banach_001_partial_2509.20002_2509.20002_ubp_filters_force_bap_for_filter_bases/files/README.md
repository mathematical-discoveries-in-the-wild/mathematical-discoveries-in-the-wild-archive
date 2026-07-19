# Partial Result Packet: UBP Filters Force BAP for Filter Bases

Status: `partial_result_likely_valid`

Source paper: V. Kadets and M. Manskova, *Norms of partial sums operators for a basis with respect to a filter*, arXiv:2509.20002.

Target context: the source asks whether, for fixed filters, a given separable Banach space can possess an `F`-basis, and says this remains open for concrete filters such as the statistical-convergence filter. The source proves a negative result for slow analytic filters using Pisier's projection lower bound.

## Result

Let `F` be a Banach-UBP filter. If a Banach space `X` has an `F`-basis whose coordinate functionals are continuous, then `X` has the bounded approximation property.

Consequently, any separable Banach space without the approximation property has no such `F`-basis. In particular, if `F` is both analytic and a Banach-UBP filter, then no continuity hypothesis is needed: by de Rancourt--Kania--Swaczyna, every `F`-basis has continuous coordinate functionals.

## Proof Idea

The partial sum operators `S_n` of an `F`-basis are finite-rank operators and converge pointwise to the identity along `F`. Hence they are pointwise `F`-bounded. A Banach-UBP filter turns pointwise `F`-boundedness into an `F`-large uniform operator-norm bound. Choosing one uniformly bounded `S_n` from the intersection of the `F`-large approximation sets for a finite net of a compact set gives uniformly bounded finite-rank approximation on that compact set. This is exactly BAP.

## Scope

This is not a full answer to the source's fixed-filter problem. It excludes the Banach-UBP class of filters, and analytic Banach-UBP filters without any extra continuity assumption. It does not settle the statistical-convergence filter, since that filter is analytic but is not a Banach-UBP filter. It also does not close the source's endpoint gap for `(w*, ell_p^*, F)`-acceptable sequences.

## Novelty And Duplicate Check

Cheap run indexes were searched for `2509.20002`, the title, `F-basis`, `filter basis`, `bounded approximation property`, `BAP`, `UBP`, and `approximation property`. No prior packet or attempt for arXiv:2509.20002 appeared. Nearby entries concern filter-pi properties, ideal Schauder systems, and filter-basis minimality, but not this BAP obstruction.

External web searches on 2026-07-01 for exact and close phrases including `"filter basis" "bounded approximation property"`, `"F-basis" "bounded approximation property"`, and `"F-basis" "Uniform Boundedness Principle" filter Banach` did not reveal a direct prior statement of this obstruction.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local render of arXiv:2509.20002 from the source TeX.
- `supporting_paper_2001.01663.pdf`: local render of the filter-UBP source.
- `supporting_paper_2203.15123.pdf`: local render of the analytic-filter
  coordinate-continuity source.
- `figures/open_problem_crop.png`: rendered page containing the source open-problem passage.

## Human Review Focus

Check that the source's convention for `F`-basis gives finite-rank partial sums with the stated pointwise `F`-convergence, and that the De Bondt--Vernaeve Banach-UBP definition is exactly the normed-space `F`-boundedness used in the proof.
