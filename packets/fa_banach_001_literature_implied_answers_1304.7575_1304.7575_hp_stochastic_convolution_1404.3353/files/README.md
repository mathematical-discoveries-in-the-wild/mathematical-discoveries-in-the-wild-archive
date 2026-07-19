# Literature-Implied Partial Boundary: Stochastic Convolution Hypothesis `(H_p)`

Status: `literature_implied_answer (partial characterization / negative boundary example)`

Source problem paper: J. van Neerven, M. Veraar, and L. Weis,
*Stochastic integration in Banach spaces - a survey*, arXiv:1304.7575.

Supporting paper: J. van Neerven, M. Veraar, and L. Weis,
*On the R-boundedness of stochastic convolution operators*, arXiv:1404.3353.

## Target

In the stochastic maximal `L^p`-regularity section of arXiv:1304.7575, after
Theorem 7.3, the authors prove Hypothesis `(H_p)` for spaces isomorphic to
closed subspaces of `L^q(O)`, `q >= 2`, and note that it also holds for
corresponding Sobolev spaces. They then ask for a description of the class of
Banach spaces `X` to which the result of Theorem 7.3 can be extended.

Equivalently in the surrounding discussion, `(H_p)` is an `R`-boundedness
condition for a family of stochastic convolution operators. The survey already
records one sufficient condition from earlier work: `X` is a UMD Banach
function space with norm `||x||_X = || |x|^2 ||_F`, where `F` is another UMD
Banach function space.

## Supporting Literature Result

The later paper arXiv:1404.3353 studies precisely the `R`-boundedness of the
stochastic convolution families used in the proof of stochastic maximal
`L^p`-regularity. Its Theorem 7.1 gives an equivalence between:

- `R`-boundedness of stochastic convolution families on deterministic
  integrands;
- the corresponding adapted-process versions;
- for Banach lattices, `ell^1`-boundedness of an associated deterministic
  convolution family on `L^{p/2}(R_+; X^2)`.

Theorem 7.2 then gives a positive criterion: if `X` is a Banach lattice with
type 2 and the dual of its 2-concavification `X^2` is an HL lattice, then the
relevant stochastic convolution families are `R`-bounded for all Hilbert spaces
`H` and all `p in (2, infinity)`. The following corollary applies this to the
kernel class used in the stochastic maximal regularity setting.

Finally, Section 8 records that it had been open whether the same
`R`-boundedness holds for all UMD Banach spaces/lattices with type 2. Theorem
8.2 gives a negative answer in the Banach lattice `X = ell^2(ell^4)`: for every
`2 < p < infinity`, the relevant stochastic convolution family fails to be
`R`-bounded.

## Scope

This packet records a literature-implied partial answer to the source
classification problem:

- positive side: a larger Banach-lattice class is covered by the HL-lattice
  condition on `(X^2)^*`;
- structural reduction: in Banach lattices the stochastic question is
  equivalent to `ell^1`-boundedness of deterministic convolution operators on
  the 2-concavification;
- negative boundary: UMD plus type 2 is not sufficient, even among Banach
  lattices, because `ell^2(ell^4)` fails.

This is not a full classification of all Banach spaces satisfying `(H_p)`.
The broad "describe the class" problem remains open beyond the positive
criterion and counterexample recorded here.

## Evidence

- `source_paper.pdf`: local copy of arXiv:1304.7575.
- `supporting_paper_1404.3353.pdf`: local copy of arXiv:1404.3353.
- `main.tex` and `solution_packet.pdf`: compact status note with theorem
  mapping and limitations.

## Search Bounds

Before packaging, the run indexes were searched for `1304.7575`, `stochastic
maximal regularity`, `Hypothesis (H_p)`, `R-bounded stochastic convolution`,
`ell^1-boundedness`, `UMD type 2`, `Hardy-Littlewood maximal`, and
`ell^2(ell^4)`. Existing packets contained adjacent stochastic Weiss,
gamma-radonifying, RMF/UMD, and UMD-lattice counterexample entries, but no
prior packet for this exact source problem. The web/arXiv check on June 15,
2026 identified arXiv:1404.3353 as the direct follow-up source.

## Human Review Notes

Recommended review focus:

- Verify that the packet is counted only as a partial literature-implied
  classification/boundary result, not as a full answer to the broad source
  question.
- Check whether later work after arXiv:1404.3353 gives a full intrinsic
  classification of Banach spaces satisfying `(H_p)`.
- Check theorem numbering in the published versions of arXiv:1304.7575 and
  arXiv:1404.3353.
