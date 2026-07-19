# Literature-Implied Answer: No `C_p(X) -> C_k(X)_w` Surjection For Infinite Compact `X`

status: `literature_implied_answer (full problem)`

source_problem:
- arXiv: `2107.04662`
- paper: Jerzy Kakol and Arkady Leiderman, "On linear continuous operators between distinguished spaces `C_p(X)`"
- location: Problem 4.1, Section 4, PDF page 10

supporting_source:
- arXiv: `2509.08634`
- paper: Jerzy Kakol, Ondrej Kurka, Wieslaw Sliwa, "Lotz-Peck-Porta and Rosenthal's theorems for spaces `C_p(X)`"
- location: Introduction, immediately after Problem 1, quoting restrictions from LLP and Kakol-Leiderman2

## Identification

Problem 4.1 of `2107.04662` asks whether there exists an infinite compact space `X` admitting a continuous linear surjection
`T: C_p(X) -> C_k(X)_w`, where `C_k(X)_w` is the Banach space `C(X)` with its weak topology.

The later source `2509.08634` recalls the following restriction from Leiderman-Levin-Pestov: if `X` is Tychonoff and `E` is an infinite-dimensional normed space, then there is no sequentially continuous linear surjection from `C_p(X)` onto `E_w`. Applying this with `E=C(X)` answers Problem 4.1 negatively: for infinite compact Hausdorff `X`, the Banach space `C(X)` is infinite-dimensional, and every continuous linear map is sequentially continuous.

## Scope

This is a literature-implied answer rather than a new result. The supporting paper does not appear to state explicitly that it is resolving Problem 4.1 of `2107.04662`; the implication is obtained by matching its quoted LLP restriction to the problem statement.

## Files

- `source_paper.pdf`: original problem source, arXiv `2107.04662`.
- `supporting_paper_2509.08634.pdf`: later paper quoting the decisive no-surjection theorem.
- `figures/open_problem_crop.png`: crop of Problem 4.1 from the source PDF.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

## Verification

Cheap indexes had no exact prior packet for `2107.04662`. Local source search found the supporting `2509.08634` passage, and web search found the same two primary arXiv sources. The implication uses only: continuous implies sequentially continuous; infinite compact Hausdorff `X` implies `C(X)` is infinite-dimensional; and the quoted LLP theorem.

ledger: `runs/fa_banach_001/ledger/results/2107.04662_cp_to_weak_ck_forbidden_by_llp.json`
