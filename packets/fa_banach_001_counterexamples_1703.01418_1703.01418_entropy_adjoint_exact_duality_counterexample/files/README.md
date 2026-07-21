# Exact entropy duality fails in dimension two

Status: `candidate_counterexample_likely_valid`

Source: K. P. Deepesh and V. B. Kiran Kumar, *Approximation of Entropy
Numbers*, arXiv:1703.01418, Remark 4.4 and Problem 4.1(1), PDF page 9.

## Counterexample

Over the real field, take the coordinate identity

```text
T : ell_1^2 -> ell_2^2.
```

Its adjoint is the coordinate identity

```text
T* : ell_2^2 -> ell_infinity^2.
```

The packet proves the exact values

```text
epsilon_2(T)  = sqrt(5/8),
epsilon_2(T*) = (1+1/sqrt(2))/2.
```

The first number is the optimal radius for covering the `ell_1^2` diamond by
two Euclidean disks. The second is the optimal radius for covering the
Euclidean disk by two axis-parallel squares. In each case an explicit cover
gives the upper bound, and five boundary points whose incompatibility graph is
an odd cycle give the matching lower bound.

Since

```text
((1+1/sqrt(2))/2)^2 - 5/8 = (sqrt(2)-1)/4 > 0,
```

the source's literal exact identity `epsilon_k(T)=epsilon_k(T*)` fails already
for a rank-two compact operator between two-dimensional Banach spaces.

## Scope

- The counterexample is over real Banach spaces. It refutes the source's
  statement for arbitrary Banach spaces; a complex-only interpretation is not
  addressed.
- It does not contradict exact duality between two Hilbert spaces.
- It does not settle classical essential/asymptotic entropy duality or the
  separate rate-transfer question in Problem 4.1(1).

See `main.tex` and `solution_packet.pdf` for the proof,
`verification.md` for the adversarial audit, and
`code/verify_exact_values.py` for numerical sanity checks.

Bounded exact-phrase and finite-dimensional identity searches found the source
and classical essential-duality literature but no record of this exact planar
counterexample. This is not an exhaustive novelty certification.

Human review recommendation: **send to a specialist in geometric functional
analysis or entropy numbers**. The main review points are the entropy-number
indexing convention, the real-scalar scope, and the two odd-cycle lower bounds.
