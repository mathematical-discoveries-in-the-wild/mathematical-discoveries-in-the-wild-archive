# Characterization Toolkit for Kurka's `c0 + X` Borel Question

Status: `partial_result (collapse-set obstruction, Sobczyk-Kurka characterization, quotient-persistence obstruction, unconditional-embedding exclusion, CDDK route dichotomy, unique nonmeager class theorem, and paving-entry criterion)`

Run: `fa_banach_001`  
Agent: `agent_lane_08`  
Source: arXiv:1711.03328, Ondrej Kurka, "The isomorphism class of c0 is not Borel"

## Source Question

Kurka proves that the isomorphism class of `c0` is complete analytic and notes that his method also gives non-Borelness of the isomorphism class of `c0 + X` when `X` is "not big" in several senses. He then says that it is not known whether there is any Banach space `X` for which the isomorphism class of `c0 + X` is Borel.

## Sobczyk-Kurka Characterization

The latest push adds a sharp reformulation. For every separable Banach space
`X`, the isomorphism class of `c0 + X` is Borel if and only if `X` contains
`c0` and the isomorphism class of `X` itself is Borel.

Indeed, if `X` contains no `c0`, Kurka's Theorem 1.2 already gives
non-Borelness of `[c0 + X]`. If `X` contains `c0`, Sobczyk's theorem
complements a copy of `c0` inside `X`; hence `X ~= c0 + Z` for some separable
`Z`, and so `c0 + X ~= c0 + c0 + Z ~= X`.

Thus Kurka's open question is equivalent to the following cleaner question:

```text
Does there exist a separable Banach space containing c0 whose isomorphism
class is Borel?
```

This does not settle the problem, but it localizes the remaining difficulty.
Every known Borel-class candidate that does not contain `c0` is irrelevant,
and every known non-Borel `c0`-containing space is a confirmed negative
instance. A positive example must be a separable `c0`-containing space with
Borel isomorphism class.

Equivalently, for separable `X`, the following are the same:

- `X` contains `c0`;
- `X` contains a complemented copy of `c0`;
- `X ~= c0 + X`.

Thus adding `c0` has only two regimes: if `X` already contains `c0`, the
operation does not change the isomorphism class; if `X` does not contain `c0`,
Kurka's theorem makes the new class non-Borel.

## Quotient-Persistence Obstruction

The full-result push adds a structural obstruction that is often easy to test.
Let `Y` be separable and contain `c0`. If there is a copy `E ~= c0` in `Y`
such that the quotient `Y/E` satisfies any of Kurka's three "not big"
hypotheses, then the isomorphism class of `Y` is not Borel. In particular this
holds if:

- `Y/E` contains no `c0`;
- `Y/E` contains no infinite-dimensional reflexive subspace;
- `Y/E` embeds into a space with an unconditional basis.

Indeed, by Sobczyk, `E` is complemented, so `Y ~= c0 + (Y/E)`, and Kurka's
Theorem 1.2 applies to the quotient.

Consequently, a Borel positive example `Y` would have to be strongly
`c0`-persistent: after quotienting by any copy of `c0`, the quotient must still
contain `c0`, contain an infinite-dimensional reflexive subspace, and avoid
embedding into any space with an unconditional basis. This rules out all naive
direct sums `c0 + Z` where the complement `Z` is small in Kurka's sense.

## Unconditional-Embedding Exclusion

The new push extracts an especially useful global form of the previous
obstruction. If a separable space `Y` contains `c0` and embeds into a Banach
space with an unconditional basis, then the isomorphism class of `Y` is not
Borel.

Indeed, Sobczyk gives `Y ~= c0 + Z`. Since `Z` is a complemented subspace of
`Y`, it also embeds into the same unconditional-basis ambient space. Kurka's
Theorem 1.2 then applies to `Z` and gives non-Borelness of
`[c0 + Z] = [Y]`.

Thus a Borel positive example cannot have an unconditional basis and cannot be
isomorphic to a subspace of `c0`. This also rules out the tempting paving-side
shortcut through spaces of the form `(sum E_n)_c0` with finite-dimensional
blocks: such spaces embed into `c0`, hence cannot supply the desired Borel
`c0`-containing class.

## CDDK Low-Complexity and Category Barrier

