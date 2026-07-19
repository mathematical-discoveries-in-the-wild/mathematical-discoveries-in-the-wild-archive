# Counterexample: Real Dirichlet Dilation Need Not Be Borel

Run: `fa_banach_001`

Status: `counterexample_likely_valid`

Source target:

- Ondrej F. K. Kalenda and Jiri Spurny, *On simpliciality of function spaces
  not containing constants*, arXiv:2401.16100.

## Result

Question 7.10 of the source asks, among other things, whether for a real
simplicial function space `H` not containing constants on a non-metrizable
compact space `K`, and continuous `f:K -> R`, the Dirichlet dilation `Df` is
Borel.

This packet gives a negative answer to that Borel part of the real question.
There is a real simplicial function space `H` not containing constants on a
non-metrizable compact space `K` such that, for the continuous constant
function `1`, the dilation `D1` is not Borel.

## Mechanism

The construction is a real two-point variant of the source paper's complex
Example 6.17 / Example 7.9. Instead of using a CH-built map `g:T -> T`, take
any non-Borel two-valued function `eps:[0,1] -> {-1,1}`. Split the graph of
`eps` inside the Stacey porcupine compactum over `[0,1] x {-1,1}`, and define
`H` by the relations

```text
f(t,s,0) = s f(t,1,0),
f(t,eps(t),0) = (f(t,eps(t),-1)+f(t,eps(t),1))/2.
```

The unique boundary measure representing `(t,s,0)` is

```text
s eps(t)/2 * (delta_(t,eps(t),-1) + delta_(t,eps(t),1)).
```

Therefore `D1(t,s,0)=s eps(t)`, and on the closed slice
`[0,1] x {1} x {0}` this is exactly `eps`, which is not Borel.

## Scope

This packet does not answer the first bullet of Question 7.10 about
`\widetilde D f`. It also does not settle every possible interpretation of the
separate `H`-affinity clause in the second bullet. It only disproves the
universal real Borel assertion for `Df`.

## Novelty Check

- Cheap indexes were searched for `2401.16100`, `D1`, `Dirichlet problem`,
  `simplicial function space`, `not Borel`, and related terms.
- The source paper itself contains a complex CH example where `D1` is not
  Borel, but explicitly leaves the real case open.
- The local 2025 follow-up arXiv:2501.12876 was checked; its Dirichlet
  subsection treats vector-valued function spaces in a different setting and
  did not contain this real scalar counterexample.
- Web phrase searches for the exact Question 7.10 wording and the real
  non-Borel `D1` variant did not reveal a later answer.

## Files

- `README.md`: this summary.
- `main.tex`: full counterexample packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2401.16100 PDF.
- `source_2401.16100.tex.gz`: local arXiv source archive.
- `figures/open_problem_crop.png`: page crop containing Example 7.9 and
  Question 7.10.
- `tmp/`: build intermediates and rendered page image.

## Human Review Recommendation

Check especially the finite-fiber boundary-measure argument proving that the
constructed real space is simplicial and that the listed `delta_x` measures
are indeed the unique `H`-boundary representatives.
