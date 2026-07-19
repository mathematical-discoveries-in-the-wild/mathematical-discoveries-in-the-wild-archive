# Counterexample Packet: Absolute-sum lower bound for the Lipschitz numerical index

Status: candidate_counterexample_likely_valid_needs_human_review

Source paper: Geunsu Choi, Mingu Jung, Hyung-Joon Tag, "On the Lipschitz numerical index of Banach spaces", arXiv:2110.13821.

Target question: Question 4.4 asks whether, in the absolute-sum setting, one has
\[
n_L\left(\left[\bigoplus_{\lambda\in\Lambda} X_\lambda\right]_E\right)
\geq \inf_{\lambda\in\Lambda} n_L(X_\lambda)
\]
in general, possibly with further conditions.

Claim: The literal general inequality is false, even for two one-dimensional summands and a finite-dimensional order-continuous absolute norm.

Counterexample: Let \(\Lambda=\{1,2\}\), let \(E=\ell_2^2\), and let each \(X_\lambda\) be the scalar field \(\mathbb K\). Then the absolute sum is the Hilbert plane \(\mathbb K^2_2\), while each summand has Lipschitz numerical index \(1\). In the real case a norm-one quarter-turn has Lipschitz numerical radius \(0\); in the complex case a norm-one nilpotent has Lipschitz numerical radius \(1/2\). Hence the left side is \(0\) in the real convention and at most \(1/2\) in the complex convention, while the right side is \(1\).

Scope: This disproves Question 4.4 under the broad "hold in general" reading. It does not settle a narrower version with additional structural hypotheses such as the classical MMPR conditions involving \(n(E)=1\).

Novelty/literature check: Local indexes had no entry for arXiv:2110.13821 or this absolute-sum question. Source-corpus searches found the original 2012 Lipschitz numerical-radius paper and the 2010 MMPR absolute-sum paper, but no packet or later local answer. Web searches on 2026-06-16 for "Lipschitz numerical index absolute sums Banach spaces", quoted variants of "absolute sums", and "n_L" found the source paper, the 2010 MMPR paper, the 2012 foundational Lipschitz paper, and a 2025 real-space \(n_L=n\) paper, but no exact prior answer to Question 4.4.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of Question 4.4 on source PDF page 22.
