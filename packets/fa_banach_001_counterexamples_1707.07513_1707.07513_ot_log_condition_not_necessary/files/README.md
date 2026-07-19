# Counterexample to necessity of the logarithmic OT condition

Status: `counterexample_likely_valid`

Source paper: P. M. Berna, O. Blasco, G. Garrigos, E. Hernandez, and
T. Oikhberg, *Embeddings and Lebesgue-type inequalities for the greedy
algorithm in Banach spaces*, arXiv:1707.07513.

## Target

Question 2 in Section 7 asks for a characterization of systems satisfying

```text
max{L_N, L_N^*} \lesssim log(N+1).
```

Immediately after the question, the authors note that
`\overline T_N(D,D^*) \lesssim log(N+1)` is sufficient and ask whether it is
necessary.

## Counterexample

The packet constructs a 1-unconditional direct-sum basis from two discrete
Lorentz spaces with reciprocal logarithmic fundamental functions

```text
eta(n) = sqrt(n(2+log n)),    xi(n) = sqrt(n/(2+log n)).
```

For the basis in

```text
X = ell^1_{\widehat eta} \oplus_\infty ell^1_{\widehat xi},
```

the primal and dual democracy ratios are both `O(log N)`.  A standard
unconditional greedy estimate therefore gives

```text
max{L_N, L_N^*} \lesssim log(N+1).
```

However the upper democracy functions satisfy `D(N)=eta(N)` and
`D^*(N) >= eta(N)`, and Abel summation gives

```text
\overline T_N(D,D^*) >= c (log N)^2.
```

Thus the sufficient condition from the source paper is not necessary for
Question 2.  This does not characterize all systems in Question 2, and it does
not settle Question 1.

## Novelty / Duplicate Check

Cheap run indexes were searched for `1707.07513`, the paper title, greedy
Lebesgue constants, `OT_N(D,D^*)`, `T_N(D,D^*)`, and related democracy
keywords.  The only close run-memory hits concerned different greedy-basis
questions.  Web/arXiv searches for exact `OT_N(D,D^*)` phrases and the source
question found the source paper and later related greedy-basis literature, but
no explicit answer to this necessity question.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source passage containing
  Questions 1 and 2 and the necessity sentence.

Human-review recommendation: check the unconditional Lebesgue estimate and the
dual direct-sum democracy calculation.  These are standard, but they are the
two structural steps on which the counterexample rests.
