# Triage And Search Notes

## Source Signal

The deterministic scan hit arXiv:2011.14591 at the remark after Proposition
`bochner bdp` in the section `Lebesgue Bochner Function Spaces`.

The source asks whether the converses of Propositions `bochner bhp` and
`bochner bdp` are true in general. It immediately notes that the BHP converse
fails for `p=1`: `R` has BHP, but scalar `L^1[0,1]` does not.

## Viability Check

Local indexes were searched for:

```text
2011.14591
2108.02908
BDP / BHP / BSCSP
Lebesgue-Bochner
L^p(mu,X)
bochner bdp / bochner bhp
small diameter properties
Kothe-Bochner
```

No prior packet for this BDP-converse consequence was found. The same paper is
also present as arXiv:2108.02908 with substantial text overlap.

## Later Literature Check

The later paper arXiv:2307.03631, `Two aspects of small diameter properties`,
was checked because it explicitly revisits Kothe-Bochner stability. It proves:

```text
E(X) has BDP  => X has BDP
E(X) has BHP  => X has BHP
```

under its Kothe-Bochner hypotheses, and leaves the analogous BSCSP question
open. This is adjacent to the target but does not answer or supersede the
scalar p=1 BDP-converse counterexample.

Web searches for exact phrases from the source remark and close variants
returned the source arXiv page and the 2023 sequel, but no separate explicit
answer to the BDP converse.

## Final Scope

The promoted packet records the p=1 counterexample:

```text
X = R has BDP, but L^1([0,1], R) = L^1[0,1] has no slice of diameter < 2.
```

This closes the unrestricted `in general` BDP converse question. It does not
claim a result for `1 < p < infinity`, purely atomic measures, or the later
Kothe-Bochner BSCSP question.
