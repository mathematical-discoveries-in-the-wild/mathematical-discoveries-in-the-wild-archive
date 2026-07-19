# 2401.17465: Kottman-domain extension of one-point beta positivity

- date: 2026-06-14
- status: not solved
- arxiv_id: 2401.17465
- source: `data/parsed/arxiv_sources/2401.17465/source.tex`
- archived_claim: `runs/fa_banach_001/agents/archive/2026-06-14/2401.17465_an_asymptotic_analog_of_a_local_to__agent_lane_03.md`

## Target

Baudier--Lancien prove that if a Banach space `(X, ||.||)` satisfies

```text
\bar\beta_{||.||}(t0) > 0
```

for some `t0 in (0,1)`, then `X` admits an equivalent norm with Rolewicz's
property `(beta)`. In the final paragraph they note that the beta modulus can
also be considered on `[0,K(X))`, where `K(X)` is Kottman's constant, and ask
whether the condition in Theorem 1.2 can be pushed beyond `1`.

The sharpened target tested here was:

```text
If \bar\beta_{||.||}(t0)>0 for some t0 in (1,K(X)),
must X admit an equivalent property-(beta) norm?
```

## Bounded duplicate and literature check

The cheap run indexes contain no prior entry for `2401.17465`, the
local-to-global beta renorming question, or the Kottman-domain extension.

The only local Kottman hits in the registry/solutions concern unrelated
separated-set questions. A bounded web phrase search for the exact title,
`Kottman's constant`, `property (beta)`, `asymptotic beta modulus`, and the
phrase `pushed beyond 1` did not reveal a later explicit answer.

## Proof-dependency audit

The published proof uses `t0 < 1` in several independent places.

1. In Lemma 3.2, which produces the upper tree estimates leading to AUS
   renormability, the separated tail construction only gives distances
   arbitrarily close to `1` from below. The key line chooses `eta > 0` with
   `1 - 2 n eta > t0`; this has no analogue for `t0 > 1`.

2. In Proposition 4.1, non-reflexivity is excluded through James' criterion by
   showing `\bar\beta(t)=0` for every `t in (0,1)`. The same argument gives no
   obstruction at a Kottman-scale `t > 1`, so it does not prove reflexivity
   under the enlarged hypothesis.

3. In Proposition 4.2 and Theorem 4.8, one uses a point `t1` with
   `t0 < t1 < 1` to obtain positive asymptotic convexity and then a finite
   sigma/Szlenk derivation at a scale below `1`. If `t0 > 1`, this interval is
   empty. A finite sigma derivation at a scale above `1`, even if obtainable,
   would not feed Corollary 4.7, whose submultiplicative descent starts from an
   `eps0 in (0,1)`.

Thus a direct proof extension would need a genuinely new step, not just a
change of constants.

## Attempted route 1: lower the large Kottman scale

A natural positive route would be:

```text
\bar\beta(t0)>0 for some t0<K(X)  ==>  \bar\beta(s)>0 for some s<1.
```

This would immediately reduce the problem to Theorem 1.2. I did not find such
a monotonicity or compression argument. The beta modulus is increasing in the
separation parameter, so positivity at a large scale gives no formal
information at smaller scales. The Kottman assumption supplies separated
sequences at large scales, but it does not by itself provide the common
supporting functional or midpoint-near-one geometry needed to transfer a
large-scale bad beta configuration to a small-scale one.

## Attempted route 2: counterexamples from standard bad spaces

The most tempting negative route is to find a space that is not
property-(beta)-renormable but has positive beta modulus at some large
separation scale.

Standard candidates do not immediately work:

- In `ell_1`, taking `x=e_1` and `y_n=e_n` gives a `2`-separated sequence in
  the unit ball with `||(x+y_n)/2||_1=1`, so the natural norm has
  `\bar\beta(t)=0` for every `t<2`.
- In sup-type sums `E \oplus_\infty Y`, any large separated sequence in the
  `Y` coordinate and a fixed norm-one `E` coordinate gives midpoint norm `1`.
  Hence these norms force `\bar\beta(t)=0` for all `t<K(Y)` and cannot witness
  the desired large-scale positivity.

These checks do not rule out a more delicate renorming of a non-reflexive or
large-Szlenk space, but they remove the easiest counterexample family.

## Verdict

No full proof, counterexample, or literature-status packet was obtained.

The useful takeaway is that the Kottman-domain question is a real strengthening
of the paper's theorem. The published argument is intrinsically a below-one
argument: its tree, reflexivity, and Szlenk/AUC components each break at the
same threshold. A successful continuation likely needs either:

- a new principle converting one-point beta positivity at some `t<K(X)` into
  positivity below `1`; or
- a counterexample norm on a non-property-(beta)-renormable space where large
  separated sequences are forced to leave every midpoint-flat face.
