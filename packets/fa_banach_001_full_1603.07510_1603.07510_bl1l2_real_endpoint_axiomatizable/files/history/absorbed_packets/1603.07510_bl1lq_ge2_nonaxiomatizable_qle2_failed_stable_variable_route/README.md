# Non-axiomatizability of the fiber-dimension-restricted \(\mathcal{BL}_1L_q\) classes

Status: partial negative result, likely valid.

Source: Yves Raynaud, *New axiomatizable classes of Banach spaces via disjointness-preserving isometries*, arXiv:1603.07510.

## Result

For every \(1<q\le 2\) and every \(n\ge2\), the class of Banach spaces
linearly isometric to members of \(\mathcal{BL}_1L_q^{\ge n}\) is not
axiomatizable in the Banach-space language.

This does **not** answer Raynaud's final Question 6.17, which asks whether the
unrestricted class \(\mathcal{BL}_1L_q\) is axiomatizable for \(1<q\le2\).
It shows that the positive fiber-dimension-restricted results in the paper
cannot be extended to \(p=1\), \(q\le2\).

## Mechanism

For \(1<q\le2\), finite-dimensional \(\ell_q^n\) embeds isometrically into an
\(L_1\)-space by the standard \(q\)-stable variable construction. Therefore
\[
L_1[0,1](\ell_q^n)
\]
and \(L_1[0,1]\) are mutually finitely representable. Heinrich's ultrapower
theorem then gives isometric ultrapowers of these two Banach spaces.

Since \(L_1[0,1](\ell_q^n)\) is in \(\mathcal{BL}_1L_q^{\ge n}\), any
axiomatizable version of that class would be closed under ultrapowers and
ultraroots, forcing \(L_1[0,1]\) into the same class. But this is impossible:
members of \(\mathcal{BL}_1L_q^{\ge n}\) have duals containing a
1-complemented copy of \(\ell_{q'}^n\), whereas \(L_1[0,1]^*=L_\infty[0,1]\)
is 1-injective and hence cannot have a 1-complemented non-injective finite
dimensional subspace \(\ell_{q'}^n\), \(1<q'<\infty\).

## Files

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: source paper.
- `figures/question_6_17_crop.png`: source open question crop.
- `figures/question_5_8_crop.png`: adjacent Nakano question crop.

Human review should focus on the lemma excluding \(L_1[0,1]\) from
\(\mathcal{BL}_1L_q^{\ge n}\), especially the use of 1-injectivity of
\(L_\infty\) and the existence of a 1-complemented \(\ell_{q'}^n\) in duals of
nonzero \(\mathcal{BL}_1L_q^{\ge n}\) members.
