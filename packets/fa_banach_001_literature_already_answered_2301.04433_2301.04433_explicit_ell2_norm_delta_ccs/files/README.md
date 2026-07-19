# Explicit `ell_2` Renorming With Superreflexive `Delta` And ccs `Delta` Point

Status: literature-known partial subcase; includes an additional direct proof
found during this run. This is not counted as a new partial result.

Source: Miguel Martin, Yoel Perreau, and Abraham Rueda Zoca,
*Diametral notions for elements of the unit ball of a Banach space*,
arXiv:2301.04433.

## Target

Question 7.7 asks for isomorphic restrictions on Banach spaces containing
`Delta`-points and related diametral notions. In particular, it asks whether a
reflexive or super-reflexive Banach space can contain `Delta`, super `Delta`,
ccs `Delta`, Daugavet, or super Daugavet points.

This packet answers only the `Delta`, super `Delta`, and ccs `Delta`
subcases. It does not answer the Daugavet or super-Daugavet subcases.

## Literature-Known Result With Direct Proof

Let `Y` be `ell_2` with the equivalent norm

```text
N(x)=max{|x_1|, ||(x_n)_{n>=2}||_2, sup_{n>=2}|x_1-2x_n|}.
```

Then `Y` is superreflexive, because it is linearly isomorphic to Hilbert
space. The point `e_1` is a super `Delta`-point and a ccs `Delta`-point in
`Y`; hence it is also an ordinary `Delta`-point.

The proof is direct. The vectors `e_1+e_n` all have `N`-norm `1`, converge
weakly to `e_1`, and satisfy `N(e_1-(e_1+e_n))=N(e_n)=2`. Thus every weak
neighborhood of `e_1` in the unit ball contains points at maximal distance
from `e_1`. The ccs part follows because the norm makes `e_1` an extreme point
of the unit ball.

## Novelty And Provenance

The theorem is not new as a mathematical answer: a later paper,
Abrahamsen--Aliaga--Lima--Martiny--Perreau--Prochazka--Veeorg
arXiv:2303.00511, explicitly answers this subcase by constructing a
superreflexive renorming of `ell_2`.

This packet belongs in `literature_already_answered` because the mathematical
subcase was already answered in later literature. It preserves the additional
run-local direct renorming proof rather than citing the later theorem as a
black box. No external novelty claim is made for the proof method beyond the
run-local observation.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: compiled literature-known packet with direct proof.
- `source_paper.pdf`: local copy of arXiv:2301.04433.
- `supporting_paper_2303.00511.pdf`: local copy of the later literature paper.
- `figures/open_problem_crop.png`: crop of Question 7.7.

## Human Review Recommendation

Review as a literature-known partial subcase with an additional direct proof. The key
checks are:

- `N` is an equivalent norm on `ell_2`.
- `e_1+e_n -> e_1` weakly in the renormed space.
- `N(e_1+e_n)=1` and `N(e_n)=2`.
- `e_1` is extreme in the `N`-unit ball.
- Extremality correctly forces every slice in a ccs representation containing
  `e_1` to contain `e_1`, allowing the weak-convergence argument to be reused.
