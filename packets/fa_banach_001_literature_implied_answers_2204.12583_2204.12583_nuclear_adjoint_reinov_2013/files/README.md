# Literature-implied answer: nuclearity of an operator and its adjoint

Status: `literature_implied_answer`.

Source paper: Asuman Guven Aksoy and Daniel Akech Thiong, *Schauder's Theorem and s-Numbers*, arXiv:2204.12583.

Supporting paper: O. I. Reinov, *On linear operators with s-nuclear adjoints: 0 < s <= 1*, arXiv:1311.2270.

## Identification

The source paper remarks, in Section "Hutton's Theorem Revisited" after its proof of Hutton's theorem, that since nuclear operators are compact it is natural to ask how nuclearity of an operator `T` and of its adjoint `T^*` are related. It recalls the known positive result that if `X^*` has the approximation property and `T^*` is nuclear, then `T` is nuclear with equal nuclear norm.

Reinov's paper gives the broader answer after reformulation in terms of `s`-nuclearity. Lemma 2 states that for `T:X -> Y`, `pi_Y T` is `s`-nuclear as an operator into `Y^{**}` if and only if `T^*` is `s`-nuclear. Theorem 1 says that if either `X^*` or `Y^{***}` has `AP_s`, then `T^*` `s`-nuclear implies `T` is nuclear. Theorem 2 shows sharpness: for each `r in (2/3,1]` there is a Banach space `Z_0` and a non-nuclear operator `T:Z_0^{**}->Z_0` such that `pi_{Z_0} T` is `r`-nuclear. Taking `r=1` and using Lemma 2 gives a non-nuclear operator whose adjoint is nuclear.

## Scope

This packet records a literature-implied answer to the nuclear-adjoint part of the 2022 remark. It does not claim a new result, and it does not address the source paper's separate questions about comparison of general s-numbers, Q-compactness, or approximation schemes.

The supporting paper predates arXiv:2204.12583 and does not cite it; the relation is an agent-identified implication.

## Files

- `source_paper.pdf`: arXiv:2204.12583.
- `supporting_paper_1311.2270.pdf`: arXiv:1311.2270.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status packet.

