# Literature-Already-Answered Packet: Separation Growth of `ell_p`, `p>2`

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is an exact later-literature answer to Question 83 from
Naor's *Extension, separation and isomorphic reverse isoperimetry*, not a new
proof from this run.

## Source Problem

- Assaf Naor, *Extension, separation and isomorphic reverse isoperimetry*,
  arXiv:2112.11523; Memoirs of the European Mathematical Society 11, 2024.
- Local PDF: `source_paper.pdf`.
- Evidence image:
  - `figures/open_question_crop.png` (page 44, Question 83).

Question 83 asks whether, for every fixed `p in (2,infty)`,

```text
SEP^n(ell_p) / log n -> 0,
```

and, more ambitiously, whether

```text
SEP^n(ell_p) <= C_p sqrt(log n).
```

Here `SEP^n(M)` is the supremum of the separation moduli of subsets of `M`
with cardinality at most `n`.

## Supporting Literature

- Assaf Naor, Kevin Ren, *Euclidean embedding, randomized clustering, and
  Lipschitz extension for finite and doubling subsets of `L_p` when `p>2`*,
  arXiv:2502.10543.
- Local PDF: `supporting_paper_2502.10543.pdf`.
- Evidence images:
  - `figures/supporting_answer_crop.png` (page 11, explicit citation to
    `[80, Question 83]` and Theorem 1.10).
  - `figures/supporting_references_crop.png` (page 59, bibliography entries
    `[77]` and `[80]`, identifying the 2017 SODA question and Naor 2024).

## Literature Status

The ambitious `sqrt(log n)` form is now known. Naor--Ren explicitly say that
the question was reiterated as `[80, Question 83]`, where `[80]` is Naor's
2024 EMS monograph. Their Theorem 1.10 proves that for every `2<p<infty`,

```text
SEP^n(L_p) asymp_p sqrt(log n),
```

more precisely `sqrt(log n) <= C SEP^n(L_p) <= C_p p^2 sqrt(log n)`.

Since `ell_p` embeds isometrically into an `L_p` space, every `n`-point subset
of `ell_p` is also an `n`-point subset of `L_p`. Therefore

```text
SEP^n(ell_p) <= SEP^n(L_p) <= C_p sqrt(log n),
```

which answers both parts of Question 83 affirmatively for each fixed `p>2`.

## Proof Idea

The source question was difficult because finite subsets of `ell_p`, `p>2`,
had no known dimension-reduction mechanism comparable to Johnson--Lindenstrauss
in Hilbert space. Naor--Ren bypass this by proving a direct randomized
partition theorem for finite subsets of the whole `L_p` space. Once such
partitions exist for every finite subset of `L_p` with separation loss
`O_p(sqrt(log n))`, the `ell_p` case follows by viewing `ell_p` as an
isometric subspace of `L_p`.

## Limitations

- This is a literature-status packet, not an original proof from this run.
- It answers Question 83 of arXiv:2112.11523 for fixed `p>2`.
- It does not settle the same supporting paper's remaining range where `p`
  is allowed to grow with `n`, specifically
  `sqrt[4](log n) lesssim p = o(log n)`.
- It does not address the other isomorphic reverse-isoperimetry conjectures
  or shape-optimization questions in arXiv:2112.11523.

## Files

- `README.md`: this packet summary.
- `main.tex`: literature-status packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original source paper.
- `supporting_paper_2502.10543.pdf`: later paper answering the question.
- `figures/open_question_crop.png`: source Question 83 crop.
- `figures/supporting_answer_crop.png`: supporting theorem and answer crop.
- `figures/supporting_references_crop.png`: supporting bibliography crop.
- `tmp/`: LaTeX build intermediates.

## Verification And Search Notes

Before packaging, the run lightweight indexes were searched for `2112.11523`,
the title phrase, `isomorphic reverse isoperimetry`, `separation growth`,
`SEP^n`, and nearby core terms. No existing exact packet or attempt was found.
The only nearby hit was the distinct arXiv:1506.04398 / arXiv:2502.10543
packet on Lipschitz extension upper bounds.

The source and supporting arXiv PDFs and TeX sources were checked directly.
The supporting paper explicitly identifies the source as `[80]` and says the
sharp `sqrt(log n)` question was asked in `[77,80]`, with `[80, Question 83]`
the exact source question packaged here.

## Human Review Recommendation

Treat Question 83 of arXiv:2112.11523 as already answered affirmatively, in
its fixed-`p>2` and `sqrt(log n)` form, by arXiv:2502.10543. Keep the other
conjectures and reverse-isoperimetry questions in arXiv:2112.11523 separate.
