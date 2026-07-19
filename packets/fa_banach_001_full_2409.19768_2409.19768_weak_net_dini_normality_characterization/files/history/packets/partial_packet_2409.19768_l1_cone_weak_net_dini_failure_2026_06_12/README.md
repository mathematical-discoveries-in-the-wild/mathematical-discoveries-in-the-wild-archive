# Partial Result: Weak-Net Dini Failure For The Non-Normal `ell^1` Cone

Run: `fa_banach_001`

Source paper: Jochen Glueck, "Increasing sequences in ordered Banach spaces
-- new theorems and open problems", arXiv:2409.19768.

Target: the concrete uncertainty immediately before Open Problem 6.2. The
paper asks whether, for the explicit non-normal cone on `ell^1` from Example
6.1, every increasing weakly convergent net might nevertheless be norm
convergent.

Status: candidate partial answer. The answer is negative for that explicit
cone. This does not solve Open Problem 6.2 in full.

## Claim

Let `X=ell^1(N_0)` and

```text
X_+ = {x in ell^1 : x_0 >= sum_{k>=1} |x_k| / 2^k}.
```

Then there is an increasing net in `X_+` which converges weakly in `ell^1`
but does not converge in norm.

## Packet Files

- `source_paper.pdf`: local copy of the arXiv PDF.
- `figures/open_problem_crop.png`: crop of Example 6.1 and Open Problem 6.2.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet, if LaTeX rendering succeeds.
- `code/verify_scalar_inequality.py`: small check of the scalar inequality
  used for monotonicity.

## Human Review Recommendation

Check the directed set order and the finite-annihilation lemma. The key point
is that finite subsets of `ell^\infty` can be annihilated by a unit `ell^1`
vector supported arbitrarily far out in the tail, giving weak convergence of
a net without norm convergence.
