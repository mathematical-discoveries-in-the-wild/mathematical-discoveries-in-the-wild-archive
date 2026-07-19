# Full Solution Packet: Countable \(C(K)\) Calkin Lifts Have Stable Rank One

Status: `full_solution_likely_valid`

Run: `fa_banach_001`  
Agent: `agent_super_01`  
Source paper: Bence Horvath, *Banach spaces whose algebras of operators are Dedekind-finite but they do not have stable rank one*, arXiv:1807.10578.

## Target

Remark 2.23 of the source paper discusses the Motakis--Puglisi--Zisimopoulou spaces \(X_K\), where \(K\) is countable compact metric and
\[
  \mathcal B(X_K)/\mathcal K(X_K) \simeq C(K).
\]
The paper observes that \(\mathcal B(X_K)\) has left stable rank \(1\) or \(2\), then asks whether some such \(K\) could make \(\mathcal B(X_K)\) Dedekind-finite but not stable-rank-one.

## Result

No. More strongly, if \(X\) is any complex Banach space and \(K\) is countable compact metric with
\[
  \mathcal B(X)/\mathcal K(X) \simeq C(K)
\]
as unital Banach algebras, then \(\mathcal B(X)\) has stable rank one.

Thus the MPZ examples \(X_K\) cannot give further Dedekind-finite/non-stable-rank-one examples in the countable compact metric \(C(K)\) Calkin family.

## Proof Intuition

The source paper's method for proving Dedekind-finiteness only needs invertibles in the quotient to lift, and the author notes that connectedness-based lifting is not applicable because \(K\) is totally disconnected. The missing observation is that total disconnectedness is actually favorable for stable rank one: countable compact metric \(K\) is zero-dimensional, and for zero-dimensional compact \(K\), \(C(K)\) has dense invertibles and its invertible group is path-connected.

Once the quotient \(C(K)\) has stable rank one and connected invertibles, the compact ideal supplies the other half. Horvath's Proposition 2.7 gives stable rank one for the unitization of \(\mathcal K(X)\). A short extension lemma then upgrades these two stable-rank-one facts, plus quotient invertible lifting, to stable rank one of the full algebra \(\mathcal B(X)\).

## Files

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local rendering of arXiv:1807.10578 from cached source.
- `figures/open_problem_crop.png`: rendered source crop containing Remark 2.23 and the target question.
- `figures/open_problem_page.png`: full rendered page 7 of the source PDF.
- `code/README.md`: notes that no computational verification is needed.

## Verification And Novelty Check

The packet was rendered with `pdflatex`. The proof is purely functional-analytic/topological; no numerical computation is involved.

Before promotion, the cheap run indexes were searched for `1807.10578`, `Dedekind-finite`, `stable rank`, `X_K`, `Calkin`, `MPZ`, and countable compact `C(K)` phrases. Hits were adjacent Calkin-algebra packets but no duplicate of this stable-rank-one conclusion. A bounded external web search for the exact phrases around `B(X_K)`, `stable rank one`, `C(K)`, `Calkin`, and `1807.10578` did not find an exact prior answer. Local source checks included the source paper and Motakis's later arXiv:2110.10868 paper, which records complementary structure and a Dedekind-finiteness route but not this stable-rank-one extension observation.

Novelty confidence: `moderate`. The argument is short and standard once isolated, so human review should check whether this extension lemma appears implicitly in Banach-algebra stable-rank folklore.

## Human Review Recommendation

Review as a likely valid full solution to the specific countable compact metric \(C(K)\)-Calkin question in Remark 2.23. The main points to verify are the stable-rank-one extension lemma and the elementary zero-dimensional \(C(K)\) logarithm/approximation argument.
