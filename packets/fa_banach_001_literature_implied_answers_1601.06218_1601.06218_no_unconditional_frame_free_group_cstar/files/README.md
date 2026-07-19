# Literature-Implied Answer: no unconditional frame for \(C_r^*(F_2)\)

- Source/open-problem paper: Rui Liu and Zhong-Jin Ruan, *Cb-frames for operator spaces*, arXiv:1601.06218.
- Supporting paper: Samir Kabbaj and Rafik Karkri, *Structure of Banach spaces and besselian Schauder frames*, arXiv:2411.00777.
- Packet status: `literature_implied_answer`.
- Scope: negative answer to the source paper's Remark 2.2 sentence asking whether there is any unconditional frame for \(C_r^*(F_2)\). This does **not** settle the broader cb-basis problem for separable C*-algebras or weakly amenable reduced group C*-algebras.

## Identification

Liu--Ruan construct a concrete cb-frame for \(C_r^*(F_2)\) and note in Remark 2.2 that their frame is not unconditional. They end the remark by saying it is not known whether there is any unconditional frame for \(C_r^*(F_2)\).

Kabbaj--Karkri later prove that unconditional Schauder frames are Besselian and that a Banach space with a Besselian frame has Pełczyński's property (u). They also record that \(C([0,1])\) has no Besselian frame, hence no unconditional frame.

The bridge is standard: if \(a\) is a free generator and \(H=\langle a\rangle\cong\mathbb Z\), the canonical Fourier projection is a contractive conditional expectation
\[
E_H:C_r^*(F_2)\to C_r^*(H)\cong C(\mathbb T).
\]
Unconditional frames pass to complemented subspaces. Thus an unconditional frame for \(C_r^*(F_2)\) would give one for \(C(\mathbb T)\), and \(C(\mathbb T)\) is isomorphic to \(C([0,1])\) by the classical Milutin theorem. This contradicts the supporting paper's no-unconditional-frame result for \(C([0,1])\).

## Files

- `source_paper.pdf`: local copy of arXiv:1601.06218.
- `supporting_paper_2411.00777.pdf`: local copy of arXiv:2411.00777.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

## Review Notes

This is an agent-identified implication: the supporting paper does not appear to explicitly cite the Liu--Ruan question. Human review should mainly check the terminology match between "unconditional frame" in Liu--Ruan and "unconditional Schauder frame" in Kabbaj--Karkri, and the standard conditional expectation \(C_r^*(F_2)\to C_r^*(\mathbb Z)\).
