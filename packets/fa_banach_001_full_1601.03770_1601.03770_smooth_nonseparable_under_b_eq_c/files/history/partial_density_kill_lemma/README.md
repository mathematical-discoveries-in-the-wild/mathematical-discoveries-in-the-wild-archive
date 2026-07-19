# Bounding-number density-killing lemma for smooth compactifications

Status: `partial_result_likely_valid`

Source paper: Piotr Drygier and Grzegorz Plebanek, *Compactifications of
\(\omega\) and the Banach space \(c_0\)*, arXiv:1601.03770.

Supporting source: Piotr Drygier and Grzegorz Plebanek, *Nonseparable growth of
the integers supporting a measure*, arXiv:1501.06972.

## Target

The source paper asks which compactifications \(\gamma\omega\) are smooth, i.e.
when the natural copy of \(c_0\) is complemented in \(C(\gamma\omega)\).  It
proves under CH that there is a smooth compactification with nonseparable
remainder, and notes that the authors do not know whether this can be proved in
ZFC; they also suggest that the argument may relax to \(\mathfrak b=\mathfrak c\).

## Result

This packet proves the local strengthening needed for that relaxation.

The source Lemma 6.3 is a countable-algebra step: given a countable Boolean
algebra \(\mathcal B\), a countable dense family of nonprincipal ultrafilters,
and a sequence of nonatomic measures witnessing smoothness, one can add a set
\(X\subseteq\omega\) that destroys density of that family while preserving the
measure witness.

Here the same conclusion is proved for every Boolean algebra
\(\mathcal B\subseteq P(\omega)\) of cardinality \(<\mathfrak b\).  The proof
uses the domination/s-family lemma from arXiv:1501.06972 to replace the
countable enumeration of \(\mathcal B\).

Concretely, if \(|\mathcal B|<\mathfrak b\), \((p_j)\) is countable dense in
\(K_\mathcal B^*\), and \((\nu_n)\) is a nonatomic probability sequence on
\(\mathcal B\) with \(\nu_n|\mathrm{Fin}=0\) and
\(\nu_n-\delta_n\to0\) pointwise on \(\mathcal B\), then there is an infinite
\(X\subseteq\omega\) such that:

- every extension of the \(p_j\)'s to \(\mathcal B[X]\) is non-dense in
  \(K_{\mathcal B[X]}^*\);
- the measures \(\nu_n\) extend to nonatomic probabilities
  \(\widetilde\nu_n\) on \(\mathcal B[X]\) with
  \(\widetilde\nu_n-\delta_n\to0\).

## Scope

This does not yet prove the full \(\mathfrak b=\mathfrak c\) version of the
large smooth compactification theorem.  The remaining issue is global
bookkeeping: one must present all countable dense extension candidates along a
long construction without losing the ability to apply the \(<\mathfrak b\)
local lemma.  The packet isolates and solves the local countability bottleneck.

## Verification

- Cheap indexes were searched for `1601.03770`, `1501.06972`, `smooth
  compactification`, `nonseparable remainder`, and `b=c`; no duplicate packet
  or prior attempt for this target was found.
- Web search found the source arXiv record and the companion arXiv:1501.06972
  result on nonseparable growth supporting a measure under \(\mathfrak b =
  \mathfrak c\), but no later smoothness answer.
- The LaTeX packet renders successfully to `solution_packet.pdf`.

## Human Review Focus

Check the construction of the decreasing sets \(S_j(k)\), especially the finite
bad-set absorption that gives
\(\nu_n(S_j(k))<2^{-(j+3)}\) whenever \(n\notin S_j(k)\).  Then check the use
of the \(<\mathfrak b\) s-family finite-cover lemma and the inner/outer measure
estimates used to extend \(\nu_n\) over \(\mathcal B[X]\).
