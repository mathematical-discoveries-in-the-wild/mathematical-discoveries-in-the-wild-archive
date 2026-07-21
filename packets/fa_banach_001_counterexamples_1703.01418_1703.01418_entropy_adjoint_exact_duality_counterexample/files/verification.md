# Adversarial verification report

Status: passed symbolic and computational audit; candidate counterexample,
likely valid.

## Claim-to-source match

- Remark 4.4 on source PDF page 9 calls exact equality
  `epsilon_k(T)=epsilon_k(T*)` open even for finite-rank or compact operators
  between Banach spaces.
- Problem 4.1(1) repeats the exact identity for arbitrary Banach spaces.
- The proposed operator has rank two and is therefore finite rank and compact.
- The packet disproves the identity at `k=2` under the source's convention
  that `epsilon_2` permits two covering balls. This is also the usual second
  dyadic entropy number, since `2^(2-1)=2`.

## Proof audit

1. **Adjoint identification.** The duals of real `ell_1^2` and `ell_2^2` are
   `ell_infinity^2` and `ell_2^2`, respectively. Thus the adjoint of the
   coordinate identity `ell_1^2 -> ell_2^2` is exactly the coordinate identity
   `ell_2^2 -> ell_infinity^2`.

2. **Diamond upper bound.** Intersecting the diamond with `x>=y` gives the
   convex hull of four explicitly listed vertices. Every vertex has squared
   Euclidean distance `5/8` from `(1/4,-1/4)`. Convexity of the disk covers the
   whole half; central symmetry covers the other half.

3. **Diamond lower bound.** The five listed diamond-boundary points form a
   five-cycle whose successive Euclidean distances are at least
   `sqrt(5/2)=2 sqrt(5/8)`. Any smaller disk can contain no adjacent pair, so
   two disks would two-colour an odd cycle.

4. **Disk upper bound.** With `a=1/sqrt(2)`, the two supremum-norm balls are
   exactly `[-a,1]^2` and `[-1,a]^2`. A point outside both must have one
   coordinate below `-a` and the other above `a`, forcing Euclidean norm
   strictly larger than one.

5. **Disk lower bound.** The five listed circle points form a five-cycle whose
   successive supremum distances are at least `1+a`, twice the claimed square
   radius. The same odd-cycle obstruction applies.

6. **Strict gap.** Squaring the positive radii gives a difference
   `(sqrt(2)-1)/4`, so there is no numerical-rounding issue.

## Computational check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1703.01418_entropy_adjoint_exact_duality_counterexample/code/verify_exact_values.py
```

The script checks the finite vertex and cycle calculations and samples 80,004
boundary points against the advertised covers. This supports but is not used
in the proof.

## Deliberately excluded overclaims

- No claim is made for complex Banach spaces only.
- No claim is made about equality when both spaces are Hilbert.
- The example does not decide essential/asymptotic entropy duality or whether
  polynomial decay of entropy numbers transfers to the adjoint.

## Literature boundary

Cheap run indexes and bounded primary-source searches found no exact duplicate
or occurrence of this two-dimensional construction. Search results did find
the classical literature on entropy duality up to constants or asymptotic
order. Those are distinct from the literal pointwise equality disproved here.
