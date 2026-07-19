# Smooth nonseparable compactification under b = c

Status: `full_solution_likely_valid (b=c strengthening; ZFC case remains open)`

Source paper: Piotr Drygier and Grzegorz Plebanek, *Compactifications of
\(\omega\) and the Banach space \(c_0\)*, arXiv:1601.03770.

Supporting source: Piotr Drygier and Grzegorz Plebanek, *Nonseparable growth of
the integers supporting a measure*, arXiv:1501.06972.

## Target

The source proves under CH that there is a smooth compactification
\(\gamma\omega\) whose remainder is nonseparable, and comments that the authors
expect their argument may relax to \(\mathfrak b=\mathfrak c\).  This packet
proves that strengthening.

## Result

Assume \(\mathfrak b=\mathfrak c\).  Then there is a compactification
\(\gamma\omega\) of the discrete natural numbers such that:

- the natural copy of \(c_0\) is complemented in \(C(\gamma\omega)\);
- the remainder \(\gamma\omega\setminus\omega\) is nonseparable.

Equivalently, there is a Boolean algebra
\(\mathrm{Fin}\subseteq\mathcal A\subseteq P(\omega)\) carrying probability
measures \((\mu_n)\) with \(\mu_n|\mathrm{Fin}=0\) and
\(\mu_n-\delta_n\to0\) pointwise on \(\mathcal A\), while
\(\mathcal A/\mathrm{Fin}\) is not \(\sigma\)-centered.

## Proof Idea

The earlier partial packet proved that the source paper's countable
density-killing lemma works for Boolean algebras of size \(<\mathfrak b\).  The
full promotion adds the missing bookkeeping observation.

At stage \(\xi<\mathfrak c=\mathfrak b\), the current algebra still has size
\(<\mathfrak b\).  If its remainder is already nonseparable, we stop.  If not,
choose a countable dense set in the current remainder.  The successor step uses
two countable families simultaneously:

- a fixed enumerated dense set in the initial Cantor-like remainder, to ensure
  every future extension of that base dense set contains the new set \(X_\xi\);
- a dense set in the current remainder, to ensure
  \(\nu_n^*(X_\xi)=1\) and preserve the smoothness measures by
  Los--Marczewski extension.

If the final remainder had a countable dense set, its restriction to the
initial algebra would appear in the \(\mathfrak c\)-length enumeration.  At the
corresponding stage, all future extensions of those base ultrafilters are forced
to contain \(X_\xi\), while the nonempty clopen
\(\omega\setminus X_\xi\) remains missed.  Contradiction.

## Scope

This proves the advertised \(\mathfrak b=\mathfrak c\) strengthening of the
source CH theorem.  It does not settle the stronger ZFC question mentioned in
the source.

## Verification

- Cheap indexes were searched for `1601.03770`, `1501.06972`, `smooth
  compactification`, `nonseparable remainder`, and `b=c`.
- Web search for the same phrases found the source and the companion
  nonseparable-growth paper, but no later smoothness theorem.
- The previous local partial packet is preserved under
  `history/partial_density_kill_lemma/`.
- The LaTeX packet renders successfully to `solution_packet.pdf`.

## Human Review Focus

Review the successor lemma first.  The key point is that the base dense family
forces every future extension to contain \(X\), while the current dense family
is used only for the measure outer-measure estimate.  Then check the
\(\mathfrak b=\mathfrak c\) induction and the final nonseparability
contradiction.
