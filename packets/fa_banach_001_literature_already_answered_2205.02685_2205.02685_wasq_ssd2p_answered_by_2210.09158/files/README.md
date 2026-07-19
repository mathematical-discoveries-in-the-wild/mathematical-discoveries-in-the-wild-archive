# Literature Status: WASQ And SSD2P Questions For Lipschitz-Free Spaces

Status: literature already answered.

Source paper: arXiv:2205.02685, *The Lipschitz-free space over length space is
locally almost square but never almost square*.

Later paper: arXiv:2210.09158, *weakly almost square Lipschitz-free spaces*.

## Questions Identified

In the introduction of arXiv:2205.02685, after proving that `F(M)` is LASQ
when `M` is length and that no Lipschitz-free space is ASQ, the authors ask two
natural questions:

- whether `F(M)` is WASQ whenever `M` is a length metric space;
- whether there exists a Lipschitz-free space with the symmetric strong
  diameter 2 property, SSD2P.

## Resolution By Later Literature

arXiv:2210.09158 explicitly cites arXiv:2205.02685 as `HKO` and answers both
questions negatively.

For the WASQ question, Section 2 constructs a length metric space
`M = [0,1] x (0,1/2] union {(0,0),(1,0)}` with a graph-like metric. The paper
notes that `M` is length, hence `F(M)` is LASQ by arXiv:2205.02685, and then
Theorem `notWASQ` proves that `F(M)` is not WASQ. Thus length does not imply
WASQ for Lipschitz-free spaces.

For the SSD2P question, Section 4 proves Theorem `thm: F(M) never SSD2P`:
no Lipschitz-free space has SSD2P; in fact no Lipschitz-free space has
SSD(2d)P for any `0 < d <= 1`.

## Scope Notes

This packet claims no new theorem. It records that the two explicit
arXiv:2205.02685 questions are settled in later literature.

The later paper leaves a sharper characterization open: whether `F(M)` is WASQ
if and only if `M` is geodesic. It also proves a finite-support positive
result for geodesic spaces, but not the full geodesic characterization.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: locally rendered source paper arXiv:2205.02685, if build
  succeeds.
- `supporting_paper_2210.09158.pdf`: locally rendered later paper, if build
  succeeds.
