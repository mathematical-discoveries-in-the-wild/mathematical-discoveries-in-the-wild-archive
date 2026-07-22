# Verification report

## Formal checks

For singleton-cut totals `s_1,...,s_4` and the three `2--2` cut totals `q_12,q_13,q_14`, the six pair-distance equations were entered into SymPy. Their equal-distance solution space is exactly

```text
s_1=s_2=s_3=s_4=s,
q_12=q_13=q_14=q.
```

The common side and coordinatewise-middle center radius simplify to

```text
lambda = 2s+2q,
r      = s+3q/2,
lambda-r = s+q/2 > 0.
```

The strict inequality follows because `s,q >= 0` and `lambda>0`.

## Exact finite-instance checks

The verifier constructs 12 permutation-symmetrized blocks. Each of the 24 coordinates in a block has three positive rational gaps, so the check exercises coordinates in which the singleton and `2--2` cuts are genuinely compressed together. It verifies exactly, using `fractions.Fraction`, that:

- all six pair distances coincide;
- the middle-midpoint vector has four equal radii;
- the radius is smaller than the side;
- one new coordinate of size `lambda-r` extends all four points;
- all ten pair distances of the explicit five-point set equal 4.

Command:

```bash
conda run --no-capture-output -n sandbox python code/verify.py
```

The script is an algebra and regression check. It is not used as a substitute for the arbitrary-coordinate proof in the packet.
