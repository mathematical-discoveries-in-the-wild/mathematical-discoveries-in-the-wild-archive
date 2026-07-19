# Literature-Implied Answer: BCAP-Free Calkin Embedding Fails in General

- status: literature_implied_answer, likely valid
- run: `fa_banach_001`
- source arXiv id: `1301.0054`
- source paper: March T. Boedihardjo and William B. Johnson, *On Mean Ergodic Convergence in the Calkin Algebras*
- target: Remark 1 after Theorem 2.1 asks whether the Calkin representation theorem remains true without assuming that `X` has the BCAP.

## Answer

No, not in the Banach-space embedding sense of Theorem 2.1.

The previous lane-5 packet proved that the Boedihardjo--Johnson representation
norm is exactly the Hausdorff/Kolmogorov measure-of-noncompactness norm

```text
||hat T|| = gamma(T) = inf_E ||Q_E T||.
```

Astala--Tylli's 1987 results, as cited in later sources, show that this
measure-of-noncompactness quotient norm is not equivalent to the usual
essential norm on some Calkin algebra. Therefore there are operators `T_n` on
some Banach space `X` with

```text
||T_n||_e = 1,     ||hat T_n|| = gamma(T_n) -> 0.
```

Thus the representation is not bounded below for that `X`, so Theorem 2.1 does
not remain true for all Banach spaces without BCAP.

## Supporting Evidence

- Boedihardjo--Johnson ask the BCAP-free question in Remark 1 after Theorem 2.1.
- The prior lane-5 packet identifies the representation norm with the
  Hausdorff/Kolmogorov noncompactness norm.
- K. Astala and H.-O. Tylli, *On the bounded compact approximation property and
  measures of noncompactness*, J. Funct. Anal. 70 (1987), 388--401, is cited by
  later papers for the comparison between essential norm, compact approximation
  properties, and the measure-of-noncompactness quotient norm.
- A later source explicitly notes that the measure-of-noncompactness norm on
  `L(X,Y)/K(X,Y)` need not be complete, citing Astala--Tylli Theorem 2.5.
- Skillicorn's arXiv survey records that a result of Astala--Tylli gave the
  first example of a Calkin algebra with a non-unique norm; this is the
  non-equivalent measure-of-noncompactness norm.
- Crossref metadata for Dongyang Chen, *Characterizations of bounded compact
  approximation property by Calkin representations*, Proc. Amer. Math. Soc. 150
  (2022), 5397--5402, DOI `10.1090/proc/16056`, states that the paper
  characterizes BCAP via Calkin representations and lists both Boedihardjo--
  Johnson and Astala--Tylli in its references. The AMS PDF was blocked by
  Cloudflare from this environment, so the compact packet does not quote its
  theorem statement directly.

## Files

- `main.tex`: compact status note and proof of implication
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: source paper arXiv:1301.0054
- `supporting_paper_1507.08118.pdf`: Skillicorn survey
- `supporting_paper_2212.06723.pdf`: later paper quoting the Astala--Tylli theorem numbers for the noncompactness norm
- `figures/open_problem_crop.png`: source remark crop from the earlier packet

## Human Review Focus

Check the Astala--Tylli/Skillicorn identification: the non-equivalent Calkin
norm supplied by Astala--Tylli must be the Hausdorff measure-of-noncompactness
quotient norm `gamma`. Once that is confirmed, the disproof of the BCAP-free
embedding follows immediately from the prior norm-identification packet.
