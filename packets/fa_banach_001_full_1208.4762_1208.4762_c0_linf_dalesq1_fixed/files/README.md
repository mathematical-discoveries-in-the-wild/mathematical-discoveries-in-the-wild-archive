# Positive answer to Dales Question (II) for `c_0 \oplus \ell_\infty`

Status: `claimed_full_solution` for the specific subquestion
`E = c_0 \oplus \ell_\infty`.

Source paper: H. G. Dales, T. Kania, T. Kochanek, P. Koszmider, and
N. J. Laustsen, *Maximal left ideals of the Banach algebra of bounded
operators on a Banach space*, arXiv:1208.4762v3.

Open-problem location: source PDF pages 23--24, in Section 5, where the
authors state: "We do not know the answer to Question (II) for
`E = c_0 \oplus \ell_\infty`". Here Question (II) asks whether every
finitely-generated maximal left ideal of `B(E)` is fixed.

Result: every finitely-generated maximal left ideal of
`B(c_0 \oplus \ell_\infty)` is fixed.

Packet contents:

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1208.4762v3.
- `figures/open_problem_crop_page23.png` and
  `figures/open_problem_crop_page24.png`: source evidence for the open
  subquestion.

Proof mechanism:

1. If a finitely-generated maximal left ideal `L` were non-fixed, the source
   dichotomy gives `F(E) subset L`.
2. The finite-generator criterion then gives a bounded-below operator in `L`
   because `E = c_0 \oplus \ell_\infty` is isomorphic to all finite powers.
3. The strong dichotomy gives `E(E) subset L`, where `E(E)` denotes the
   inessential operators.
4. For `E=c_0 \oplus \ell_\infty`, any maximal left ideal containing a
   bounded-below operator and all inessential operators must contain the
   source paper's ideal `K_1`.
5. Source Proposition 7.8 proves that this `K_1` is not contained in any
   finitely-generated maximal left ideal, contradiction.

Novelty / literature check:

- Local cheap indexes checked: `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv`; no hit for arXiv
  `1208.4762`, DalesQ1, or the `c_0 \oplus \ell_\infty` maximal-left-ideal
  subquestion.
- Web searches on 2026-06-14 for exact phrases around DalesQ1,
  `c_0 \oplus \ell_\infty`, `C[0,1]`, and finitely-generated maximal left
  ideals found the source paper but no later exact answer.
- Novelty confidence is moderate rather than high: the proof uses the source
  paper heavily, especially Proposition 7.8. The additional step is the
  bounded-below-operator-to-`K_1` containment argument for `c_0 \oplus
  \ell_\infty`.

Scope limitation: this packet does not settle the remaining `C(K)` cases
highlighted in the source paper, such as `K=[0,1]` or ordinal intervals
`[0,\alpha]` with `\alpha \ge \omega^\omega`.

Human-review recommendation: check carefully that the inessential-operator
containment used in Lemma 2 applies to all off-diagonal blocks for
`c_0 \oplus \ell_\infty`, and that the appeal to source Proposition 7.8 is
legitimate in combination with the bounded-below operator forced by finite
generation.
