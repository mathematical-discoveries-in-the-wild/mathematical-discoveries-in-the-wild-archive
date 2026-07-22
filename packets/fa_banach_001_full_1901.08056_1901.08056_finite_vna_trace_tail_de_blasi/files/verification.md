# Verification report

Verdict: `candidate_full_solution_likely_valid`

## Scope match

Question 12.1 of arXiv:1901.08056 explicitly asks for a trace formula for the De Blasi measure, at least for finite sigma-finite von Neumann algebras. The packet proves an exact formula for every bounded subset of `M_*` after choosing any faithful normal finite trace on such an algebra. It does not claim the arbitrary semifinite, infinite-trace case.

## Analytic audit

1. A finite sigma-finite von Neumann algebra admits a faithful normal finite trace, and its predual identifies isometrically with `L1(M,tau)`.
2. The source paper's Theorem 11.1(b') applies to a relatively weakly compact set `K` and supplies one normal control state `psi`.
3. Writing `psi=tau(g·)` and splitting `g=g_0+r` with `0<=g_0<=c1` gives, uniformly for projections `e` and contractions `a`,

   `||ea||_psi^2 <= c tau(e)+||r||_1`.

   This makes `ea` uniformly small in the control seminorm when `tau(e)` is small. Duality then yields uniform smallness of `||h e||_1` for `h in K`.
4. Right multiplication by a projection is contractive on `L1`, so the trace-tail quantity is bounded above by the De Blasi distance to any relatively weakly compact set.
5. For `h=v|h|`, spectral truncation at height `c` has error `h 1_(c,infinity)(|h|)`, whose support projection has trace at most `||h||_1/c`.
6. The retained truncations have squared `L2` norm at most `c sup_A ||h||_1`. Because `tau(1)<infinity`, the inclusion `L2(M,tau)->L1(M,tau)` is bounded; the image of the relevant closed `L2` ball is weakly compact. This proves the reverse De Blasi inequality.

No circular use of the desired formula occurs. The only substantive external input is the source paper's qualitative weak-compactness characterization.

## Computational sanity check

Command:

```bash
/opt/homebrew/Caskroom/miniforge/base/envs/sandbox/bin/python code/verify_trace_tail.py
```

Output:

```text
PASS: 240 matrix/truncation cases; max error 5.151e-14
```

The checked identities are the spectral-tail equality, the trace Markov bound, the `L2` truncation bound, and right-multiplication contractivity. This is not used as proof.

## Rendering audit

The five-page PDF was rendered page by page and inspected. The source crop is readable and complete; there are no clipped equations, overflow warnings, missing references, or illegible glyphs.

## Reviewer focus

An expert reviewer should concentrate on the specialization of Theorem 11.1(b') and on the two tracial estimates in Lemma 1. The remainder is standard noncommutative `L1/L2` spectral truncation.
