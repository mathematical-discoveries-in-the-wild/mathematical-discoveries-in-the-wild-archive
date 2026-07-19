# Full solution packet: alternating operator scaling at the spectral-gap rate

Status: candidate full solution, likely valid

## Source problem

Tsz Chiu Kwok, Lap Chi Lau, and Akshay Ramachandran, *Spectral Analysis of
Matrix Scaling and Operator Scaling*, arXiv:1904.03213.  After Corollary 1.6
the authors ask whether exact alternating left/right normalization has the same
linear convergence rate as their gradient flow under the nearly-balanced
spectral-gap assumptions.

## Result

The answer is affirmative.  For universal constants, if the input is
epsilon-nearly doubly balanced, has lambda spectral gap, and

`lambda^2 >= C epsilon log(2m)`,

then one full alternating cycle contracts the normalized Frobenius marginal
error by `1-c lambda`.  The spectral gap persists globally, and an
eta-nearly balanced scaling is reached in

`O(lambda^{-1} log((m+n)/eta))`

alternating iterations.

The proof compresses the normalized completely positive map to traceless
matrix spaces.  The spectral gap contracts the linearized left/right error,
while exact inverse-square-root expansions control nonlinear terms.  A
two-phase bootstrap uses the source's `epsilon log m << lambda^2` assumption
to keep cumulative scalings small until Frobenius norm controls operator norm.

## Files

- `solution_packet.pdf`: review-ready proof.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_question_crop.png`: source evidence from PDF page 6.
- `code/numerical_cycle_check.py`: auxiliary randomized sanity check.
- `tmp/`: build and render intermediates.

## Human review focus

Check the traceless-compression use of the source's spectral lemma, the scalar
component in the first half-cycle, and preservation of the second singular
value under cumulative noncommuting left/right scalings.  The numerical script
is not part of the proof.
