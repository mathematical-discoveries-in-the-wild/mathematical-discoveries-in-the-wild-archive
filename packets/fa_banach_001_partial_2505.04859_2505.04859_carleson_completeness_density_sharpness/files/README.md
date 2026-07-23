# Exact arithmetic phase diagram for two-ray Carleson systems

Status: **candidate exact classification theorem for a natural model;
likely valid; human review recommended**.

Source: Ilya Krishtal and Brendan Miller, *Demystifying Carleson Frames*,
arXiv:2505.04859v2, revised 8 July 2026; published in *Applied and
Computational Harmonic Analysis*, DOI
`10.1016/j.acha.2025.101811`.

## Source program

The source paper says in its introduction that fully understanding the
spanning properties of Carleson systems remains far from achieved and
proposes further work using sampling and interpolation. Its Theorem 3.5
proves that a canonical Carleson system with spectrum in the sector
\(\mathbb D_c\) is complete whenever
\[
L(\Lambda)>\frac c\pi.
\]

The future-work passage is reproduced in
`figures/open_problem_crop.png`; the threshold theorem is reproduced in
`figures/source_theorem_crop.png`.

## Result

Fix \(A>0\), \(0<\theta<\pi\), and the two-ray spectrum
\[
z_n^\pm=\tanh(A(n+1))e^{\pm i\theta}.
\]
The packet proves this is a Carleson sequence and completely classifies
every arithmetic fractional-power orbit:
\[
\{D^{\alpha k}g\}_{k\ge0}
\begin{cases}
\text{is a frame},&\alpha\theta\notin\pi\mathbb Z,\\
\text{has infinite-dimensional orthogonal complement},
&\alpha\theta\in\pi\mathbb Z.
\end{cases}
\]

Equivalently, for
\(\Lambda_d=\{k/d:k\in\mathbb N_0\}\), one has
\(L(\Lambda_d)=d\), and the system is a frame at every density except
\[
d=\frac{\theta}{m\pi}\qquad(m\in\mathbb N),
\]
where it has infinite defect. Thus density alone does not determine
spanning in this model.

As a corollary, for every \(0<c<\pi\) and \(0<d\le c/\pi\), choosing
\(\theta=\pi d\) produces an infinite-defect system in
\(\mathbb D_c\) with \(L(\Lambda_d)=d\). At \(d=c/\pi\), this proves
that the strict inequality in Theorem 3.5 is optimal and cannot be
replaced by a non-strict inequality.

The positive direction is the substantive upgrade. Off resonance, the
powered spectrum
\[
\{\tanh(A(n+1))^\alpha e^{\pm i\alpha\theta}\}_{n\ge0}
\]
is again Carleson. Its canonical generator differs from the sampled
generator by a bounded invertible diagonal operator, so the canonical
Carleson-frame theorem gives a frame. At resonance, every radial pair
collides and supplies an independent annihilator.

## Verification

The proof in `main.tex` is self-contained. In particular, it proves the
full product Carleson condition, not only pairwise separation.

Run the numerical sanity checker with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2505.04859_carleson_completeness_density_sharpness/code/verify_construction.py
```

The script checks the original and nonresonant powered Carleson products,
the within-ray pseudohyperbolic identity, cross-ray estimates, diagonal
weight-ratio bounds, the resonant powered-pair collision, and a
finite-window approximation to logarithmic block density. These checks
are not used as proof.

See `VERIFICATION.md` for the adversarial proof audit and recorded output.

## Limitations and novelty

This is a necessary-and-sufficient theorem for all arithmetic
fractional-power orbits of the stated two-ray spectra. It does not
characterize arbitrary spectra or nonarithmetic index sets, so the source
paper's unrestricted spanning-properties program remains open.

The source paper's Remark 2.6 already observes that an integer-power
spectral collision obstructs the frame property. The present theorem
turns that one-sided obstruction into an exact dichotomy for every real
arithmetic step. The positive direction requires proving all
nonresonantly powered spectra remain Carleson and transferring their
canonical frames through uniformly controlled weights. Because the
negative mechanism is visible in the source paper, novelty confidence
remains moderate.

A bounded search on 23 July 2026 covered the run indexes,
arXiv:2505.04859v2, *The Mystery of Carleson Frames*, the published
article page, the new arXiv:2607.18491 preprint on block-diagonal
Carleson frames, and exact/close searches for `powered spectrum`,
`two rays`, `fractional powers`, `phase collision`, `Carleson systems`,
and `logarithmic block density`. No explicit statement of this exact
phase diagram was found. The block-diagonal paper's classification is
for nonnegative spectra.

## Human review recommendation

The main review points are the positive lower bound for the powered
hyperbolic-coordinate derivative, the uniform cross-ray product, and the
bounded diagonal frame transfer. If those pass, the result is a complete
classification theorem for the two-ray model and is suitable for a short
note. A reviewer should still assess novelty relative to the collision
remark and standard canonical-frame theorem.

Ledger:
`ledger/results/2505.04859_carleson_completeness_density_sharpness.json`.
