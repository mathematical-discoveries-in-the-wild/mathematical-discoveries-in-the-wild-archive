# Literature-Implied Negative Answer: Boundary-Lipschitz Harmonic Functions

## Source Question

- Source: Alexander V. Kolesnikov and Emanuel Milman, *Remarks on the KLS conjecture and Hardy-type inequalities*, arXiv:1405.0617v2.
- Location: Remark 13, PDF page 11, at the end of the section “Reduction to harmonic functions.”
- Source PDF: `source_paper.pdf`.

The source asks whether it is enough to control variances only for harmonic
functions whose boundary restrictions are 1-Lipschitz.  The stated obstacle is
whether such a harmonic function has a controlled Lipschitz constant on the
whole convex domain; the authors specifically note the lack of control of the
normal derivative.

## Status

`literature_implied_answer (negative; explicit disk witness)`

This is not recorded as a new counterexample.  Classical endpoint regularity
theory already distinguishes Lipschitz boundary data from Lipschitz harmonic
extensions.  Hile--Stanoyevitch (1999), Theorem 2, gives the generally sharp
logarithmic type of pointwise gradient control on smooth domains, and Olofsson
(2020), Theorem 6.7 together with Proposition 6.8, characterizes the endpoint
Lipschitz property on the unit disk through a conjugate-function/Hilbert-
transform condition.  The supporting authors do not appear to identify their
results as answers to Remark 13 of arXiv:1405.0617; the connection is therefore
literature-implied rather than `literature_already_answered`.

## Concrete Identification

Let `D` be the unit disk and, for `-pi <= t <= pi`, define

```text
g(e^{it}) = (2/pi)|t|.
```

This is 1-Lipschitz on the circle for the ambient Euclidean metric.  Its
Poisson extension is

```text
H(r,e^{it}) = 1 - (8/pi^2) sum_{m>=0}
              r^{2m+1} cos((2m+1)t)/(2m+1)^2.
```

Along the radius ending at `1`,

```text
dH/dr(r,0) = -(4/(pi^2 r)) log((1+r)/(1-r)),
```

which diverges as `r` tends to `1`.  Hence `H` is harmonic on `D`, continuous
on its closure, has a 1-Lipschitz boundary restriction, and is not Lipschitz on
the disk.

The negative conclusion also survives the smooth-up-to-the-boundary reading.
For `0 < rho < 1`, set `H_rho(z)=H(rho z)`.  Its boundary trace is the Poisson
average of `g`, so rotational invariance and positivity of the Poisson kernel
give boundary Lipschitz norm at most 1.  Each `H_rho` is harmonic in a
neighborhood of the closed disk, while

```text
|dH_rho/dr(1,0)| = (4/pi^2) log((1+rho)/(1-rho)) -> infinity.
```

Thus no domain-dependent uniform boundary-to-interior Lipschitz estimate exists
even for the fixed smooth strictly convex domain `D` and smooth harmonic data.

## Literature and Novelty Check

The bounded check covered:

- the run's registry, solution, attempt, and proof-gap indexes for
  `1405.0617`, the exact title, harmonic boundary Lipschitz control, Poisson
  extension, normal derivative, and related KLS/Hardy terms;
- web searches for the exact source phrase, arXiv id/title, and variants of
  “harmonic extension of Lipschitz boundary data is not Lipschitz”;
- Hile--Stanoyevitch (1999), Katzourakis arXiv:1601.00190, and Olofsson
  (2020), especially Theorem 6.7 and Proposition 6.8.

No source was found that explicitly cites Remark 13 and announces its
resolution.  The general endpoint theory and unit-disk characterization make
the mathematical answer known after the direct identification above, so the
novelty confidence is low and the packet is intentionally provenance-only.

## Limitations

- This answers only the boundary-to-interior Lipschitz property raised as a
  possible route in Remark 13; it does not resolve the KLS conjecture.
- It does not rule out variance bounds for the boundary-Lipschitz harmonic
  subclass by a method that does not require an interior Lipschitz bound.
- The local copy `supporting_paper_hile_stanoyevitch_1999.pdf` supplies the
  classical logarithmic gradient estimate.  Olofsson's decisive endpoint
  characterization is cited by DOI; the publisher PDF could not be copied
  through the available download path, although the open full-text article was
  inspected.

## Files

- `solution_packet.pdf`: compact rendered status packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:1405.0617v2.
- `supporting_paper_hile_stanoyevitch_1999.pdf`: supporting 1999 paper.
- `verification_report.md`: explicit step-by-step verification.
- `code/verify_disk_formula.py`: numerical sanity check for the exact Fourier
  derivative identity and its growth.

## Human Review Recommendation

Confirm that the intended reading of “bounded Lipschitz constant” in Remark 13
is a uniform estimate from the boundary Lipschitz norm.  The single nonsmooth
boundary datum refutes even finiteness of the global Lipschitz seminorm, while
the Poisson-smoothed family refutes the uniform estimate within the smooth
class used elsewhere in the source paper.
