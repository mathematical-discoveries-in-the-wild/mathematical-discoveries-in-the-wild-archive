# Twisted weak-(1,1) transference and quantum-torus spectral multipliers

Status: `candidate_partial_likely_valid`

Source: Leonard Cadilhac, Jose M. Conde-Alonso, and Javier Parcet,
*Spectral multipliers in group algebras and noncommutative
Calderon-Zygmund theory*, arXiv:2105.05036.

Target: Remark 2.5 on arXiv PDF page 13 asks for Calderon-Zygmund
decompositions and weak type (1,1) singular-integral estimates in fully
noncommutative geometric settings, naming quantum Euclidean spaces and the
hyperfinite II_1 factor.

Result: if Gamma is a discrete amenable group, sigma is any normalized
unitary 2-cocycle, and the Herz-Schur multiplier S_M is weak type (1,1),
then the Fourier multiplier T_M^sigma on the twisted group von Neumann
algebra L_sigma(Gamma) is weak type (1,1) with no larger constant. Matrix
amplifications transfer with the same bound. Combining this with Theorem C(i)
of the source gives complete weak-(1,1) Mikhlin spectral multiplier estimates
on every quantum torus, uniformly in its deformation parameter.

Proof idea: compress the twisted left regular representation to a Folner net
and pass to a tracial ultraproduct. The cocycle appears only as unimodular
phases in matrix entries. Schur multiplication by M(r s^{-1}) therefore
intertwines exactly with the twisted Fourier multiplier on every finite
compression. Amenability makes the compressions asymptotically multiplicative,
while trace preservation passes both L_1 norms and spectral distribution
functions to the limit.

Scope: this is a substantial convolution/spectral-multiplier subcase. It does
not construct a fully noncommutative Calderon-Zygmund decomposition, treat
nonconvolution quantum kernels, or settle the locally compact quantum
Euclidean algebra R_Theta.

Novelty check: run indexes, the local arXiv corpus, and bounded web/arXiv
searches through 22 July 2026 were checked for weak-(1,1) twisted Fourier
transference, cocycle-twisted group von Neumann algebras, quantum-torus weak
endpoints, and Mikhlin multipliers. No explicit duplicate was found. The
literature contains strong-L_p twisted transference, and a 2025 seminar
announcement describes cocycle-uniform L_p transference, but the searches did
not locate the weak-L_1 theorem proved here. Novelty confidence is moderate.

Human review recommendation: verify the spectral-distribution passage from
finite Folner compressions to the tracial ultraproduct and confirm the exact
normalization of the quantum-torus cocycle. The algebraic intertwining and
boundary estimate are explicit.

Files:

- `main.tex`, `solution_packet.pdf`: theorem, proof, corollary, and limitations.
- `source_paper.pdf`: arXiv:2105.05036.
- `supporting_paper_1705.01081.pdf`: quantum Euclidean/quantum-torus context.
- `figures/open_problem_crop.png`: Remark 2.5 from source PDF page 13.
- `verification.md`: independent line-by-line proof audit within this run.
