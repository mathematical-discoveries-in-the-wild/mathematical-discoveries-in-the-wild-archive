# Conditional packet: biased-coin Tylli problem via a resolvent multiplier bound

status: conditional reduction, likely valid  
source: arXiv:0708.0560, William B. Johnson and Gideon Schechtman, "Multiplication operators on \(L(L_p)\) and \(\ell_p\)-strictly singular operators"  
run: fa_banach_001  
agent: agent_lane_08  
date: 2026-07-03

## Claim

Let \(1<p<2\). For \(0<\delta<1\), let \(T_\delta\) be the biased-coin
operator on \(L_p(\Delta)\), so \(T_\delta w_A=\delta^{|A|}w_A\) on Walsh
characters. Suppose that:

1. \(T_\delta:L_p(\Delta)\to L_2(\Delta)\) is bounded, and
2. the positive-resolvent Walsh multipliers
   \[
   Q_t w_A=\frac{t}{t+\delta^{|A|}}w_A,\qquad t>0,
   \]
   are uniformly bounded on \(L_p(\Delta)\).

Then every \(T_\varepsilon\) with \(\delta<\varepsilon<1\) belongs to the norm
closure of the operators on \(L_p(\Delta)\) that factor through Hilbert space.
Consequently \(T_\varepsilon\) satisfies both the Tylli conclusion and the
Weak Tylli conclusion.

Since Johnson--Schechtman note that \(T_\delta:L_p\to L_2\) is bounded for
\(\delta\) sufficiently small, the remaining dependency is a single concrete
Walsh-chaos multiplier estimate. Sectoriality of \(T_\delta\) would imply this
estimate, but the packet does not prove sectoriality.

## Conditional dependency

The unproved dependency is the uniform \(L_p\)-boundedness of
\[
m_t(n)=\frac{t}{t+\delta^n},\qquad n=0,1,2,\ldots,\quad t>0,
\]
as a multiplier on the Walsh chaos decomposition. Equivalently, the positive
resolvent family \(t(tI+T_\delta)^{-1}\) should be uniformly bounded on
\(L_p(\Delta)\).

This is the exact hinge of the proof. A full solution for the original biased
coin problem would follow if this multiplier estimate were proved for one
small hypercontractive \(\delta\) below the desired \(\varepsilon\).

## Proof idea

Choose \(\delta<\varepsilon\) so small that \(T_\delta\) already factors
through \(L_2\). If \(T_\delta\) admits the positive-resolvent bound above,
then the Balakrishnan integral
\[
\frac{\sin(\pi\alpha)}{\pi}\int_0^\infty
t^{\alpha-1}T_\delta(tI+T_\delta)^{-1}\,dt,
\qquad
\alpha=\frac{\log\varepsilon}{\log\delta},
\]
converges in operator norm. Every integrand factors through Hilbert space
because \(T_\delta\) does, so the integral lies in the closed Hilbert-factor
ideal. On Walsh characters the scalar integral equals
\((\delta^{|A|})^\alpha=\varepsilon^{|A|}\), hence the integral is exactly
\(T_\varepsilon\).

## Literature and obstruction notes

- The source paper explicitly asks whether \(T_\varepsilon\) satisfies the
  Tylli or Weak Tylli conclusion for \(1<p<2\) and \(0<\varepsilon<1\), and
  observes that the answer is yes only for sufficiently small \(\varepsilon\).
- Cheap index checks found no existing packet or attempt for arXiv:0708.0560.
  Nearby Johnson--Schechtman closed-ideal packets concern other strictly
  singular operators and do not answer this biased-coin problem.
- Later local-source and web searches for the exact biased-coin/Tylli phrases
  found the source problem and background functional-calculus papers, but no
  explicit later answer to the biased-coin question.
- A tempting Ritt/Stolz/Besov functional-calculus route is not enough by
  itself: the root \(z^\alpha\), \(0<\alpha<1\), is not holomorphic at \(0\),
  while the standard disk/Stolz calculi for sampled semigroups require
  holomorphic functions at the origin. This is why the packet records the
  positive-resolvent multiplier bound as the real missing estimate.

## Files

- `main.tex`: conditional proof packet.
- `solution_packet.pdf`: rendered PDF.
- `source_paper.pdf`: arXiv:0708.0560.
- `figures/open_problem_crop.png`: crop of the source open problem on PDF page 14.
- `code/crop_open_problem.py`: reproducible crop script.

## Human review recommendation

Review as a conditional reduction, not as a full solution. The proof after the
resolvent multiplier dependency is complete and short. The main verification
target is now the uniform \(L_p\)-boundedness of the multipliers
\(t/(t+\delta^n)\) on Walsh chaos, or a counterexample to that estimate.
