# Counterexample Packet: Algebraic Envelopes and Directed Unions

Run: `fa_banach_001`
Agent: `agent_lane_04`
Status: claimed counterexample; needs human review

## Source

- Paper: Valentin Ferenczi and Jordi Lopez-Abad, "Envelopes in Banach spaces"
- arXiv: `2112.11795`
- Source question: after Corollary 3.3, the paper asks whether the directed-union formula for the isometric envelope remains true for the algebraic envelope.

## Result

The packet gives a counterexample in a real \(L_p\)-space, \(1<p<\infty\), \(p\ne2\).

Let
\[
\Omega=[0,1]\times\{0,1\},\qquad
\mu=\lambda\otimes\left(\frac13\delta_0+\frac23\delta_1\right),
\]
and let \(Y\) be the base-coordinate subspace.  Let \(Y_n\) be the finite dyadic base subspaces.  Then
\[
Y=\overline{\bigcup_n Y_n},\qquad
\overline{\bigcup_n \operatorname{Env}^{\rm alg}(Y_n)}=Y,
\]
but
\[
\operatorname{Env}^{\rm alg}(Y)\supsetneq Y.
\]

The strictness is witnessed by \(\mathbf 1_{[0,1]\times\{0\}}\).  Unequal fiber weights force every base-fixing measure automorphism to fix this sheet.

## Files

- `main.tex`: human-readable proof packet
- `solution_packet.pdf`: compiled packet
- `source_paper.pdf`: original arXiv PDF
- `figures/open_problem_context_p19.png`: crop of Corollary 3.3
- `figures/open_problem_question_p20.png`: crop of the algebraic-envelope question

## Verification

Build command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

Human review should focus on the Banach-Lamperti step and the fiber-measure calculation.
