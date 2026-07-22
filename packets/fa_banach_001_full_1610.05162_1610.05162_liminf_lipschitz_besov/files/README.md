# Full solution packet: the liminf Besov criterion characterizes Lipschitz functions

Status: `candidate_full_solution_likely_valid` (full positive answer to
Remark 2.13, pending human review)

Source: Julien Brasseur, *A Bourgain-Brezis-Mironescu characterization of
higher order Besov-Nikol'skii spaces*, arXiv:1610.05162, Theorem 2.12 and
Remark 2.13 on p. 9 of the arXiv PDF (published in *Annales de l'Institut
Fourier* 68 (2018), 1671-1714).

## Result

For `1 <= q < infinity` and `f in L^infinity(R^N)`, put

\[
 A_r(f)=\int_{\mathbb R^N}
 \frac{\|f(\cdot+h)-f\|_\infty^q}{|h|^{N+rq}}\,dh,
 \qquad 0<r<1.
\]

There are constants `c_(N,q), C_(N,q)>0` such that, with extended-real
values allowed,

\[
 c_{N,q}[f]_{\mathrm{Lip}}
 \le \liminf_{r\uparrow1}(1-r)^{1/q}\|f\|_{B^r_{\infty,q}}
 \le \limsup_{r\uparrow1}(1-r)^{1/q}\|f\|_{B^r_{\infty,q}}
 \le C_{N,q}[f]_{\mathrm{Lip}}.
\]

Here finite translation Lipschitz seminorm is equivalent to the existence of
a bounded Lipschitz representative. Consequently, the finiteness hypothesis
and the two-sided estimate in Brasseur's Theorem 2.12 remain valid when every
`limsup` is replaced by `liminf`. This fully answers Remark 2.13 positively.

## Main idea

Let `omega(h)=||f(.+h)-f||_infinity`. The triangle identity for translations
gives `omega(a) <= omega(h)+omega(a-h)`. If `omega(a_0)/|a_0|` is large,
subdividing `a_0` shows that the supremal modulus is comparably large at every
smaller radius. Averaging the triangle inequality converts this into a lower
bound for the cumulative mass
`F(t)=integral_(|h|<=t) omega(h)^q dh`. Stieltjes integration by parts then
produces exactly the missing `1/(1-r)` factor. Thus a non-Lipschitz function
forces the normalized **liminf**, not only the limsup, to diverge.

## Packet contents

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: full-width crop of Theorem 2.12 and
  Remark 2.13.
- `code/make_open_problem_crop.py`: reproducible crop script.
- `code/verify_constants.py`: numerical sanity checks for the radial constants
  and a model translation modulus.
- `verification_report.md`: proof audit, novelty bounds, and reviewer focus.

## Novelty and review

The four cheap run indexes were searched for the arXiv id, title, BBM/Besov
terms, `liminf`, and Lipschitz criteria. Two bounded web-search rounds on
2026-07-21 used the exact sentence from Remark 2.13, the paper title and
authors, and close variants involving translation moduli, Abel means, Besov
norms, and Lipschitz regularity. Local full-text citation searches inspected
the five cached arXiv papers citing this source. No later answer or matching
proof was located. This is not an exhaustive priority search, so novelty
confidence is **moderate**.

Recommended review focus: the cumulative-modulus estimate, the Stieltjes
integration-by-parts boundary term at zero, and the identification of a finite
translation seminorm with a Lipschitz representative.
