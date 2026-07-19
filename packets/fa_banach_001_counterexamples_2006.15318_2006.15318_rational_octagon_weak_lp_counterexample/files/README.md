# Rational-Octagon Counterexample to Necessity of the Weak L-P Count

Status: candidate full counterexample, likely valid.

For the two-dimensional polygonal Banach space `X` whose unit ball is

```text
conv( +/-{(1,0), (2/3,2/3), (0,1), (-2/3,2/3)} ),
```

the pair `(X,X)` has weak Lindenstrauss--Perles property: every extreme
contraction `T:X->X` maps at least one extreme point of `B_X` to an extreme
point of `B_X`. Nevertheless, `B_X` has eight extreme points. In the notation
of Theorem 2.5 of arXiv:2006.15318, `n=m=p=2`, so `mp=n+p=4` and the theorem's
strict sufficient inequality fails. This gives a negative answer to the
source's unresolved necessity question for arbitrary polygonal planes.

## Exact certificate

The operator ball is a four-dimensional rational polytope cut out by 32
inequalities. The verifier enumerates all `C(32,4)=35,960` four-subsets of
active inequalities using exact rational Gauss--Jordan elimination. It finds
exactly 96 operator-ball vertices, grouped into six signed-permutation orbits
of sizes `8,8,16,16,16,32`, and verifies that all 96 map an octagon vertex to
an octagon vertex.

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2006.15318_rational_octagon_weak_lp_counterexample/code/verify_rational_octagon_weak_lp.py
```

The verifier uses only Python's standard library and exact `Fraction`
arithmetic.

## Packet contents

- `solution_packet.pdf`: full statement, proof, exact orbit table, and source context.
- `source_paper.pdf`: arXiv:2006.15318.
- `figures/open_problem_crop.png`: source page 8, including the unresolved paragraph.
- `code/verify_rational_octagon_weak_lp.py`: exhaustive exact certificate.
- `code/make_open_problem_crop.py`: reproducible crop script.

## Novelty status

A bounded search on 2026-07-19 found the weak L-P terminology only in the
2019 introduction (arXiv:1902.06917), the 2020 source paper
(arXiv:2006.15318), and a commented definition in arXiv:2407.05545 within the
35,297-paper local source corpus. Exact web searches found the 2019 and 2020
papers but no later answer or rational-octagon example. Novelty confidence is
moderate to high, not definitive.

## Human review recommendation

Check the 32-inequality description of the operator ball, the standard fact
that every vertex of a four-dimensional polytope is captured by four
independent active inequalities, and the six orbit representatives in Table
1 of the packet. Then rerun the exact verifier.

