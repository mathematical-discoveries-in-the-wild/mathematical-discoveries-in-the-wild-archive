# Verification report

Verdict: **candidate full solution, likely valid, needs expert review**.

## Symbolic proof checks

- Differentiated the proposed truncated moment
  \[
  M(t)=t^{\lambda+q}(1+t^q)^{-\lambda/q-1}
  \]
  and recovered (M'(t)=t^\lambda p_{q,\lambda}(t)).
- Checked that the mixing density
  \[
  p_{q,\lambda}(c)=(q+\lambda)c^{q-1}
  (1+c^q)^{-\lambda/q-2}
  \]
  has total mass one.
- Re-derived every Weber--Schafheitlin parameter after setting
  \(\rho=n/2-\lambda-1\), \(\mu=a/2\), \(\nu=b/2\).
- Checked the Gamma denominators in both frequency chambers:
  \(\Gamma((\lambda+2-b)/2)\) for (A>B) and
  \(\Gamma((\lambda+2-a)/2)\) for (B>A).
- Checked Euler's transformation and its positive parameters
  \((\lambda+2-a)/2\), \((\lambda+2)/2\) in the first chamber,
  with the symmetric pair in the second chamber.
- Checked local integrability: the cone exponent is at worst
  \(s=\lambda+1-n/2>-1\), while homogeneity at the origin is
  \(\lambda-n>-n\).
- Checked the endpoint separately by closure of the cone of positive
  tempered distributions.

## Reproducible numerical sanity check

Run from the repository root:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/0704.0061_q_l_ball_intersection_classification/code/verifier.py
```

The script checks:

- normalization and the exact mixture identity on a grid of (q,\lambda,r,s);
- Euler's hypergeometric transformation on representative asymmetric and
  symmetric block dimensions;
- strict positivity of the transformed hypergeometric expression on a grid
  approaching the frequency cone.

Observed output on 2026-07-22:

```text
mixture cases: 36
hypergeometric cases: 30
PASS: all sanity checks succeeded
```

These finite-precision evaluations are not part of the proof.

## Literature/novelty bounds

Searched on 2026-07-22:

- the four run indexes for `0704.0061`, `(q,l)-ball`, and the exact threshold;
- exact web phrases for the notation (B^n_{q,\ell}) and
  `max(n-l,l)-2`;
- title/arXiv-id searches for Rubin's source and its citing-paper titles;
- Rubin's related arXiv:math/0701317;
- product-of-Euclidean-balls and Weber--Schafheitlin/intersection-body
  combinations.

No explicit later answer to the open problem was found.  Search coverage is
bounded and novelty remains provisional.

## Reviewer checklist

1. Verify the Weber--Schafheitlin chamber formula with the packet's Fourier
   convention.
2. Verify that the condition \(\rho<1\) rules out a singular distribution
   supported on (A=B), leaving the locally integrable function displayed.
3. Verify positive-mixture passage in \(\mathcal S'\).
4. Verify continuity in \(\lambda\) at the threshold.
5. Perform an independent MathSciNet/zbMATH/full-text novelty search.
