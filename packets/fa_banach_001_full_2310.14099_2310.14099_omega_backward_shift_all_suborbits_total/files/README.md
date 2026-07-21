# A hypercyclic backward shift on `omega` whose every infinite suborbit is total

Status: `candidate_full_likely_valid`

Source: Mohammad Ansari, *Three results in linear dynamics*, arXiv:2310.14099,
the invitation at the end of Section 4 to investigate the non-total-suborbit
question for operators on locally convex spaces.

## Full negative resolution

Let

`omega = K^(N_0)`, `K in {R,C}`,

with its product Fréchet topology, and let the unilateral backward shift be

`B(x_0,x_1,...) = (x_1,x_2,...)`.

The packet proves that there is a hypercyclic vector `x` for `B` such that,
for every infinite set `J subset N_0`,

`closure(span{B^n x : n in J}) = omega`.

Since a hypercyclic vector is supercyclic, this is a counterexample to the
locally convex extension asked about in the source: no strictly increasing
sequence of positive iterate indices has non-dense closed linear span.

In fact, the set of vectors with this property is residual in `omega`.

## Proof mechanism

The shift `B` is topologically mixing on `omega`, so its hypercyclic vectors
form a dense `G_delta`. For every `d >= 0` and every tuple of distinct indices
`n_0 < ... < n_d`, impose the finite Hankel-minor condition

`det[x_(n_i+j)]_(i,j=0)^d != 0`.

Each condition is open and dense. Openness is immediate. Density follows
because the determinant is a nonzero polynomial in finitely many coordinates:
at the witness `x_k=q^(k^2)`, `q>1`, it factors into nonzero row and column
factors times the Vandermonde determinant in the distinct numbers
`q^(2n_i)`. Baire's theorem therefore supplies a hypercyclic `x` satisfying
all of the countably many conditions simultaneously.

Given any infinite `J` and any `d`, choose `d+1` indices from `J`. The
corresponding first-`d+1` coordinate projections of the iterates form a basis
of `K^(d+1)`. Hence the span of the selected suborbit projects surjectively
onto every finite initial coordinate block, which is precisely density in the
product topology.

## Verification

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2310.14099_omega_backward_shift_all_suborbits_total/code/verify_full_spark_hankel.py
```

The script checks the determinant/Vandermonde identity in exact integer
arithmetic for every row tuple of size at most five drawn from the first eight
indices. The proof in `main.tex` is analytic and does not rely on the finite
check.

## Novelty check and scope

A bounded arXiv/web search on 2026-07-21 used the phrases `every infinite
suborbit total hypercyclic omega`, `all its suborbits are total hypercyclic`,
`every suborbit total backward shift hypercyclic`, and `full spark Hankel
hypercyclic vector backward shift omega`. It found the source question and the
related paper of Bernal-Gonzalez and Bonilla, *Total and non-total suborbits for
hypercyclic operators*, but no statement of this residual full-spark
counterexample. Novelty confidence is moderate rather than definitive.

The construction exploits the very weak product topology of `omega`; it does
not contradict the affirmative theorem for normed spaces.

## Human review recommendation

Check the density of each determinant condition, the countable Baire
intersection with the hypercyclic set, and the finite-projection criterion for
density in `omega`. These are the only substantive steps.

