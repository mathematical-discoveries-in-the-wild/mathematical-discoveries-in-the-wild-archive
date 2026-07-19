# Partial result: zero-dimensional measure extraction is stable under the source-paper extension step

Status: `partial_result_likely_valid`

Source paper: Damian Glodkowski, "A Banach space C(K) reading the dimension of K", arXiv:2207.00149.

Targeted problem: Problem 7.3 asks for a description of compact Hausdorff spaces \(K\) such that every non-zero Radon measure on \(K\) has a non-zero-measure zero-dimensional compact subset.

## Result

The packet proves a strong closure theorem for a strengthened version of the property:

> For every finite positive Radon measure \(\mu\) on \(K\) and every \(\eta>0\), there is a compact zero-dimensional \(Z\subseteq K\) with \(\mu(K\setminus Z)<\eta\).

This strong property:

- is inherited by compact subspaces;
- holds for compact metrizable spaces and for zero-dimensional compact spaces;
- is preserved by finite products;
- is preserved by the extension operation used in the source paper, provided the exceptional set \(K\setminus D((f_n))\) is zero-dimensional.

Consequently, every finite tower of the source-paper dimension-preserving extension steps, starting from a compact metrizable space, has the strong measure-extraction property.

## Why This Is Only Partial

This does not remove the set-theoretic hypothesis from the paper's main theorem. The construction needs the extracted zero-dimensional compact set to be usable through a countable decreasing neighbourhood sequence, and this packet only gives a compact zero-dimensional set, not a \(G_\delta\) or countable-character one. Limit stages of long inverse systems are also not settled by the closure theorem.

## Novelty Check

Local run indexes had no prior packet for arXiv:2207.00149 or Problem 7.3. Web searches for the exact problem phrase, "zero-dimensional compact subset non-zero Radon measure", "Radon measure compact Hausdorff zero-dimensional subset", and Maharam/uniform-regularity variants did not reveal a later paper explicitly answering Problem 7.3. Related literature on uniformly regular measures and simple extensions was found, but it does not by itself provide the \(G_\delta\) extraction needed for the full ZFC construction route.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2207.00149.
- `figures/open_problem_crop.png`: crop of Problem 7.3 from the source PDF.

## Human Review Recommendation

Review as a useful partial theorem around Problem 7.3. The key points to check are the extension-step decomposition over \(D((f_n))\) and \(K\setminus D((f_n))\), and whether the strong property can be sharpened to require the zero-dimensional compact subset to be \(G_\delta\) in the non-metrizable settings relevant to the ZFC construction.
