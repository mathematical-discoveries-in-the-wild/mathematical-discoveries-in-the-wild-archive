# Levy--Prokhorov Truncation Counterexample

Status: likely valid counterexample to the naive Banach-style extension for
general complete separable metric spaces.

Source: Geher--Titkos, "A characterisation of isometries with respect to the
Levy--Prokhorov metric", arXiv:1701.04267. The main Banach-space question is
answered in the source paper itself; the relevant prompt is the final remark
asking for characterisations of surjective `pi`-isometries in other complete
separable metric settings.

Result: Let `X={a,b,c}` with

```text
d(a,b)=2, d(a,c)=5/2, d(b,c)=3.
```

All nonzero distances are at least `1`, so the Levy--Prokhorov metric on
`P_X` is exactly total variation:

```text
pi(mu,nu) = sup_A |mu(A)-nu(A)|.
```

Therefore every permutation of `X` induces a surjective `pi`-isometry of
`P_X`. The transposition swapping `a` and `b` and fixing `c` is not an isometry
of the base metric, because it sends the pair `(a,c)` of distance `5/2` to the
pair `(b,c)` of distance `3`. Its push-forward is nevertheless a surjective
`pi`-isometry. Since the action on Dirac masses determines the underlying map,
this probability-space isometry is not induced by any base-space isometry.

Packet contents:

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:1701.04267.
- `figures/open_problem_crop.png`: crop of the final source prompt.
- `code/crop_open_problem.py`: crop-generation script.
- `code/check_finite_example.py`: small sanity checker for the finite metric.

Scope caveat: This does not classify all complete separable metric spaces and
does not contradict the Banach-space theorem. It shows that any broader
classification must account for the scale-`1` truncation in the
Levy--Prokhorov metric.

Novelty check: I searched the run indexes and bounded web queries for
arXiv:1701.04267, Levy--Prokhorov finite metric spaces, Prokhorov metric
isometries, and total-variation simplex variants. I found the source paper but
no exact prior packet or exact finite-truncation counterexample. Novelty
confidence is moderate because the construction is elementary.
