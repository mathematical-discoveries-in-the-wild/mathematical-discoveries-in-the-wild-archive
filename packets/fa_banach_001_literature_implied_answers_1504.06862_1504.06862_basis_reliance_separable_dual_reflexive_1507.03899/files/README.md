# Literature status: partial removal of the basis hypothesis from 1504.06862

Status: literature-implied answer, partial subcase.

Source paper: arXiv:1504.06862, *Amalgamations of classes of Banach spaces with a monotone basis*.

Later paper: arXiv:1507.03899, *Zippin's embedding theorem and amalgamations of classes of Banach spaces*.

## Source signal

After Theorem 1.2 in arXiv:1504.06862, Kurka writes that it is not known whether the reliance on a monotone basis can be dropped, as in the isomorphic setting.

The broad remark concerns the basis hypothesis in the isometric amalgamation theorem for classes with monotone bases. The same introduction also mentions a separate Schur-space/basis issue; this packet does not address that issue.

## Later partial answer

The later paper arXiv:1507.03899 identifies the same obstruction: the previous isometric technique applies only to spaces with a monotone basis, so the basis-reliance problem reappears. It then proves:

- If `C` is an analytic set of Banach spaces with separable dual, there is a Banach space `E` with a shrinking monotone basis containing an isometric copy of every member of `C`.
- If `C` is an analytic set of separable reflexive Banach spaces, there is a reflexive Banach space `E` with a monotone basis containing an isometric copy of every member of `C`.

Thus, for the separable-dual and reflexive branches of the source theorem, the monotone-basis assumption on the input class can be removed. The copies in the later theorem are isometric; the packet does not claim that they are `1`-complemented.

## Scope notes

This is not a new result and not a full solution of all open directions in arXiv:1504.06862.

The packet records only the later positive partial answer for analytic families of spaces with separable dual and analytic families of separable reflexive spaces. It does not settle:

- the source theorem's non-isometrically-universal class without a basis hypothesis;
- the strictly convex class without a basis hypothesis;
- the Schur-space question in Remark 2.4(c).

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source paper arXiv:1504.06862.
- `supporting_paper_1507.03899.pdf`: later paper giving the partial answer.
