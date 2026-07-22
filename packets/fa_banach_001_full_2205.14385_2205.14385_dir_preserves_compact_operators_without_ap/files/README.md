# Compact operators remain compact under the bidual direct-limit functor

status: `candidate_full_solution_likely_valid`

model: `GPT5.6`

## Source and exact question

- Sebastian Gwizdek, *Isometric direct limits of bidual Banach spaces*,
  arXiv:2205.14385.
- Location: PDF page 11, immediately after the compactness theorem in
  Section 2; labelled Hypothesis 2.14.
- Source transcription:

  > We conjecture that the approximation property assumption can be omitted.
  > **Hypothesis 2.14.** For any Banach space \(X\) if \(T\in B(X)\) is a
  > compact operator then \(\operatorname{Dir}(T)\) is a compact operator.

The local source PDF is `source_paper.pdf`, and the rendered source evidence is
`figures/open_problem_crop.png`.

## Claimed contribution

Hypothesis 2.14 is true. In fact, the self-map assumption is unnecessary:

> **Theorem.** Let \(X,Y\) be Banach spaces and let \(T:X\to Y\) be compact.
> Then
> \[
>   \operatorname{Dir}(T):\operatorname{Dir}(X)\longrightarrow
>   \operatorname{Dir}(Y)
> \]
> is compact.

No approximation property is assumed on either space. For a compact
\(T\in B(X)\), the source's adjoint identification also gives compactness of
\(\operatorname{Inv}(T)\) by Schauder's theorem.

## Proof intuition

The source approximates a compact operator by finite-rank operators, which is
where the approximation property enters. The direct argument instead follows
the compact image itself through the tower.

If \(S:E\to F\) is compact and
\(K=\overline{S(B_E)}\), Goldstine's theorem and weak-star continuity of
\(S^{**}\) show
\[
  S^{**}(B_{E^{**}})\subseteq \kappa_F(K).
\]
Thus bidualization creates no new image points: it only moves the same compact
set into the canonical copy of \(F\) inside \(F^{**}\). Iterating this fact
shows that the image of the unit ball at every finite tower stage lies in the
canonical copy of the original compact set \(K\) inside
\(\operatorname{Dir}(Y)\). Density of the algebraic direct limit in its
completion then gives the same containment for the completed unit ball.

## Formal proof

For a Banach space \(X\), write
\[
 X_0=X,\qquad X_{n+1}=X_n^{**},
\]
and let \(\kappa^X_{n,n+1}:X_n\to X_{n+1}\) be the canonical embedding.
Write \(\iota_n^X:X_n\to\operatorname{Dir}(X)\) for the canonical isometry.
For \(T:X\to Y\), set \(T_0=T\) and \(T_{n+1}=T_n^{**}\). By construction,
\[
 \operatorname{Dir}(T)\,\iota_n^X=\iota_n^Y T_n.
\]

**Lemma.** If \(S:E\to F\) is compact and
\(K=\overline{S(B_E)}\), then
\[
 S^{**}(B_{E^{**}})\subseteq \kappa_F(K).
\]

**Proof of the lemma.** Fix \(z\in B_{E^{**}}\). By Goldstine's theorem there
is a net \((x_\alpha)\subseteq B_E\) such that
\(\kappa_E x_\alpha\to z\) in \(\sigma(E^{**},E^*)\). Hence
\[
 \kappa_F(Sx_\alpha)=S^{**}(\kappa_E x_\alpha)
       \longrightarrow S^{**}z
\]
in \(\sigma(F^{**},F^*)\). The set \(K\) is norm compact. Consequently
\(\kappa_F(K)\) is weak-star compact, hence weak-star closed in the Hausdorff
space \(F^{**}\) with its weak-star topology. Every term of the displayed net
lies in \(\kappa_F(K)\), so its limit \(S^{**}z\) does as well. This proves
the lemma.

Now let \(T:X\to Y\) be compact and put
\[
 K_n=\overline{T_n(B_{X_n})}\subseteq Y_n.
\]
The lemma, used inductively, gives both compactness of every \(T_n\) and
\[
 K_{n+1}\subseteq \kappa^Y_{n,n+1}(K_n).
\]
Therefore, for every \(n\),
\[
 \iota_n^Y(K_n)\subseteq \iota_0^Y(K_0),
\]
because the canonical maps in a direct limit satisfy
\(\iota_{n+1}^Y\kappa^Y_{n,n+1}=\iota_n^Y\). It follows that
\[
 \operatorname{Dir}(T)(A_X\cap B_{\operatorname{Dir}(X)})
 \subseteq \iota_0^Y(K_0),
 \qquad
 A_X:=\bigcup_{n\ge 0}\iota_n^X(X_n).
\]

The set \(A_X\) is dense in \(\operatorname{Dir}(X)\), and its unit ball is
dense in the completed unit ball: if \(a_j\in A_X\) tends to a point of norm
at most one, replace \(a_j\) by
\(a_j/\max\{1,\lVert a_j\rVert\}\). Since \(\operatorname{Dir}(T)\) is
continuous and \(\iota_0^Y(K_0)\) is compact, hence closed, the preceding
containment passes to the completion:
\[
 \operatorname{Dir}(T)(B_{\operatorname{Dir}(X)})
 \subseteq \iota_0^Y(K_0).
\]
The image of the unit ball is therefore relatively compact, so
\(\operatorname{Dir}(T)\) is compact. \(\square\)

## Verification status

The proof received an adversarial step-by-step audit recorded in
`verification.md`. The audit specifically checks:

1. that \(\kappa_F(K)\) really is weak-star closed;
2. that the compact sets nest in the correct direction under every bidual;
3. that the unit ball of the algebraic direct limit is dense in the completed
   unit ball; and
4. that the claimed `Inv` corollary uses the source's adjoint identification.

No computational verifier is relevant: the argument is qualitative and uses
only compactness, Goldstine's theorem, and the direct-limit identities. See
`code/README.md`.

## Bounded novelty check

Performed on 21 July 2026. The following were searched:

- the run's `registry_index.tsv`, `solutions/index.tsv`, and
  `attempts/index.tsv` for arXiv:2205.14385 and the phrases “Dir compact”,
  “bidual direct limit compact operator”, and “approximation property”;
- arXiv/web searches using the exact conjecture sentence, the paper title,
  the arXiv id, the author, “Hypothesis 2.14”, and close variants involving
  compactness of \(\operatorname{Dir}(T)\);
- visible citation/title results for later work by the author, including the
  2025 Polish dissertation *Izometryczne granice induktywne przestrzeni
  dualnych*.

No later paper explicitly resolving Hypothesis 2.14 was found in this bounded
search. The dissertation material visible in the search results still
describes compactness with an extra assumption and traces the result to the
source paper. This is negative search evidence only, not a priority claim or
an exhaustive literature review.

## Limitations and human-review recommendation

- Status remains `candidate_full_solution_likely_valid` until human review.
- The result is a full answer to Hypothesis 2.14 and a stronger two-space
  theorem. It does not assert any additional preservation property for
  noncompact operators.
- Recommended human action: verify the compact-image lemma and the passage
  from the algebraic direct-limit unit ball to the completed unit ball. These
  are the only substantive proof steps.

## References

1. Sebastian Gwizdek, *Isometric direct limits of bidual Banach spaces*,
   arXiv:2205.14385 (2022; source PDF version dated 2023).
2. Robert E. Megginson, *An Introduction to Banach Space Theory*, Graduate
   Texts in Mathematics 183, Springer, 1998. Standard reference for
   Goldstine's and Schauder's theorems.
