# Full Solution Packet: Borel Factor-Subspace Selection

## Status

Claimed full answer to Question 6.1 in:

- Leandro Antunes, Kevin Beanland, Bruno de Mendonca Braga, *Uniformly Factoring Weakly Compact operators and Parametrized Dualization*, arXiv:1909.07475.
- Source location: Section 6, Question 6.1, PDF page 30.

The source asks whether the Borel measurable versions of Theorem 5.1, Corollary 5.12, and Corollary 5.13 hold. The answer supplied here is yes.

## Idea of the Proof

In the source proof, all maps are Borel until the final Kurka rational-amalgamation step. The authors choose an arbitrary closed tree representing the analytic range of a Borel code map and then use Jankov-von Neumann uniformization, which gives only `sigma(Sigma^1_1)` measurability.

The fix is to choose the tree differently. For a Borel map `eta:S -> N^N`, the Borel graph of `eta` has an injective closed parametrization. Projecting this parametrization onto the second coordinate gives a closed set `C subset N^N x N^N` with first projection `eta(S)` and, crucially, a Borel lift `s -> (eta(s), gamma_s)` into `C`. Using the tree with branch set `C` in the original amalgamation proof gives the required Borel branch choice.

## Packet Contents

- `main.tex`: full solution note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/open_question_page30.png`: source crop with Question 6.1.

## Verification

No computational verifier is needed. The proof is a descriptive-set-theoretic replacement of one measurability step in the published proof:

- The new closed-tree lemma is proved from the standard theorem that every Borel subset of a Polish space is a one-to-one continuous image of a closed subset of Baire space.
- The Kurka amalgamation proof is otherwise unchanged.
- The reflexivity argument remains valid because every branch of the new closed tree has first coordinate `eta(A)` for some original operator `A`.

## Novelty and Search Bounds

Cheap run-index searches for `1909.07475`, `FactoringSubspaces`, `Borel measurable versions`, `CorSBShrink`, `parametrized dualization`, and `uniformization` found no existing packet or attempt for this target.

Bounded web searches on 2026-06-14 for exact phrases including `"Borel measurable versions" "FactoringSubspaces"`, `"Uniformly Factoring Weakly Compact" "Borel measurable"`, `"1909.07475" "FactoringSubspaces"`, `"sigma(Sigma_1^1)" "FactoringSubspaces"`, `"Question 6.1" "Borel measurable versions" "FactoringSubspaces"`, `"Theorem 5.1" "Corollary 5.12" "Corollary 5.13" "Borel measurable"`, and `"Antunes" "Beanland" "Braga" "Kurka" "Borel"` returned no later answer hits beyond the source arXiv page. Searches also found arXiv:1508.02066, the earlier Braga paper whose Borel claim is explicitly corrected by the source paper.

Deeper citation/database checks on 2026-06-14:

- The paper is published as *Forum of Mathematics, Sigma* 9 (2021), e22, DOI `10.1017/fms.2020.68`.
- Crossref reports `is-referenced-by-count: 0` for the DOI.
- OpenAlex resolves the same DOI as work `W3133705180` and reports `cited_by_count: 1`.
- The one OpenAlex citing work is Cúth--Doležal--Doucha--Kurka, *Polish spaces of Banach spaces: Complexity of isometry and isomorphism classes*, DOI `10.1017/s1474748023000440`. Text extraction from the published PDF shows the Antunes--Beanland--Braga paper appears only in the bibliography; searches inside that PDF for `Borel measurable`, `FactoringSubspaces`, `CorSBRefl`, `CorSBShrink`, `uniformization`, and `Question 6.1` found no hits.
- arXiv API exact-phrase searches for `"Borel measurable versions"`, `"FactoringSubspaces"`, and `"CorSBShrink"` returned zero results.
- Semantic Scholar API access was rate-limited during this pass, so no Semantic Scholar citation list was used.

This is still not an exhaustive proof of historical novelty. Treat the novelty status as: no known answer found by local run search, local parsed-corpus search, exact public web search, arXiv API phrase search, Crossref, OpenAlex citation inspection, and manual inspection of the one OpenAlex citing paper.

## Human Review Recommendation

Review the closed-tree lemma and confirm that replacing the arbitrary analytic tree by this graph-parametrized closed tree preserves the hypotheses of Kurka's amalgamation proposition. For Corollary 5.13, also check the omitted proof in the source paper/Braga 2015: the packet uses the source authors' statement that the same rational-amalgamation step is the only measurability obstruction.
