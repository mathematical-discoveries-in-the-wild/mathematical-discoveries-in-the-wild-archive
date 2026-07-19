# Literature Status: Weak-Star Diameter Two Properties In Lipschitz Spaces

Status: `literature_already_answered`

## Source Question

- Source paper: Rainis Haller, Eve Oja, and Mart Poldvere, "Diameter two properties for spaces of Lipschitz functions", arXiv:2205.13287.
- Location: after the theorem separating SSD2P, SD2P, and D2P for Lipschitz function spaces.
- Question selected for this packet: for spaces of Lipschitz functions, do the non-weak-star diameter two properties coincide with their weak-star versions? More concretely, does the `w*`-SSD2P imply the slice-D2P for `Lip_0(M)`?

## Supporting Answer

- Supporting paper: Rainis Haller, Jaan Kristjan Kaasik, and Andre Ostrak, "Separating diameter two properties from their weak-star counterparts in spaces of Lipschitz functions", arXiv:2404.11430.
- Location: introduction and Section 3, especially Example 3.6 in the parsed arXiv source.
- Answer: no. The supporting paper constructs a metric space `M` such that `Lip_0(M)` has the `w*`-SSD2P but does not have the slice-D2P.

## Evidence

The source paper records that, for Lipschitz function spaces, it remained open whether the non-weak-star diameter two properties coincide with their weak-star analogues, and even whether `w*`-SSD2P implies slice-D2P.

The supporting paper explicitly returns to the Haller--Oja--Poldvere setting and states that it remained open whether any diameter two property coincides with its weak-star counterpart in spaces of Lipschitz functions. It then gives a metric space `M = {a_1,a_2,b_k,c_k : k in N}`. The paper verifies that `M` has SLTP, hence `Lip_0(M)` has the `w*`-SSD2P, and constructs a slice of the unit ball of `Lip_0(M)` whose diameter is strictly smaller than `2`. Therefore `Lip_0(M)` lacks the slice-D2P.

This gives a negative answer to the selected arXiv:2205.13287 question.

## Scope

This packet records a later literature answer, not a new proof from this run.

It should not be used to close the separate arXiv:2205.13287 question asking whether there is a metric space `M` such that `Lip_0(M)` has the slice-D2P but not the D2P. The supporting paper still lists the distinction between (`w*`-)slice-D2P and (`w*`-)D2P in Lipschitz function spaces as an open question.

## Files

- `source_paper_2205.13287.pdf`: source paper.
- `supporting_paper_2404.11430.pdf`: supporting later paper.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

## Review Recommendation

Treat the weak-star-counterpart question from arXiv:2205.13287 as answered negatively by arXiv:2404.11430, specifically through the example with `w*`-SSD2P but not slice-D2P. Keep the slice-D2P versus D2P question open.
