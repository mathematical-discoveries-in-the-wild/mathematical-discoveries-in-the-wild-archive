# Full result for the combined multiplier route

Status: `full_solution_likely_valid` for the concrete multiplier-combination
question on page 3 of arXiv:1706.01731.

Source problem: Ivan S. Yaroslavtsev, *Martingale decompositions and weak
differential subordination in UMD Banach spaces*, arXiv:1706.01731, page 3.
The source notes that Fourier multiplier estimates had been obtained from
purely discontinuous martingales and from continuous martingales, and asks
whether one can combine the two approaches using the general weak differential
subordination theorem.

Result: yes. The pure-jump and continuous Fourier multiplier approaches can be
combined through one application of the general weak differential subordination
theorem for the natural mixed Levy/Gaussian multiplier class of Yaroslavtsev's
earlier multiplier theorem arXiv:1703.07817. If
\[
\Lambda(\xi)=\int_{\mathbb R^d}(1-\cos \xi\cdot z)\,V(dz)
+\frac12\int_{S^{d-1}}(\xi\cdot\theta)^2\,\mu(d\theta),
\]
and
\[
m(\xi)=\frac{\int_{\mathbb R^d}(1-\cos \xi\cdot z)\phi(z)\,V(dz)
+\frac12\int_{S^{d-1}}(\xi\cdot\theta)^2\psi(\theta)\,\mu(d\theta)}
{\Lambda(\xi)}
\]
with `|phi|, |psi| <= 1` and `m=0` on `{Lambda=0}`, then the Fourier multiplier
`T_m` is bounded on `L^p(R^d;X)` for every UMD Banach space `X`.

The proof is a one-shot mixed martingale proof: run the parabolic martingale for
a Levy process with both a jump part and a Brownian covariance part, transform
the jump increments by `phi` and the Brownian directional integrands by `psi`,
observe weak differential subordination of the transformed martingale to the
untransformed one, and apply the general theorem from arXiv:1706.01731.

Scope note: this is a full solution only to the multiplier-combination route
selected from the source paper. It is not a sharper replacement for
arXiv:1703.07817, Theorem 4.1, whose special proof already gives the stronger
bound `beta_{p,X}` for this symbol class. It also does not settle the source's
separate sharp Hilbert-transform/continuous-WDS constant questions or the broad
stochastic-integral BDG problem for arbitrary martingale noise.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1706.01731.
- `supporting_paper_1703.07817.pdf`: earlier mixed multiplier theorem used for
  the exact symbol class and as comparison.
- `figures/open_problem_crop.png`: source open-problem sentence.
- `figures/supporting_mixed_multiplier_crop.png`: theorem statement from
  arXiv:1703.07817.

Novelty check: local run indexes had no exact packet for arXiv:1706.01731.
Nearby packets for arXiv:1703.07817 and arXiv:1805.03948 concern antisymmetric
or deterministic stochastic-integral subcases. Exact web phrase searches for
the open sentence and for combined weak-differential-subordination multiplier
proofs did not find a later explicit answer. Human reviewers should still check
whether a later harmonic-analysis paper records this proof route.
