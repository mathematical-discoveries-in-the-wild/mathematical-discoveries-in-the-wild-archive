# Record-Time Compactness Solves Remark 5.2

Source: Marianne Akian, Stephane Gaubert, and Roger Nussbaum, "A
Collatz-Wielandt characterization of the spectral radius of order-preserving
homogeneous maps on cones", arXiv:1112.5968.

Status: `candidate_full_solution_likely_valid`, pending human review.

## Full result

Let `C` be a proper cone in a Banach space, assume that `C` is a
sup-semilattice, and let `h:C -> C` be continuous, positively homogeneous,
and order-preserving. If

```text
rho(h,C) < r(h,C),
```

then there is a nonzero `x in C` such that

```text
h(x) = r(h,C) x.
```

This is exactly the conclusion conjectured in Remark 5.2 of the source. It
removes the additional bounded-orbit hypothesis from Theorem 5.1 without
adding normality, uniform monotonicity, uniform continuity, or an interior
point assumption.

## Proof mechanism

After scaling `r(h,C)=1`, the first part of source Theorem 5.1 supplies
`z != 0` with `z <= h(z)`. Let

```text
z_n = h^n(z),   A_n = max_{0 <= j <= n} ||z_j||.
```

The orbit spectral-radius definition gives `A_n^(1/n) -> 1`. If `(A_n)` is
bounded, the source theorem already finishes the proof. Otherwise choose
record times `k_i` at which `||z_{k_i}||=A_{k_i}` and

```text
A_{k_i+i}/A_{k_i} -> 1.
```

Normalize `x_i=z_{k_i}/A_{k_i}`. For an iterate `m` whose
measure-of-noncompactness coefficient is `c<1`, define backward record sets

```text
E_q = { z_{k_i-qm}/A_{k_i} : i >= q+1 }.
```

Every `E_q` lies in the unit ball, while `E_q` is `h^m(E_{q+1})` with one
indexed point adjoined. Finite-set invariance of the source measure of noncompactness
therefore gives

```text
nu(E_0) <= c^q nu(E_q) <= c^q nu(B_X).
```

Thus `E_0` is relatively compact. A limit `x` of the normalized record
vectors has norm one, satisfies `x <= h(x)`, and has bounded forward orbit;
the forward bound follows from the flat record window. The second part of
source Theorem 5.1 then supplies the desired fixed point.

## Files

- `main.tex`: complete full-solution packet.
- `solution_packet.pdf`: compiled and visually checked proof packet.
- `verification.md`: line-by-line mathematical and novelty audit.
- `source_paper.pdf`: exact source paper.
- `figures/`: source crops containing Theorem 5.1 and Remark 5.2.
- `code/render_open_problem_crop.py`: reproducible crop script.
- `tmp/`: LaTeX and page-render intermediates.

## Human review recommendation

The highest-value checks are:

1. the flat-record-time lemma for the subexponential running maximum;
2. the identity of `E_q` with `h^m(E_{q+1})` after adjoining one indexed
   point;
3. the uniform unit-ball bound on every backward record set;
4. the passage from a compact record subsequence to a super-eigenvector with
   bounded forward orbit.
