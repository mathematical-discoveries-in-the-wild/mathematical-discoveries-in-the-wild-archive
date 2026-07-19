# Literature Already Answered Packet: Haar Basis 1-Greedy Renorming

Status: literature already answered. This packet records an exact status match: a later paper explicitly says it resolves the older problem. It is not an original proof, counterexample, or literature completion by this pipeline.

Original paper:
- S. J. Dilworth, D. Kutzarova, E. Odell, Th. Schlumprecht, A. Zsak, `Renorming spaces with greedy bases`, arXiv:1403.3777.
- Local copy: `source_paper.pdf`.

Open problem closed:
- Problem 14 asks whether, for `1 < p < infinity`, there is an equivalent norm on `L_p[0,1]` with respect to which the Haar basis is `1`-greedy.
- Screenshot of the exact statement: `figures/open_problem_crop.png`.

Supporting paper:
- F. Albiac, J. L. Ansorena, M. Berasategui, P. M. Berna, `Isometric Renormings for Greedy Bases in Banach Spaces, with applications to the Haar system in L_p[0,1], 1<p<infty`, arXiv:2603.21733.
- Local copy: `supporting_paper_2603.21733.pdf`.

Status match:
- The supporting paper explicitly notes that Albiac and Wojtaszczyk asked whether the Haar system in `L_p` can be made isometrically greedy under an equivalent renorming, citing `AW2006` Problem 6.2.
- It then states that the paper resolves that long-standing question.
- The later theorem proves that for every `1 < p < infinity`, `L_p[0,1]` admits an equivalent norm under which the normalized Haar system is isometrically greedy.
- In the terminology of the original problem, "isometrically greedy" is exactly `1`-greedy.

Files:
- `main.tex`: human-readable solution packet.
- `solution_packet.pdf`: compiled packet.
- `tmp/`: LaTeX and image-rendering scratch files.
