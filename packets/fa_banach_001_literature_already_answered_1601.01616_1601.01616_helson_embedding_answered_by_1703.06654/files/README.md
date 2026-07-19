# Helson and the \(0<p<2\) Embedding Problem Answered by Harper

Status: `literature_already_answered` for Helson's problem, and
`literature_already_answered (partial subrange)` for the embedding problem.

Source/open-problem paper:

- arXiv:1601.01616, Eero Saksman and Kristian Seip, "Some open questions in analysis for Dirichlet series".
- Exact source locations:
  - Problem `helson` in Section 3, source lines 265-267.
  - Problem `embedding` in Section 2, source lines 174-181.

Supporting answer:

- arXiv:1703.06654, Adam J. Harper, "Moments of random multiplicative functions, I: Low moments, better than squareroot cancellation, and critical multiplicative chaos".
- Exact answer locations:
  - Theorem 1 and the sentence following Theorem 2 in the introduction, source lines 148-158.
  - The paragraph immediately after Theorem 2, source lines 160-162, for the embedding problem subrange \(0<p<2\).

## Identification

Saksman-Seip ask whether

```tex
\left\|\sum_{n=1}^N n^{-s}\right\|_{\mathcal H^1}=o(\sqrt N).
```

Under the Bohr/Steinhaus identification of the source paper, this is exactly

```tex
\mathbb E\left|\sum_{n\le N} f(n)\right|=o(\sqrt N)
```

for a Steinhaus random multiplicative function. Harper proves the stronger
asymptotic order

```tex
\mathbb E\left|\sum_{n\le x} f(n)\right|
  \asymp \frac{\sqrt x}{(\log\log x)^{1/4}}.
```

This gives a full affirmative answer to Problem `helson`. The result is already in
the literature and is not a new solution from this run.

## Secondary answered subrange: embedding

Saksman-Seip also ask whether a local \(L^p\) integral on
\(\operatorname{Re}s=1/2\) is bounded by a universal constant times the
\(\mathcal H^p\) norm to the \(p\)-th power for all Dirichlet polynomials.

Harper explicitly states that Theorem 1 gives a negative answer to this
embedding problem for all exponents \(0<2q<2\), i.e. \(0<p<2\). The
counterexample family is

```tex
P_x(s)=\sum_{n\le x} n^{-s}.
```

On a fixed segment of the critical boundary line the \(p=2q\) local integral is
\(\asymp x^q\), while the \(\mathcal H^{2q}\) mean is
\(o(x^q)\) by Harper's Theorem 1 for every fixed \(0<q<1\). Hence no universal
embedding constant can exist in this range.

This is a scoped answer only. The packet does not classify the remaining
embedding exponents outside \(0<p<2\), nor any other problems in the survey.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source paper arXiv:1601.01616.
- `supporting_paper_1703.06654.pdf`: supporting answer paper.
