# Banach-Saks quantitative equality: already answered negatively

Status: `literature_already_answered`

Original source: Hana Bendova, Ondrej F. K. Kalenda, and Jiri Spurny,
*Quantification of the Banach-Saks property*, arXiv:1406.0684, final question
in Section 6, page 17.

Supporting source: Zdenek Silber, *Quantification of Banach-Saks properties of
higher orders*, arXiv:2111.12773, Example 6.2 and the paragraph immediately
following it, pages 27-28.

## Identification

The original paper asks whether every bounded set `A` necessarily satisfies

```text
wbs(A) = 2 sm(A) = 2 wus(A).
```

Silber explicitly cites this question and says that Example 6.2 answers it
negatively.  In an equivalent signed Schreier norm, for
`A={e_n:n in N}`, the example proves (in the later paper's notation)

```text
sm_1(A)=1/2,   wus_1(A)=1,   wbs_0(A)=1.
```

The same paper states the notation bridge
`wbs=wbs_0`, `sm=sm_1`, and `wus=wus_1`.  Consequently

```text
wbs(A)=2 sm(A)=1,   but   2 wus(A)=2.
```

This is a complete negative answer, and the supporting author explicitly knew
that the construction answered the original question.  It is therefore a
literature answer, not a new result of this run.

## Scope

The original triple-equality question is fully answered negatively.  Silber
notes that a different equality involving the higher-order quantities
`wbs_xi`, `wbs_xi^s`, and `2 sm_{xi+1}` remains open; that is not the 2015
question recorded here.

## Evidence

The packet contains both arXiv PDFs.  The exact source question is on page 17
of `source_paper.pdf`.  The counterexample and explicit resolution sentence
are on pages 27-28 of `supporting_paper_2111.12773.pdf`.

Human review recommendation: `quick provenance verification only`.
