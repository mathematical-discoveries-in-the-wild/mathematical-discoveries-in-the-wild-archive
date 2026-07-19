# Literature-Implied Status: adapted antisymmetric case with Hilbert-transform constant

Status: `literature_implied_answer (partial constant)`

Source/open-problem paper: Ivan Yaroslavtsev, "Fourier multipliers and weak
differential subordination of martingales in UMD Banach spaces",
arXiv:1703.07817v5.

Supporting papers:

- Adam Osekowski and Ivan Yaroslavtsev, "The Hilbert transform and orthogonal
  martingales in Banach spaces", arXiv:1805.03948.
- Ivan Yaroslavtsev, "On strongly orthogonal martingales in UMD Banach
  spaces", arXiv:1812.08049, used only for a concise restatement of the same
  orthogonal martingale consequence and the surrounding constant gap.

## Identification

Remark 5.12 of arXiv:1703.07817 asks for the antisymmetric analogue of Theorem
5.10. For an adapted stochastic integral
\[
M=(\Phi\cdot W^H), \qquad N=((\Phi A)\cdot W^H),
\]
where \(A^*=-A\) and \(\|A\|\le 1\), the pair is orthogonal and \(N\) is weakly
differentially subordinate to \(M\).

Theorem 2.1 of arXiv:1805.03948, applied with
\(\Phi(x)=\Psi(x)=\|x\|^p\), gives
\[
\mathbb E\|N_t\|^p \le \hbar_{p,X}^p\,\mathbb E\|M_t\|^p,
\]
where \(\hbar_{p,X}\) is the \(L^p(\mathbb R;X)\) Hilbert-transform norm.

## Scope

This is not the full beta-constant analogue of Theorem 5.10. It gives the
adapted antisymmetric estimate with \(\hbar_{p,X}\), not with
\(\beta_{p,X}\). The upgrade \(\hbar_{p,X}\lesssim_p \beta_{p,X}\) is the
celebrated open linear Hilbert-transform/UMD-constant comparison problem,
explicitly noted in arXiv:1805.03948 and arXiv:1812.08049.

The earlier local partial packet
`solutions/partial/1703.07817_deterministic_contraction_stochastic_integrals/`
is complementary: it proves constant \(1\) for non-adapted integrands. This
packet records the adapted literature bound and explains why it does not
promote to a full solution of Remark 5.12.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: arXiv:1703.07817v5.
- `supporting_paper_1805.03948.pdf`: decisive support theorem.
- `supporting_paper_1812.08049.pdf`: concise later restatement/context.
