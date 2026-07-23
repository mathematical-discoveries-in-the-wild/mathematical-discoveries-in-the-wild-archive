# Verification

The diagnostic verifier checks the two normalizations most vulnerable to a
factor error:

```text
conda run --no-capture-output -n sandbox \
  python runs/fa_banach_001/solutions/full/\
2502.18140_w2p_trace_conjunction_bbm_formula/code/verify_constants.py
```

Expected checks:

- direct beta quadrature agrees with
  `pi^((N-1)/2) Gamma((p+1)/2) / Gamma((N+p)/2)` for the hemisphere
  integral;
- the Mellin integral for `A(r)=A0+r^q` converges monotonically to `A0/p`;
- the script exits with `all constant checks passed`.

The numerical checks are not used in the proof.

## Recorded output

Run on July 23, 2026:

```text
angular N=2 p=1: quadrature=2 formula=2 abs_error=8.882e-16
angular N=2 p=2: quadrature=1.5707963267949 formula=1.5707963267949 abs_error=4.441e-16
angular N=3 p=1.5: quadrature=2.51327412287183 formula=2.51327412287183 abs_error=8.882e-16
angular N=4 p=3.25: quadrature=1.54255495321782 formula=1.54255495321782 abs_error=6.883e-15
angular N=7 p=4.5: quadrature=0.632983000809893 formula=0.632983000809949 abs_error=5.596e-14
mellin target A0/p=0.472727272727273
mellin s=0.9: value=0.565750528541226 abs_error=9.302e-02
mellin s=0.99: value=0.484811864872288 abs_error=1.208e-02
mellin s=0.999: value=0.473972990572181 abs_error=1.246e-03
mellin s=0.9999: value=0.472852229773288 abs_error=1.250e-04
all constant checks passed
```

## Expert review focus

1. The `L^p`-valued fundamental theorem along rays that begin at the
   Sobolev trace, including `p=1`.
2. Uniformity of the boundary expansion as the ray becomes tangential.
3. Uniform boundedness of the fixed-height large-radius kernel.
4. Whether the source’s phrase “some suitable Sobolev space” is intended
   literally; the packet proves existence of such a class but does not
   identify the optimal one.
