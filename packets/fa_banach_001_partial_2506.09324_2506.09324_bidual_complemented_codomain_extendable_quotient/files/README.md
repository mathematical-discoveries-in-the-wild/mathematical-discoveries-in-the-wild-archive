# Partial solution packet: bidual-complemented codomains and the extendable quotient model

## Source

- Paper: Anil Kumar Karn and Arindam Mandal, *Position of `L(X, Y)` in `Lip_0(X, Y)`*
- arXiv: `2506.09324`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `partial_result_likely_valid`
- Target questions:
  - Question 1.1 asks whether `L(X,Y)` is complemented in `Lip_0(X,Y)`.
  - Question 1.2 asks for an operator-space description of `Lip_0(X,Y)/L(X,Y)`.
- Packet claim:
  1. If `Y` is isometrically complemented in a dual Banach space, in particular if the canonical copy of `Y` is complemented in `Y**`, then `L(X,Y)` is complemented in `Lip_0(X,Y)`.
  2. For arbitrary `Y`, the quotient `Lip_0(X,Y)/L(X,Y)` is linearly isometric to the space of extendable operators on `ker(beta_X^Y)`, equipped with the extension norm. If `Y` is injective this reduces to the source paper's usual-norm identification with `L(ker(beta_X^Y),Y)`.

## Relation to the source paper

The source paper proves Question 1.1 when `Y` is itself a dual space and proves the Question 1.2 quotient description with the usual operator norm when `Y` is injective. This packet gives a complementary partial extension:

- The projection theorem passes through any bounded projection from a dual host space back onto `Y`.
- The quotient theorem removes injectivity by replacing all operators on `ker(beta_X^Y)` with the range of the restriction map and its quotient/extension norm.

This is not a full solution of Question 1.1 for arbitrary codomains.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: source page containing Question 1.1.
- `figures/quotient_question_crop.png`: source page containing Question 1.2 and the injective-codomain quotient statement.
- `tmp/`: LaTeX build output and source-page renders.

## Verification notes

The first proof uses Theorem 2.2 of the source paper with codomain equal to a dual host `Z`; composing the resulting norm-one projection with a projection `Z -> Y` gives the desired projection onto `L(X,Y)`.

The second proof is the standard first-isomorphism theorem applied to the source paper's isometry
`Lip_0(X,Y) ~= L(F_Y(X),Y)` and the restriction map to `D=ker(beta_X^Y)`. The kernel is exactly `L(X,Y)` by Lemma 4.4 of the source paper. The quotient norm is therefore exactly the extension norm.

Cheap-index searches found no exact previous packet for `2506.09324`. Bounded web searches for the paper title, `L(X,Y)` in `Lip_0(X,Y)`, complementedness, dual codomains, and quotient keywords did not surface a later direct answer.
