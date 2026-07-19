# A Dimension-Dependent Subcase of Ostrovskii's Projection-Factorization Problem

Status: `partial_result_likely_valid`

Run: `fa_banach_001`  
Agent: `agent_lane_02`  
Source paper: M. I. Ostrovskii, *Compositions of projections in Banach spaces and relations between approximation properties*, arXiv:0811.1763.

## Result

Problem 3 in the source asks whether there is a universal constant `C` such that for every triple `X_1 subset X_2 subset X_3`, with `X_1` and `X_2` finite-dimensional, there are projections `P_1:X_2 -> X_1` and `P_2:X_3 -> X_2` satisfying

```text
||P_2|| <= C lambda(X_2,X_3)
||P_1 P_2|| = lambda(X_1,X_3).
```

This packet proves a dimension-dependent version:

```text
If dim(X_1) = d, then the problem holds with C_d = 1 + 2 sqrt(d).
```

It also proves the sharper correction bound

```text
||P_2|| <= (1 + 2 lambda(X_1,X_3)) lambda(X_2,X_3).
```

The earlier one-dimensional result is the special case `d = 1`, giving `C_1 = 3`.

## Proof Mechanism

Let `P:X_3 -> X_1` be a minimal projection and `R:X_3 -> X_2` a minimal projection. Define

```text
P_1 = P|_{X_2}
P_2 x = R x + P x - P(Rx).
```

The correction term `P - (P|_{X_2})R` vanishes on `X_2`, so `P_2` is still a projection onto `X_2`. It also forces `P_1 P_2 = P`, hence the product projection is minimal onto `X_1`.

The norm estimate is

```text
||P_2|| <= lambda(X_2,X_3) + lambda(X_1,X_3) + lambda(X_1,X_3)lambda(X_2,X_3)
        <= (1 + 2 lambda(X_1,X_3)) lambda(X_2,X_3).
```

Finally, if `dim(X_1)=d`, the classical Kadets-Snobar theorem gives `lambda(X_1,X_3) <= sqrt(d)`, yielding `C_d = 1 + 2 sqrt(d)`.

## Files

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:0811.1763.
- `figures/open_problem_crop.png`: crop of Problem 3 from the source PDF.

## Verification

No computational verification is needed. The proof is a direct finite-rank correction argument using standard attainment of relative projection constants for finite-dimensional ranges, plus the classical Kadets-Snobar finite-dimensional projection theorem.

Bounded novelty checks:

- Cheap run indexes searched for `0811.1763`, title keywords, `compositions of projections`, `projectional approximation`, and approximation-property keywords.
- Local parsed corpus searched for the exact Problem 3 wording and related projection-factorization phrases.
- Web search used exact phrases from Problem 3 and the title; no obvious prior packet or published answer to this correction theorem was found.

Novelty confidence: modest. The correction theorem is elementary but gives a useful fixed-dimension strengthening of the original one-dimensional subcase; Kadets-Snobar sharpens the dimension dependence from linear to square-root.

## Limitations

This is not a full solution of Problem 3. The source asks for a single universal constant independent of `dim(X_1)`. The packet gives a constant depending on `sqrt(dim(X_1))` or, more sharply, on `lambda(X_1,X_3)`.
