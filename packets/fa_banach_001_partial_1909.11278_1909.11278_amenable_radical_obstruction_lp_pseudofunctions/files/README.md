# Partial Result: Amenable Normal Subgroups Obstruct Simplicity of `F^p_r(G)`

Run: `fa_banach_001`

Result type: `partial`

Status: `partial_result_likely_valid`

Agent: `agent_super_01`

Date: 2026-07-01

## Source Problem

- N. Christopher Phillips, *Simplicity of reduced group Banach algebras*,
  arXiv:1909.11278v1.
- Local source inspected:
  `data/parsed/arxiv_sources/1909.11278/source.tex`.
- Source signal: introduction, around parsed source lines 408--414.

Phillips proves that if `C^*_r(G)` is simple, then the reduced `L^p` group
Banach algebras `F^p_r(G)` and `B^{p,*}_r(G)` have the Powers property and are
simple. He then notes that the reverse implications are not addressed and asks,
in particular, whether simplicity of `F^p_r(G)` implies the Powers property.

Since Phillips also observes that the Powers property for `F^p_r(G)` implies
the Powers property for `C^*_r(G)`, the full question asks whether Banach
algebra simplicity forces the C*-simplicity/Powers averaging side.

## Result

This packet proves a necessary condition in that direction.

Let `G` be a discrete group, let `N` be an amenable normal subgroup, and let
`1 <= p < infinity`. The quotient map `G -> G/N` induces a contractive
homomorphism with dense range

```text
F^p_r(G) -> F^p_r(G/N).
```

Consequently, if `N` is nontrivial and `1 < p < infinity`, then neither
`F^p_r(G)` nor `B^{p,*}_r(G)` is simple. In particular, simplicity of either
algebra forces the amenable radical of `G` to be trivial.

## Proof Intuition

The quotient representation on `ell^p(G/N)` can be approximated inside the
left regular representation on `ell^p(G)` by spreading each quotient-basis
vector uniformly over a finite Folner set in the corresponding coset of `N`.
For a fixed finitely supported group-algebra element, only finitely many
translations inside `N` occur. Amenability makes the chosen Folner set almost
invariant under all of them, so the `G`-operator on the spread vectors
approximates the quotient `G/N`-operator.

The induced map need not be proved onto. Dense range is enough: if `n` is a
nontrivial element of `N`, then `w_n - 1` maps to zero, while the canonical
trace on `F^p_r(G)` shows `w_n - 1` is nonzero. Thus the kernel is a nonzero
proper closed ideal.

## Relation To Prior Literature

Gardella--Thiel, *Functoriality of group algebras acting on L^p-spaces*,
arXiv:1408.6137, proved a quotient theorem for reduced `L^p` group algebras
when `N` is amenable and `G/N` is finite, and explicitly noted that the finite
quotient assumption was likely unnecessary. The Folner-spreading proof here
removes that finite quotient restriction for the contractive dense-range map
needed in Phillips's simplicity question.

## Scope And Limitations

- This is not a full solution to Phillips's reverse-implication question.
- It rules out all groups with nontrivial amenable normal subgroup as possible
  counterexamples to "simple but no Powers property".
- It does not rule out groups with trivial amenable radical that fail
  C*-simplicity, where the known obstructions are dynamical rather than normal
  amenable subgroups.
- The proof is written for `F^p_r(G)` and the symmetrized
  `B^{p,*}_r(G)`. It does not treat the Orlicz or Lorentz sequence-space
  algebras from later sections of Phillips's paper.

## Evidence

- `source_paper.pdf`: arXiv:1909.11278v1.
- `supporting_paper_1408.6137.pdf`: Gardella--Thiel arXiv:1408.6137.
- `main.tex` / `solution_packet.pdf`: proof packet.

## Novelty Check

Cheap run indexes were searched for `1909.11278`, `Simplicity of reduced group
Banach algebras`, `Powers property`, `reduced group Banach algebra`, `F^p_r`,
`amenable normal subgroup`, and `amenable radical`; no existing run packet
covered this target.

Local parsed-source searches found later papers citing arXiv:1909.11278, but
no local source answering Phillips's reverse implication. The closest local
support is Gardella--Thiel arXiv:1408.6137, whose finite-quotient functoriality
result is strengthened here exactly in the direction they marked as likely.

No external web search was used for novelty beyond the local arXiv source
corpus.

## Human Review Recommendation

Review as a likely valid partial result. The main proof point to check is the
Folner-spreading approximation for the quotient representation and the use of
dense range plus nonzero kernel to obstruct simplicity.
