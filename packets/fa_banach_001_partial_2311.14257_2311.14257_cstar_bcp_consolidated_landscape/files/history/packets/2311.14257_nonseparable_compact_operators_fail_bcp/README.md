# Finite-Dimensional Extensions of Nonseparable Compact-Operator Algebras Fail BCP

Status: partial result, high confidence after line-by-line proof audit.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the \(C(K)\) BCP/UBCP criterion.

## Result

For every nonzero Hilbert space \(H\) and every finite-dimensional
\(C^*\)-subalgebra \(F\subseteq\mathcal B(H)\), put
\[
  A_F=\mathcal K(H)+F.
\]
Then
\[
  A_F \text{ has BCP}
  \quad\Longleftrightarrow\quad
  H \text{ is separable}
  \quad\Longleftrightarrow\quad
  A_F \text{ has UBCP}.
\]

Consequently, if \(H\) is nonseparable, then \(\mathcal K(H)\) is a type-I
continuous-trace \(C^*\)-algebra with one-point primitive ideal space and no
BCP.  This shows that the separable-fibre hypothesis in the lane's
continuous-trace positive theorem is necessary.

Taking \(F=\mathbb C1\) gives a unital type-I \(C^*\)-algebra with finite
primitive ideal space and no BCP.  More generally, no finite-dimensional
extension \(\mathcal K(H)+F\) repairs the obstruction.

## Proof Mechanism

Given countably many centers \(a_n=f_n+T_n\), with \(f_n\in F\) and
\(T_n\in\mathcal K(H)\), decompose the finite-dimensional representation of
\(F\) into matrix blocks with multiplicity spaces.  One multiplicity space is
nonseparable.  Choose a vector \(\eta\) in that multiplicity space orthogonal
to the coordinate supports of all ranges of \(T_n\) and \(T_n^*\).  The
finite-dimensional slice \(V=E\otimes\mathbb C\eta\) then reduces all compact
parts and carries the same \(F\)-matrix block as infinitely many slices in
the complement.

Pick a rank-one projection \(p\) inside \(V\).  For each center \(a_n\), the
complement block already has norm \(\|a_n\|\), because compact perturbations
cannot shrink the norm of a finite-dimensional matrix block repeated on an
infinite-dimensional multiplicity space.  Therefore
\[
  \|p-a_n\|\ge\|a_n\|
\]
for every \(n\), so \(p\) escapes every canonical BCP ball.

## Why This Matters

Earlier packets showed that continuous-trace algebras with separable
elementary fibres obey the expected countable-\(\pi\)-base criterion.  This
packet proves the fibre separability assumption cannot be removed, even when
the primitive ideal space is as small as possible.

It also gives a cleaner type-I analogue of the earlier one-point primitive
obstruction using \(\mathrm{II}_1\) factors.  Here the obstruction is not
diffuseness, but the ability to put a fresh rank-one projection outside the
separable support of any countable family of compact centers.

The finite-dimensional-extension clause directly attacks the previous
"unitizations and finite-dimensional extensions" wall: for nonseparable
compact-operator fibres, the bad behavior survives adding any
finite-dimensional \(F\subseteq\mathcal B(H)\).

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: compiled PDF.
- `figures/open_problem_crop.png`: crop of the source-paper question.
- `source_paper.pdf`: local copy of the source paper used for the crop.

## Review Notes

The only substantive checks are:

1. Compact operators on an arbitrary Hilbert space have separable range.
2. The countable closed span of those ranges and adjoint ranges is separable.
3. A finite-dimensional representation of \(F\) decomposes into matrix blocks
   with multiplicity spaces, one of which is nonseparable.
4. Choosing a slice over a vector orthogonal to the compact supports makes all
   compact parts block diagonal.
5. Compact perturbations cannot shrink the norm of a finite-dimensional matrix
   block repeated on an infinite-dimensional multiplicity space.
6. The final block diagonal computation gives \(\|p-a_n\|\ge\|a_n\|\).

Once these points are accepted, the BCP failure is immediate.
