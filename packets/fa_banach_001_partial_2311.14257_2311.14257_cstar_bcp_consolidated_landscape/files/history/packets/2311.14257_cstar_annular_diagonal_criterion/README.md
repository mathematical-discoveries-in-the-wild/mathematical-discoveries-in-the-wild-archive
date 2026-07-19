# C*-Annular Diagonal Criterion for BCP Failure

Status: `partial_criterion_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_cstar_annular_diagonal_criterion/`

## Result

This packet turns the quotient-level asymptotic diagonal criterion into a
C*-usable localizer theorem.

For a C*-quotient `q : B -> B/I`, if every countable lifted center family
admits multiplier contractions `a_k,c_k` such that:

- `a_k b_{pi(k)} c_k` nearly norms `q(b_{pi(k)})`;
- `a_k d c_k -> 0` along assigned fibers for every `d in I`;
- one global unit quotient class has prescribed local behavior;
- the prescribed local pieces escape the local center pieces;

then `B/I` fails BCP.

The packet also gives a concrete **phase-annular** corollary for unital
quotients, using right localizers `g_k` and a scalar gluing map. This is the
checklist form behind sigma-unital multiplier coronas.

## Why This Matters

The previous packet gave a Banach quotient criterion. This one is the C*-
language version: localizers, annuli, corners, ideal-vanishing, and gluing.
It is designed as a reusable theorem for future C*-classes rather than a new
proof written from scratch each time.

It recovers:

- sigma-unital multiplier coronas, via approximate-unit annuli;
- Hilbert-module block coronas, via compact block projections;
- ordinary `c0` product quotients with unital fibers, via disjoint central
  coordinate projections.

## Files

- `main.tex`: self-contained criterion packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a C*-usable criterion. The proof is a specialization of the
quotient diagonal estimate; the key review points are the localizer
hypotheses and the phase-annular corollary.
