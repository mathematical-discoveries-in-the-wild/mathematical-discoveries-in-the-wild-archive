# Partial solution packet: unitary representation amalgamation

Status: `partial_result_likely_valid`

Source paper: Michal Doucha, "Universal actions and representations of locally finite groups on metric spaces", arXiv:1612.09448.

Target: Question 4.5 on page 21 asks whether two unitary representations of groups `G_1,G_2` with common subgroup `G_0`, sharing an equivalent `G_0`-subrepresentation `H_0`, admit an amalgam. It also asks for the finite-group / finite-dimensional version.

Result in this packet: the unrestricted Hilbert-space amalgamation question has a positive answer. After identifying the two copies of the common `G_0`-subrepresentation, the representations amalgamate as a unitary representation of the free product with amalgamation `G_1 *_G_0 G_2`.

Strengthening added after the first packet: if `G_0,G_1,G_2` are finite and `H_0,H_1,H_2` are finite-dimensional, the amalgamating Hilbert space can also be chosen finite-dimensional. The proof pads `H_0`, `H_1 \ominus H_0`, and `H_2 \ominus H_0` inside a large multiple of the regular `G_0`-representation, then transports large regular representations of `G_1` and `G_2` that extend the fixed `G_0`-action.

Scope limitation: this still does not prove that the generated amalgamating group/image can be chosen finite. If Question 4.5 is intended as a finite Fraisse-class amalgamation question, that finite-image issue remains open in this packet. The preceding question about a universal unitary representation of a universal locally finite group is also not settled here.

Proof mechanism: for the general theorem, build the Bass-Serre tree of `G_1 *_G_0 G_2`, put a copy of `H_i` on every vertex of type `G_i`, put a copy of `H_0` on every edge, and take the Hilbert direct limit over the tree. For the finite-dimensional strengthening, replace the tree construction by regular-representation padding over `G_0`.

Evidence and verification:

- `source_paper.pdf` is the original arXiv PDF.
- `figures/open_problem_crop.png` is a crop of page 21 containing Question 4.5.
- `code/verify_packet_assets.py` checks that the source PDF contains the target question text and can reproduce the crop.
- The LaTeX packet is `main.tex`; rendered review PDF is `solution_packet.pdf`.

Novelty check: on 2026-06-19, web searches for the exact question phrase, the paper title plus "unitary representation amalgam", and variants of "amalgamate unitary representations common subgroup" did not find a separate explicit answer. This is a bounded search, not a publication-level novelty guarantee.

Human review recommendation: check the associated-bundle convention on the Bass-Serre tree, the Hilbert direct-limit lemma, and the regular-representation padding argument. Also decide whether the source's finite/fd sentence requires finite image for the generated amalgamating group; this packet does not claim that stronger interpretation.