Combining the Sobczyk-Kurka characterization with the Cuth-Dolezal-Doucha-Kurka
complexity theorem gives a further obstruction in their Polish norm codings
`\mathcal B` and `\mathcal P_\infty`:

- No class `[c0 + X]` is `F_sigma`.
- If `[c0 + X]` is `G_delta`, then `c0 + X` must be isomorphic to the Gurarii
  space.
- More generally, the Gurarii isomorphism class is the unique nonmeager
  isomorphism class in the CDDK topology. This does not require the class to be
  Borel: all isomorphism classes are analytic and hence have the Baire property.
  Thus any non-Gurarii Borel positive example would have to be meager and not
  `F_sigma`.

Thus the easiest possible positive example is ruled out, and a `G_delta`
or nonmeager positive example is exactly the Gurarii-space problem. The
remaining question is genuinely at the level of whether a `c0`-containing
space, especially the Gurarii space, can have a Borel but not topologically
simple isomorphism class.

In particular, in the CDDK codings Kurka's question has a positive answer if
and only if one of the following two routes works:

1. the Gurarii space has Borel isomorphism class;
2. there is a separable `c0`-containing space whose isomorphism class is
   Borel, meager, and not `F_sigma`.

This is the most useful route dichotomy from the final polish pass: it says a
nonmeager Borel positive example is equivalent to the Gurarii Borel problem,
while every other positive example must live in the harder meager/high-Borel-
complexity regime.

## Candidate Audit from the Full-Result Push

The final full-result push checked the obvious positive candidates and found
that the known literature blocks the simple routes:

- `C[0,1]`: by Milutin's theorem it is isomorphic to `C(2^N)`; Kurka's
  introduction cites the known result that the isomorphism class of `C(2^N)` is
  not Borel.
- Pelczynski's universal space: Kurka cites Bossard's theorem that its
  isomorphism class is not Borel.
- `L_p[0,1]` for `1 < p < infinity`, `p != 2`: Kurka cites known non-Borelness.
- `ell_p`, `1 < p < infinity`: Godefroy proves these isomorphism classes are
  Borel, but these spaces do not contain `c0`, so they cannot answer the
  reduced question.
- `ell_1`: Kurka records that its Borel status was not known; in any case
  `ell_1` has the Schur property and does not contain `c0`.
- Gurarii space: it contains `c0` by universality, but CDDK explicitly record
  that even the Borel status of its isomorphism class is unknown.
- Subspaces of `c0`, spaces with unconditional bases, and `c0`-sums of
  finite-dimensional spaces: the unconditional-embedding exclusion above makes
  all `c0`-containing examples in this family non-Borel.

Thus the full result did not crack, but the search now rules out the standard
candidate shortcuts and leaves exactly the two routes in the CDDK dichotomy:
Gurarii Borelness, or a meager Borel non-`F_sigma` `c0`-containing class.

## Paving and Finite-Dimensional-Structure Entry Point

CDDK prove that any separable infinite-dimensional Banach space determined by
its pavings has a `G_{delta sigma}` isomorphism class in their norm codings.
Combining this with the Sobczyk-Kurka characterization gives a practical
criterion:

```text
If a separable Banach space Y contains c0 and is determined by its pavings,
then Kurka's question has a positive answer.
```

The same applies a fortiori to spaces determined by their finite-dimensional
subspaces, since that condition implies being determined by pavings. If such a
space is not the Gurarii space, the CDDK route dichotomy forces its isomorphism
class to be meager and not `F_sigma`.

This does not produce an example by itself. The standard paving-determined
examples highlighted by CDDK, such as certain `ell_2`-sums of finite-dimensional
spaces, are reflexive and therefore do not contain `c0`. The other natural
local-structure shortcut, a `c0`-sum of finite-dimensional blocks, is ruled out
by the unconditional-embedding exclusion because it embeds into `c0`. Thus a
successful paving route would have to be much less coordinate-like: a
`c0`-containing paving-determined space that does not embed into any space with
an unconditional basis.

## Collapse-Set Partial Result

Let `H` be Hurewicz's complete analytic set of compact families of subsets of `N` containing an infinite set. Let `X_M` be Kurka's Bourgain-Delbaen family, so that `M in H` implies `X_M ~= c0`, while finite-only `M` give `c0`-free obstruction spaces. Let `B` be Kurka's Borel set containing `H` on which `X_M^*` is separable.

