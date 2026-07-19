# Partial packet: product-type UHF automorphisms have no finite nonzero CA entropy

status: partial_result

source: David Kerr and Hanfeng Li, *Dynamical entropy in Banach spaces*,
arXiv:math/0407386.

target: Question 9.4 asks whether there is a `*`-automorphism of
`M_p^{\otimes Z}`, or any other simple AF algebra, with finite nonzero CA
entropy.

packet: `runs/fa_banach_001/solutions/partial/0407386_product_type_uhf_ca_entropy_dichotomy/`

## Result

This packet proves a partial negative answer for a natural class. Let

```text
A = tensor_{j in J} M_p
```

be a countable UHF tensor product with `p >= 2`, and let `alpha` be a
product-type automorphism obtained from a permutation `sigma` of `J`, together
with factorwise `*`-automorphisms. Then:

```text
hc(alpha) = 0      if every sigma-orbit is finite,
hc(alpha) = infinity if sigma has an infinite orbit.
```

Thus product-type UHF automorphisms never have finite nonzero CA entropy.

## Scope

This does not solve Question 9.4. It excludes the most shift-like/permutation
product automorphisms, including the source paper's tensor shift, but leaves
general AF automorphisms that mix Bratteli levels in a non-product way.

## Verification

- Cheap run indexes were searched for `0407386`, the paper title, `CA entropy`,
  `simple AF algebra`, and finite-nonzero entropy keywords; no prior packet or
  attempt for this target was found.
- Web searches for exact CA-entropy/simple-AF phrases found the source paper
  but no later direct resolution during this pass.
- The proof uses only Proposition 3.1 and Lemma 9.1 from the source paper,
  plus the elementary finite-orbit invariant-subalgebra observation.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: crop of Question 9.4.
- `code/crop_evidence.py`: reproduces the source-question crop.
