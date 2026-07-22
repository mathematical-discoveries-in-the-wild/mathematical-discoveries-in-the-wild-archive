# SAP is equivalent to lunarity for coordinatewise-injective 4x4 maps

Status: **candidate full result; likely valid; computer-assisted exact proof;
awaiting expert review**.

Source: Yong Han, Yanqi Qiu, and Zipeng Wang, *Self-absorption of Hankel
systems on monoids -- a seemingly universal property*, arXiv:2407.01048v1,
Problem 7 on PDF page 21.

## Result

Let `Phi:[4]x[4]->L` be coordinatewise injective. Its associated Hankel
system has the self-absorption property (SAP) if and only if `Phi` is lunar.
This gives a positive answer to Problem 7 in the standing
coordinatewise-injective setting of the source.

The implication lunar `=>` SAP is Theorem B of the source paper. The new
converse is a finite computer-assisted proof:

- all 17,427,192 canonical proper colorings of the 4x4 grid are enumerated;
- 15,667,716 are non-lunar;
- complete directed failure normal forms and the full symmetry group reduce
  them to 14,828 non-lunar orbits;
- 7,331 orbits have exact scalar norm witnesses;
- the remaining 7,497 have exact witnesses with 2x2 integer matrix
  coefficients.

Every strict norm gap is accepted only after exact characteristic-polynomial
and Sturm root-count checks at a rational threshold. Floating point was used
to discover candidate coefficients, not to certify them.

## Verification

From the `code/` directory, run:

```bash
conda run --no-capture-output -n sandbox python verify_full_problem7.py
```

Expected final lines:

```text
exact certificates: 7,331 scalar; 7,497 at matrix level 2
PASS: every non-lunar coordinatewise-injective 4x4 map fails SAP
```

The verifier recompiles the C++ classifier in a temporary directory, rebuilds
all 14,828 representatives, independently checks properness and non-lunarity,
checks exact certificate coverage, and redoes every Sturm computation.

## Packet contents

- `solution_packet.pdf`: expert-facing statement and proof.
- `verification.md`: adversarial audit and limitations.
- `code/classify_all_failure_orbits.cpp`: exhaustive enumeration and orbit
  quotient.
- `code/verify_full_problem7.py`: standalone exact verifier.
- `code/directed_failure_scalar_certificates.json`: 7,331 scalar records.
- `code/directed_failure_matrix_certificates.json`: 7,497 matrix records.
- `source_paper.pdf` and `figures/open_problem_crop.png`: source provenance.

## Novelty and review status

A bounded search on 2026-07-22 checked arXiv and general web results using the
exact title, exact Problem 7 wording, `lunar map`, `Hankel SAP converse`,
`prob-hsap`, and the author names. It found arXiv:2407.01048v1 and a 2024 talk
announcement mentioning unspecified progress, but no later public paper or
stated theorem resolving Problem 7. Novelty confidence is therefore medium;
the authors should be contacted before any originality claim is made.

The main human-review targets are the directed normal-form lemma, the orbit
quotient including transposition, and several independent certificate spot
checks. The packet records three discarded reductions that were caught during
adversarial review and are not used in the final proof.
