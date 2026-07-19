# Counterexample packet: the nonsectorial Laplace--Carleson box condition is not sufficient

status: counterexample_likely_valid

model: GPT5.6

source_arxiv: 1907.11583

source_problem: Section 5 of Eskil Rydhe, *On Laplace--Carleson embeddings, and \(L^p\)-mapping properties of the Fourier transform*, asks whether
\[
  \mu(Q_I)\lesssim |I|^{1/2}
\]
for every interval \(I\subset\mathbb R\) implies boundedness of
\(\mathcal L:L^{3/2}(\mathbb R_+)\to L^{3/2}(\mathbb C_+,\mu)\) for a general positive Borel measure.

## Result

The answer is **no**. Use the same measure that the source introduces to obstruct its interpolation strategy:
\[
  \mu=\sum_{n=1}^{\infty}\delta_{n^2+i}.
\]
It satisfies \(\mu(Q_I)\le 2|I|^{1/2}\). For \(N\ge1\), set
\[
  f_N(t)=\mathbf 1_{(0,1)}(t)e^{2\pi t}
         \sum_{k=1}^{N}e^{-2\pi i k^2t}.
\]
Integer-frequency orthogonality gives
\[
  \mathcal L f_N(n^2+i)=\mathbf 1_{\{n\le N\}},
\]
so \(\|\mathcal Lf_N\|_{L^{3/2}(\mu)}=N^{2/3}\). On the other hand,
\[
  \|f_N\|_{3/2}\le e^{2\pi}\left\|\sum_{k=1}^N e^{-2\pi i k^2t}\right\|_2
  =e^{2\pi}\sqrt N.
\]
The norm ratio is at least \(e^{-2\pi}N^{1/6}\to\infty\).

The packet proves the stronger statement that the analogous box condition fails to imply boundedness for every \(1<p\le q<2\).

## Evidence And Files

- `source_paper.pdf`: arXiv:1907.11583.
- `figures/open_problem_crop.png`: Section 5 question on PDF page 17.
- `main.tex`: self-contained proof and bounded novelty check.
- `solution_packet.pdf`: rendered review packet.
- `verification.md`: explicit adversarial step check.
- `code/verify_square_counterexample.py`: finite sanity checks; not part of the proof.
- `code/crop_open_problem.py`: reproducible crop coordinates.

## Novelty Check

The bounded search on 2026-07-19 covered the run's four lightweight indexes and local source scan, then exact/near web searches using the arXiv id, paper title, `Laplace--Carleson`, `L^{3/2}`, `q<2`, `case/region (III)`, `non-sectorial`, the exact source sentence, and the atomic support `n^2+i`. No prior resolution of this question was found.

The searches recovered the source paper, the earlier Jacob--Partington--Pott theory (arXiv:1201.1021), and the 2026 paper *Laplace--Carleson embeddings and infinity-norm admissibility* (arXiv:2109.11465; DOI 10.1007/s13324-026-01203-9). The latter cites Rydhe but treats \(L^\infty\), Orlicz inputs, and output exponents \(q\ge2\); it does not state this \(p=q=3/2\) counterexample. No novelty guarantee beyond these bounded searches is claimed.

## Human Review Recommendation

Prioritize the four elementary steps: the uniform square count in translated intervals, the sign of the Laplace damping, exact orthogonality on \((0,1)\), and the direction \(\|S_N\|_{3/2}\le\|S_N\|_2\). The verifier found all four valid. The result is suitable for expert review as a likely full negative answer.
