# Partial Solution Packet: finite-n constants for p=4 and p=6

Status: `partial_result_likely_valid`

Source paper: Alexandros Eskenazis, Piotr Nayar, and Tomasz Tkocz, "Sharp comparison of moments and the log-concave moment problem", arXiv:1801.07597.

Target: Question 5 asks, for \(q\in(2,\infty)\), \(n\ge 1\), and \(X\) uniform on \(B_q^n\), for the missing optimal finite-dimensional upper constants \(B_{p,q,n}\) when \(p\ge2\), and for the unit vectors that maximise \(\|\sum a_iX_i\|_p\).

Result: the question is solved for \(p=4\) and \(p=6\). In both cases the maximisers are exactly the vectors with equal absolute coordinates, \(|a_i|=1/\sqrt n\). Explicitly, if \(Y\) has density proportional to \(e^{-|x|^q}\), \(m_{2r}=E Y^{2r}\), and \(\rho_{2r}=m_{2r}/m_2^r\), then
\[
B_{4,q,n}=\frac{\beta_{4,q,n}}{\beta_{2,q,n}}\left(3+\frac{\rho_4-3}{n}\right)^{1/4}
\]
and
\[
B_{6,q,n}=\frac{\beta_{6,q,n}}{\beta_{2,q,n}}
\left(\frac{\rho_6+15(n-1)\rho_4+15(n-1)(n-2)}{n^2}\right)^{1/6}.
\]

Human review focus:
- Check the use of Lemma 11 from the source paper to obtain \(m_4<3m_2^2\) and \(m_6<5m_4m_2\) for \(q>2\).
- Check the sixth-moment Schur-concavity criterion: the derivative bracket is \(2c_2+3c_3(x_i+x_j)\), where \(c_2=15m_2(m_4-3m_2^2)\) and \(c_3=m_6-15m_4m_2+30m_2^3\).
- Check that the beta-factor transfer from the iid \(Y\)-model back to the uniform measure on \(B_q^n\) matches equation (2) in the source paper.

Files:
- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_page_4.png`: source page containing Question 5.
- `code/verify_p4_p6_moments.py`: numerical/symbolic sanity checks for the formulas and Schur brackets.
- `history/full_push_2026-07-18.md`: follow-up notes on the attempted extension beyond `p=6`.
- `code/full_push_even_moment_checks.py`: reproducibility script for the even-moment and Fourier-route checks from that push.
