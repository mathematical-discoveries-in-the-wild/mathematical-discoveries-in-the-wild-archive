# Full packet: simple AF automorphisms with prescribed CA entropy

status: full_solution, subject to human review

source: David Kerr and Hanfeng Li, *Dynamical entropy in Banach spaces*,
arXiv:math/0407386.

target: Question 9.4 asks whether there is a `*`-automorphism of
`M_p^{\otimes Z}`, or any other simple AF algebra, with finite nonzero CA
entropy.

packet: `runs/fa_banach_001/solutions/full/0407386_kerr_li_q94_simple_af_arbitrary_ca_entropy/`

## Result

The packet gives a full affirmative answer to the `any other simple AF algebra`
branch of Question 9.4. For every `r in [0, infinity]`, it constructs a simple
unital separable AF algebra `A_r` and an automorphism `beta_r` such that

```text
h_c(beta_r) = r.
```

In particular, there are simple AF automorphisms with finite nonzero CA entropy.

## Scope

This does not settle the fixed-UHF branch asking specifically about
`M_p^{\otimes Z}`. The construction uses diagonal orbit embeddings of
matrix-valued Cantor algebras rather than a fixed tensor-product shift.

## Verification

- The previous product-type UHF partial packet remains valid after the two
  corrections recorded in the full packet.
- The full proof reduces CA entropy to topological entropy for a minimal Cantor
  homeomorphism via locality of contractive rank, finite matrix amplification,
  and increasing invariant unions.
- The supplied agent packet reported no published direct resolution in exact
  phrase and citation searches; a lightweight refresh on June 20, 2026 did not
  surface a direct literature answer.

## Files

- `main.tex`: promoted full packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: crop of Question 9.4.
- `history/product_type_partial_packet/`: previous partial packet, absorbed
  into this promoted full packet.
- `evidence/supplied_agent_packet/`: TeX/PDF supplied by the external agent.
- `evidence/0407386_full_simple_af_finite_ca_entropy_push.md`: earlier push
  attempt retained as provenance.
