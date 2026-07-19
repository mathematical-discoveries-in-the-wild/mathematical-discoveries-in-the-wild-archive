# Literature-implied answer packet: high-dimensional Krivine schemes are asymptotically optimal

Status: literature-implied answer, partial/variant scope.

Source/open-problem paper: Mark Braverman, Konstantin Makarychev, Yury Makarychev, and Assaf Naor, *The Grothendieck constant is strictly smaller than Krivine's bound*, arXiv:1103.6161.

Source question addressed: after refuting Krivine's and Konig's conjectures, the source asks whether one can analytically describe high-dimensional maximizers of Konig's bilinear form and whether such maximizers form alternating Krivine rounding schemes. The source notes that if this optimistic picture held, then `K_G` could be recovered from the high-dimensional operator norms.

Supporting paper: Assaf Naor and Oded Regev, *Krivine schemes are optimal*, arXiv:1205.6415.

Implied answer: although it does not identify the Konig-form maximizers or the two-dimensional tiger partition, the later paper proves that for every dimension `k` there exists a `k`-dimensional oblivious Krivine scheme of quality `(1+O(1/k)) K_G`. Thus the broad high-dimensional Krivine-scheme program is asymptotically complete: restricting to oblivious Krivine schemes loses only a `1+O(1/k)` factor.

Remaining open: this is not a full answer to the source's analytic questions. It does not describe `f_infty`, does not prove convergence of the `sigma` iteration, and does not show that maximizers of Konig's bilinear form themselves are alternating Krivine schemes.

Files:
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1103.6161.
- `supporting_paper_1205.6415.pdf`: arXiv:1205.6415.

Review recommendation: record the source target as partially answered in the literature for the broad high-dimensional Krivine-scheme route, but do not mark the analytic maximizer/tiger-partition questions as solved.
