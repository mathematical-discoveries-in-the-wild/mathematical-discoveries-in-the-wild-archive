# Verification report

Command:

```bash
conda run --no-capture-output -n sandbox python code/verify_all_order_top.py --through 7
```

Exact output:

```text
j=1, d=3, numerator monomials=5: H0=pi**2, H1/H0=-1/3
j=2, d=7, numerator monomials=15: H0=14*pi**4/5, H1/H0=-1/6
j=3, d=11, numerator monomials=33: H0=62*pi**6/21, H1/H0=-1/9
j=4, d=15, numerator monomials=62: H0=508*pi**8/225, H1/H0=-1/12
j=5, d=19, numerator monomials=104: H0=146*pi**10/99, H1/H0=-1/15
j=6, d=23, numerator monomials=162: H0=5657908*pi**12/6449625, H1/H0=-1/18
j=7, d=27, numerator monomials=238: H0=32764*pi**14/66825, H1/H0=-1/21
All exact full-recurrence assertions passed.
```

The script independently checks:

1. the complete invariant recurrence, rather than the projected proof
   recurrence;
2. the Bernoulli closed form for `H0`;
3. the top-two-residue identity `H1/H0=-1/(3j)`;
4. positivity of the final trace constant.

All assertions use exact SymPy rational, gamma, and Bernoulli arithmetic.
