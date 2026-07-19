# Literature-implied partial answer: local block-minimal analogue

Status: `literature_implied_answer (partial local-block-minimal variant)`

Source/open-problem paper: arXiv:1111.6444, Valentin Ferenczi and Gilles
Godefroy, *Tightness of Banach spaces and Baire category*.

Supporting paper: arXiv:0711.1350, Valentin Ferenczi and Christian Rosendal,
*Banach spaces without minimal subspaces*.

## Identification

The source paper asks, at the end of Section 4, for a space `X` which embeds
as a block-subspace of all its block-subspaces while the block-subspace
isomorphism relation `Is` is meager.

This packet records a known theorem that answers the natural weaker variant
with `locally block minimal` in place of `block-minimal`: arXiv:0711.1350,
Example `OdellSchlumprecht`, proves that there exists a reflexive Banach space
which is tight and locally block minimal.

The source paper itself proves that if a space with a basis is tight, then the
embeddability relation `Emb` is meager on `b(X)^2`; since `Is` is contained in
`Emb`, the same supporting example has meager `Is`.

## Scope

This does **not** solve the exact source problem.  Local block minimality is a
finite-dimensional/block finite-representability property, weaker than
requiring a copy of `X` inside every block-subspace.  The exact block-minimal
construction remains open from this packet's point of view.

## Files

- `main.tex` - compact status note.
- `solution_packet.pdf` - rendered status note.
- `source_paper.pdf` - arXiv:1111.6444.
- `supporting_paper_0711.1350.pdf` - arXiv:0711.1350.

## Search Notes

The run indexes were searched for `1111.6444`, the source title,
`block-minimal`, `block minimal`, `locally block minimal`, `Is is meager`, and
the exact problem sentence.  No existing packet for this implication was
found.  Web searches for the exact block-minimal problem and close variants did
not reveal a later exact solution during this bounded pass.
