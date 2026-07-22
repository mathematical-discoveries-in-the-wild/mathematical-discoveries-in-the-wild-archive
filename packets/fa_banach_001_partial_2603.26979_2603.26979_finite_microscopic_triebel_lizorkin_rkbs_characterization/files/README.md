# Triebel--Lizorkin RKBS Pairs for the Bessel Kernel

Source paper: Tjeerd Jan Heeringa, "Characterization of the reproducing
structure of the Bessel potential spaces beyond p=2", arXiv:2603.26979.

Status: candidate partial result, likely valid. The packet gives a complete
characterization for spatial exponents `1<p,q<infinity` and finite Banach
microscopic exponents `1<=a,b<infinity`. Spatial endpoints and nonseparable
microscopic endpoints remain open.

## Result

The spaces `F^u_{p,a}(R^d)` and `F^v_{q,b}(R^d)` form an RKBS pair with
kernel `K_s(x,y)=G_{2s}(x-y)` exactly when

```text
1/p+1/q >= 1,
d/p < u < 2s-d/p',
d/q < v < 2s-d/q',
u+v >= 2s+d(1/p+1/q-1),
```

with one extra condition on the doubly critical face

```text
1/p+1/q=1 and u+v=2s:
1/a+1/b >= 1.
```

When `1/p+1/q>1`, equality in the Sobolev balance imposes no condition on
the microscopic exponents. Setting `a=b=2` recovers the reflexive part of
the source theorem.

## Proof Idea

The reproducing identities force the pairing on Schwartz functions to be
`[g,f]=<(I-Delta)^s f,g>`. Triebel--Lizorkin duality and the sharp Sobolev
embedding theorem then give the lower balance conditions and the new
microscopic boundary clause. A dyadic annulus argument proves the exact
membership rule

```text
G_alpha in F^t_{r,c}  iff  t<alpha-d/r',
```

which supplies both the lower point-evaluation bounds (use `G_0=delta_0`)
and the upper kernel-section bounds (use `G_{2s}`).

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2603.26979.
- `supporting_paper_1112.5388.pdf`: sharp Triebel--Lizorkin embedding source.
- `figures/open_problem_crop.png`: future-work question on source PDF page 14.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Human Review Recommendation

Review as a strong partial solution. The highest-value checks are:

1. the endpoint `c=infinity` part of the Bessel-distribution membership lemma;
2. duality `(F^v_{q,b})*=F^{-v}_{q',b'}` when `b=1`;
3. the forced-pairing argument using Schwartz density;
4. the distinction between `p<q'`, where critical embedding ignores `a,b`,
   and `p=q'`, where `a<=b'` is necessary;
5. the two reproducing identities for the constructed pairing.

The novelty search found no later or parallel RKBS characterization for
Triebel--Lizorkin pairs, but it was bounded rather than exhaustive.
