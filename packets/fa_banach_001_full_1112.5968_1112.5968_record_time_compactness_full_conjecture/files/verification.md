# Verification report

## Claim audited

Under exactly the hypotheses of Theorem 5.1 of arXiv:1112.5968 before its
additional conditions (a) and (b), there is a nonzero eigenvector at the cone
spectral radius. This is the full assertion conjectured in Remark 5.2.

## Source checks

- Exact source: arXiv:1112.5968v2, PDF pages 10--11.
- Theorem 5.1 first gives `z != 0` with `h(z) >= r(h,C)z` from the proper
  sup-semilattice cone, continuity, homogeneity, order preservation, and
  strict essential-spectral-radius gap.
- Its second part gives an eigenvector if such a super-eigenvector has a
  bounded normalized orbit.
- Remark 5.2 conjectures that the extra bounded-orbit assumption is
  unnecessary.
- Source Proposition 3.3 states that adjoining a relatively compact set does
  not change the homogeneous generalized measure of noncompactness.
- The definition of `nu(h^m,C)` applies to every bounded subset of `C`, and
  `rho(h,C)<1` supplies an iterate with coefficient below one.

## Formal proof audit

1. The strict gap forces `r(h,C)>0`, so scaling to `r=1` is legal.
2. Source Theorem 5.1 supplies `z<=h(z)`. Thus `z_n=h^n(z)` is increasing in
   the cone order, although its norm need not be monotone because the cone is
   not assumed normal.
3. Define `A_n=max_{j<=n}||z_j||`. The orbit definition of the cone spectral
   radius gives `limsup ||z_n||^(1/n)<=1`. Taking a finite running maximum does
   not change this upper exponential rate, while `A_n>=||z||>0`; hence
   `A_n^(1/n)->1`.
4. If `(A_n)` is bounded, the original `z` already satisfies the source
   bounded-orbit condition, so only the unbounded case needs work.
5. For fixed `L` and `eta>0`, arbitrarily late `n` satisfy
   `A_{n+L}<exp(eta)A_n`. Otherwise iteration in blocks of length `L` forces
   exponential rate at least `exp(eta/L)>1`.
6. With `L=i` and `eta=1/i`, choose `n_i` beyond all previous record
   thresholds and choose `k_i<=n_i` where the maximum `A_{n_i}` is attained.
   If `k_i+i<=n_i`, the running maximum remains constant through `k_i+i`;
   otherwise `k_i+i<=n_i+i`. In either case
   `A_{k_i+i}/A_{k_i}<exp(1/i)`.
7. The thresholds can be chosen so that `k_i>im` and `(k_i)` is strictly
   increasing. Thus every backward index used below is nonnegative.
8. Define
   `E_q={z_{k_i-qm}/A_{k_i}: i>=q+1}`. Since `k_i-qm<=k_i`, every `E_q` lies
   in the same closed unit ball; this is the point of using a running maximum
   and record times.
9. Positive homogeneity gives `E_q=h^m(E_{q+1}) union {u_q}`, where `u_q`
   is the term indexed by `i=q+1`. (If it duplicates a later term, the union
   simply adds nothing.) Proposition 3.3 and the coefficient
   `c=nu(h^m,C)<1` give
   `nu(E_q)<=c nu(E_{q+1})`.
10. Since all `E_q` lie in the unit ball,
    `nu(E_0)<=c^N nu(B_X)` for every `N`. Therefore `nu(E_0)=0`, and `E_0`
    has compact closure.
11. A convergent subsequence of the unit record vectors has a limit `x` of
    norm one. Closedness of the cone and `x_i<=h(x_i)` give `x<=h(x)`.
12. For each fixed `j`, eventually `j<=i`, and
    `||h^j(x_i)||<=A_{k_i+i}/A_{k_i}<exp(1/i)`. Continuity of `h^j` gives
    `||h^j(x)||<=1`. Hence `x` has a bounded forward orbit.
13. The second part of source Theorem 5.1 now applies to `x` and supplies a
    nonzero fixed point. Scaling back gives the desired eigenvector.

No step assumes cone normality, norm monotonicity, uniform monotonicity,
uniform continuity on bounded sets, or nonempty cone interior.

## Adversarial checks

- Norms of an order-increasing orbit may oscillate on a nonnormal cone. The
  proof never treats `||z_n||` as monotone; it uses the monotone running
  maximum `A_n`.
- The compactness estimate cannot start from forward normalized shifts,
  whose norms might be large. It starts arbitrarily far backward from record
  times, where the unit-ball bound is automatic.
- The sets `E_q` have different starting indices. Each is the shifted next
  set with one indexed point adjoined; even if that point is a duplicate,
  source Proposition 3.3 gives the required equality of measures.
- The limiting vector need not itself be fixed. The proof only claims it is a
  nonzero super-eigenvector with bounded orbit, then invokes the already
  proved conditional clause of Theorem 5.1.
- Continuity is used only for fixed iterates after selecting a norm-convergent
  record subsequence; no uniform-in-`j` passage is made.

## Novelty boundary

The following bounded checks were performed on 2026-07-22:

- run registry, solution, attempt, and proof-gap indexes;
- full parsed arXiv corpus for exact source title/citations and the phrases
  `Remark 5.2`, `bounded orbit`, `asymptotic fixed point`, `record time`, and
  `cone essential spectral radius`;
- exact-phrase web searches for the conjecture and its displayed inequality;
- the 30-work OpenAlex citation set for arXiv:1112.5968;
- nearby primary works arXiv:1302.3905, arXiv:1406.6657,
  arXiv:1612.01755, and Thieme's 2017 paper
  `doi:10.3934/dcdsb.2017053`.

No later source explicitly resolving Remark 5.2 and no matching record-time
argument were located. This is not a systematic publication-level literature
review; the status is therefore `candidate_full_solution_likely_valid`, not a
claim of certified novelty.

## PDF and reproducibility checks

`code/render_open_problem_crop.py` regenerates both source crops from the
150-dpi source-page renders. The final packet must be compiled with `latexmk`,
checked by `pdfinfo` and text extraction, scanned for LaTeX warnings and box
overflow, rendered with Poppler, and visually inspected page by page.

Final verification completed on 2026-07-22:

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed after the
  required cross-reference rerun;
- `solution_packet.pdf` has 7 letter-size pages and is not encrypted;
- the final LaTeX log contains no warnings, undefined references, errors,
  overfull boxes, or underfull boxes;
- Poppler text extraction contains the title, both lemma statements, the full
  theorem, the explicit Remark 5.2 conclusion, and the human-review section;
- all 7 pages were rendered at 144 dpi and individually inspected; equations,
  source crops, hyperlinks, headings, and page boundaries are legible, with no
  clipping, overlap, or missing glyphs.

## Human review recommendation

Prioritize Steps 5--10 above. They are the new record-time compactness
mechanism that upgrades the earlier uniformly-monotone partial theorem to the
full conjecture.
