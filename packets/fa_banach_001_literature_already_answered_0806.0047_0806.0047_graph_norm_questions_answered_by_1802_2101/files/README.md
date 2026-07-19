# Hatami Graph-Norm Questions Answered By arXiv:1802.05007 and arXiv:2101.12145

Run: `fa_banach_001`

Status: `literature_already_answered (two closing questions)`.

## Source Problem

- Hamed Hatami, *Graph norms and Sidorenko's conjecture*,
  arXiv:0806.0047; Israel J. Math. 175 (2010), 125--150.
- Local PDF: `source_paper.pdf`.

In the concluding remarks, Hatami asks several graph-norm questions. This
packet records later literature answers to two of them:

- Is there any edge-transitive bipartite graph that is not weakly Holder?
- Prove or disprove that hypercubes are Holder.

The same concluding section also asks other questions, which are outside the
scope of this packet.

## Terminology Match

Hatami defines Holder and weakly Holder bipartite graphs in Section 2.2 and
then proves in Theorem 2.9 that:

- `H` is Holder iff `||.||_H` is always a seminorm.
- `H` is weakly Holder iff `||.||_{r(H)}` is always a norm.

The later graph-limit literature refers to the corresponding properties as
norming and weakly norming. Thus later papers on weakly norming/norming
graphs directly address Hatami's questions.

## Supporting Answer 1: Edge-Transitive Weakly Holder Question

- Roman Kral, Ta Sheng Noel Sandeep, Jan Volec, and Fan Wei,
  *The step Sidorenko property and non-norming edge-transitive graphs*,
  arXiv:1802.05007; J. Combin. Theory Ser. A 162 (2019), 34--54.
- Local PDF: `supporting_paper_1802.05007.pdf`.

The abstract and introduction explicitly state that the paper shows the
existence of a bipartite edge-transitive graph that is not weakly norming, and
that this answers a question of Hatami. More concretely, the paper proves that
most toroidal grids, including edge-transitive graphs of the form
`C_n square C_n` outside the listed exceptional cases, are not weakly norming.

Therefore Hatami's question "Is there any edge transitive bipartite graph that
is not weakly Holder?" has a positive existence answer: yes, such graphs exist.
Equivalently, the universal assertion that all edge-transitive bipartite graphs
are weakly Holder is false.

## Supporting Answer 2: Hypercubes Holder Question

- Joonkyung Lee and Alexander Sidorenko,
  *On graph norms for complex-valued functions*, arXiv:2101.12145;
  J. London Math. Soc. 106 (2022), 1507--1538.
- Local PDF: `supporting_paper_2101.12145.pdf`.

The paper says that Hatami proposed six open problems about graph norms and
that it answers the last remaining one: whether the hypercubes, already proven
weakly norming by Hatami, are norming. Its Theorem 1.4 states that the
`d`-dimensional hypercube `Q_d` is not norming whenever `d>2`.

This gives a negative answer to Hatami's question "Prove or disprove that
hypercubes are Holder" for all hypercubes of dimension greater than two.

## Scope Limitations

This is an already-known literature status packet, not a new proof. It does
not resolve the general Sidorenko conjecture. It also does not settle Hatami's
remaining concluding questions about:

- the hypergraph generalization of the graph-norm framework,
- whether `K_2 square C_6` is weakly Holder,
- whether `K_{5,5}` with a Hamiltonian cycle removed is weakly Holder,
- determining moduli of smoothness and convexity of `r(H)` when it is a norm.

## Search Notes

The lightweight run indexes were searched for `0806.0047`, `Graph norms and
Sidorenko`, `Sidorenko`, `graph norm`, `weakly norming`, `norming`,
`Holder`, and `weakly Holder`. No existing exact packet for these two Hatami
questions was found at reservation time.

The decisive supporting papers are primary arXiv sources. arXiv:1802.05007
explicitly says it answers Hatami's edge-transitive weakly norming question,
and arXiv:2101.12145 explicitly says it resolves Hatami's remaining hypercube
norming question.

## Human Review Recommendation

Archive the extracted `0806.0047` target as `literature_already_answered` for
these two graph-norm questions. Keep the unrelated Sidorenko and graph-specific
questions available for future targets.
