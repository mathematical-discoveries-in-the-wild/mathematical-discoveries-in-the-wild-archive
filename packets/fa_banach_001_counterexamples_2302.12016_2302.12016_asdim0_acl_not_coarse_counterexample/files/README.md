# Counterexample Packet: Asymptotic Dimension Zero Does Not Force Coarse Equivalence

Run: `fa_banach_001`
Agent: `agent_lane_13`
Status: claimed counterexample; needs human review

## Source

- Paper: Bruno M. Braga and Gilles Lancien, "Asymptotic coarse Lipschitz equivalence"
- arXiv: `2302.12016`
- Source target: Problem 2.15 asks whether asymptotically coarse Lipschitz equivalent
  metric spaces with asymptotic dimension zero must be coarse (Lipschitz) equivalent.

## Result

The answer is negative as stated.

There are metric spaces `X` and `Y` such that:

```text
asdim(X) = asdim(Y) = 0,
X and Y are asymptotically coarse Lipschitz equivalent,
X and Y are not coarsely equivalent.
```

Since coarse Lipschitz equivalence implies coarse equivalence, this disproves the proposed
conclusion.

## Construction

Let `A` be an uncountable set and fix `a0 in A`.

Define `X = {x_n : n in N}` with

```text
d_X(x_n, x_m) = 0 if n=m, and 2^n + 2^m if n != m.
```

Define `Y = N x A` with

```text
d_Y((n,a),(m,b)) = 0,              if (n,a)=(m,b),
                 = n,              if n=m and a != b,
                 = 2^n + 2^m,       if n != m.
```

The maps

```text
f(x_n) = (n,a0),      g(n,a) = x_n
```

are `1`-Lipschitz.  Moreover, `g f = Id_X`, while

```text
d_Y(f g(n,a), (n,a)) <= n = o(2^n).
```

Thus `f` and `g` witness asymptotic coarse Lipschitz equivalence.

## Why It Is Not Coarsely Equivalent

If `Y` were coarsely equivalent to countable `X`, then for some coarse maps `F:X -> Y` and
`G:Y -> X`, the composition `F G` would be uniformly close to `Id_Y`.  Let that closeness
constant be `C`.  Pick `n>C`.  Every `C`-ball around a point of the uncountable fiber
`{n} x A` is a singleton.  Hence `F G` would have to be the identity on `{n} x A`, forcing
the countable set `F(X)` to contain the uncountable fiber, impossible.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: compiled packet
- `source_paper.pdf`: original arXiv PDF
- `figures/problem_2_15_crop.png`: crop of the source problem

## Scope

This answers Problem 2.15 exactly as stated for arbitrary metric spaces.  The construction is
deliberately nonseparable and uses uncountable fibers.  It does not address strengthened
versions with countability, separability, bounded geometry, or uniformly finite fibers.

## Verification

Build command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

Human review should focus on whether Problem 2.15 implicitly intended an additional
separability or bounded-geometry hypothesis.  Without such a hypothesis, the counterexample
is direct.
