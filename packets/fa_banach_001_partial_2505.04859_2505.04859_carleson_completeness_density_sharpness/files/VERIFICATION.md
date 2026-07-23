# Verification report

Status: candidate exact classification theorem for the two-ray model,
likely valid.

## Analytic audit

The proof was checked against the current arXiv v2 definitions.

- The original same-ray calculation uses the exact identity
  \[
  \frac{\tanh x-\tanh y}{1-\tanh x\tanh y}
  =\tanh(x-y).
  \]
- For every \(\alpha>0\), the hyperbolic coordinate of the powered
  radius has positive derivative with limit \(2\). Its infimum on
  \([A,\infty)\) is therefore positive, giving a full same-ray product
  bound after powering.
- Off resonance, the powered rays have distinct boundary points. The
  cross-ray product has both a common factor lower bound and uniformly
  summable deficits.
- The weight ratio
  \(\sqrt{(1-r^2)/(1-r^{2\alpha})}\) extends positively to \(r=1\),
  so the powered canonical frame and the sampled orbit are related by a
  bounded invertible diagonal operator.
- At resonance, every radial pair collides after powering and supplies
  a separate orthogonal annihilator.
- The logarithmic block-density computation uses harmonic-sum
  asymptotics for \(\Lambda=d^{-1}\mathbb N_0\).
- The phase calculation uses the paper's principal branch
  \(z^\lambda=e^{\lambda(\log r+i\theta)}\).

## Numerical checker

The reusable script `code/verify_construction.py` checks a representative
finite truncation. It is a sanity check only; no finite computation proves
the infinite-product or density limits.

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2505.04859_carleson_completeness_density_sharpness/code/verify_construction.py
```

Recorded output:

```text
parameters: c=1.0471975512, d=0.2, theta=0.628318530718
tested spectral pairs: 20
maximum within-ray identity error: 1.595e-10
minimum 40-point Carleson product: 0.0321854049044
cross-ray common lower bound q: 0.223328396637
truncated sum of radial defects: 1.99999963745
minimum loss/bound ratio observed: 0.144289816726
maximum phase-alias error: 2.597e-14
nonresonant alpha: 1.3
minimum powered-spectrum Carleson product: 0.0276666033448
frame-transfer weight-ratio range: [0.877058048909, 0.964794237324]
resonant alpha: 5
maximum powered-pair collision error: 6.171e-16
logarithmic block-density approximation: 0.200013796952
all numerical sanity checks passed
```

## PDF review

The upgraded eight-page exact-classification packet was built from
`main.tex`, rendered page-by-page to PNG, and visually inspected at full
page scale. All theorem statements, displays, source figures, tables,
references, and page boundaries were readable and unclipped. The final
PDF has 8 pages and is 417240 bytes.

SHA-256 of the reviewed PDF:

```text
d2a82b4a6497ee915c8942539eabbaceb65bd35075eeb5c548b15b74bd973928
```

## Human verifier focus

1. Confirm that the powered hyperbolic-coordinate derivative has a
   positive infimum for every \(\alpha>0\).
2. Confirm the off-resonance powered cross-ray product estimate.
3. Confirm the diagonal comparison transfers the canonical powered frame
   to the sampled orbit.
4. Assess novelty relative to Remark 2.6 of the source paper, which
   already supplies the basic integer collision mechanism.
