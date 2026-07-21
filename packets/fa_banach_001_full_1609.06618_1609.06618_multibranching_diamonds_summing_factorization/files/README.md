# Fixed-branching diamonds factor through the summing basis

Status: `candidate_full_likely_valid`

Source: Mikhail I. Ostrovskii and Beata Randrianantoanina, *A new
approach to low-distortion embeddings of finite metric spaces into
non-superreflexive Banach spaces*, arXiv:1609.06618, Remark 1.7.

## Result

The source asks whether, for every fixed branching number `k`, all
multibranching diamonds `D_{n,k}` admit maps into `ell_1`, uniformly in
`n`, whose `ell_1` and summing-norm distances factor the graph metric.  It
states that even the existence of `C(3)` was unknown.

This packet gives a positive answer for every finite `k`.  If `C_2` is any
uniform constant for the binary diamonds supplied by Johnson--Schechtman,
then one may take

```text
C(k) = 2 C_2 ceil(log_2 k),       k >= 2.
```

The construction is short.  Give the `k` branch labels distinct binary
words of length `m=ceil(log_2 k)`.  Each bit induces a canonical
1-Lipschitz projection

```text
pi_j : D_{n,k} -> D_{n,2}.
```

For every pair of vertices `x,y`, at least one `pi_j` preserves their
distance exactly.  This is because a pair is either separated for the first
time into two parallel arms of one recursive subdiamond, in which case any
bit distinguishing those two arm labels preserves the distance, or its
distance is vertical and every projection preserves it.

Compose the `m` projections with the known binary factorization map and
concatenate the resulting coordinate blocks, scaled by `1/m`.  The
`ell_1` upper bound follows by averaging 1-Lipschitz maps.  The summing norm
of a concatenation is at least half the summing norm of any one block, which
gives the displayed constant.

## Files

- `main.tex` / `solution_packet.pdf`: theorem and complete proof.
- `source_paper.pdf`: the original arXiv paper.
- `supporting_johnson_schechtman_2009.pdf`: the binary-diamond input.
- `figures/open_question_crop.png`: rendered source evidence from page 4.
- `proof_intuition.md`: compact expert-facing proof idea.
- `verification.md`: adversarial audit and computational checks.
- `novelty.md`: bounded literature-search record.
- `code/verify_binary_projections.py`: exhaustive finite-depth verifier.

Human review recommendation: **high priority**.  The argument is elementary
and the exact point to audit is the recursive distance-preservation lemma for
the binary projections.  If accepted, the result answers all of Remark 1.7,
strictly stronger than the singled-out `k=3` case.

