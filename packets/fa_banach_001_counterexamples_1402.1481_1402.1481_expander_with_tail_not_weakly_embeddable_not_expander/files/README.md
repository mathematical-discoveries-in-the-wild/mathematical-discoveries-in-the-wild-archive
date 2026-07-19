# Expander With a Tail Counterexample

Status: likely valid counterexample to the literal final question in Arzhantseva--Tessera, arXiv:1402.1481.

Source question: Section 8 asks whether a sequence of finite graphs with uniformly bounded degree that does not weakly embed into \(\ell^2\) is necessarily an expander.

Result: No, as literally stated. Let \(E_n\) be any bounded-degree expander sequence and attach to \(E_n\) a path \(P_n\) of length comparable to \(|E_n|\) by a single edge. The resulting connected bounded-degree graphs \(X_n\) are not expanders, because the path gives a one-edge bottleneck. But \(X_n\) do not weakly embed into \(\ell^2\), because the isometric copy of \(E_n\) has linear size in \(X_n\), and every uniformly Lipschitz map from an expander to Hilbert space collapses a positive proportion of vertices into one bounded ball.

Scope caveat: This is a literal-wording counterexample, not a deep replacement for the source paper's intended frontier. The source immediately notes that large subsets of expanders already obstruct weak embedding. The interesting strengthened question should exclude linear-size expander pieces, or ask for a structural characterization up to such pieces.

Packet contents:

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:1402.1481.
- `figures/open_problem_crop.png`: crop of the source question.

Novelty check: Cheap indexes and exact web searches for the wording of the final question did not reveal an existing packet or exact answer. Later papers explicitly answer other open problems from the same section, but not this literal final question. Novelty confidence is intentionally modest because the construction is an elementary consequence of the source paper's own large-subset observation.
