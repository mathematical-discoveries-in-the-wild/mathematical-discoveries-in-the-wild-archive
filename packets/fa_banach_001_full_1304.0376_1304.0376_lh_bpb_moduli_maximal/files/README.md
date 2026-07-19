# The BPB Moduli of \(L(H)\) Are Maximal

Result type: `full`

Status: candidate full solution, likely valid pending human review.

Source paper:

- Mario Chica, Vladimir Kadets, Miguel Martin, Soledad Moreno-Pulido,
  Fernando Rambla-Barreno, "Bishop-Phelps-Bollobas moduli of a Banach
  space", arXiv:1304.0376.
- Local source PDF: `source_paper.pdf`
- Source discussion crop: `figures/source_discussion_crop.png`

## Claimed Contribution

The source paper asks whether \(L(H)\), for finite- or infinite-dimensional
Hilbert space \(H\), has the maximum Bishop-Phelps-Bollobas moduli. The
paper's centralizer and M-ideal criteria do not apply because \(L(H)\) has
trivial center.

This packet gives a positive answer for every complex Hilbert space
\(\dim H\ge 2\):

> If \(X=L(H)=B(H)\), then
> \[
> \Phi_X(\delta)=\Phi_X^S(\delta)=\sqrt{2\delta}
> \qquad (0<\delta\leq 1/2).
> \]

The earlier \(M_2(\mathbb C)\) packet is preserved in
`history/1304.0376_m2_bpb_moduli_maximal/`.

## Key Idea

The first \(M_2\) packet used a witness with one lowered singular value.
That does not lift directly, because in \(M_n\) a nearby nonunitary
contraction may have a large top singular face.

The fix is to reverse the witness. Choose a rank-one projection \(p\), an
orthogonal rank-one projection \(q\), and set
\[
x=(1-\varepsilon)I+\varepsilon p,\qquad
\rho=(1-\varepsilon/2)\omega_p+(\varepsilon/2)\omega_q.
\]
Now \(x\) has a simple top singular value \(1\), while all other singular
values equal \(1-\varepsilon\). If \(\|y-x\|<\varepsilon\), the second
approximation number of \(y\) is strictly below \(1\). Hence any norm-one
functional \(\varphi\) satisfying \(\varphi(y)=1\) must be a rank-one vector
functional coming from the unique top singular direction of \(y\).

Finally, \(\rho\) has trace-norm distance at least \(\varepsilon\) from
every rank-one norm-one vector functional, by the Ky Fan-Mirsky singular
value inequality.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local rendered copy of the original arXiv source.
- `figures/source_discussion_crop.png`: crop of the \(L(H)\) question.
- `history/1304.0376_m2_bpb_moduli_maximal/`: previous partial packet.
- `tmp/`: LaTeX build intermediates.

## Human Review Notes

The proof is written for complex Hilbert spaces, matching the source paper's
unital complex \(C^*\)-algebra discussion. The real Hilbert-space analogue
should follow by the same singular-value argument, but it is not claimed in
this packet.

The main review point is Lemma 2: if \(y\in B(H)\), \(\|y\|=1\), and the
second approximation number \(a_2(y)<1\), then every norm-one functional
that norms \(y\) is a rank-one vector functional. The proof uses the
standard C*-algebra polar decomposition of functionals and the fact that the
top spectral projection of \(|y|\) is rank one.
