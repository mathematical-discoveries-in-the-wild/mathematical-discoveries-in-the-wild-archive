# Candidate Full Solution: Weak-Net Dini Normality Characterization

Run: `fa_banach_001`

Source paper: Jochen Glueck, "Increasing sequences in ordered Banach spaces
-- new theorems and open problems", arXiv:2409.19768.

Target: Open Problem 6.2, asking whether the property that every increasing
weakly convergent net is norm convergent forces the cone of an ordered Banach
space to be normal. The source also asks whether the answer changes if the
net is assumed norm bounded.

Status: candidate full solution, likely valid. The packet proves that a closed
pointed cone is normal if and only if every increasing weakly convergent net
is norm convergent; equivalently, it is enough to test norm-bounded increasing
weakly convergent nets.

## Claim

If `X_+` is non-normal, then some order interval `[0,u]` is norm unbounded.
For every finite set of functionals, the symmetric interval `[-u,u]` remains
norm unbounded on the finite-codimensional annihilator. This lets one build a
directed net of large annihilating vectors, scale it to a decreasing positive
weakly null net with norm tending to 1, and subtract it from `u`. The result is
a norm-bounded increasing net in `[0,u]` that weakly converges to `u` but does
not converge in norm.

## Packet Files

- `source_paper.pdf`: local copy of the arXiv/source paper.
- `figures/open_problem_crop.png`: crop of Example 6.1 and Open Problem 6.2.
- `main.tex`: consolidated proof packet.
- `solution_packet.pdf`: rendered packet.
- `evidence/2026-06-21_weak_net_dini_normality/`: supplied TeX/PDF report.
- `history/packets/partial_packet_2409.19768_l1_cone_weak_net_dini_failure_2026_06_12/`: earlier active partial packet, now absorbed as history.

## Duplicate And Novelty Notes

The local duplicate check found the old explicit-cone partial packet and two
unpromoted attempts for `2409.19768`; it did not find an existing full
normality-characterization packet. The supplied report records a literature
search through 2026-06-21. This incorporation did not run a fresh external
literature search, so external novelty should be independently checked.

## Human Review Recommendation

Review as a candidate full solution. The main technical checks are the
finite-codimensional slice lemma, the principal order ideal closed-graph
argument, and the cited equivalence between non-normality and existence of an
unbounded order interval.
