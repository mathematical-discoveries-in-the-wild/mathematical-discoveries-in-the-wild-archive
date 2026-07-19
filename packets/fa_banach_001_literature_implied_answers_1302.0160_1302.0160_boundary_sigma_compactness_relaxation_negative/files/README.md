# Literature-implied answer: dropping `w*`-sigma-compactness in Theorem `boundary`

Status: `literature_implied_answer` for arXiv:1302.0160.

## Source target

The source paper is V. P. Fonf, A. J. Pallares, R. J. Smith, and S. Troyanski,
*Polyhedrality in Pieces*, arXiv:1302.0160.  The target is the remark after
Theorem `boundary`: the theorem assumes that `E subset X*` is both
`sigma-w*`-LRC and `w*`-sigma-compact, and the authors say that the
`w*`-sigma-compactness is imposed to control limit points and that they do not
know how far it can be relaxed.

## Identification

The broad relaxation obtained by simply deleting `w*`-sigma-compactness is
impossible.  Smith, arXiv:1804.02899, records Bible's example of a Banach space
`Z = ell_1 direct_sum ell_1(S_{ell_infty})` which is neither Asplund nor
`c_0`-saturated, hence is not isomorphically polyhedral, but which admits an
equivalent norm with a relatively `w*`-discrete boundary.

Smith also recalls that any relatively `w*`-discrete subset of a dual Banach
space is `w*`-LRC.  Thus Bible's boundary is already `sigma-w*`-LRC, using one
piece.  If Theorem `boundary` from arXiv:1302.0160 remained true after deleting
the `w*`-sigma-compactness hypothesis, this renormed `Z` would admit an
equivalent polyhedral norm.  That contradicts Smith's necessary conditions.

## Scope

This packet gives a negative answer only to the strongest naive relaxation:

```text
sigma-w*-LRC boundary alone does not force isomorphic polyhedrality.
```

It does not rule out intermediate hypotheses that still control weak-star
limit points, such as closure-inside-`E` decompositions, compactly generated
subclasses, or other explicit substitutes for the `w*`-sigma-compactness used
in the source proof.

## Evidence files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_1302.0160.tex`: parsed source TeX for the original paper.
- `supporting_source_1804.02899.tex`: parsed supporting TeX for Smith's paper.
- `related_source_2502.17001.tex`: parsed related later source that isolates
  the weak-star sigma-discrete boundary implication.

The local arXiv cache contains source downloads but no PDFs for these ids at
packet creation time.
