# Conditional packet: weakening GCH to diamond plus coding arithmetic

## Source

- Paper: P. Koszmider, S. Shelah, M. Swietek, *There is no bound on sizes of indecomposable Banach spaces*
- arXiv: `1603.01753`
- Published version: Adv. Math. 323 (2018), 745--783
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `conditional`
- Source question: Introduction, page 5, after the repeated Theorem 5.3, asks whether the generalized continuum hypothesis can be removed from Theorem 1.3.
- Packet claim: for any regular cardinal `kappa` which is the successor of a cardinal of uncountable cofinality, the source construction and conclusion of Theorem 5.3 go through assuming only:

```text
diamond(E^kappa_omega),
kappa^omega = kappa,
and alpha^omega < kappa for every alpha < kappa.
```

Consequently, whenever such cardinals occur above a prescribed cardinal, the corresponding instance of Theorem 1.3 follows without assuming full GCH.

## Conditional Dependencies

This packet does not prove the needed set-theoretic hypotheses in ZFC. It records a conditional reduction: full GCH is stronger than needed in the source proof, but `diamond(E^kappa_omega)` and the displayed countable-coding arithmetic remain assumptions.

## Proof Intuition

The source proof invokes GCH in only two roles. First, it provides the countable cardinal arithmetic used to keep the completed free Boolean algebra and all countable codes at size `kappa`, and to make the coding-closure set club. Second, by Gregory's theorem it provides a `diamond(E^kappa_omega)` sequence. Once these two ingredients are assumed directly, the ladder-family recursion, asymmetric-distribution verification, and Banach-space consequences run unchanged.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_page5_gch_removal.png`: crop of the source open question.
- `code/crop_evidence.py`: reproduces the evidence crop with PyMuPDF.
- `tmp/`: LaTeX build output.

## Verification Notes

The run indexes had no prior packet/attempt/proof-gap for arXiv:1603.01753 or the GCH-removal question. Local corpus searches for the title, authors, `GCH`, `diamond`, `few operators`, `black boxes`, and later indecomposable-space papers did not reveal a later exact answer. A web search for the exact title and for GCH-removal phrases likewise found no separate paper explicitly removing GCH from the arbitrary-density few-operators construction.

The main reviewer focus is set-theoretic: verify that no hidden use of GCH remains outside the two displayed hypotheses, especially in Lemma 3.13 (`density-cardinality`), the existence of the coding map `Psi`, and the clubness of `C_Psi`.
