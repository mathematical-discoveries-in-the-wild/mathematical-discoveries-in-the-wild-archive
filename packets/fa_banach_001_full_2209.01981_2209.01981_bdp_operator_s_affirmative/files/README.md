# 2209.01981 - affirmative answer for the BDP status of the operator S

Status: candidate full solution, likely valid.

Source paper: Eduard Emelyanov and Svetlana Gorokhova, "Operators Affiliated to Banach Lattice Properties and the Enveloping Norms", arXiv:2209.01981.

## Question

In Example 3.1.1 the paper defines
\[
S:L^1[0,1]\to \ell^\infty,\qquad
S(f)=\left(\int_0^1 f(t) r_k^+(t)\,dt\right)_{k=1}^\infty,
\]
where \(r_k\) are the Rademacher functions. Immediately after the example, on page 15, the authors ask whether this operator is a \([BDP]\)-operator.

## Result

Yes. In fact, every bounded linear operator from \(L^1[0,1]\) into any Banach space is a \([GPP]\)-operator, hence a \([BDP]\)-operator. Therefore the specific operator \(S\) is \([BDP]\).

The proof is immediate from the definitions recalled in the source paper: all separable Banach spaces have the Gelfand-Phillips property, \(L^1[0,1]\) is separable, and a bounded operator maps relatively compact sets to relatively compact sets. Since relatively compact sets are relatively weakly compact, \([GPP]\) implies \([BDP]\).

## Verification Notes

The Rademacher sequence used in Example 3.1.1 is stated there to be almost limited. That is enough to obstruct the strong version \([s\text{-}GPP]\), but it is not a limited-set obstruction to \([GPP]\). Under Definition 1.2.2 in the source paper, \([GPP]\) and \([BDP]\) test limited subsets of the domain.

Bounded novelty check performed on 2026-06-16:

- Local indexes searched for `2209.01981`, `Operators Affiliated`, `Banach lattice properties`, and `BDP`.
- Web searched exact/near-exact phrases including `"We do not know whether or not the operator S" "BDP"`, `"Operators Affiliated to Banach Lattice Properties" "BDP" "S"`, and `"[BDP]-operator" "r_k^+"`.
- No separate later answer was found; the proof is recorded as a direct observation from the source definitions and the classical Bourgain-Diestel fact recalled by the source.

## Files

- `main.tex` - human-readable solution packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:2209.01981.
- `figures/open_problem_crop.png` - source crop of the open question on page 15.

