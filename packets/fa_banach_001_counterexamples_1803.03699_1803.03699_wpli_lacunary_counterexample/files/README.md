# PLI is necessary below density zero

Status: `counterexample_likely_valid`.

Source paper: Marek Balcerzak, Michal Poplawski, and Artur Wachowicz,
*Ideal convergent subseries in Banach spaces*, arXiv:1803.03699;
Quaestiones Mathematicae 42 (2019), no. 6, 765-779.

## Result

Question 4.6 asks whether the source's PLI theorem remains true under the
weaker wPLI hypothesis, especially for the lacunary ideal `Lac` of Example 3.
This packet gives a negative answer, including the intended measure-one core
of the theorem.

The stronger result is:

> If an ideal `I` is contained in the asymptotic-density-zero ideal `I_d` and
> there is a divergent real series whose Bernoulli subseries are
> `I`-convergent with probability one, then `I` has PLI.

The source proves the converse implication. Hence, for ideals contained in
`I_d`, PLI is equivalent to the existence of such a divergent series.

The ideal `Lac` is contained in `I_d`, has wPLI, and does not have PLI.
Therefore no divergent real series has almost every Bernoulli subseries
`Lac`-convergent. This disproves the proposed wPLI extension and settles the
particular example named in Question 4.6.

## Proof Mechanism

Measure-one ideal convergence first implies that the original series is
ideal-convergent, by pairing a Bernoulli selector with its complement. Since
`I` is contained in `I_d`, all these convergences are statistical.

Statistical convergence and Fubini yield deterministic endpoints along which
the centered Bernoulli partial sums converge in probability. Levy's maximal
inequality on the intervening independent symmetric blocks then forces the
coefficients to tend to zero. Finally, an ordinarily divergent,
`I`-convergent series with null coefficients forces a single member of `I` to
contain intervals of every finite length, which is exactly PLI.

## Printed-Theorem Note

Theorem 4.3 additionally prints `x_n` not tending to zero. Its displayed
construction actually has block coefficients `+/- 2^{-k}`, so they do tend to
zero. The new necessity argument shows that the printed strengthening is
impossible for every `I` contained in `I_d`, including `I_d` itself. The
source's core PLI construction, with the extra phrase removed, remains valid.

## Files

- `main.tex`: full proof and bounded novelty audit.
- `solution_packet.pdf`: rendered reviewer packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: source page 11 crop containing Question 4.6.

## Reviewer Focus

The main checkpoint is Lemma 2 in the packet: the extraction of deterministic
endpoints from almost-sure statistical convergence and the subsequent use of
Levy's maximal inequality. The remaining PLI implication is elementary.
