# One-point cone rigidification for finite preserved-extreme 2-connected spaces

Status: `partial_result_likely_valid`

Supersession note: this packet is superseded by
`solutions/partial/2402.08266_finite_metric_one_point_rigidification/`, which
proves one-point rigidification for every finite metric space.  The cone
2-connected theorem here remains a simpler sufficient criterion and a useful
route to the stronger finite result.

## Source

- arXiv:2402.08266
- Marek Cuth, Michal Doucha, and Tamas Titkos, *Isometries of Lipschitz-free Banach spaces*
- Source target: Question 3 in Section 8.2, asking whether every metric space embeds isometrically into a Lipschitz-free rigid space with only one additional point.

## Result

Let \(M\) be a finite metric space whose preserved-extreme graph has vertex set
all of \(M\) and is 2-connected.  If \(R>\operatorname{diam} M\), add one new
point \(p\) with \(d(p,x)=R\) for every \(x\in M\).  The resulting one-point
extension \(M_R=M\cup\{p\}\) is Lipschitz-free rigid.

The proof observes that the preserved-extreme graph of \(M_R\) is exactly the
cone over the preserved-extreme graph of \(M\).  A cone over a 2-connected graph
is 3-connected, so the source paper's 3-connected preserved-extreme graph
criterion applies.

## Scope

This is a genuine one-point positive subcase of Question 3, not a full answer.
It covers finite spaces with 2-connected preserved-extreme graph, including
finite 2-connected graph metrics.  It does not address finite spaces whose
preserved-extreme graph has cut vertices, infinite spaces, or the Euclidean
\(\mathbb R^d\) rigidity question.

## Files

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: locally compiled source paper from the arXiv TeX source.
- `figures/open_problem_crop.png`: crop of the source paper's problem list.

## Novelty Check

Cheap run indexes had no exact `2402.08266` entry before this packet.  Web
searches for `"Lipschitz-free rigid" "one additional point"`, `"Is R^d"
"Lipschitz-free rigid"`, and the paper title returned the source paper but no
later settlement.  Local corpus search found only the source paper and later
papers citing it for unrelated extreme-point material.

Human review should check the finite preserved-extreme graph identification and
the use of the source Theorem 4.9.
