# General \(L^2\) Poisson Concentration With Sharp Uniform Factor

Status: **candidate full result, likely valid; human review requested**

Source paper: Jaime Gómez, David Kalaj, Petar Melentijević, and João P. G.
Ramos, *Uniform stability of concentration inequalities and applications*,
arXiv:2411.16010 (2024).

Source question: Remark 5, pp. 41-42 asks whether one can obtain a
concentration inequality for Poisson extensions of arbitrary
\(L^2(\partial\mathbb D)\) data, rather than only analytic \(H^2\) data.

## Result

Let \(u=P[h]\) be the Poisson extension of
\(h\in L^2(\mathbb T,dt/(2\pi))\). If
\[
 d\mu(z)=(1-|z|^2)^{-2}\,dA(z),\qquad \mu(\Omega)=s<\infty,
\]
then
\[
 \int_\Omega |u(z)|^2(1-|z|^2)^{-1}\,dA(z)
 \le
 2\pi\log\!\left(1+\frac{s}{\pi}\right)\|h\|_2^2.
\]
The factor \(2\) is the best factor that works uniformly for all \(s>0\).
The analytic sharp factor \(1\) fails for every fixed \(s>0\).

Thus the literal existence question has a sharp uniform affirmative answer.
The packet does not claim to determine the best constant separately at each
fixed \(s\).

## Proof Map

1. Split the harmonic extension as \(u=f+\overline g\), where
   \(f,g\in H^2\) and
   \(\|f\|_{H^2}^2+\|g\|_{H^2}^2=\|h\|_2^2\).
2. Apply the source paper's sharp analytic inequality to \(f\) and \(g\)
   separately and use
   \(|f+\overline g|^2\le 2(|f|^2+|g|^2)\).
3. For sharpness, use normalized boundary Poisson kernels \(h_\rho\) and
   pseudohyperbolic disks \(\Omega_\rho\) centered at \(\rho\).
4. After pulling back by the disk automorphism sending \(0\) to \(\rho\),
   compute the exact limit
   \[
   \lim_{\rho\uparrow1}
   \int_{\Omega_\rho}|P[h_\rho](z)|^2(1-|z|^2)^{-1}\,dA(z)
   =
   \pi\left[
   \log\!\left(1+\frac{s}{\pi}\right)+\frac{s}{s+\pi}\right].
   \]
   This exceeds the analytic bound for every \(s>0\), and its ratio to that
   bound tends to \(2\) as \(s\downarrow0\).

## Packet Contents

- `solution_packet.pdf`: typeset proof and review packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: local copy of arXiv:2411.16010.
- `figures/open_problem_crop_page41.png` and
  `figures/open_problem_crop_page42.png`: the complete two-page source remark.
- `VERIFICATION.md`: adversarial verification report.
- `code/verify_boundary_kernel.py`: independent quadrature checks for the
  angular identity and pre-limit kernel masses.
- `tmp/`: LaTeX and rendering intermediates.

## Computational Check

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2411.16010_general_l2_poisson_concentration/code/verify_boundary_kernel.py
```

The script checks four radii in the angular identity and twelve pre-limit
integrals (four values of \(s\), three values of \(\rho\)). The masses converge
to the exact formula as \(\rho\) approaches \(1\). This is a normalization
check, not part of the proof.

## Novelty Check

On 2026-07-23, bounded arXiv/web searches used the exact source question,
“Poisson extensions,” “general \(L^2\),” “harmonic concentration,” and the
four source authors. They located arXiv:2411.16010 and unrelated
Poisson/harmonic literature, but no later paper answering this exact question.
Novelty remains subject to a broader expert literature review.

## Human Review Recommendation

Review especially:

1. the normalization of the boundary Poisson kernel;
2. the three disk-automorphism identities in the sharpness proof;
3. the angular mean \(1-r^2/2\);
4. the distinction between the best **uniform** factor \(2\) and the
   uncomputed fixed-\(s\) optimum.
