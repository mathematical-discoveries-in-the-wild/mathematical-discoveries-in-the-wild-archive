# Bernoulli Wreath Product Relative Biflatness

Status: partial result likely valid, needs human review.

Source target: arXiv:1602.05259, Jason Crann and Zsolt Tanko, "On the operator homology of the Fourier algebra and its cb-multiplier completion."

Extracted problem: the source conjectures that relative operator 1-biflatness of `A(G)` is equivalent to `G` being QSIN.

Result packaged here: for every nontrivial compact group `K_0` and every discrete group `Gamma`, with `K=K_0^Gamma` carrying the Bernoulli shift action, the Fourier algebra `A(K rtimes Gamma)` is relatively 1-biflat if and only if `Gamma` is amenable.

Why this matters: when `Gamma` is nonamenable, these compact Bernoulli wreath products are a standard non-QSIN family. The packet proves they are not counterexamples to the Crann--Tanko conjecture; the conjecture holds exactly on this family.

Main mechanism:
- Crann--Tanko Proposition 4.3 says relative 1-biflatness of `A(K rtimes H)` forces the Koopman representation of `H` on `L^2_0(K)` to weakly contain the trivial representation.
- For `K=K_0^Gamma`, the Bernoulli Koopman representation decomposes into finite-support tensor pieces induced from finite stabilizers.
- Those induced pieces are weakly contained in the left regular representation of `Gamma`.
- Hence relative 1-biflatness forces `1_Gamma` to be weakly contained in `lambda_Gamma`, so `Gamma` is amenable.

Files:
- `main.tex` - proof packet source.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of the source paper.
- `source_1602.05259.tex` - local copy of the source TeX.
- `figures/open_problem_crop.png` - crop of the source conjecture.
- `figures/semidirect_obstruction_crop.png` - crop of the source semidirect-product obstruction.
- `code/crop_source_pages.py` - reproducible crop script.

Verification:
- LaTeX packet builds successfully with `latexmk`.
- PDF pages were rendered with `pdftoppm` and visually inspected.
- No finite numerical computation is needed; the argument is representation-theoretic.
