# Counterexample Packet: Unbounded Lemma 4.2 Fails for Hairpin Curves

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `2012.12984`
- source paper: Scott Zimmerman, *Singular integrals on $C_{w^*}^{1,\alpha}$ regular curves in Banach duals*
- target passage: PDF page 14, Remark 4.3 and the following question asking whether Lemma 4.2 holds on an unbounded interval.

## Claim

Lemma 4.2 does not extend to unbounded parameter intervals under the natural
regularity hypotheses. There is a `C^{1,1}` unit-speed curve
`\gamma:[0,\infty)\to\mathbb R^2` whose image is 1-Ahlfors-David regular, but
for balls containing the first `N` hairpins, every interval satisfying the
source's condition (4.3) captures only uniformly bounded `H^1` length while
`H^1(B\cap\Gamma)\simeq N`.

Thus no uniform positive `theta` can work in the unbounded-domain version of
Lemma 4.2.

## Construction

The curve is a rounded infinite hairpin ladder in the Hilbert plane. Each block
contains two unit horizontal strands separated by a tiny `epsilon`, followed by
a vertical connector to the next block. The arclength parametrization is
`C^{1,1}` after uniform circular smoothing.

Condition (4.3) implies a `1/2` lower Lipschitz bound on any admissible
parameter interval. But within every hairpin there are two points separated by
distance `epsilon` in the plane and order-one arclength along the parameter.
An admissible interval therefore cannot contain a full hairpin, so its length
is uniformly bounded.

## Files

- `main.tex`: full counterexample packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:2012.12984
- `figures/open_problem_crop.png`: crop of the source question
- `code/make_open_problem_crop.py`: reproducible crop script

## Novelty Check

The run indexes were searched for `2012.12984`, the paper title, `Singular
integrals`, `C_{w^*}^{1,\alpha}`, `unbounded interval`, and `Lemma 4.2`.
No prior packet for this target was found. A bounded exact-phrase web search
on 2026-06-23 found the source paper but no later answer.

Human review should focus on the interval-length bound: once (4.3) is seen to
force a lower Lipschitz estimate, the hairpin obstruction is immediate.
