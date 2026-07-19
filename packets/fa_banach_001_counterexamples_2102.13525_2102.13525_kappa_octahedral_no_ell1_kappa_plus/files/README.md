# Counterexample: kappa-octahedral need not contain ell_1(kappa+)

Status: `counterexample_likely_valid` for Question 6.2 of arXiv:2102.13525.

Source paper: Stefano Ciaci, Johann Langemets, Aleksei Lissitsin,
*A Characterization of Banach Spaces Containing ell_1(kappa) via
ball-covering properties*, arXiv:2102.13525.

Question addressed: if a Banach space is kappa-octahedral, must it contain an
isomorphic copy of `ell_1(kappa+)`?

Claim: no. For every infinite cardinal `kappa`, the space constructed in
Theorem 5.13 of the source paper,

```text
X = (direct sum over n of ell_{p_n}(kappa+))_1,
```

is kappa-octahedral, but it contains no isomorphic copy of `ell_1(kappa+)`.

The new observation is that any embedding of `ell_1(kappa+)` into this
countable `ell_1`-sum would have a large subfamily of basis vectors whose
tails are uniformly small beyond a common finite block. This uses regularity
of the successor cardinal `kappa+`. The corresponding finite-coordinate
projection would then embed `ell_1(kappa+)` into a finite direct sum of
reflexive `ell_p` spaces, which is impossible.

Artifacts:

- `source_paper.pdf`: compiled source paper.
- `figures/open_problem_crop.png`: crop of Question 6.2 from page 15.
- `code/make_crop.py`: reproducible crop script.
- `main.tex`: review packet source.
- `solution_packet.pdf`: compiled packet.

Novelty check: cheap run indexes were searched for arXiv id `2102.13525`,
`kappa-octahedral`, and close `ell_1(kappa+)` phrases. External exact-phrase
web searches on 2026-07-01 found only the source paper or irrelevant results;
no later exact answer was found in the bounded check. Human review should
focus on the finite-block/reflexivity obstruction.
