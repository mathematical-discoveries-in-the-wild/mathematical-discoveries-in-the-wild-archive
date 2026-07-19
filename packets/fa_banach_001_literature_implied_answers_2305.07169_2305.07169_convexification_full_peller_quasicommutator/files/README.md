# Literature-Implied Full Answer: Convexification Mazur Map

Status: `literature_implied_answer (full source question)`

Source paper: Javier Alejandro Chavez-Dominguez, *Uniform homeomorphisms
between spheres of unitarily invariant ideals*, arXiv:2305.07169.

Source question: In Section 4, after Theorem
`thm-homeomorphism-convexification`, the author asks whether the theorem's
restriction `p >= 3` is really needed. The restriction enters through the
second inequality in Lemma `lemma-sum`, where the proof cites Jocic's Theorem
3.1 only for `p >= 3`.

Supporting theorem: A. B. Aleksandrov and V. V. Peller, *Functions of
operators under perturbations of class S_p*, arXiv:0908.3623, Section 11,
Theorem `sigmaq`, proves a pointwise singular-value estimate for
quasicommutators `f(A)Q - Qf(B)` with `f` Holder.

Identification: Apply Theorem `sigmaq` with `alpha=1/p`,
`f(t)=sign(t)|t|^(1/p)`, `A=x^p`, `B=-y^p`, and `Q=b`. It gives
coordinatewise singular-value domination

```text
s_j(|xb+by|^p) <= C_p ||b||_infty^(p-1) s_j(x^p b + b y^p).
```

Monotonicity of every 1-symmetric sequence norm then yields exactly the
missing reverse estimate in Lemma `lemma-sum` for every `p > 1`, not merely
for `p >= 3`.

Conclusion: The proof of arXiv:2305.07169, Section 4, therefore extends
verbatim to every `1 < p < infinity`: for every 1-symmetric sequence space
`E`, the p-convexification Mazur map `G_p` is a uniform homeomorphism
between the unit spheres of `S_{E^(p)}` and `S_E`.

Provenance: This is not presented as a new theorem independent of the
literature. Aleksandrov--Peller's theorem predates the source paper and does
not explicitly advertise itself as resolving this question; the answer is
obtained by the direct substitution above. That is why this packet is filed
under `literature_implied_answers/`.

Files:

- `main.tex`: compact status note with the full substitution argument.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: arXiv:2305.07169.
- `supporting_paper_0908.3623.pdf`: arXiv:0908.3623.
