# Same-Szlenk Basis Embedding Answered by arXiv:1408.3311

Status: `literature_already_answered` (basis-embedding subquestion).

Source/open-problem paper: Edward Odell, Thomas Schlumprecht, and Andras
Zsak, *Banach spaces of bounded Szlenk index*, arXiv:0706.0656.

Source question: in the open-problems paragraph on page 4 of the source PDF,
the authors ask whether, for every countable ordinal `alpha`, every space in
`C_{omega^alpha}` embeds into a space with a basis in the same class.

Supporting answer paper: Edward Odell and Thomas Schlumprecht, *On Zippin's
Embedding Theorem of Banach spaces into Banach spaces with bases*,
arXiv:1408.3311.

Answer: yes. The Main Theorem of arXiv:1408.3311, on page 2, proves that if
`X` has separable dual then `X` embeds into a space `W` with a shrinking basis
and `Sz(W)=Sz(X)`. If `X` is reflexive, then `W` is reflexive and
`Sz(W*)=Sz(X*)`. Applying this to a separable reflexive
`X in C_{omega^alpha}` gives a basis space `W` still in `C_{omega^alpha}`.

Packet contents:

- `source_paper.pdf`: original arXiv:0706.0656 PDF.
- `supporting_paper_1408.3311.pdf`: supporting arXiv:1408.3311 PDF.
- `main.tex`: compact LaTeX status note.
- `solution_packet.pdf`: rendered status note.
- `tmp/`: LaTeX build outputs.

Scope:

This packet clears only the basis-embedding subquestion in the second open
problem from arXiv:0706.0656. It does not answer the source's universal-element
questions for `C_{omega^{alpha omega}}` or `C_{omega^alpha}`.
