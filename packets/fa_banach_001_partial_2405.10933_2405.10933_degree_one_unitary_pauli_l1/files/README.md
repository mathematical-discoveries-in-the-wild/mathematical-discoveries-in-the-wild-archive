# Sharp degree-one Pauli \(\ell_1\) bound and a higher-degree criterion

Status: `candidate_partial_likely_valid`

Source: Srinivasan Arunachalam, Arkopal Dutt, Francisco Escudero
Gutiérrez, and Carlos Palazuelos, *Learning low-degree quantum objects*,
arXiv:2405.10933, Question 4 on page 6.

## Result

Question 4 asks whether every Pauli-degree-\(d\) unitary has Pauli Fourier
\(\ell_1\)-norm bounded by a constant \(C(d)\) independent of the number of
qubits.  This packet settles the first nontrivial degree sharply:

\[
 C(1)=\sqrt 6.
\]

In fact, every degree-at-most-one unitary is a two-qubit junta.  If it really
uses two qubits, its identity coefficient vanishes and, up to a global phase,
it has the form

\[
 U=r_1Q_1+i r_2Q_2,
 \qquad r_1^2+r_2^2=1,
\]

where the \(Q_j\) are traceless Hermitian one-qubit unitaries acting on
distinct qubits.  This gives the upper bound \(\sqrt6\), and

\[
 Q=(X+Y+Z)/\sqrt3,\qquad
 U_\star=(Q\otimes I+iI\otimes Q)/\sqrt2
\]

attains it.  Tensor powers of \(U_\star\) also show that every affirmative
answer to the full question must obey

\[
 C(d)\ge 6^{d/2}.
\]

The Hermitian degree-one subcase has sharp constant \(\sqrt3\).

The packet now also proves two higher-degree structural statements:

- Every degree-\(d\) unitary has a one-ancilla Hermitian-unitary dilation of
  degree at most \(d+1\), whose Pauli \(\ell_1\)-norm dominates that of the
  original unitary.
- If the Fourier support of a degree-\(d\) Hermitian unitary has no repeated
  product labels among distinct commuting Pauli pairs, then
  \[
  \mathcal A(U)\le \sqrt{1+\sum_{k=1}^d k!3^{k^2+k}}.
  \]

Indeed, the collision-free condition forces the support to be pairwise
anticommuting.  The sunflower lemma then bounds its cardinality solely in
terms of \(d\).  Thus any counterexample to the full question must exploit
large, structured families of commuting-product collisions.  At degree two,
such collisions first appear through the three perfect matchings on four
qubits, which explains why the degree-one proof does not directly iterate.

## Proof mechanism

Write a degree-one unitary as \(U=aI+\sum_j B_j\), where each \(B_j\) is a
traceless operator supported on qubit \(j\).  The two-qubit part of
\(U^*U=I\) says

\[
 B_j^*\otimes B_k+B_j\otimes B_k^*=0.
\]

A rank-one tensor lemma forces each nonzero \(B_j\) to be a complex phase
times a Hermitian matrix, and the phases for two active qubits must differ by
\(\pi/2\).  Three pairwise phase differences of \(\pi/2\) are impossible, so
at most two qubits are active.  Parseval and Cauchy--Schwarz then give the
sharp norm bound.

## Verification and scope

- `main.tex` contains the sharp theorem, classification, lower-bound family,
  Hermitian dilation, collision-free theorem, literature check, and review
  notes.
- `solution_packet.pdf` is the rendered review packet.
- `source_paper.pdf` is the original arXiv paper.
- `figures/open_problem_crop.png` is a full-width crop of Question 4.
- `code/verify_extremizer.py` checks the sharp two-qubit example and its
  tensor-power coefficient norms.  It is a consistency check, not part of the
  proof.

The original question remains open unconditionally for every fixed
\(d\ge2\).  Exact-phrase
and close-variant searches through July 2026 found the source question and the
older Hermitian quantum-Boolean framework, but no paper stating this sharp
arbitrary-unitary degree-one classification.  Novelty confidence is therefore
moderate, not definitive.

Human review recommendation: **review as a likely-valid sharp partial
answer**.  The main points to check are the elementary tensor-dependence
lemma, the phase-normal-form step for the two active qubits, and the exact
collision-free hypothesis used in the sunflower reduction.