For a fixed separable Banach space `X`, define the Kurka collapse set

```text
C_X = { M in B : X_M + X is isomorphic to c0 + X }.
```

If `C_X \ H` is analytic, then the isomorphism class of `c0 + X` is not Borel.

Equivalently, if the isomorphism class of `c0 + X` is Borel, then `C_X \ H` must be nonanalytic. In that case `c0 + X` complementably contains `X_M` for a nonanalytic family of finite-only parameters `M`; these `X_M` have separable dual, contain no `c0`, and are reflexively saturated.

## Interpretation

Kurka's published theorem proves non-Borelness by showing `C_X \ H` is empty under three structural hypotheses on `X`: no `c0`, no infinite-dimensional reflexive subspace, or embeddability into a space with an unconditional basis.

The packet isolates the general mechanism. To prove non-Borelness for a new class of spaces `X`, it is enough to show that the finite-only collapse set is analytic; in particular, it is enough to control the possible absorption of Kurka's finite-only Bourgain-Delbaen spaces by `c0 + X` through any analytic structural test. A Borel positive example would have to evade all such tests by absorbing a nonanalytic collapse family.

The Sobczyk-Kurka characterization explains why this remaining case is hard:
if `X` contains `c0`, then `c0 + X` is just `X` up to isomorphism. So the
question becomes a direct Borel-class question for `X`, not a separate direct
sum phenomenon.

For a proposed family of spaces, the packet now gives the following reusable
filter:

1. Check whether the family contains `c0`; if not, Kurka's theorem already
   gives non-Borelness for `c0 + X`.
2. If it contains `c0`, check whether its own isomorphism class is Borel; this
   is exactly the original question for `c0 + X`.
3. If the class is Borel and nonmeager in the CDDK codings, it must be Gurarii.
4. If the class is Borel and not Gurarii, it must be meager, non-`F_sigma`, and
   must evade the collapse-set analyticity obstruction.

## Proof Inputs

- Kurka's Borel family `M -> X_M`.
- Hurewicz's theorem: `H` is complete analytic and not Borel.
- Kurka's Borel selector for `X_M + X`.
- Lusin separation for disjoint analytic sets.
- Kurka's properties of finite-only `X_M`: no `c0`; on `B`, separable dual and reflexive saturation.

## Limitations

This does not solve Kurka's question. It gives a necessary and sufficient
reformulation of the positive-example search, a quotient-persistence
obstruction for `c0`-containing spaces, an unconditional-embedding exclusion,
low-complexity/category barriers in the CDDK codings, a unique nonmeager
isomorphism-class theorem, a paving/finite-dimensional-structure entry
criterion for producing positive examples, and a necessary collapse-set
condition for any Borel positive example. The condition `C_X \ H` analytic is
still a property of the Kurka collapse relation, so human review should judge
how useful it is for natural spaces not already covered by Kurka's Theorem 1.2.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: Kurka source paper.
- `figures/open_problem_crop.png`: source excerpt containing the `c0 + X` question and Theorem 1.2.

## Human Review Focus

1. Check that the Borelness of the isomorphism class of `c0 + X` indeed makes the collapse set `C_X` Borel via Kurka's selector.
2. Check the Lusin-separation step: if `C_X` is Borel, `H subset C_X`, and `C_X \ H` is analytic, then `H` would be Borel.
3. Check the interpretation of `C_X \ H`: for every parameter in it, `c0 + X` contains a complemented copy of the corresponding finite-only Kurka space.
4. Check the Sobczyk absorption step: if separable `X` contains `c0`, then `X ~= c0 + Z`, hence `c0 + X ~= X`.
5. Check the low-complexity/category barrier is interpreted in the Cuth-Dolezal-Doucha-Kurka Polish norm codings, not as a topology-free strengthening of non-Borelness.
6. Check the paving-entry criterion: CDDK's `G_{delta sigma}` theorem for spaces determined by pavings, together with `c0` containment, really gives a Borel positive example.
7. Check the quotient-persistence obstruction: for every copy `E ~= c0` in a separable positive example, `Y/E` must evade all three hypotheses in Kurka's Theorem 1.2.
8. Check the unconditional-embedding exclusion: if `Y` contains `c0` and embeds into an unconditional-basis space, Sobczyk makes the complement embed there too, so Kurka's Theorem 1.2 applies.
