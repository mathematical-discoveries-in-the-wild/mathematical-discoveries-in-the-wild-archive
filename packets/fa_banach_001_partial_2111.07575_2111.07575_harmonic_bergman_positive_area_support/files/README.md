# Partial Result: Harmonic Bergman Point Evaluations with Positive-Area Support

Run: `fa_banach_001`

Result type: `partial`

Status: `partial_result_likely_valid`

Agent: `agent_super_01`

Date: 2026-07-01

## Source Problem

- Yong Han, Yanqi Qiu, Zipeng Wang, *Complete weighted Bergman spaces have
  bounded point evaluations*, arXiv:2111.07575.
- Source inspected:
  `data/parsed/arxiv_sources/2111.07575/source.tex`.
- Exact target: Question 2 in the source asks whether, for a planar domain
  `Omega` with a positive Radon measure `mu`, completeness of the weighted
  harmonic Bergman space `B^p(Omega,mu)` implies locally uniformly bounded
  point evaluations.

The source proves this under the sufficient assumption that `int supp(mu)` is
nonempty. This packet gives a strictly weaker sufficient condition.

## Result

Let `Omega` be a planar domain, let `mu` be a positive Radon measure on
`Omega`, and let `1 <= p < infinity`. If `B^p(Omega,mu)` is a Banach space and
the support of `mu` has positive planar Lebesgue measure, then `B^p(Omega,mu)`
has locally uniformly bounded point evaluations.

This answers the source harmonic question positively for measures whose
support may have empty interior but positive area, for example fat Cantor-type
supports inside the domain.

## Proof Idea

The source proof for holomorphic Bergman spaces uses the closed graph theorem
on restriction maps to relatively compact subdomains. The only uniqueness
input needed is:

```text
if a harmonic function vanishes on a positive-area set, it is identically zero.
```

This is the standard real-analytic zero-set fact for nonzero harmonic
functions. Hence a compact positive-area subset of `supp(mu)` can replace the
source's interior-support hypothesis.

## Scope

- This is a partial positive answer to Question 2 only.
- It does not settle the harmonic question when `supp(mu)` has zero planar
  measure but is still a uniqueness set for harmonic functions.
- It does not settle Question 1 about individual bounded point evaluations
  without completeness, nor Question 3 in several complex variables.

## Evidence

- `main.tex` / `solution_packet.pdf`: proof note.
- `source_paper.pdf`: source paper arXiv:2111.07575.

## Novelty Check

Cheap run indexes were searched for `2111.07575`, the source title, bounded
point evaluations, locally uniformly bounded point evaluations, and weighted
harmonic Bergman spaces. No existing run packet covered this source question.

Local parsed-source searches for the arXiv id and exact title found no later
local source answering the questions.

## Human Review Recommendation

Review as a small but likely valid partial result. The only mathematical
point to check is the use of the standard fact that the zero set of a nonzero
harmonic function in the plane has two-dimensional Lebesgue measure zero.
