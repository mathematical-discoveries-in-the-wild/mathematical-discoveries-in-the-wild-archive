# 4M-4 phase retrieval conjecture from arXiv:1302.4618

Status: `literature_already_answered`

Source/open-problem paper: Afonso S. Bandeira, Jameson Cahill, Dustin G.
Mixon, and Aaron A. Nelson, *Saving phase: Injectivity and stability for phase
retrieval*, arXiv:1302.4618.

Supporting answer papers:

- Aldo Conca, Dan Edidin, Milena Hering, and Cynthia Vinzant, *An algebraic
  characterization of injectivity in phase retrieval*, arXiv:1312.0158.
- Cynthia Vinzant, *A small frame and a certificate of its injectivity*,
  arXiv:1502.04656.

## Identification

On PDF page 7, arXiv:1302.4618 poses the `4M-4 Conjecture` for complex phase
retrieval: for measurement vectors in `C^M`, if `M >= 2`, then (a) fewer than
`4M-4` measurements should never be injective, and (b) at least `4M-4`
measurements should be injective for generic frames.  The source paper proves
only the cases `M=2` and `M=3`.

arXiv:1312.0158 explicitly identifies this conjecture and proves its generic
sufficiency half: Theorem 1.1 states that if `N >= 4M-4`, then a generic frame
has injective intensity measurements.  The introduction says this proves part
(b) of the `4M-4 Conjecture`.

arXiv:1502.04656 explicitly disproves the necessity half.  Its abstract and
introduction present a complex frame of eleven vectors in `C^4` that defines
injective measurements and says this disproves the Bandeira-Cahill-Mixon-Nelson
conjecture.  Since `4M-4=12` for `M=4`, this gives an injective example with
`N<4M-4`, contradicting part (a).

## Scope

This packet records that the `4M-4 Conjecture` as stated in arXiv:1302.4618 is
settled in the literature: part (b) is true and part (a) is false.  It does not
claim a complete classification of the exact minimal number of complex
measurements in every dimension, nor does it address the source paper's
separate stability questions or Wright-conjecture refinements.

## Search Evidence

The lane-3 queue selected arXiv:1302.4618.  Cheap run indexes were searched for
`1302.4618`, title words, `phase retrieval`, `4M-4`, and nearby supporting
authors; no duplicate durable packet for this source was found.  Targeted
searches for `4M-4 Conjecture phase retrieval`, `Saving phase 4M-4
conjecture`, `generic 4M-4 phase retrieval Conca Edidin Hering Vinzant`, and
`small frame certificate injectivity 4M-4` identified arXiv:1312.0158 and
arXiv:1502.04656 as the decisive later papers.

## Files

- `source_paper.pdf`: arXiv:1302.4618.
- `supporting_paper_1312.0158.pdf`: arXiv:1312.0158.
- `supporting_paper_1502.04656.pdf`: arXiv:1502.04656.
- `source_1302.4618.tex`: local parsed source TeX used to locate the conjecture.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.
