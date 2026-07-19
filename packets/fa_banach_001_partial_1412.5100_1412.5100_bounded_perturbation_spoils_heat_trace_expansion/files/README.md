# Bounded Perturbations Can Spoil Heat-Trace Expansions

Status: `partial_result_likely_valid`

Source:

- Michal Eckstein and Artur Zajac, "Asymptotic and exact expansions of heat traces", arXiv:1412.5100.
- Source location: concluding discussion, p. 38.
- Local source PDF: `source_paper.pdf`.
- Source crop: `figures/source_perturbation_question_crop.png`.

## Result

The source paper identifies the effect of bounded perturbations on heat-trace
asymptotic expansions as an important next step. It notes that if a positive
compact-resolvent operator `P` is replaced by `P + A` with bounded `A`, the
leading small-time behavior of the heat trace is unchanged, but the full
asymptotic expansion may be spoiled.

This packet gives a concrete diagonal example. On `ell_2(N)`, let
`P0 e_n = n e_n`. Then

```text
Tr exp(-t P0) = 1/(exp(t)-1)
              = t^{-1} - 1/2 + O(t).
```

There is a bounded positive diagonal perturbation `A`, with `0 <= A <= I`,
such that for `P = P0 + A` the heat trace still has leading behavior
`Tr exp(-tP) ~ t^{-1}`, but there is no constant `c` satisfying

```text
Tr exp(-tP) = t^{-1} + c + o(1).
```

Thus bounded perturbations can destroy the classical heat-trace expansion
already at the constant term.

## Proof Idea

Choose a subset `S` of the positive integers made of alternating enormous
occupied and empty blocks. Let `A e_n = 1_S(n)e_n`. If
`F_S(t)=sum_{n in S} exp(-tn)`, then

```text
Tr exp(-t(P0+A)) = Tr exp(-tP0) + (exp(-t)-1) F_S(t).
```

The block construction forces `t F_S(t)` to have two subsequential limits:
one positive and one zero. Since `exp(-t)-1 = -t + O(t^2)`, the would-be
constant term of the perturbed heat trace has two different subsequential
limits.

## Novelty Check

Cheap run indexes had no exact row for arXiv:1412.5100. Web searches for
bounded perturbation, heat trace, asymptotic expansion, compact resolvent, and
diagonal counterexample found standard preservation statements in structured
geometric/spectral-triple settings and the source paper itself, but no exact
diagonal obstruction of this form.

This is recorded as a narrow partial result for the perturbation direction,
not as a complete theory of bounded perturbations.

## Human Review Recommendation

Check the scope: the perturbation is bounded and self-adjoint but not compact
or pseudodifferential. The example answers the broad perturbation question in
the negative for arbitrary positive compact-resolvent Hilbert-space operators;
it does not address structured elliptic, regular spectral-triple, trace-class,
or pseudodifferential perturbations.
