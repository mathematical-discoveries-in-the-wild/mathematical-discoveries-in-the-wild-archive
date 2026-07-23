# Verification report

Verdict: `candidate full counterexample, likely valid`

## Target match

Section 2 of arXiv:2502.16929 says that computing the two-sided derivative in
equation (2.1) “for all continuous functions” is a nontrivial task not carried
out there.  The example uses a continuous real-valued perturbation and makes
the integral finite for every `|t|<1`, but the two-sided derivative fails.

## Proof audit

1. `phi=indicator_infinity[-1,1]` is convex, lower semicontinuous, and
   `integral exp(-phi)=2`, hence belongs to the source class `Cvx_1`.
2. Directly from the definition of the Legendre transform,
   `phi*(y)=|y|`.
3. `xi(y)=|y| sin(log(1+|y|))` is continuous, even, real-valued, and satisfies
   `|xi(y)|<=|y|`.
4. For `a_t=1-|t|`, the perturbed function
   `q_t(y)=|y|+t xi(y)` satisfies `q_t(y)>=a_t|y|`; hence it is coercive for
   `|t|<1`.
5. If `|x|<=a_t`, then `xy-q_t(y)<=0` for every `y`, while `y=0` gives
   equality. Thus `q_t*(x)=0`.
6. For `t>0`, the coefficient of `|y|` equals `a_t` at
   `|y|=exp(3pi/2+2pi k)-1`. For `t<0`, it equals `a_t` at
   `|y|=exp(pi/2+2pi k)-1`.
7. If `|x|>a_t`, choosing the sign of `y` to agree with `x` along the relevant
   sequence makes `xy-q_t(y)=|y|(|x|-a_t)` tend to infinity. Therefore
   `q_t*(x)=+infinity`.
8. Hence `q_t*` is exactly the infinite-valued indicator of
   `[-a_t,a_t]`, and its exponential integrates to `2a_t=2(1-|t|)`.
9. The one-sided derivatives at zero are `-2` and `+2`, so no two-sided
   derivative exists.

No computational input is used.

## Limitations

The perturbation has no recession limit because `xi(y)/|y|` oscillates.  The
example therefore does not rule out a theorem for cosmically continuous
perturbations or another class with controlled recession data.

## Reviewer focus

Verify Steps 6-7 and confirm that the phrase “all continuous functions” is
intended literally rather than as shorthand for an unstated recession-regular
class.
