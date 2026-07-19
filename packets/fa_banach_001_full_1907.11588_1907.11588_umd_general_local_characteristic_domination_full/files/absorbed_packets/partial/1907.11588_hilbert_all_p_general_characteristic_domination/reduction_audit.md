# Reduction audit: general local martingales to independent increments

Status: hardened audit completed on 2026-06-16 by `agent_lane_19`.

## Source chain checked

- `source.tex` lines 600-649: canonical decomposition exists in UMD spaces and its components have equivalent strong `L^p` maximal norms.
- `source.tex` lines 643-650: accessible-jump martingales have jumps exhausted by countably many predictable stopping times.
- `source.tex` lines 976-1040: local characteristics split according to continuous, quasi-left-continuous, and accessible parts; accessible compensators are supported on predictable times.
- `source.tex` lines 120-155 and 840-883: discrete tangent/decoupled tangent martingale difference sequences exist and satisfy maximal `L^p` equivalence in UMD spaces.
- `source.tex` lines 1843-1921: finite accessible-jump martingales are represented as discrete martingale difference sequences, and tangent estimates pass through this representation.
- `source.tex` lines 1926-2054: the accessible-jump decoupled tangent construction gives, for almost every base point, independent mean-zero jumps with conditional laws equal to the predictable jump kernels.
- `source.tex` lines 2058-2112: the full decoupled tangent theorem gives a decoupled tangent local martingale whose conditional law has independent increments and local characteristics equal to the original local characteristics.
- `source.tex` lines 3264-3289: an independent-increment martingale is determined in distribution by its local characteristics.
- `source.tex` lines 4000-4010 and 4085-4104: characteristic domination is defined by continuous covariation domination plus total spatial jump-compensator domination, and Remark 12.10 identifies the missing independent-increment comparison.
- `source.tex` lines 4180-4225: accessible-jump truncations by the first `m` predictable jumps converge in strong `L^p`.

## Important correction

The first packet proof used the phrase "the accessible-jump compensator of `N` is dominated by that of `M`." This is not justified by the source definition of characteristic domination. The definition compares only the total spatial jump compensators

```text
nu^N(R_+ x B) <= nu^M(R_+ x B).
```

It does not force the time-atomic/accessibly supported part of `nu^N` to be dominated by the time-atomic part of `nu^M`; mass can be moved between accessible and quasi-left-continuous time supports.

The proof was therefore rerouted through the full decoupled tangent theorem. After decoupling, both martingales are conditionally independent-increment martingales with their full local characteristics. The Hilbert comparison is then applied to the full characteristics, not separately to canonical jump components.

## Hardened reduction

For almost every base point, the decoupled tangent martingales have deterministic characteristics

```text
([N^c], nu^N) and ([M^c], nu^M).
```

Characteristic domination gives trace domination of the continuous Hilbert covariation and aggregate domination of the full jump compensator. The new Proposition `ind-incr-hilbert` compares the resulting independent-increment martingales directly:

```text
E sup_t ||L_t||^p <= C_p E sup_t ||K_t||^p.
```

For `1 <= p < 2`, the proof uses the same Laplace-deficit estimate as the discrete theorem, but with three factors in the square characteristic: deterministic continuous trace, nonatomic Poisson jump part, and independent predictable-time jump variables. For `p >= 2`, scalar Rosenthal for the nonnegative square characteristic gives the comparison.

Finally, Yaroslavtsev's tangent maximal estimate recouples the independent-increment martingales back to the original martingales.

## Verdict

The reduction is now airtight modulo standard scalar Rosenthal for nonnegative independent-increment square sums and the cited source theorems. The corrected proof avoids the only component-splitting pitfall found during the audit.
