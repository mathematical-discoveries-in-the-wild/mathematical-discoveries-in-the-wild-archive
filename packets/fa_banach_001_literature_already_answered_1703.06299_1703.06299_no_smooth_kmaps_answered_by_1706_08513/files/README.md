# Literature-Already-Answered Packet: Banach spaces without smooth K-maps

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Genrich Belitskii and Victoria Rayskin, *Extension of local smooth maps of Banach spaces*, arXiv:1703.06299.
- Local PDF: `source_paper.pdf`.

In Section 5, Open questions, item 1 asks for which spaces `C^\infty` K-maps exist and specifically asks whether Banach spaces without `C^\infty` K-maps exist. It also asks the separate harder subquestion whether such maps exist on `l_p` for non-even `p`.

The source definition says that a `C^q` K-map is a globally defined bounded `C^q` representative of the identity germ at the origin; equivalently, it is a bounded `C^q` local identity.

## Supporting Answer Source

- Genrich Belitskii and Victoria Rayskin, *A New Method of Extension of Local Maps of Banach Spaces. Applications and Examples*, arXiv:1706.08513.
- Local PDF: `supporting_paper_1706.08513.pdf`.
- Underlying cited result: S. D'Alessandro and P. Hajek, *Polynomial algebras and smooth functions in Banach spaces*, Journal of Functional Analysis 266 (2014), 1627--1646, DOI `10.1016/j.jfa.2013.11.017`; see also P. Hajek and M. Johanis, *Smooth Analysis in Banach Spaces*, de Gruyter, 2014.

## Status

The existence subquestion is already answered affirmatively in the later literature: there are Banach spaces without smooth K-maps.

The terminology changes from `K-map` in arXiv:1703.06299 to `blid map` in arXiv:1706.08513, but the definitions coincide. The later paper defines a `C^q` blid map as a globally defined bounded local identity at zero. In Section "More examples and open questions", the later paper states that the question whether Banach spaces without smooth blid maps exist has an affirmative answer, citing D'Alessandro--Hajek and Hajek--Johanis: those works provide Banach spaces that do not allow `C^2` extension, and hence do not admit a `C^2` blid map. A fortiori such spaces cannot admit a `C^\infty` blid/K-map.

## Verification Notes

- Same-paper check: arXiv:1703.06299 asks the existence question in its open-questions section and does not answer it there.
- Definition check: arXiv:1703.06299's K-map and arXiv:1706.08513's blid map are the same object: a bounded smooth map that agrees with the identity near zero.
- Separate-source check: arXiv:1706.08513 is a later distinct source and explicitly records the affirmative status, with bibliographic pointers to the underlying D'Alessandro--Hajek / Hajek--Johanis results.
- Logical implication: absence of a `C^2` blid map rules out the existence of a `C^\infty` K-map, since every `C^\infty` K-map is in particular a `C^2` bounded local identity.

## Search Bounds

- Checked the active state and local source passages for arXiv:1703.06299.
- Searched the run registry, ledger, solutions, and attempts for `1703.06299`, `1706.08513`, `K-map`, `blid`, `bounded local identity`, `smooth blid`, and `l_p` non-even variants.
- Found an existing no-promotion attempt for the separate non-even `l_p` blid subquestion in arXiv:1706.08513 and an existing weak-topology partial packet for arXiv:1812.11064; neither is this existence-status packet.
- Checked the later arXiv:1706.08513 source passage and its bibliography.
- Verified the D'Alessandro--Hajek bibliographic record and DOI by web search.

## Limitations

This packet only records the affirmative answer to the existence of Banach spaces without smooth K-maps. It does not classify the spaces that admit K/blid maps. It does not answer the non-even `l_p` problem, the sphere-in-`C[0,1]` problem, the arbitrary subspace of `C[0,1]` problem, or the infinite-dimensional Whitney-extension question.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original arXiv:1703.06299 PDF.
- `supporting_paper_1706.08513.pdf`: later arXiv:1706.08513 PDF with the explicit status statement.
- `tmp/`: local render intermediates.

## Human Review Recommendation

Verify the terminology identification between K-maps and blid maps, and check whether reviewers want the underlying D'Alessandro--Hajek JFA paper copied into the packet when publisher access permits. The mathematical status recorded here depends only on the later explicit status statement plus the elementary implication from no `C^2` blid map to no `C^\infty` K-map.
